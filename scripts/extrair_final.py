#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrator FINAL de enunciados das Jornadas de Direito Civil CJF/STJ.
"""

import pdfplumber
import re
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PDF_DIR = os.path.expanduser(r"~\.claude\projects\C--Users-renan-Desktop-jurisprud-ncia-e-doutrina\69eab488-78ab-4580-96b2-2a33834e0a0b\tool-results")

JORNADAS_META = {
    "I": {"numero": "I", "ano": 2002, "local": "Brasilia-DF", "total_enunciados": 137, "periodo": "12 a 13 de setembro de 2002"},
    "III": {"numero": "III", "ano": 2004, "local": "Brasilia-DF", "total_enunciados": 134, "periodo": "1 a 3 de dezembro de 2004"},
    "IV": {"numero": "IV", "ano": 2006, "local": "Brasilia-DF", "total_enunciados": 125, "periodo": "25 e 26 de outubro de 2006"},
    "V": {"numero": "V", "ano": 2011, "local": "Brasilia-DF", "total_enunciados": 133, "periodo": "8 e 9 de novembro de 2011"},
    "VI": {"numero": "VI", "ano": 2013, "local": "Brasilia-DF", "total_enunciados": 46, "periodo": "11 e 12 de marco de 2013"},
    "VII": {"numero": "VII", "ano": 2015, "local": "Brasilia-DF", "total_enunciados": 37, "periodo": "28 e 29 de setembro de 2015"},
    "VIII": {"numero": "VIII", "ano": 2018, "local": "Brasilia-DF", "total_enunciados": 32, "periodo": "26 e 27 de abril de 2018"},
    "IX": {"numero": "IX", "ano": 2022, "local": "Brasilia-DF", "total_enunciados": 49, "periodo": "19 e 20 de outubro de 2022"},
}

JORNADA_RANGES = {
    "I": (1, 137),
    "III": (138, 271),
    "IV": (272, 396),
    "V": (397, 529),
    "VI": (530, 575),
    "VII": (576, 612),
    "VIII": (613, 644),
    "IX": (645, 693),
}

def get_jornada(num):
    for j, (s, e) in JORNADA_RANGES.items():
        if s <= num <= e:
            return j
    return None

def extract_pdf_text(filepath):
    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text

def parse_compilacao(text):
    """I, III, IV, V Jornadas - formato: 'numero – Art. XX: Texto'"""
    enunciados = []
    # Pattern para o formato da compilacao
    pattern = r'(\d+)\s*[–\-]\s*(Arts?\.\s*[^:]+):\s*(.*?)(?=\n\d+\s*[–\-]\s*Arts?\.|$)'
    matches = re.finditer(pattern, text, re.DOTALL)
    for m in matches:
        num = int(m.group(1))
        artigo = m.group(2).strip()
        texto_raw = m.group(3).strip()
        # Limpar
        texto = ' '.join(texto_raw.split())
        # Remover headers de pagina
        texto = re.sub(r'\d+\s+(?:I|III|IV|V)(?:\s*,\s*(?:I|III|IV|V))*\s*Jornadas?\s+de\s+Direito\s+Civil\s*\d*', '', texto)
        texto = re.sub(r'\d+\s+Enunciados\s+aprovados', '', texto)
        texto = texto.strip()
        if num > 0 and num <= 529 and texto:
            enunciados.append({"numero": num, "texto": texto, "artigo_referencia": artigo})
    return enunciados

def parse_standard(text):
    """VI, VII, VIII, IX - formato: 'ENUNCIADO 530 – Texto'"""
    enunciados = []
    # Split por ENUNCIADO
    parts = re.split(r'(ENUNCIADO\s+\d+\s*[–\-‐‑])', text)

    i = 1
    while i < len(parts):
        header = parts[i]
        num_match = re.search(r'ENUNCIADO\s+(\d+)', header)
        if not num_match:
            i += 1
            continue
        num = int(num_match.group(1))

        body = parts[i+1] if i+1 < len(parts) else ""
        i += 2

        # Separar texto da justificativa
        body_parts = re.split(r'\n\s*Justificativa\s*:', body, maxsplit=1, flags=re.IGNORECASE)
        pre_justificativa = body_parts[0]

        # Separar texto do artigo
        text_parts = re.split(r'\n\s*(?:Artigos?|Parte da legisla[çc][aã]o|Refer[eê]ncia [Ll]egislativa)\s*:', pre_justificativa, maxsplit=1, flags=re.IGNORECASE)

        texto = ' '.join(text_parts[0].split()).strip()

        artigo = ""
        if len(text_parts) > 1:
            artigo = ' '.join(text_parts[1].split()).strip()
        else:
            # Tentar extrair artigo do bloco completo
            artigo_match = re.search(r'(?:Artigos?|Parte da legisla[çc][aã]o|Refer[eê]ncia [Ll]egislativa)\s*:\s*(.*?)(?:\n|Justificativa|$)', body, re.IGNORECASE)
            if artigo_match:
                artigo = ' '.join(artigo_match.group(1).split()).strip()

        # Para IX Jornada, o artigo pode estar no inicio do texto: "Art. XXX: Texto..."
        if not artigo and texto.startswith("Art."):
            art_match = re.match(r'(Art\.\s*[\d\w\-\.\,\s§ºªeEincIIV]+?):\s*(.*)', texto)
            if art_match:
                artigo = art_match.group(1).strip()
                texto = art_match.group(2).strip()

        if num > 0 and texto:
            enunciados.append({"numero": num, "texto": texto, "artigo_referencia": artigo})

    return enunciados

def determine_area(text, numero):
    """Determina area tematica pelo cabecalho de secao mais proximo."""
    pos = -1
    for pat in [f"ENUNCIADO {numero} ", f"ENUNCIADO {numero}\n", f"ENUNCIADO {numero}–", f"ENUNCIADO {numero} –", f"ENUNCIADO {numero} -",
                f"{numero} –", f"{numero} -"]:
        idx = text.find(pat)
        if idx != -1:
            pos = idx
            break

    if pos == -1:
        return "parte geral"

    preceding = text[:pos].upper()

    headers = [
        ("DIREITO DIGITAL E NOVOS DIREITOS", "direito digital"),
        ("DIREITO DIGITAL", "direito digital"),
        ("NOVOS DIREITOS", "direito digital"),
        ("FAMÍLIA E SUCESSÕES", "família e sucessões"),
        ("DIREITO DE FAMÍLIA E SUCESSÕES", "família e sucessões"),
        ("FAMILIA E SUCESS", "família e sucessões"),
        ("DIREITO DE FAM", "família"),
        ("SUCESS", "sucessões"),
        ("RESPONSABILIDADE CIVIL", "responsabilidade civil"),
        ("DIREITO DAS OBRIGA", "obrigações"),
        ("OBRIGA", "obrigações"),
        ("CONTRATOS", "contratos"),
        ("DIREITO DAS COISAS", "direitos reais"),
        ("PROPRIEDADE INTELECTUAL", "direitos reais"),
        ("DIREITO DA EMPRESA", "empresa"),
        ("EMPRESA", "empresa"),
        ("PARTE GERAL", "parte geral"),
    ]

    best_area = "parte geral"
    best_pos = -1

    for header, area in headers:
        lp = preceding.rfind(header)
        if lp > best_pos:
            best_pos = lp
            best_area = area

    return best_area

def main():
    print("=" * 70)
    print("EXTRATOR FINAL - Enunciados Jornadas de Direito Civil CJF/STJ")
    print("=" * 70)

    all_enunciados = {}

    # 1) Compilacao I, III, IV, V
    fp = os.path.join(PDF_DIR, "webfetch-1773497804421-fgaq01.pdf")
    if os.path.exists(fp):
        print("\n  [1/4] Compilacao I, III, IV, V...")
        text = extract_pdf_text(fp)
        encs = parse_compilacao(text)
        print(f"    {len(encs)} enunciados")
        for en in encs:
            en["area_tematica"] = determine_area(text, en["numero"])
            all_enunciados[en["numero"]] = en

    # 2) VI Jornada
    fp = os.path.join(PDF_DIR, "webfetch-1773497806418-cj6gh0.pdf")
    if os.path.exists(fp):
        print("\n  [2/4] VI Jornada...")
        text = extract_pdf_text(fp)
        encs = parse_standard(text)
        encs = [e for e in encs if 530 <= e["numero"] <= 575]
        print(f"    {len(encs)} enunciados")
        for en in encs:
            en["area_tematica"] = determine_area(text, en["numero"])
            all_enunciados[en["numero"]] = en

    # 3) VII Jornada
    fp = os.path.join(PDF_DIR, "webfetch-1773497807545-uzd3uu.pdf")
    if os.path.exists(fp):
        print("\n  [3/4] VII Jornada...")
        text = extract_pdf_text(fp)
        encs = parse_standard(text)
        encs = [e for e in encs if 576 <= e["numero"] <= 612]
        print(f"    {len(encs)} enunciados")
        for en in encs:
            en["area_tematica"] = determine_area(text, en["numero"])
            all_enunciados[en["numero"]] = en

    # 4) VIII Jornada
    fp = os.path.join(PDF_DIR, "webfetch-1773498828743-hzt55r.pdf")
    if os.path.exists(fp):
        print("\n  [4a/4] VIII Jornada...")
        text = extract_pdf_text(fp)
        encs = parse_standard(text)
        encs = [e for e in encs if 613 <= e["numero"] <= 644]
        print(f"    {len(encs)} enunciados")
        for en in encs:
            en["area_tematica"] = determine_area(text, en["numero"])
            all_enunciados[en["numero"]] = en

    # 5) IX Jornada
    fp = os.path.join(PDF_DIR, "webfetch-1773497808951-js46v2.pdf")
    if os.path.exists(fp):
        print("\n  [4b/4] IX Jornada...")
        text = extract_pdf_text(fp)
        encs = parse_standard(text)
        encs = [e for e in encs if 645 <= e["numero"] <= 693]
        print(f"    {len(encs)} enunciados")
        for en in encs:
            en["area_tematica"] = determine_area(text, en["numero"])
            all_enunciados[en["numero"]] = en

    # Adicionar jornada e ano
    for num, en in all_enunciados.items():
        j = get_jornada(num)
        if j:
            en["jornada"] = j
            en["ano"] = JORNADAS_META[j]["ano"]
        else:
            en["jornada"] = "?"
            en["ano"] = 0

    sorted_enunciados = sorted(all_enunciados.values(), key=lambda x: x["numero"])

    # Estatisticas
    print(f"\n{'='*70}")
    print(f"  RESULTADO: {len(sorted_enunciados)} enunciados extraidos")
    print(f"{'='*70}")
    print(f"\n  {'Jornada':>10} | {'Ano':>4} | {'Ext':>4} | {'Esp':>4} | {'%':>5}")
    print(f"  {'-'*10}-+-{'-'*4}-+-{'-'*4}-+-{'-'*4}-+-{'-'*5}")
    total_e = 0
    total_x = 0
    for j in ["I", "III", "IV", "V", "VI", "VII", "VIII", "IX"]:
        c = sum(1 for e in sorted_enunciados if e.get("jornada") == j)
        exp = JORNADAS_META[j]["total_enunciados"]
        pct = f"{c/exp*100:.0f}%" if exp else "?"
        print(f"  {j:>10} | {JORNADAS_META[j]['ano']:>4} | {c:>4} | {exp:>4} | {pct:>5}")
        total_e += c
        total_x += exp
    print(f"  {'-'*10}-+-{'-'*4}-+-{'-'*4}-+-{'-'*4}-+-{'-'*5}")
    print(f"  {'TOTAL':>10} |      | {total_e:>4} | {total_x:>4} | {total_e/total_x*100:.0f}%")

    # Areas
    areas = {}
    for e in sorted_enunciados:
        a = e.get("area_tematica", "?")
        areas[a] = areas.get(a, 0) + 1
    print(f"\n  Areas tematicas:")
    for a, c in sorted(areas.items(), key=lambda x: -x[1]):
        print(f"    {a}: {c}")

    # Gerar JSONL
    output = r"C:\Users\renan\Desktop\dossie_judiciario\enunciados\jornadas_direito_civil\enunciados.jsonl"
    with open(output, "w", encoding="utf-8") as f:
        meta = {
            "tipo": "metadados_jornadas",
            "descricao": "Enunciados das Jornadas de Direito Civil do Conselho da Justica Federal (CJF/STJ)",
            "fonte": "PDFs oficiais do CJF - www.cjf.jus.br",
            "total_jornadas": 8,
            "nota": "Nao houve II Jornada de Direito Civil. A II Jornada foi de Direito Comercial.",
            "jornadas": JORNADAS_META
        }
        f.write(json.dumps(meta, ensure_ascii=False) + "\n")
        for e in sorted_enunciados:
            rec = {
                "tipo": "enunciado",
                "numero": e["numero"],
                "jornada": e.get("jornada", ""),
                "ano": e.get("ano", 0),
                "texto": e["texto"],
                "artigo_referencia": e.get("artigo_referencia", ""),
                "area_tematica": e.get("area_tematica", "")
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    sz = os.path.getsize(output)
    print(f"\n  Arquivo: {output}")
    print(f"  Tamanho: {sz/1024:.1f} KB")
    print(f"  Registros: {len(sorted_enunciados) + 1}")

    # Verificar lacunas
    nums = set(e["numero"] for e in sorted_enunciados)
    gaps = []
    for j, (s, end) in JORNADA_RANGES.items():
        for n in range(s, end+1):
            if n not in nums:
                gaps.append((j, n))
    if gaps:
        print(f"\n  Enunciados faltantes ({len(gaps)}):")
        by_j = {}
        for j, n in gaps:
            by_j.setdefault(j, []).append(n)
        for j, ns in by_j.items():
            if len(ns) <= 10:
                print(f"    {j}: {ns}")
            else:
                print(f"    {j}: {ns[:5]}...{ns[-5:]} ({len(ns)} total)")

if __name__ == "__main__":
    main()
