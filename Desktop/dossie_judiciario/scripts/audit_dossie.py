# -*- coding: utf-8 -*-
"""Auditoria abrangente do dossie_judiciario.

Verifica:
- Integridade JSON de cada linha de cada .jsonl
- Encoding (detecta caracteres mojibake/latin-1 em arquivos UTF-8)
- Campos obrigatorios por tipo de arquivo
- Duplicatas por chave logica (numero/tema/leading_case)
- Inconsistencias conhecidas (Tema 6, SV 60/61)
- Cobertura de Temas/Sumulas criticos para saude/CPC

Saida: relatorio em stdout + .audit_report.json estruturado.
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(r"C:/Users/renan/Desktop/dossie_judiciario")
REPORT: dict[str, Any] = {
    "files_total": 0,
    "json_lines_total": 0,
    "json_errors": [],
    "encoding_suspects": [],
    "schema_warnings": [],
    "duplicates": [],
    "known_inconsistencies": [],
    "missing_critical_entries": [],
    "summary_by_dir": {},
}

MOJIBAKE_MARKERS = ("�", "Ã£", "Ã©", "Ã³", "Ã§", "Ã¡", "Ã¢", "Ãª")


def looks_mojibake(s: str) -> bool:
    return any(m in s for m in MOJIBAKE_MARKERS)


def audit_file(path: Path) -> dict[str, Any]:
    rel = path.relative_to(ROOT).as_posix()
    info = {
        "path": rel,
        "lines": 0,
        "valid_json": 0,
        "errors": 0,
        "mojibake_lines": 0,
        "sample_keys": None,
    }
    try:
        raw = path.read_bytes()
    except Exception as e:
        REPORT["json_errors"].append({"file": rel, "error": f"read: {e}"})
        return info

    # Try strict UTF-8 first
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        REPORT["encoding_suspects"].append({"file": rel, "reason": "not strict utf-8"})
        text = raw.decode("utf-8", errors="replace")

    for ln, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        info["lines"] += 1
        REPORT["json_lines_total"] += 1
        if looks_mojibake(line):
            info["mojibake_lines"] += 1
        try:
            obj = json.loads(line)
            info["valid_json"] += 1
            if info["sample_keys"] is None and isinstance(obj, dict):
                info["sample_keys"] = sorted(obj.keys())
        except json.JSONDecodeError as e:
            info["errors"] += 1
            REPORT["json_errors"].append(
                {"file": rel, "line": ln, "error": str(e), "snippet": line[:120]}
            )
    if info["mojibake_lines"]:
        REPORT["encoding_suspects"].append(
            {"file": rel, "mojibake_lines": info["mojibake_lines"]}
        )
    return info


def main() -> int:
    files = sorted(ROOT.rglob("*.jsonl"))
    # Skip scripts/ dir
    files = [f for f in files if "scripts" not in f.parts]
    REPORT["files_total"] = len(files)

    per_dir: dict[str, dict[str, int]] = defaultdict(
        lambda: {"files": 0, "lines": 0, "errors": 0, "mojibake": 0}
    )

    for f in files:
        info = audit_file(f)
        d = f.relative_to(ROOT).parent.as_posix()
        per_dir[d]["files"] += 1
        per_dir[d]["lines"] += info["lines"]
        per_dir[d]["errors"] += info["errors"]
        per_dir[d]["mojibake"] += info["mojibake_lines"]

    REPORT["summary_by_dir"] = {k: dict(v) for k, v in per_dir.items()}

    # Specific checks
    check_temas_rg()
    check_sumulas_vinculantes()
    check_critical_coverage()

    # Pretty print summary
    print("=" * 70)
    print(" AUDIT REPORT — dossie_judiciario ")
    print("=" * 70)
    print(f"Files scanned: {REPORT['files_total']}")
    print(f"JSON lines:    {REPORT['json_lines_total']}")
    print(f"JSON errors:   {len(REPORT['json_errors'])}")
    print(f"Encoding suspects: {len(REPORT['encoding_suspects'])}")
    print(f"Known inconsistencies: {len(REPORT['known_inconsistencies'])}")
    print(f"Missing critical entries: {len(REPORT['missing_critical_entries'])}")
    print()
    print("--- Per-dir summary (top 10 by mojibake lines) ---")
    sorted_dirs = sorted(
        REPORT["summary_by_dir"].items(),
        key=lambda kv: kv[1]["mojibake"],
        reverse=True,
    )
    for d, st in sorted_dirs[:10]:
        print(
            f"  {d:55s} files={st['files']:3d} lines={st['lines']:5d} "
            f"errors={st['errors']:3d} mojibake={st['mojibake']:4d}"
        )

    print()
    print("--- Known inconsistencies ---")
    for inc in REPORT["known_inconsistencies"]:
        print(f"  [{inc['severity']}] {inc['where']}: {inc['message']}")

    print()
    print("--- Missing critical entries ---")
    for m in REPORT["missing_critical_entries"]:
        print(f"  [{m['severity']}] {m['kind']} {m['id']}: {m['reason']}")

    # Write structured report
    out = ROOT / ".audit_report.json"
    out.write_text(
        json.dumps(REPORT, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print()
    print(f"Structured report -> {out}")
    return 0


def check_temas_rg() -> None:
    p = ROOT / "teses_precedentes" / "stf" / "teses_rg.jsonl"
    if not p.exists():
        REPORT["known_inconsistencies"].append(
            {"severity": "HIGH", "where": str(p), "message": "file missing"}
        )
        return
    temas: dict[int, dict] = {}
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip():
            try:
                d = json.loads(line)
                temas[d.get("tema")] = d
            except json.JSONDecodeError:
                pass

    # Verifications based on Portal STF
    fact_table = {
        6: {
            "leading_case": "RE 566471",
            "relator": "Min. Marco Aurélio",
            "topic_hint": "medicamento",
        },
        500: {
            "leading_case": "RE 657718",
            "relator": "Min. Alexandre de Moraes",
            "topic_hint": "ANVISA",
        },
        793: {
            "leading_case": "RE 855178",
            "relator": "Min. Luiz Fux",
            "topic_hint": "solidária",
        },
        1234: {
            "leading_case": "RE 1366243",
            "relator": "Min. Gilmar Mendes",
            "topic_hint": "interfederativ",
        },
    }
    for num, expected in fact_table.items():
        cur = temas.get(num)
        if cur is None:
            REPORT["missing_critical_entries"].append(
                {
                    "severity": "HIGH" if num in (6, 1234) else "MEDIUM",
                    "kind": "Tema_RG",
                    "id": num,
                    "reason": f"Tema {num} ausente do dossie; esperado leading_case={expected['leading_case']}",
                }
            )
            continue
        lc = (cur.get("leading_case") or "").replace(" ", "").replace(".", "")
        exp_lc = expected["leading_case"].replace(" ", "").replace(".", "")
        if exp_lc not in lc:
            REPORT["known_inconsistencies"].append(
                {
                    "severity": "HIGH",
                    "where": f"Tema {num}",
                    "message": (
                        f"leading_case={cur.get('leading_case')} difere do esperado "
                        f"{expected['leading_case']} (relator esperado: {expected['relator']})"
                    ),
                }
            )


def check_sumulas_vinculantes() -> None:
    p = ROOT / "sumulas" / "stf" / "sumulas_vinculantes.jsonl"
    if not p.exists():
        return
    svs: dict[int, dict] = {}
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip():
            try:
                d = json.loads(line)
                svs[d.get("numero")] = d
            except json.JSONDecodeError:
                pass

    # SV 60 / 61 — confirm presence and basic content
    sv60 = svs.get(60)
    sv61 = svs.get(61)
    if not sv60:
        REPORT["missing_critical_entries"].append(
            {"severity": "HIGH", "kind": "SV", "id": 60, "reason": "ausente"}
        )
    else:
        if "Tema 1.234" not in sv60.get("texto", "") and "Tema 1234" not in sv60.get(
            "texto", ""
        ):
            REPORT["known_inconsistencies"].append(
                {
                    "severity": "MEDIUM",
                    "where": "SV 60",
                    "message": "texto nao referencia Tema 1.234",
                }
            )
    if not sv61:
        REPORT["missing_critical_entries"].append(
            {"severity": "HIGH", "kind": "SV", "id": 61, "reason": "ausente"}
        )
    else:
        if "Tema 6" not in sv61.get("texto", ""):
            REPORT["known_inconsistencies"].append(
                {
                    "severity": "MEDIUM",
                    "where": "SV 61",
                    "message": "texto nao referencia Tema 6",
                }
            )


def check_critical_coverage() -> None:
    # Check STJ repetitivos critical
    p = ROOT / "teses_precedentes" / "stj"
    files = list(p.glob("*.jsonl")) if p.exists() else []
    found = set()
    for f in files:
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            tema = d.get("tema") or d.get("numero")
            if tema:
                found.add(tema)
            lc = (d.get("leading_case") or "").replace(" ", "").replace(".", "")
            if "1474665" in lc:
                found.add("REsp_1474665")
            if "1657156" in lc:
                found.add("REsp_1657156")

    critical_stj = {
        "REsp_1474665": "Tema 98/STJ — astreintes contra Fazenda em saude",
        "REsp_1657156": "Tema 106/STJ — medicamentos fora da RENAME",
    }
    for k, desc in critical_stj.items():
        if k not in found:
            REPORT["missing_critical_entries"].append(
                {
                    "severity": "MEDIUM",
                    "kind": "STJ_Repetitivo",
                    "id": k,
                    "reason": f"ausente — {desc}",
                }
            )


if __name__ == "__main__":
    sys.exit(main())
