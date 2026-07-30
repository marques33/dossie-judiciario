#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrator automatico de enunciados das Jornadas de Direito Civil do CJF/STJ.
Processa os PDFs oficiais baixados do site do CJF.
"""

import pdfplumber
import re
import json
import os
import sys

# Diretorio dos PDFs baixados
PDF_DIR = os.path.expanduser(r"~\.claude\projects\C--Users-renan-Desktop-jurisprud-ncia-e-doutrina\69eab488-78ab-4580-96b2-2a33834e0a0b\tool-results")

# Mapeamento dos PDFs para as jornadas
PDF_FILES = {
    "compilacao_I_III_IV_V": "webfetch-1773497804421-fgaq01.pdf",  # I, III, IV, V
    "vi_jornada": "webfetch-1773497806418-cj6gh0.pdf",  # VI
    "vii_jornada": "webfetch-1773497807545-uzd3uu.pdf",  # VII
    "viii_jornada": "webfetch-1773497808951-js46v2.pdf",  # VIII/IX
}

# Metadados das Jornadas
JORNADAS_META = {
    "I": {"numero": "I", "ano": 2002, "local": "Brasilia-DF, Centro de Estudos Judiciarios do CJF", "total_enunciados": 138, "periodo": "12 a 13 de setembro de 2002", "coordenador": "Min. Ruy Rosado de Aguiar Junior"},
    "III": {"numero": "III", "ano": 2004, "local": "Brasilia-DF, Centro de Estudos Judiciarios do CJF", "total_enunciados": 134, "periodo": "1 a 3 de dezembro de 2004", "coordenador": "Min. Ruy Rosado de Aguiar Junior"},
    "IV": {"numero": "IV", "ano": 2006, "local": "Brasilia-DF, Centro de Estudos Judiciarios do CJF", "total_enunciados": 125, "periodo": "25 e 26 de outubro de 2006", "coordenador": "Min. Ruy Rosado de Aguiar Junior"},
    "V": {"numero": "V", "ano": 2011, "local": "Brasilia-DF, Centro de Estudos Judiciarios do CJF", "total_enunciados": 133, "periodo": "8 e 9 de novembro de 2011", "coordenador": "Min. Ruy Rosado de Aguiar Junior"},
    "VI": {"numero": "VI", "ano": 2013, "local": "Brasilia-DF, Centro de Estudos Judiciarios do CJF", "total_enunciados": 46, "periodo": "11 e 12 de marco de 2013", "coordenador": "Min. Ruy Rosado de Aguiar Junior"},
    "VII": {"numero": "VII", "ano": 2015, "local": "Brasilia-DF, Centro de Estudos Judiciarios do CJF", "total_enunciados": 37, "periodo": "28 e 29 de setembro de 2015", "coordenador": "Min. Ruy Rosado de Aguiar Junior"},
    "VIII": {"numero": "VIII", "ano": 2022, "local": "Brasilia-DF (formato hibrido)", "total_enunciados": 32, "periodo": "25 e 26 de abril de 2022", "coordenador": "Min. Luis Felipe Salomao"},
    "IX": {"numero": "IX", "ano": 2022, "local": "Brasilia-DF, Centro de Estudos Judiciarios do CJF", "total_enunciados": 49, "periodo": "19 e 20 de outubro de 2022", "coordenador": "Min. Luis Felipe Salomao"},
}

# Ranges de enunciados por jornada
JORNADA_RANGES = {
    "I": (1, 138),
    "III": (138, 271),
    "IV": (272, 396),
    "V": (397, 529),
    "VI": (530, 575),
    "VII": (576, 612),
    "VIII": (613, 644),
    "IX": (645, 693),
}

# Areas tematicas por secao do PDF
AREA_KEYWORDS = {
    "PARTE GERAL": "parte geral",
    "NORMAS DE INTRODUÇÃO": "parte geral",
    "LINDB": "parte geral",
    "OBRIGAÇÕES": "obrigações",
    "DIREITO DAS OBRIGAÇÕES": "obrigações",
    "CONTRATOS": "contratos",
    "RESPONSABILIDADE CIVIL": "responsabilidade civil",
    "DIREITO DAS COISAS": "direitos reais",
    "DIREITO DE FAMÍLIA": "família",
    "FAMÍLIA E SUCESSÕES": "família e sucessões",
    "DIREITO DE FAMÍLIA E SUCESSÕES": "família e sucessões",
    "SUCESSÕES": "sucessões",
    "DIREITO DA EMPRESA": "empresa",
    "EMPRESA": "empresa",
    "PROPRIEDADE INTELECTUAL": "direitos reais",
    "DIREITO DIGITAL": "direito digital",
    "NOVOS DIREITOS": "direito digital",
}

def get_jornada_for_number(num):
    """Determina a jornada com base no numero do enunciado."""
    for jornada, (start, end) in JORNADA_RANGES.items():
        if start <= num <= end:
            return jornada
    return None

def extract_text_from_pdf(filepath):
    """Extrai texto de todas as paginas de um PDF."""
    full_text = ""
    try:
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
    except Exception as ex:
        print(f"  Erro ao processar {filepath}: {ex}", file=sys.stderr)
    return full_text

def parse_enunciados(text):
    """
    Extrai enunciados do texto, buscando padroes como:
    ENUNCIADO 123 - Texto do enunciado...
    ou
    Enunciado n. 123: Texto do enunciado...
    """
    enunciados = []

    # Padroes para encontrar enunciados
    # Padrao 1: ENUNCIADO 123 – Texto...
    # Padrao 2: ENUNCIADO 123 - Texto...
    # Padrao 3: Enunciado n. 123 – Texto...
    pattern = r'ENUNCIADO\s+(\d+)\s*[–\-]\s*(.*?)(?=ENUNCIADO\s+\d+\s*[–\-]|Parte da legisla|Artigos?:|Refer[eê]ncia [Ll]egislativa|Justificativa:|$)'

    matches = re.finditer(pattern, text, re.DOTALL | re.IGNORECASE)

    for match in matches:
        numero = int(match.group(1))
        texto_raw = match.group(2).strip()

        # Limpar o texto - pegar apenas o enunciado (antes de "Parte da legislação", "Artigo:", "Justificativa:")
        texto_clean = re.split(r'\n\s*(Parte da legisla|Artigos?:|Refer[eê]ncia|Justificativa)', texto_raw, flags=re.IGNORECASE)[0]
        texto_clean = ' '.join(texto_clean.split())  # Normalizar espacos
        texto_clean = texto_clean.strip()

        # Remover trailing period if needed
        if texto_clean and texto_clean[-1] not in '.?!':
            texto_clean += '.'

        # Extrair artigo de referencia
        artigo_match = re.search(r'(?:Parte da legisla[çc][aã]o|Artigos?|Refer[eê]ncia [Ll]egislativa)\s*:\s*(.*?)(?:\n|Justificativa|$)', texto_raw, re.IGNORECASE)
        artigo = ""
        if artigo_match:
            artigo = artigo_match.group(1).strip()
            artigo = ' '.join(artigo.split())

        enunciados.append({
            "numero": numero,
            "texto": texto_clean,
            "artigo_referencia": artigo
        })

    return enunciados

def determine_area(text, position, numero):
    """Determina a area tematica com base nos cabecalhos de secao."""
    # Procurar o cabecalho de secao mais proximo antes da posicao do enunciado
    best_area = "parte geral"

    # Buscar pelo numero do enunciado e verificar o contexto
    idx = text.find(f"ENUNCIADO {numero}")
    if idx == -1:
        idx = text.find(f"Enunciado {numero}")
    if idx == -1:
        return best_area

    # Pegar o texto anterior ao enunciado
    preceding = text[:idx]

    # Procurar o ultimo cabecalho de secao
    for keyword, area in AREA_KEYWORDS.items():
        # Buscar a ultima ocorrencia deste keyword antes do enunciado
        last_pos = preceding.upper().rfind(keyword.upper())
        if last_pos != -1:
            if not hasattr(determine_area, '_best_pos') or last_pos > determine_area._best_pos:
                determine_area._best_pos = last_pos
                best_area = area

    # Reset
    if hasattr(determine_area, '_best_pos'):
        result_area = best_area
        del determine_area._best_pos
        return result_area

    return best_area

def process_all_pdfs():
    """Processa todos os PDFs e extrai enunciados."""
    all_enunciados = {}

    for name, filename in PDF_FILES.items():
        filepath = os.path.join(PDF_DIR, filename)
        if not os.path.exists(filepath):
            print(f"  AVISO: PDF nao encontrado: {filepath}", file=sys.stderr)
            continue

        print(f"  Processando: {name} ({filename})...")
        text = extract_text_from_pdf(filepath)

        if not text.strip():
            print(f"    AVISO: Texto vazio para {filename}", file=sys.stderr)
            continue

        enunciados = parse_enunciados(text)
        print(f"    Encontrados {len(enunciados)} enunciados")

        for en in enunciados:
            num = en["numero"]
            if num not in all_enunciados:
                # Determinar area tematica
                area = determine_area(text, 0, num)
                en["area_tematica"] = area

                # Determinar jornada
                jornada = get_jornada_for_number(num)
                if jornada:
                    en["jornada"] = jornada
                    en["ano"] = JORNADAS_META[jornada]["ano"]
                else:
                    en["jornada"] = "desconhecida"
                    en["ano"] = 0

                all_enunciados[num] = en

    return all_enunciados

def main():
    print("=" * 60)
    print("EXTRATOR DE ENUNCIADOS - Jornadas de Direito Civil CJF/STJ")
    print("=" * 60)

    # Processar PDFs
    all_enunciados = process_all_pdfs()

    # Ordenar por numero
    sorted_enunciados = sorted(all_enunciados.values(), key=lambda x: x["numero"])

    print(f"\n  Total de enunciados extraidos: {len(sorted_enunciados)}")

    # Estatisticas por jornada
    print("\n  Enunciados por Jornada:")
    for jornada in ["I", "III", "IV", "V", "VI", "VII", "VIII", "IX"]:
        count = sum(1 for en in sorted_enunciados if en.get("jornada") == jornada)
        meta = JORNADAS_META[jornada]
        print(f"    {jornada:>4} Jornada ({meta['ano']}): {count:>3} extraidos / {meta['total_enunciados']} esperados")

    # Gerar JSONL
    output_file = r"C:\Users\renan\Desktop\dossie_judiciario\enunciados\jornadas_direito_civil\enunciados.jsonl"

    with open(output_file, "w", encoding="utf-8") as f:
        # Metadados
        meta_record = {
            "tipo": "metadados_jornadas",
            "descricao": "Enunciados das Jornadas de Direito Civil do Conselho da Justica Federal (CJF/STJ)",
            "fonte": "PDFs oficiais do CJF - www.cjf.jus.br",
            "total_jornadas": 8,
            "nota": "Nao houve II Jornada de Direito Civil (a II Jornada foi de Direito Comercial)",
            "jornadas": JORNADAS_META
        }
        f.write(json.dumps(meta_record, ensure_ascii=False) + "\n")

        # Enunciados
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

    print(f"\n  Arquivo JSONL gerado: {output_file}")
    print(f"  Total de linhas: {len(sorted_enunciados) + 1} (1 metadados + {len(sorted_enunciados)} enunciados)")

if __name__ == "__main__":
    main()
