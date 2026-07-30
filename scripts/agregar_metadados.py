# -*- coding: utf-8 -*-
"""Agrega metadados dos JSONLs do dossie_judiciario para alimentar skills e grafos.

Saida: scripts/_agregado.json com:
- jurisprudencia: por area, lista de {id, tribunal, processo, ano, leading_case, tese_curta}
- legislacao_federal: por subarea, lista de {id, denominacao, ano, tipo, status}
- legislacao_local: por subarea, lista de {id, denominacao, ano, tipo}
- sumulas: por tribunal, total e principais areas
- enunciados: por fonte, total
- teses: por tribunal, total
"""
from __future__ import annotations
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def read_jsonl(path: Path):
    if not path.exists():
        return []
    out = []
    with path.open("r", encoding="utf-8") as f:
        for ln, raw in enumerate(f, 1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                out.append(json.loads(raw))
            except json.JSONDecodeError as e:
                print(f"[warn] {path}:{ln} {e}", file=sys.stderr)
    return out

def coletar_jurisprudencia():
    base = ROOT / "jurisprudencia"
    out = {}
    for area_dir in sorted(p for p in base.iterdir() if p.is_dir()):
        f = area_dir / "decisoes.jsonl"
        items = read_jsonl(f)
        out[area_dir.name] = [
            {
                "id": x.get("id"),
                "tribunal": x.get("tribunal"),
                "processo": x.get("numero_processo"),
                "relator": x.get("relator"),
                "ano": (x.get("data_julgamento") or "")[:4],
                "areas": x.get("area") or [],
                "leading_case": bool(x.get("leading_case")),
                "overruled": bool(x.get("overruled")),
                "ementa": (x.get("ementa_resumida") or "")[:160],
                "tese": (x.get("tese_firmada") or "")[:200],
            }
            for x in items
        ]
    return out

def coletar_legislacao(base_subdir: str):
    base = ROOT / base_subdir
    out = {}
    if not base.exists():
        return out
    for sub in sorted(p for p in base.iterdir() if p.is_dir()):
        items = []
        for f in sub.glob("*.jsonl"):
            items.extend(read_jsonl(f))
        out[sub.name] = [
            {
                "id": x.get("id"),
                "tipo": x.get("tipo"),
                "denominacao": x.get("denominacao"),
                "numero": x.get("numero"),
                "ano": x.get("ano"),
                "status": x.get("status"),
                "areas": x.get("area") or [],
                "tribunais_ref": x.get("tribunal_referencia") or [],
            }
            for x in items
        ]
    return out

def coletar_sumulas():
    base = ROOT / "sumulas"
    out = {}
    for trib_dir in sorted(p for p in base.iterdir() if p.is_dir()):
        all_items = []
        for f in trib_dir.glob("*.jsonl"):
            all_items.extend(read_jsonl(f))
        areas = defaultdict(int)
        for x in all_items:
            a = x.get("area") or "outros"
            areas[a] += 1
        out[trib_dir.name] = {
            "total": len(all_items),
            "por_area": dict(sorted(areas.items(), key=lambda kv: -kv[1])),
            "primeiros_numeros": sorted({x.get("numero") for x in all_items if x.get("numero")}, key=lambda v: (str(v)))[:10],
        }
    return out

def coletar_enunciados():
    base = ROOT / "enunciados"
    out = {}
    if not base.exists():
        return out
    for fonte_dir in sorted(p for p in base.iterdir() if p.is_dir()):
        total = 0
        for f in fonte_dir.glob("*.jsonl"):
            total += sum(1 for _ in f.open("r", encoding="utf-8"))
        out[fonte_dir.name] = total
    return out

def coletar_teses():
    base = ROOT / "teses_precedentes"
    out = {}
    if not base.exists():
        return out
    for trib_dir in sorted(p for p in base.iterdir() if p.is_dir()):
        total = 0
        for f in trib_dir.glob("*.jsonl"):
            total += sum(1 for _ in f.open("r", encoding="utf-8"))
        out[trib_dir.name] = total
    return out

def main():
    agregado = {
        "jurisprudencia": coletar_jurisprudencia(),
        "legislacao_federal": coletar_legislacao("legislacao_federal"),
        "legislacao_local": coletar_legislacao("legislacao_local"),
        "sumulas": coletar_sumulas(),
        "enunciados": coletar_enunciados(),
        "teses_precedentes": coletar_teses(),
    }
    saida = ROOT / "scripts" / "_agregado.json"
    saida.write_text(json.dumps(agregado, ensure_ascii=False, indent=2), encoding="utf-8")
    # Resumo no stdout
    print(f"jurisprudencia: {sum(len(v) for v in agregado['jurisprudencia'].values())} decisoes em {len(agregado['jurisprudencia'])} areas")
    print(f"legislacao_federal: {sum(len(v) for v in agregado['legislacao_federal'].values())} normas em {len(agregado['legislacao_federal'])} subareas")
    print(f"legislacao_local: {sum(len(v) for v in agregado['legislacao_local'].values())} normas em {len(agregado['legislacao_local'])} subareas")
    print(f"sumulas: {sum(v['total'] for v in agregado['sumulas'].values())} sumulas em {len(agregado['sumulas'])} tribunais")
    print(f"enunciados: {sum(agregado['enunciados'].values())} enunciados em {len(agregado['enunciados'])} fontes")
    print(f"teses_precedentes: {sum(agregado['teses_precedentes'].values())} teses em {len(agregado['teses_precedentes'])} tribunais")
    print(f"saida: {saida}")

if __name__ == "__main__":
    main()
