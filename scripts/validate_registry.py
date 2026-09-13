#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

ROOT=Path(__file__).resolve().parents[1]

def load(p):
    return json.loads((ROOT/p).read_text(encoding="utf-8"))

errors=[]
skills=load("registry/skills.json")
packages=load("registry/packages.json")
profiles=load("registry/profiles.json")
roles=load("registry/roles.json")
ops=load("registry/operators.json")
trust=load("registry/trust-policy.json")
runtime_adapters=load("registry/runtime-adapters.json")

foundation=skills["foundation"]
employee=skills["employee"]
if len(foundation)!=20:
    errors.append(f"foundation count {len(foundation)} != 20")
if len(employee)!=80:
    errors.append(f"employee count {len(employee)} != 80")

ids=[x["id"] for x in foundation]+[x["id"] for x in employee]
if len(ids)!=len(set(ids)):
    errors.append("canonical skill IDs are not unique")

known_employee={x["id"] for x in employee}
opsids={x["id"] for x in ops["operators"]}
support={x["id"] for x in packages.get("support",[])}
policy_sources=trust.get("sources",{})
pkgids=[]

for sid,s in packages["sources"].items():
    if not re.fullmatch(r"[0-9a-f]{40}",s["commit"]):
        errors.append(f"source {sid}: invalid pin")
    if not s.get("repo") or not s.get("namespace"):
        errors.append(f"source {sid}: missing repo/namespace")

    policy=policy_sources.get(s.get("repo"))
    if not isinstance(policy,dict):
        errors.append(f"source {sid}: missing trust/redistribution policy for {s.get('repo')}")
    else:
        if not policy.get("license"):
            errors.append(f"source {sid}: missing license decision")
        if policy.get("redistribution") not in {"redistributable","fetch-only","private-local"}:
            errors.append(f"source {sid}: invalid redistribution decision")
        if s.get("license") != policy.get("license"):
            errors.append(f"source {sid}: package registry license disagrees with trust policy")
        if s.get("redistribution") != policy.get("redistribution"):
            errors.append(f"source {sid}: package registry redistribution disagrees with trust policy")
        if any(p.get("vendored") for p in s.get("packages",[])) and not policy.get("vendoring_allowed"):
            errors.append(f"source {sid}: vendored package but vendoring is not allowed")

    for p in s.get("packages",[]):
        cid=p["id"]
        pkgids.append(cid)
        selector_count=sum(bool(p.get(k)) for k in ("path","root","name"))
        if selector_count!=1:
            errors.append(f"{cid}: must define exactly one of path/root/name")
        for dep in p.get("deps",[]):
            if dep not in support:
                errors.append(f"{cid}: unknown support dependency {dep}")
        for op in p.get("operators",[]):
            if op not in opsids:
                errors.append(f"{cid}: unknown operator {op}")
        if p.get("vendored"):
            d=ROOT/"skills"/"imported"/s["namespace"]/cid
            if not (d/"SKILL.md").exists():
                errors.append(f"{cid}: vendored SKILL.md missing at {d}")

if set(pkgids)!=known_employee:
    errors.append("package registry does not match exactly the 80 employee skills")

claims={x.get("id"):x.get("public_beta_support") for x in runtime_adapters.get("adapters",[])}
if claims.get("aiverse-os")!="end-to-end":
    errors.append("aiverse-os must be the explicit public-beta end-to-end runtime claim")
for rid,claim in claims.items():
    if rid!="aiverse-os" and claim=="end-to-end":
        errors.append(f"runtime {rid}: end-to-end claim lacks current public-beta acceptance evidence")
    if claim not in {"end-to-end","package-exposure","adapter-exposure"}:
        errors.append(f"runtime {rid}: invalid public_beta_support value {claim!r}")

for x in foundation:
    if not (ROOT/"skills"/"foundation"/x["id"]/"SKILL.md").exists():
        errors.append(f"{x['id']}: foundation package missing")

known=set(ids)
for name,p in profiles["profiles"].items():
    unknown=set(p["employee_skills"])-known_employee
    if unknown:
        errors.append(f"profile {name}: unknown skills {sorted(unknown)}")

for r in roles["roles"]:
    unknown=set(r["skills"])-known
    if unknown:
        errors.append(f"role {r['id']}: unknown skills {sorted(unknown)}")
    unknown_ops=set(r["operators"])-opsids
    if unknown_ops:
        errors.append(f"role {r['id']}: unknown operators {sorted(unknown_ops)}")

if errors:
    print("AI-Verse-Skills validation FAILED")
    for e in errors:
        print(" -",e)
    sys.exit(1)

print(
    f"AI-Verse-Skills validation OK: {len(foundation)} foundation + "
    f"{len(employee)} employee = {len(ids)} canonical capabilities; "
    f"{len(support)} support packages; trust/runtime claims valid."
)
