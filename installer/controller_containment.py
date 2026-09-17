#!/usr/bin/env python3
"""Physical containment compatibility layer for the Skills lifecycle controller.

This module keeps the public-beta composition style used by AI-Verse Skills while
making every supported controller-owned state surface derive from the same
low-level containment primitive in ``generation_lifecycle``.
"""
from __future__ import annotations

import shutil
import tempfile
from pathlib import Path
from typing import Any, Dict

try:
    from . import generation_lifecycle as lifecycle
    from . import learning
    from . import public_beta
except ImportError:
    import generation_lifecycle as lifecycle
    import learning
    import public_beta


def _safe_learning_dir(root: Path) -> Path:
    return lifecycle.controller_path(Path(root), "learning")


def _safe_learning_stage_from_active(impl: Any, root: Path, pin: Any) -> Path:
    root = Path(root).expanduser().resolve()
    stage_parent = lifecycle.metadata_dir(root)
    stage_parent.mkdir(parents=True, exist_ok=True)
    stage_parent = lifecycle.metadata_dir(root)
    stage = Path(tempfile.mkdtemp(prefix=".learning-stage-", dir=str(stage_parent)))
    shutil.copytree(pin.generation_path, stage, dirs_exist_ok=True, symlinks=True)
    shutil.rmtree(stage / ".aiverse", ignore_errors=True)
    return stage


def _purge_generations(impl: Any, root: Path, *, keep: int, confirmed: bool) -> Dict[str, Any]:
    """Destructive retention maintenance with controller/generation confinement."""

    if not confirmed:
        raise RuntimeError("Destructive purge requires --yes")
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        pointer = impl.read_active_pointer(root, allow_uninstalled=True)
        active = pointer.get("generation_id") if pointer.get("state") == "active" else None
        protected = {str(active)} if active else set()
        history = [str(x) for x in pointer.get("history", [])]
        protected.update(history[:max(0, keep)])

        base = learning.learning_dir(root)
        proposals = base / "proposals"
        if proposals.exists():
            for directory in proposals.iterdir():
                proposal = public_beta._json_load(directory / "proposal.json", {})
                for key in (
                    "target_generation_id",
                    "applied_generation_id",
                    "backup_generation_id",
                    "rollback_generation_id",
                ):
                    if proposal.get(key):
                        protected.add(str(proposal[key]))
        archive = base / "archive"
        if archive.exists():
            for record in archive.glob("*/archive.json"):
                data = public_beta._json_load(record, {})
                for key in ("source_generation_id", "archived_generation_id"):
                    if data.get(key):
                        protected.add(str(data[key]))

        removed = []
        generation_root = impl.generations_dir(root)
        if generation_root.exists():
            for entry in sorted(generation_root.iterdir()):
                safe_entry = impl.generation_path(root, entry.name)
                if entry.name in protected:
                    continue
                if safe_entry.is_dir():
                    shutil.rmtree(safe_entry)
                    removed.append(entry.name)
                elif safe_entry.exists():
                    raise RuntimeError(f"Unexpected non-directory entry in Skills generation store: {safe_entry}")

        pointer["history"] = [generation_id for generation_id in history if impl.generation_path(root, generation_id).exists()]
        impl._atomic_json_write(impl.active_pointer_path(root), pointer)
        learning.append_audit(root, "lifecycle.purge", {"removed": removed, "protected": sorted(protected)})
    return {"removed": removed, "protected": sorted(protected), "automatic_purge": False}


def apply_controller_containment(impl: Any) -> None:
    """Bind public lifecycle/controller surfaces to one physical containment law."""

    if getattr(impl, "_controller_containment_v1_applied", False):
        return
    impl._controller_containment_v1_applied = True

    impl.controller_path = lifecycle.controller_path
    impl.metadata_dir = lifecycle.metadata_dir

    # Legacy mutable-layout detection is still supported, but its controller
    # manifest must obey the same root confinement as the generation lifecycle.
    impl._legacy_manifest_path = lambda root: lifecycle.controller_path(Path(root), "installed.json")

    # Learning state is controller-owned state. Route all of its dynamic path
    # construction through the same primitive without changing learning policy.
    learning.learning_dir = _safe_learning_dir
    learning._stage_from_active = _safe_learning_stage_from_active

    # public_beta functions resolve these globals at call time, including the
    # parser closures installed by apply_public_beta, so this preserves the
    # established compatibility architecture rather than duplicating commands.
    public_beta._integration_path = lambda root: lifecycle.controller_path(Path(root), "integration.json")
    public_beta._setup_path = lambda root: lifecycle.controller_path(Path(root), "setup.json")
    public_beta.purge_generations = _purge_generations
