#!/usr/bin/env python3
"""Install the original-first AI-Verse-Skills distribution."""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path

REPO_ROOT=Path(__file__).resolve().parents[1]
DEFAULT_ROOT=Path.home()/".aiverse"/"skills"
DEFAULT_CACHE=Path.home()/".cache"/"aiverse-skills"/"sources"
FRONT_NAME=re.compile(r"(?m)^name:\s*[\"']?([^\"'\n]+)")

def load(rel): return json.loads((REPO_ROOT/rel).read_text(encoding="utf-8"))
def run(cmd,cwd=None):
    p=subprocess.run(cmd,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if p.returncode: raise RuntimeError(f"Command failed ({p.returncode}): {' '.join(cmd)}\n{p.stderr.strip()}")
def cache_name(repo,commit): return repo.replace("/","__")+"@"+commit

def checkout(repo,commit,cache,offline=False):
    dst=cache/cache_name(repo,commit)
    if (dst/".git").exists(): return dst
    if offline: raise RuntimeError(f"Offline cache miss: {repo}@{commit}")
    if not shutil.which("git"): raise RuntimeError("git is required for upstream-fetch packages")
    dst.parent.mkdir(parents=True,exist_ok=True); tmp=dst.with_name(dst.name+".partial")
    if tmp.exists(): shutil.rmtree(tmp)
    tmp.mkdir(); run(["git","init","-q"],tmp); run(["git","remote","add","origin",f"https://github.com/{repo}.git"],tmp)
    run(["git","fetch","-q","--depth","1","origin",commit],tmp); run(["git","checkout","-q","--detach","FETCH_HEAD"],tmp)
    os.replace(tmp,dst); return dst

def front_name(skill_md):
    text=skill_md.read_text(encoding="utf-8",errors="replace")
    if not text.startswith("---"): return None
    end=text.find("\n---",3); m=FRONT_NAME.search(text[:end if end>=0 else len(text)])
    return m.group(1).strip() if m else None

def resolve(root,selector,cid):
    typ=selector["type"]
    if typ=="path":
        p=root/selector["path"]
        if not (p/"SKILL.md").exists(): raise RuntimeError(f"{cid}: no SKILL.md at {selector['path']}")
        return p
    if typ=="repo_root":
        if not (root/"SKILL.md").exists(): raise RuntimeError(f"{cid}: repository root has no SKILL.md")
        return root
    wanted=selector["name"].casefold(); found=[]
    for rel in selector.get("roots",["."]):
        start=(root/rel).resolve()
        try: start.relative_to(root.resolve())
        except ValueError: continue
        if not start.exists(): continue
        for f in start.rglob("SKILL.md"):
            n=front_name(f)
            if (n and n.casefold()==wanted) or f.parent.name.casefold()==wanted: found.append(f.parent.resolve())
    found=list(dict.fromkeys(found))
    if len(found)!=1: raise RuntimeError(f"{cid}: selector {selector['name']!r} resolved {len(found)} packages")
    return found[0]

def digest(root):
    h=hashlib.sha256()
    for p in sorted(x for x in root.rglob("*") if x.is_file() and ".git" not in x.parts):
        h.update(p.relative_to(root).as_posix().encode()+b"\0"); h.update(p.read_bytes()); h.update(b"\0")
    return h.hexdigest()

def copy_pkg(src,dst,force=False):
    if dst.exists():
        if not force: raise RuntimeError(f"Destination exists: {dst}; use --force to replace")
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True,exist_ok=True); shutil.copytree(src,dst,symlinks=True,ignore=shutil.ignore_patterns(".git"))

def expand_registry(reg):
    employees={}; support={}
    for sid,s in reg["sources"].items():
        for p in s.get("packages",[]):
            selector={"type":"repo_root","path":"."} if p.get("root") else ({"type":"path","path":p["path"]} if p.get("path") else {"type":"skill_name","name":p.get("name",p["id"]),"roots":p.get("roots",["."])})
            employees[p["id"]]={**p,"source":sid,"repo":s["repo"],"commit":s["commit"],"namespace":s["namespace"],"mode":"vendored" if p.get("vendored") else "upstream-fetch","target":f"imported/{s['namespace']}/{p['id']}","selector":selector,"deps":p.get("deps",[])}
    for p in reg.get("support",[]):
        s=reg["sources"][p["source"]]; support[p["id"]]={**p,"repo":s["repo"],"commit":s["commit"],"target":f"dependencies/{s['namespace']}/{p['id']}","selector":{"type":"path","path":p["path"]}}
    return employees,support

def plan(profile_name,root):
    reg=load("registry/packages.json"); profiles=load("registry/profiles.json"); employees,support=expand_registry(reg)
    if profile_name not in profiles["profiles"]: raise RuntimeError(f"Unknown profile: {profile_name}")
    prof=profiles["profiles"][profile_name]; out=[]; deps=set()
    if prof.get("include_foundation",True):
        for d in sorted((REPO_ROOT/"skills"/"foundation").iterdir()):
            if (d/"SKILL.md").exists(): out.append(("foundation",d.name,d,root/"foundation"/d.name,None))
    for cid in prof["employee_skills"]:
        p=employees[cid]; deps.update(p["deps"])
        src=REPO_ROOT/"skills"/p["target"] if p["mode"]=="vendored" else None
        out.append(("employee",cid,src,root/p["target"],p))
    for sid in sorted(deps):
        p=support[sid]; out.append(("support",sid,None,root/p["target"],p))
    return out

def cmd_install(a):
    root=Path(a.root).expanduser(); cache=Path(a.cache).expanduser(); jobs=plan(a.profile,root)
    if a.dry_run:
        for kind,cid,src,dst,p in jobs:
            origin=str(src) if src else f"{p['repo']}@{p['commit']}::{p['selector']}"
            print(f"{kind:10} {cid:32} -> {dst} [{origin}]")
        return
    root.mkdir(parents=True,exist_ok=True); installed=[]; checkouts={}
    for kind,cid,src,dst,p in jobs:
        if src is None:
            key=(p["repo"],p["commit"]); co=checkouts.get(key)
            if co is None: co=checkout(*key,cache,a.offline); checkouts[key]=co
            src=resolve(co,p["selector"],cid)
        if not (src/"SKILL.md").exists(): raise RuntimeError(f"{cid}: source package missing SKILL.md")
        copy_pkg(src,dst,a.force)
        installed.append({"kind":kind,"id":cid,"path":str(dst.relative_to(root)),"source_repo":p.get("repo") if p else "aiverse-filmmakers/AI-Verse-Skills","source_commit":p.get("commit") if p else None,"digest_sha256":digest(dst)})
        print("installed",cid)
    meta=root/".aiverse"; meta.mkdir(exist_ok=True); (meta/"installed.json").write_text(json.dumps({"schema_version":1,"profile":a.profile,"packages":installed},indent=2)+"\n")
    print(f"Installed {len(installed)} packages into {root}")

def cmd_doctor(a):
    root=Path(a.root).expanduser(); mf=root/".aiverse"/"installed.json"; errors=[]
    if not mf.exists(): errors.append(f"missing install manifest: {mf}")
    else:
        for p in json.loads(mf.read_text()).get("packages",[]):
            d=root/p["path"]
            if not (d/"SKILL.md").exists(): errors.append(f"{p['id']}: missing SKILL.md")
            elif digest(d)!=p.get("digest_sha256"): errors.append(f"{p['id']}: content digest changed")
    if errors:
        for e in errors: print("ERROR",e)
        raise SystemExit(1)
    print("AI-Verse-Skills doctor: healthy")

def cmd_list(a):
    reg=load("registry/packages.json"); rows=[]
    for sid,s in reg["sources"].items():
        for p in s.get("packages",[]): rows.append((p["rank"],p["id"],sid,"vendored" if p.get("vendored") else "upstream-fetch"))
    for rank,cid,sid,mode in sorted(rows): print(f"{rank:>2}  {cid:<32} {sid:<20} {mode}")

def cmd_uninstall(a):
    root=Path(a.root).expanduser()
    if not (root/".aiverse"/"installed.json").exists(): raise RuntimeError(f"Refusing to remove unrecognized directory: {root}")
    shutil.rmtree(root); print("Removed",root)

def cmd_adapt(a):
    root=Path(a.root).expanduser(); target=Path(a.target).expanduser(); mf=root/".aiverse"/"installed.json"
    if not mf.exists(): raise RuntimeError("Install the library before adapting it")
    runtimes={x["id"] for x in load("registry/runtime-adapters.json")["adapters"]}
    if a.runtime not in runtimes: raise RuntimeError(f"Unknown runtime: {a.runtime}")
    target.mkdir(parents=True,exist_ok=True); index=[]
    for p in json.loads(mf.read_text())["packages"]:
        if p["kind"]=="support": continue
        src=root/p["path"]; dst=target/p["id"]
        if dst.exists() or dst.is_symlink():
            if not a.force: raise RuntimeError(f"Adapter destination exists: {dst}")
            shutil.rmtree(dst) if dst.is_dir() and not dst.is_symlink() else dst.unlink()
        try: dst.symlink_to(src,target_is_directory=True); mode="symlink"
        except OSError: shutil.copytree(src,dst,symlinks=True); mode="copy"
        index.append({"id":p["id"],"source":str(src),"target":str(dst),"mode":mode})
    (target/".aiverse-adapter.json").write_text(json.dumps({"runtime":a.runtime,"packages":index},indent=2)+"\n"); print(f"Exposed {len(index)} packages to {target}")

def parser():
    p=argparse.ArgumentParser(prog="aiverse-skills"); p.add_argument("--root",default=str(DEFAULT_ROOT)); p.add_argument("--cache",default=str(DEFAULT_CACHE)); sub=p.add_subparsers(dest="cmd",required=True)
    q=sub.add_parser("install"); q.add_argument("--profile",default="full"); q.add_argument("--force",action="store_true"); q.add_argument("--offline",action="store_true"); q.add_argument("--dry-run",action="store_true"); q.set_defaults(fn=cmd_install)
    q=sub.add_parser("doctor"); q.set_defaults(fn=cmd_doctor)
    q=sub.add_parser("list"); q.set_defaults(fn=cmd_list)
    q=sub.add_parser("uninstall"); q.set_defaults(fn=cmd_uninstall)
    q=sub.add_parser("adapt"); q.add_argument("--runtime",required=True); q.add_argument("--target",required=True); q.add_argument("--force",action="store_true"); q.set_defaults(fn=cmd_adapt)
    return p

def main():
    a=parser().parse_args()
    try: a.fn(a)
    except RuntimeError as e: print("ERROR:",e,file=sys.stderr); raise SystemExit(2)
if __name__=="__main__": main()
