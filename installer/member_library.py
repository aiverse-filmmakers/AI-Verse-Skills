"""Skills-owned, private member library; OS owns discovery and workspace bindings.

Packages are immutable revisions. The single atomic index is the commit point;
an interrupted unpublished copy never becomes a live skill. No source is moved,
deleted, executed, made public or implicitly granted access by this module.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import os
import re
import shutil
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path

try:
    from .generation_lifecycle import lifecycle_lock, _is_symlink_or_reparse
    from .admission import scan_package
    from .provider_contract_v1 import package_digest_v1, skill_metadata
except ImportError:
    from generation_lifecycle import lifecycle_lock, _is_symlink_or_reparse
    from admission import scan_package
    from provider_contract_v1 import package_digest_v1, skill_metadata

CONTRACT = "aiverse-member-skill-library-v1"
PLAN_CONTRACT = "aiverse-member-skill-import-v1"
RELATIVE = Path(".aiverse/member-library")
SEGMENT = re.compile(r"^[a-z0-9][a-z0-9-]{0,99}$")
HEX = re.compile(r"^[a-f0-9]{64}$")
SCOPE = re.compile(r"^(operator|workspace:[a-z0-9][a-z0-9-]*)$")
PORTABILITY = {"reusable": True, "contains_workspace_data": False,
               "contains_credentials": False, "has_workspace_dependencies": False}


def _json_file(file, limit=4_000_000):
    file = Path(file)
    if _is_symlink_or_reparse(file) or not file.is_file() or file.stat().st_size > limit:
        raise RuntimeError("JSON input must be a bounded regular file")
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("duplicate JSON field")
            result[key] = value
        return result
    try:
        return json.loads(file.read_text(encoding="utf-8"), object_pairs_hook=pairs,
                          parse_constant=lambda value: (_ for _ in ()).throw(ValueError("non-finite JSON")))
    except (ValueError, OSError, UnicodeError) as exc:
        raise RuntimeError("invalid JSON input") from exc


def _provenance(value=None):
    if value is None:
        return {"origin": "local-import", "license": "not-declared",
                "dependencies": [], "requested_capabilities": [],
                "requires_connection": False, "requires_credential": False}
    expected = set(_provenance())
    if not isinstance(value, dict) or set(value) != expected:
        raise RuntimeError("provenance must declare origin, license and dependency/access metadata")
    for key in ("origin", "license"):
        if not isinstance(value[key], str) or not value[key].strip() or len(value[key]) > 500:
            raise RuntimeError("invalid provenance text")
    for key in ("dependencies", "requested_capabilities"):
        if (not isinstance(value[key], list) or len(value[key]) > 50
                or any(not isinstance(x, str) or not x or len(x) > 500 for x in value[key])):
            raise RuntimeError("invalid provenance requirements")
    for key in ("requires_connection", "requires_credential"):
        if type(value[key]) is not bool:
            raise RuntimeError("invalid provenance access declaration")
    if len(_bytes(value)) > 16_384:
        raise RuntimeError("provenance is too large")
    # This metadata documents requirements; it neither installs nor authorizes them.
    return json.loads(_bytes(value))


def _root(value):
    root = Path(value).expanduser().absolute()
    if _is_symlink_or_reparse(root) or (root.exists() and not root.is_dir()):
        raise RuntimeError("member library root must be a real directory")
    root = root.resolve()
    # Refuse redirected existing ancestors, including metadata files/dirs.
    for path in (root, root / ".aiverse", root / RELATIVE):
        if _is_symlink_or_reparse(path):
            raise RuntimeError("member library metadata symlink refused")
    for marker in ("active.json", "installed.json", "generations"):
        if (root / ".aiverse" / marker).exists():
            raise RuntimeError("managed Skills root cannot be used as a personal member library")
    return root


def _safe_ancestors(root, target):
    """Check before mkdir/copy, so a redirected ancestor receives no writes."""
    relative = target.relative_to(root)
    current = root
    for part in relative.parts:
        current = current / part
        if _is_symlink_or_reparse(current) or (current.exists() and not current.is_dir()):
            raise RuntimeError("member package ancestor is redirected or not a directory")


def _index_file(root):
    return _root(root) / RELATIVE / "index.json"


def _empty():
    return {"contract": CONTRACT, "sequence": 0, "skills": {}, "events": []}


def _bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def _validate_scope(source_scope, visibility, admission):
    if not isinstance(source_scope, str) or not SCOPE.fullmatch(source_scope):
        raise RuntimeError("invalid source scope")
    if visibility != "shared" and visibility != source_scope:
        raise RuntimeError("restricted visibility must match the source workspace")
    if visibility != "shared" and not visibility.startswith("workspace:"):
        raise RuntimeError("invalid restricted visibility")
    if not isinstance(admission, dict) or any(type(v) is not bool for v in admission.values()):
        raise RuntimeError("admission must contain boolean declarations")
    if admission.get("contains_credentials") is True:
        raise RuntimeError("credentials must never be stored in member skill packages")
    if visibility == "shared" and (admission != PORTABILITY or set(admission) != set(PORTABILITY)):
        raise RuntimeError("shared import requires explicit portability admission")


def read_index(root):
    file = _index_file(root)
    if not file.exists() and not _is_symlink_or_reparse(file):
        return _empty()
    if _is_symlink_or_reparse(file) or not file.is_file() or file.stat().st_size > 4_000_000:
        raise RuntimeError("invalid member library index file")
    try:
        index = _json_file(file)
    except (OSError, ValueError) as exc:
        raise RuntimeError("unreadable member library index") from exc
    if (not isinstance(index, dict) or set(index) != set(_empty())
            or index["contract"] != CONTRACT or type(index["sequence"]) is not int
            or index["sequence"] < 0 or not isinstance(index["skills"], dict)
            or not isinstance(index["events"], list)):
        raise RuntimeError("invalid member library index")
    if any(not isinstance(event, dict) for event in index["events"]):
        raise RuntimeError("invalid member library audit event")
    for key, record in index["skills"].items():
        if not isinstance(key, str) or not SEGMENT.fullmatch(key):
            raise RuntimeError("invalid member skill identity")
        if (not isinstance(record, dict) or record.get("id") != key
                or not isinstance(record.get("revisions"), dict)
                or not isinstance(record.get("active_revision"), str)
                or record.get("active_revision") not in record["revisions"]):
            raise RuntimeError("invalid member skill record")
        if (not isinstance(record.get("name"), str) or not record["name"]
                or not isinstance(record.get("description"), str) or not record["description"]):
            raise RuntimeError("invalid member skill metadata")
        for revision, metadata in record["revisions"].items():
            if not isinstance(revision, str) or not HEX.fullmatch(revision) or not isinstance(metadata, dict):
                raise RuntimeError("invalid member skill revision")
            _validate_scope(metadata.get("source_scope"), metadata.get("visibility"), metadata.get("admission"))
            if (not isinstance(metadata.get("name"), str) or not metadata["name"]
                    or len(metadata["name"]) > 100 or not isinstance(metadata.get("description"), str)
                    or not metadata["description"] or len(metadata["description"]) > 1024
                    or not isinstance(metadata.get("source"), str)):
                raise RuntimeError("invalid revision metadata")
            if "provenance" in metadata:
                _provenance(metadata["provenance"])
            if metadata.get("path") != (RELATIVE / "packages" / key / revision).as_posix():
                raise RuntimeError("member revision path mismatch")
        if "enabled" in record and type(record["enabled"]) is not bool:
            raise RuntimeError("invalid member activation state")
        active = record["revisions"][record["active_revision"]]
        if any(record.get(k) != active.get(k) for k in ("name", "description", "visibility")):
            raise RuntimeError("member active metadata mismatch")
    return index


def index_digest(root):
    return hashlib.sha256(_bytes(read_index(root))).hexdigest()


def _review_receipt(review, revision, scan):
    if review is None:
        if scan["status"] != "pass":
            raise RuntimeError("package admission requires review: " + scan["status"])
        return
    if (not isinstance(review, dict) or set(review) != {"source_revision", "findings", "reviewer", "reason"}
            or review.get("source_revision") != revision or len(_bytes(review)) > 16_384):
        raise RuntimeError("security review must bind this exact package revision")
    for key, maximum in (("reviewer", 100), ("reason", 1000)):
        if not isinstance(review[key], str) or not review[key].strip() or len(review[key]) > maximum or "\x00" in review[key]:
            raise RuntimeError("security review requires bounded reviewer and reason")
    findings = scan.get("findings", [])
    if not findings or any(item.get("severity") != "review" or item.get("code") not in {"environment-harvest", "shell-download-chain", "destructive-shell"} for item in findings):
        raise RuntimeError("security review cannot waive denied or unknown findings")
    expected = sorted((item["path"], item["code"]) for item in findings)
    acknowledged = review["findings"]
    if (not isinstance(acknowledged, list) or len(acknowledged) > 64
            or any(not isinstance(item, dict) or set(item) != {"path", "code"}
                   or not all(isinstance(item[k], str) for k in ("path", "code")) for item in acknowledged)
            or sorted((item["path"], item["code"]) for item in acknowledged) != expected):
        raise RuntimeError("security review must acknowledge every exact finding")


def _package(source, security_review=None, *, inspect_only=False):
    source = Path(source).expanduser().absolute()
    if _is_symlink_or_reparse(source) or not source.is_dir():
        raise RuntimeError("source must be a real package directory, without symlinks")
    source = source.resolve()
    files = []
    total = 0
    entries = 0
    for path in source.rglob("*"):
        entries += 1
        if entries > 1024:
            raise RuntimeError("source package exceeds member-library entry limit")
        if ".git" in path.relative_to(source).parts:
            raise RuntimeError("source package must not include repository metadata")
        if _is_symlink_or_reparse(path):
            raise RuntimeError("source package symlink requires separate review")
        if path.is_file():
            size = path.stat().st_size
            total += size
            files.append(path)
            if len(files) > 256 or size > 1_048_576 or total > 8_388_608:
                raise RuntimeError("source package exceeds member-library resource limits")
        elif not path.is_dir():
            raise RuntimeError("unsupported source package file")
    if not (source / "SKILL.md").is_file():
        raise RuntimeError("source package requires SKILL.md")
    metadata = skill_metadata(source / "SKILL.md")
    if (not metadata.get("name") or not metadata.get("description")
            or len(metadata["name"]) > 100 or len(metadata["description"]) > 1024):
        raise RuntimeError("source package requires bounded skill name and description")
    scan = scan_package(source, max_text_bytes=8_388_608)
    revision = package_digest_v1(source)
    if inspect_only:
        return {"contract":"aiverse-member-skill-inspection-v1", "source_revision":revision,
                "scan":scan}
    _review_receipt(security_review, revision, scan)
    return source, metadata, revision


def plan_import(root, source, *, admission, source_scope="operator", visibility="shared", skill_id=None, provenance=None, security_review=None):
    root = _root(root)
    _validate_scope(source_scope, visibility, admission)
    source, metadata, revision = _package(source, security_review)
    if source == root or root in source.parents or source in root.parents:
        raise RuntimeError("source and member-library roots must be independent")
    provenance = _provenance(provenance)
    index = read_index(root)
    if skill_id is not None and skill_id not in index["skills"]:
        raise RuntimeError("an update must name an existing member skill identity")
    identity = skill_id or "skill-" + uuid.uuid4().hex
    result = {"contract": PLAN_CONTRACT, "library_root": str(root), "source": str(source),
            "source_revision": revision, "expected_index": index_digest(root),
            "id": identity, "source_scope": source_scope, "visibility": visibility,
            "admission": dict(admission), "metadata": metadata, "provenance": provenance,
            "operation": "update" if skill_id else "create"}
    if security_review is not None:
        result["security_review"] = json.loads(_bytes(security_review))
    return result


@contextlib.contextmanager
def _locked(root):
    root = _root(root)
    base = root / RELATIVE
    _safe_ancestors(root, base)
    base.mkdir(parents=True, exist_ok=True, mode=0o700)
    lock = base / ".writer.lifecycle.lock"
    if _is_symlink_or_reparse(lock) or (lock.exists() and not lock.is_file()):
        raise RuntimeError("member library lock is redirected or invalid")
    # Reuse owner locking: live/unknown holders are never reclaimed; a proven
    # dead local holder can be reclaimed only after the owner's stale threshold.
    with lifecycle_lock(base / "writer", timeout_seconds=0):
        yield


def _write(root, index):
    file = _index_file(root)
    encoded = _bytes(index) + b"\n"
    if len(encoded) > 4_000_000:
        raise RuntimeError("member library index capacity reached; no commit was made")
    fd, name = tempfile.mkstemp(prefix=".index-", dir=file.parent)
    try:
        with os.fdopen(fd, "wb") as output:
            output.write(encoded)
            output.flush()
            os.fsync(output.fileno())
        os.replace(name, file)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def revision_path(root, identity, revision):
    if not SEGMENT.fullmatch(identity) or not HEX.fullmatch(revision):
        raise RuntimeError("invalid member revision identity")
    root = _root(root)
    path = root / RELATIVE / "packages" / identity / revision
    if _is_symlink_or_reparse(path) or (path.exists() and path.resolve() != path):
        raise RuntimeError("member revision path is redirected")
    return path


def _activate(record, revision):
    metadata = record["revisions"][revision]
    record.update(active_revision=revision, name=metadata["name"],
                  description=metadata["description"], visibility=metadata["visibility"])


def apply_import(root, source, *, plan, admission, source_scope="operator", visibility="shared", provenance=None, security_review=None):
    root = _root(root)
    if not isinstance(plan, dict) or plan.get("contract") != PLAN_CONTRACT:
        raise RuntimeError("a supported import preview is required")
    if set(plan) - {"security_review"} != {"contract", "library_root", "source", "source_revision", "expected_index",
                     "id", "source_scope", "visibility", "admission", "metadata", "provenance", "operation"}:
        raise RuntimeError("invalid import preview fields")
    _validate_scope(source_scope, visibility, admission)
    provenance = _provenance(provenance)
    source, metadata, revision = _package(source, security_review)
    if source == root or root in source.parents or source in root.parents:
        raise RuntimeError("source and member-library roots must be independent")
    if plan.get("source_revision") != revision:
        raise RuntimeError("source changed since preview")
    if plan.get("security_review") != security_review:
        raise RuntimeError("security review differs from preview")
    expected = {"library_root": str(root), "source": str(source),
                "source_scope": source_scope, "visibility": visibility,
                "admission": admission, "metadata": metadata, "provenance": provenance}
    if any(plan.get(key) != value for key, value in expected.items()):
        raise RuntimeError("import arguments differ from preview")
    identity = plan.get("id", "")
    if not isinstance(identity, str) or not SEGMENT.fullmatch(identity):
        raise RuntimeError("invalid planned member identity")
    with _locked(root):
        index = read_index(root)
        record = index["skills"].get(identity)
        retry_key = hashlib.sha256(_bytes(plan)).hexdigest()
        if any(event.get("effect_id") == retry_key for event in index["events"]):
            if record and revision in record["revisions"]:
                if _package(revision_path(root, identity, revision), security_review)[2] != revision:
                    raise RuntimeError("imported revision integrity failure")
                return {"state": "already-imported", "id": identity, "revision": revision,
                        "qualified_id": "local:" + identity, "source_preserved": True}
            raise RuntimeError("import receipt does not match member record")
        if index_digest(root) != plan.get("expected_index"):
            raise RuntimeError("member library changed since preview")
        if (plan.get("operation") == "create" and record is not None
                or plan.get("operation") == "update" and record is None
                or plan.get("operation") not in {"create", "update"}):
            raise RuntimeError("import operation does not match member identity")
        target = revision_path(root, identity, revision)
        _safe_ancestors(root, target.parent)
        target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        if target.parent.resolve() != target.parent:
            raise RuntimeError("member package parent is redirected")
        if target.exists():
            if _package(target, security_review)[2] != revision:
                raise RuntimeError("existing immutable revision is damaged")
        else:
            stage = Path(tempfile.mkdtemp(prefix=".stage-", dir=target.parent))
            try:
                shutil.copytree(source, stage, dirs_exist_ok=True)
                if _package(stage, security_review)[2] != revision or _package(source, security_review)[2] != revision:
                    raise RuntimeError("source changed while staging")
                for path in stage.rglob("*"):
                    if path.is_dir():
                        path.chmod(0o700)
                    else:
                        path.chmod(0o700 if path.stat().st_mode & 0o111 else 0o600)
                os.replace(stage, target)
            finally:
                if stage.exists():
                    shutil.rmtree(stage)
        revision_metadata = {"name": metadata["name"], "description": metadata["description"],
                             "visibility": visibility, "source_scope": source_scope,
                             "source": str(source), "admission": dict(admission), "provenance": provenance,
                             "path": target.relative_to(root).as_posix()}
        if security_review is not None:
            revision_metadata["security_review"] = json.loads(_bytes(security_review))
        record = record or {"id": identity, "revisions": {}}
        if revision in record["revisions"] and record["revisions"][revision] != revision_metadata:
            raise RuntimeError("revision scope/provenance cannot be changed by content reuse")
        record["revisions"][revision] = revision_metadata
        _activate(record, revision)
        index["skills"][identity] = record
        index["sequence"] += 1
        index["events"].append({"action": plan["operation"], "id": identity,
                                "revision": revision, "effect_id": retry_key,
                                "at": datetime.now(timezone.utc).isoformat()})
        _write(root, index)
    return {"state": "imported", "id": identity, "qualified_id": "local:" + identity,
            "revision": revision, "source_preserved": True, "index_digest": index_digest(root)}


def select_revision(root, identity, revision, *, expected_index):
    with _locked(root):
        index = read_index(root)
        if index_digest(root) != expected_index:
            raise RuntimeError("member library changed since preview")
        record = index["skills"].get(identity)
        if record is None or revision not in record["revisions"]:
            raise RuntimeError("unknown member skill revision")
        if _package(revision_path(root, identity, revision), record["revisions"][revision].get("security_review"))[2] != revision:
            raise RuntimeError("member revision integrity failure")
        if record["active_revision"] == revision:
            return {"state": "already-selected", "id": identity, "revision": revision}
        _activate(record, revision)
        index["sequence"] += 1
        index["events"].append({"action": "select-revision", "id": identity,
                                "revision": revision, "at": datetime.now(timezone.utc).isoformat()})
        _write(root, index)
    return {"state": "selected", "id": identity, "revision": revision}


def verify(root):
    errors = []
    try:
        index = read_index(root)
        for identity, record in index["skills"].items():
            for revision in record["revisions"]:
                if _package(revision_path(root, identity, revision), record["revisions"][revision].get("security_review"))[2] != revision:
                    errors.append(f"revision digest mismatch: {identity}/{revision}")
    except (RuntimeError, OSError, ValueError) as exc:
        errors.append(str(exc))
    return {"contract": CONTRACT, "ok": not errors, "errors": errors}


def set_enabled(root, identity, enabled, *, expected_index):
    if type(enabled) is not bool:
        raise RuntimeError("member enabled state must be boolean")
    with _locked(root):
        index = read_index(root)
        if index_digest(root) != expected_index:
            raise RuntimeError("member library changed since preview")
        record = index["skills"].get(identity)
        if not record:
            raise RuntimeError("unknown member identity")
        if record.get("enabled", True) == enabled:
            return {"state": "unchanged", "id": identity}
        record["enabled"] = enabled
        index["sequence"] += 1
        index["events"].append({"action": "enable" if enabled else "disable", "id": identity,
                                "at": datetime.now(timezone.utc).isoformat()})
        _write(root, index)
    return {"state": "enabled" if enabled else "disabled", "id": identity}


def learning_binding(impl, managed_root):
    try:
        from .generation_lifecycle import controller_path
    except ImportError:
        from generation_lifecycle import controller_path
    file = controller_path(Path(managed_root), "learning", "member-library.json")
    if not file.exists() and not file.is_symlink():
        return None
    data = _json_file(file, 8192)
    if (not isinstance(data, dict) or set(data) != {"contract", "library_root"}
            or data["contract"] != "aiverse-member-learning-route-v1"
            or not isinstance(data["library_root"], str) or not Path(data["library_root"]).is_absolute()):
        raise RuntimeError("invalid member learning route")
    return _root(data["library_root"])


def configure_learning(impl, managed_root, library_root, *, apply=False):
    try:
        from .generation_lifecycle import controller_path
    except ImportError:
        from generation_lifecycle import controller_path
    managed_root = Path(managed_root).resolve()
    library_root = _root(library_root)
    if managed_root == library_root or managed_root in library_root.parents or library_root in managed_root.parents:
        raise RuntimeError("managed and member roots must be independent")
    current = learning_binding(impl, managed_root)
    if current is not None and current != library_root:
        raise RuntimeError("member learning route already belongs to another library; explicit reconciliation required")
    result = {"contract": "aiverse-member-learning-route-v1", "library_root": str(library_root)}
    if not apply:
        return {"state": "planned", **result}
    with impl.lifecycle_lock(managed_root):
        current = learning_binding(impl, managed_root)
        if current is not None and current != library_root:
            raise RuntimeError("member learning route changed")
        if current is None:
            file = controller_path(managed_root, "learning", "member-library.json")
            impl._atomic_json_write(file, result)
    return {"state": "configured", **result}


def apply_learning_proposal(impl, managed_root, proposal, *, approved_by):
    try:
        from . import learning as learning_owner
    except ImportError:
        import learning as learning_owner
    library_root = learning_binding(impl, managed_root)
    if library_root is None or proposal.get("kind") != "create":
        return None
    scope = proposal.get("scope", {})
    source_scope = scope.get("aiverse_scope") or ("workspace:" + scope["workspace_id"] if scope.get("workspace_id") else "operator")
    portable = proposal.get("portability") == PORTABILITY and all(type(v) is bool for v in (proposal.get("portability") or {}).values())
    shared = portable and proposal.get("source_ownership") == "agent_learned"
    if not shared and not source_scope.startswith("workspace:"):
        raise RuntimeError("learning candidate needs portability review before shared activation; draft retained")
    visibility = "shared" if shared else source_scope
    admission = PORTABILITY if shared else {}
    candidate = Path(managed_root) / ".aiverse/learning/proposals" / proposal["proposal_id"] / "candidate"
    provenance = {"origin": "learning:" + proposal["proposal_id"], "license": "member-private",
                  "dependencies": proposal.get("requested_dependencies", []),
                  "requested_capabilities": proposal.get("requested_capabilities", []),
                  "requires_connection": proposal.get("requires_connection", False),
                  "requires_credential": proposal.get("requires_credential", False)}
    common = {"admission": admission, "source_scope": source_scope, "visibility": visibility, "provenance": provenance}
    plan = proposal.get("member_import_plan")
    if plan is None:
        plan = plan_import(library_root, candidate, **common)
        proposal["member_import_plan"] = plan
        learning_owner._save_proposal(impl, managed_root, proposal)
    result = apply_import(library_root, candidate, plan=plan, **common)
    proposal.update(state="applied", member_library_root=str(library_root), member_import=result,
                    approved_by=approved_by or "policy:auto", applied_at=datetime.now(timezone.utc).isoformat())
    proposal["history"].append({"state": "applied", "at": proposal["applied_at"], "by": proposal["approved_by"]})
    learning_owner._save_proposal(impl, managed_root, proposal)
    learning_owner.append_audit(managed_root, "learning.member.applied", {"proposal_id": proposal["proposal_id"], "qualified_id": result["qualified_id"], "revision": result["revision"]})
    return proposal


def apply_member_library(impl):
    """Extend the canonical CLI; --library-root never means managed --root."""
    base_parser = impl.parser

    def parser():
        result = base_parser()
        actions = next(a for a in result._actions if isinstance(a, argparse._SubParsersAction))
        library = actions.add_parser("library")
        library.add_argument("--library-root", type=Path, required=True)
        commands = library.add_subparsers(dest="library_operation", required=True)
        def inspect_command(args):
            output = verify(args.library_root) if args.library_operation == "doctor" else read_index(args.library_root)
            print(json.dumps(output))
            if args.library_operation == "doctor" and not output["ok"]:
                raise SystemExit(2)
        for action in ("list", "doctor"):
            command = commands.add_parser(action)
            command.set_defaults(fn=inspect_command)
        command = commands.add_parser("inspect")
        command.add_argument("--source", type=Path, required=True)
        command.set_defaults(fn=lambda args: print(json.dumps(_package(args.source, inspect_only=True))))
        command = commands.add_parser("configure-learning")
        command.add_argument("--apply", action="store_true")
        command.set_defaults(fn=lambda args: print(json.dumps(configure_learning(impl, args.root, args.library_root, apply=args.apply))))
        command = commands.add_parser("set-enabled")
        command.add_argument("--id", required=True)
        command.add_argument("--state", required=True, choices=["enabled", "disabled"])
        command.add_argument("--expected-index", required=True)
        command.set_defaults(fn=lambda args: print(json.dumps(set_enabled(args.library_root, args.id, args.state == "enabled", expected_index=args.expected_index))))
        command = commands.add_parser("import")
        command.add_argument("--source", required=True, type=Path)
        command.add_argument("--source-scope", default="operator")
        command.add_argument("--visibility", default="shared")
        command.add_argument("--admission-json", required=True, type=Path)
        command.add_argument("--id")
        command.add_argument("--provenance-json", type=Path)
        command.add_argument("--security-review-json", type=Path)
        command.add_argument("--apply-plan", type=Path)

        def import_command(args):
            admission = _json_file(args.admission_json, 8192)
            common = {"admission": admission, "source_scope": args.source_scope,
                      "visibility": args.visibility,
                      "provenance": _json_file(args.provenance_json, 16_384) if args.provenance_json else None,
                      "security_review": _json_file(args.security_review_json, 16_384) if args.security_review_json else None}
            if args.apply_plan:
                plan = _json_file(args.apply_plan, 32_768)
                if args.id is not None and args.id != plan.get("id"):
                    raise RuntimeError("requested identity differs from preview")
                output = apply_import(args.library_root, args.source, plan=plan, **common)
            else:
                output = plan_import(args.library_root, args.source, skill_id=args.id, **common)
            print(json.dumps(output))
        command.set_defaults(fn=import_command)
        command = commands.add_parser("select-revision")
        command.add_argument("--id", required=True)
        command.add_argument("--revision", required=True)
        command.add_argument("--expected-index", required=True)
        command.set_defaults(fn=lambda args: print(json.dumps(select_revision(
            args.library_root, args.id, args.revision, expected_index=args.expected_index))))
        return result

    impl.parser = parser
