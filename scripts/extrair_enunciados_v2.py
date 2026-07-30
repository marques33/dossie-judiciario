#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrator v2 de enunciados das Jornadas de Direito Civil do CJF/STJ.
Processa os PDFs oficiais baixados do site do CJF com multiplos formatos.
"""

import pdfplumber
import re
import json
import os
import sys

PDF_DIR = os.path.expanduser(r"~\.claude\projects\C--Users-renan-Desktop-jurisprud-ncia-e-doutrina\69eab488-78ab-4580-96b2-2a33834e0a0b\tool-results")

PDF_FILES = {
    "compilacao": "webfetch-1773497804421-fgaq01.pdf",
    "vi_jornada": "webfetch-1773497806418-cj6gh0.pdf",
    "vii_jornada": "webfetch-1773497807545-uzd3uu.pdf",
    "viii_ix_jornada": "webfetch-1773497808951-js46v2.pdf",
}

JORNADAS_META = {
    "I": {"numero": "I", "ano": 2002, "local": "Brasilia-DF", "total_enunciados": 138, "periodo": "12 a 13 de setembro de 2002"},
    "III": {"numero": "III", "ano": 2004, "local": "Brasilia-DF", "total_enunciados": 134, "periodo": "1 a 3 de dezembro de 2004"},
    "IV": {"numero": "IV", "ano": 2006, "local": "Brasilia-DF", "total_enunciados": 125, "periodo": "25 e 26 de outubro de 2006"},
    "V": {"numero": "V", "ano": 2011, "local": "Brasilia-DF", "total_enunciados": 133, "periodo": "8 e 9 de novembro de 2011"},
    "VI": {"numero": "VI", "ano": 2013, "local": "Brasilia-DF", "total_enunciados": 46, "periodo": "11 e 12 de marco de 2013"},
    "VII": {"numero": "VII", "ano": 2015, "local": "Brasilia-DF", "total_enunciados": 37, "periodo": "28 e 29 de setembro de 2015"},
    "VIII": {"numero": "VIII", "ano": 2022, "local": "Brasilia-DF (formato hibrido)", "total_enunciados": 32, "periodo": "25 e 26 de abril de 2022"},
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

def fix_encoding(text):
    """Tenta corrigir problemas de encoding comuns em PDFs brasileiros."""
    replacements = {
        '�': 'ã', '�': 'á', '�': 'é', '�': 'í', '�': 'ó', '�': 'ú',
        '�': 'ç', '�': 'Ç', '�': 'ê', '�': 'ô', '�': 'â',
        '�': 'à', '�': 'õ', '�': 'ü',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def extract_text_from_pdf(filepath, page_range=None):
    """Extrai texto de um PDF, opcionalmente apenas de certas paginas."""
    full_text = ""
    try:
        with pdfplumber.open(filepath) as pdf:
            pages = pdf.pages
            if page_range:
                start, end = page_range
                pages = pages[start:end]
            for page in pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
    except Exception as ex:
        print(f"  Erro: {ex}", file=sys.stderr)
    return full_text

def parse_compilacao(text):
    """
    Parse enunciados do formato da compilacao I/III/IV/V:
    'numero - Art. XX: Texto do enunciado.'
    ou 'numero - Arts. XX e YY: Texto...'
    """
    enunciados = []

    # Padrao: numero seguido de travessao e art
    # Ex: "1 – Art. 2º: A proteção que o Código..."
    # ou: "1 � Art. 2�: A prote��o..."
    pattern = r'(\d+)\s*[–\-�]\s*(Arts?\.\s*[^:]+):\s*(.*?)(?=\n\d+\s*[–\-�]\s*Arts?\.|$)'

    matches = re.finditer(pattern, text, re.DOTALL)

    for match in matches:
        numero = int(match.group(1))
        artigo = match.group(2).strip()
        texto_raw = match.group(3).strip()
        # Limpar texto - remover quebras de linha extras
        texto = ' '.join(texto_raw.split())
        # Remover referencia a pagina do PDF (ex: "17 I, III, IV e V Jornadas...")
        texto = re.sub(r'\d+\s+(?:I|III|IV|V|Enunciados)\s*(?:,\s*(?:I|III|IV|V))*\s*Jornadas?\s+de\s+Direito\s+Civil\s*\d*', '', texto)
        texto = re.sub(r'\d+\s+Enunciados\s+aprovados', '', texto)
        texto = texto.strip()

        if numero > 0 and texto:
            enunciados.append({
                "numero": numero,
                "texto": texto,
                "artigo_referencia": artigo
            })

    return enunciados

def parse_standard(text):
    """
    Parse enunciados do formato padrao (VI, VII, VIII, IX):
    'ENUNCIADO 530 – Texto do enunciado.'
    """
    enunciados = []

    # Encontrar todos os enunciados
    pattern = r'ENUNCIADO\s+(\d+)\s*[–\-]\s*(.*?)(?=\nENUNCIADO\s+\d+\s*[–\-]|\nPARTE\s+GERAL|\nDIREITO\s+D[AE]S?\s|\nRESPONSABILIDADE|\nOBRIGA[ÇC][ÕO]ES|\nCONTRATOS|\nFAM[IÍ]LIA|\nSUCESS[ÕO]ES|\nCOMISS[ÕO]ES\s+DE\s+TRABALHO|\nLISTA\s+DE\s+AUTORES|\nREFER[EÊ]NCIAS|$)'

    matches = re.finditer(pattern, text, re.DOTALL | re.IGNORECASE)

    for match in matches:
        numero = int(match.group(1))
        bloco = match.group(2).strip()

        # Separar texto do enunciado da justificativa e artigo
        # O texto do enunciado vai ate "Artigo:", "Parte da legislação:", etc.
        parts = re.split(r'\n\s*(?:Artigos?|Parte da legisla[çc][aã]o|Refer[eê]ncia [Ll]egislativa|Justificativa)\s*:', bloco, maxsplit=1, flags=re.IGNORECASE)

        texto = parts[0].strip()
        texto = ' '.join(texto.split())

        # Extrair artigo de referencia
        artigo = ""
        artigo_match = re.search(r'(?:Artigos?|Parte da legisla[çc][aã]o|Refer[eê]ncia [Ll]egislativa)\s*:\s*(.*?)(?:\n|Justificativa|$)', bloco, re.IGNORECASE)
        if artigo_match:
            artigo = artigo_match.group(1).strip()
            artigo = ' '.join(artigo.split())

        if numero > 0 and texto:
            enunciados.append({
                "numero": numero,
                "texto": texto,
                "artigo_referencia": artigo
            })

    return enunciados

def determine_area_from_context(full_text, numero):
    """Determina a area tematica pelo cabecalho de secao mais proximo."""
    # Encontrar posicao do enunciado no texto
    pos = -1
    for pat in [f"ENUNCIADO {numero}", f"ENUNCIADO {numero} ", f"{numero} –", f"{numero} -", f"{numero} �"]:
        idx = full_text.find(pat)
        if idx != -1:
            pos = idx
            break

    if pos == -1:
        return "parte geral"

    # Texto antes do enunciado
    preceding = full_text[:pos].upper()

    # Mapear cabecalhos para areas
    area_headers = [
        ("DIREITO DIGITAL E NOVOS DIREITOS", "direito digital"),
        ("DIREITO DIGITAL", "direito digital"),
        ("NOVOS DIREITOS", "direito digital"),
        ("FAMÍLIA E SUCESSÕES", "família e sucessões"),
        ("DIREITO DE FAMÍLIA E SUCESSÕES", "família e sucessões"),
        ("DIREITO DE FAMÍLIA", "família"),
        ("SUCESSÕES", "sucessões"),
        ("RESPONSABILIDADE CIVIL", "responsabilidade civil"),
        ("DIREITO DAS OBRIGAÇÕES E CONTRATOS", "obrigações e contratos"),
        ("OBRIGAÇÕES E CONTRATOS", "obrigações e contratos"),
        ("DIREITO DAS OBRIGAÇÕES", "obrigações"),
        ("OBRIGAÇÕES", "obrigações"),
        ("CONTRATOS", "contratos"),
        ("DIREITO DAS COISAS E PROPRIEDADE INTELECTUAL", "direitos reais"),
        ("DIREITO DAS COISAS", "direitos reais"),
        ("PROPRIEDADE INTELECTUAL", "direitos reais"),
        ("DIREITO DA EMPRESA", "empresa"),
        ("EMPRESA", "empresa"),
        ("PARTE GERAL E NORMAS DE INTRODUÇÃO", "parte geral"),
        ("PARTE GERAL", "parte geral"),
        ("LINDB", "parte geral"),
    ]

    best_area = "parte geral"
    best_pos = -1

    for header, area in area_headers:
        last_pos = preceding.rfind(header)
        if last_pos > best_pos:
            best_pos = last_pos
            best_area = area

    return best_area

def main():
    print("=" * 70)
    print("EXTRATOR v2 - Enunciados das Jornadas de Direito Civil CJF/STJ")
    print("=" * 70)

    all_enunciados = {}

    # 1) Compilacao I, III, IV, V
    filepath = os.path.join(PDF_DIR, PDF_FILES["compilacao"])
    if os.path.exists(filepath):
        print("\n  [1/4] Processando compilacao (I, III, IV, V)...")
        text = extract_text_from_pdf(filepath)
        encs = parse_compilacao(text)
        print(f"    Encontrados: {len(encs)}")
        for en in encs:
            if en["numero"] not in all_enunciados:
                en["area_tematica"] = determine_area_from_context(text, en["numero"])
                all_enunciados[en["numero"]] = en

    # 2) VI Jornada
    filepath = os.path.join(PDF_DIR, PDF_FILES["vi_jornada"])
    if os.path.exists(filepath):
        print("\n  [2/4] Processando VI Jornada...")
        text = extract_text_from_pdf(filepath)
        encs = parse_standard(text)
        print(f"    Encontrados: {len(encs)}")
        for en in encs:
            if en["numero"] not in all_enunciados:
                en["area_tematica"] = determine_area_from_context(text, en["numero"])
                all_enunciados[en["numero"]] = en

    # 3) VII Jornada
    filepath = os.path.join(PDF_DIR, PDF_FILES["vii_jornada"])
    if os.path.exists(filepath):
        print("\n  [3/4] Processando VII Jornada...")
        text = extract_text_from_pdf(filepath)
        encs = parse_standard(text)
        print(f"    Encontrados: {len(encs)}")
        for en in encs:
            if en["numero"] not in all_enunciados:
                en["area_tematica"] = determine_area_from_context(text, en["numero"])
                all_enunciados[en["numero"]] = en

    # 4) VIII e IX Jornada
    filepath = os.path.join(PDF_DIR, PDF_FILES["viii_ix_jornada"])
    if os.path.exists(filepath):
        print("\n  [4/4] Processando VIII/IX Jornada...")
        text = extract_text_from_pdf(filepath)
        encs = parse_standard(text)
        print(f"    Encontrados: {len(encs)}")
        for en in encs:
            if en["numero"] not in all_enunciados:
                en["area_tematica"] = determine_area_from_context(text, en["numero"])
                all_enunciados[en["numero"]] = en

    # Adicionar jornada e ano
    for num, en in all_enunciados.items():
        jornada = get_jornada(num)
        if jornada:
            en["jornada"] = jornada
            en["ano"] = JORNADAS_META[jornada]["ano"]
        else:
            en["jornada"] = "?"
            en["ano"] = 0

    # Ordenar
    sorted_enunciados = sorted(all_enunciados.values(), key=lambda x: x["numero"])

    # Estatisticas
    print(f"\n{'='*70}")
    print(f"  RESULTADO FINAL: {len(sorted_enunciados)} enunciados extraidos")
    print(f"{'='*70}")
    print(f"\n  {'Jornada':>10} | {'Ano':>4} | {'Extraidos':>9} | {'Esperados':>9} | {'%':>5}")
    print(f"  {'-'*10}-+-{'-'*4}-+-{'-'*9}-+-{'-'*9}-+-{'-'*5}")
    total_ext = 0
    total_esp = 0
    for j in ["I", "III", "IV", "V", "VI", "VII", "VIII", "IX"]:
        count = sum(1 for en in sorted_enunciados if en.get("jornada") == j)
        expected = JORNADAS_META[j]["total_enunciados"]
        pct = f"{count/expected*100:.0f}%" if expected > 0 else "?"
        print(f"  {j:>10} | {JORNADAS_META[j]['ano']:>4} | {count:>9} | {expected:>9} | {pct:>5}")
        total_ext += count
        total_esp += expected
    print(f"  {'-'*10}-+-{'-'*4}-+-{'-'*9}-+-{'-'*9}-+-{'-'*5}")
    print(f"  {'TOTAL':>10} |      | {total_ext:>9} | {total_esp:>9} | {total_ext/total_esp*100:.0f}%")

    # Areas tematicas
    areas = {}
    for en in sorted_enunciados:
        area = en.get("area_tematica", "?")
        areas[area] = areas.get(area, 0) + 1
    print(f"\n  Areas tematicas:")
    for area, count in sorted(areas.items(), key=lambda x: -x[1]):
        print(f"    {area}: {count}")

    # Gerar JSONL
    output_file = r"C:\Users\renan\Desktop\dossie_judiciario\enunciados\jornadas_direito_civil\enunciados.jsonl"

    with open(output_file, "w", encoding="utf-8") as f:
        meta = {
            "tipo": "metadados_jornadas",
            "descricao": "Enunciados das Jornadas de Direito Civil do Conselho da Justica Federal (CJF/STJ)",
            "fonte": "PDFs oficiais do CJF - www.cjf.jus.br",
            "total_jornadas": 8,
            "nota": "Nao houve II Jornada de Direito Civil. A numeracao pula de I (2002) para III (2004).",
            "jornadas": JORNADAS_META
        }
        f.write(json.dumps(meta, ensure_ascii=False) + "\n")

        for en in sorted_enunciados:
            record = {
                "tipo": "enunciado",
                "numero": en["numero"],
                "jornada": en.get("jornada", ""),
                "ano": en.get("ano", 0),
                "texto": en["texto"],
                "artigo_referencia": en.get("artigo_referencia", ""),
                "area_tematica": en.get("area_tematica", "")
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"\n  Arquivo gerado: {output_file}")
    file_size = os.path.getsize(output_file)
    print(f"  Tamanho: {file_size/1024:.1f} KB")
    print(f"  Registros: {len(sorted_enunciados) + 1}")

if __name__ == "__main__":
    main()
