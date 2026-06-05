#!/usr/bin/env python3
"""Valida a integridade do repositorio: OpenAPI valido, catalogo consistente, links existem."""
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
METHODS = ("get", "post", "put", "delete", "patch", "head", "options")
errors = []
warnings = []
checked = {"specs": 0, "ops": 0, "links": 0}


def err(m):
    errors.append(m)


def warn(m):
    warnings.append(m)


# 1) Todo openapi.json: JSON valido + estrutura + contagens
spec_counts = {}  # (app,version) -> (ops, paths, categories)
for root, dirs, files in os.walk(BASE):
    if ".git" in root:
        continue
    if "openapi.json" in files:
        rel = os.path.relpath(os.path.join(root, "openapi.json"), BASE).replace("\\", "/")
        try:
            spec = json.load(open(os.path.join(root, "openapi.json"), encoding="utf-8"))
        except Exception as e:
            err(f"{rel}: JSON invalido ({e})")
            continue
        checked["specs"] += 1
        for k in ("openapi", "info", "paths"):
            if k not in spec:
                err(f"{rel}: falta chave '{k}'")
        paths = spec.get("paths", {})
        ops = 0
        bytag = {}
        for p, item in paths.items():
            for m in METHODS:
                if m in item:
                    ops += 1
                    for tg in (item[m].get("tags") or ["_"]):
                        bytag.setdefault(tg, 0)
                        bytag[tg] += 1
        checked["ops"] += ops
        parts = rel.split("/")
        spec_counts[(parts[0], parts[1])] = (ops, len(paths), len(bytag))

# 2) catalog.json consistente com os specs
cat = json.load(open(os.path.join(BASE, "catalog.json"), encoding="utf-8"))
for app, d in cat["apps"].items():
    for v in d["versions"]:
        key = (app, v["version"])
        # arquivos existem
        for f in (v["openapi"], v["reference"]):
            checked["links"] += 1
            if not os.path.exists(os.path.join(BASE, f)):
                err(f"catalog: arquivo inexistente {f}")
        # contagens batem com o spec
        if key in spec_counts:
            ops, paths, cats = spec_counts[key]
            if v["operations"] != ops:
                err(f"{app}/{v['version']}: operations catalogo={v['operations']} != spec={ops}")
            if v["paths"] != paths:
                err(f"{app}/{v['version']}: paths catalogo={v['paths']} != spec={paths}")
            if v.get("categories") != cats:
                warn(f"{app}/{v['version']}: categories catalogo={v.get('categories')} != spec={cats}")
        else:
            err(f"catalog: sem openapi.json correspondente para {app}/{v['version']}")

# 3) links relativos nos READMEs/llms/catalog apontam para arquivos existentes
def check_md_links(fname):
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        return
    text = open(path, encoding="utf-8").read()
    for m in re.finditer(r"\]\((?!https?://|#)([^)]+)\)", text):
        target = m.group(1).split("#")[0]
        if target.startswith("./"):
            target = target[2:]
        if not target:
            continue
        checked["links"] += 1
        if not os.path.exists(os.path.join(BASE, target)):
            err(f"{fname}: link quebrado -> {target}")

for f in ("README.md", "README.en.md"):
    check_md_links(f)

# llms.txt: caminhos openapi/reference citados existem
llms = open(os.path.join(BASE, "llms.txt"), encoding="utf-8").read()
for m in re.finditer(r"`([a-z0-9\-]+/v[^`]+\.(?:json|md))`", llms):
    checked["links"] += 1
    if not os.path.exists(os.path.join(BASE, m.group(1))):
        err(f"llms.txt: caminho inexistente -> {m.group(1)}")

# Resultado
print(f"Specs validos: {checked['specs']} | operacoes: {checked['ops']} | links checados: {checked['links']}")
if warnings:
    print(f"\nAVISOS ({len(warnings)}):")
    for w in warnings:
        print(f"  ! {w}")
if errors:
    print(f"\nERROS ({len(errors)}):")
    for e in errors:
        print(f"  X {e}")
    sys.exit(1)
print("\nOK: tudo valido e consistente.")
