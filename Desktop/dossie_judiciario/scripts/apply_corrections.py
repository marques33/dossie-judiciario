# -*- coding: utf-8 -*-
"""Aplica correcoes priorizadas no dossie_judiciario.

Acoes:
1. Substitui Tema 6/STF: RE 566.349 -> RE 566.471 (medicamento alto custo)
2. Substitui Tema 500/STF: RE 660.861 -> RE 657.718 (medicamento sem ANVISA)
3. Move entradas antigas dos Temas 6 e 500 para temas_pendente_verificacao.jsonl
4. Adiciona Tema 1234/STF (RE 1.366.243)
5. Adiciona Tema 98/STJ (REsp 1.474.665/RS) e Tema 106/STJ (REsp 1.657.156/RJ)

Fonte das correcoes: portal.stf.jus.br + scon.stj.jus.br (consultados em maio/2026).
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(r"C:/Users/renan/Desktop/dossie_judiciario")
RG = ROOT / "teses_precedentes" / "stf" / "teses_rg.jsonl"
RP = ROOT / "teses_precedentes" / "stj" / "repetitivos.jsonl"
PENDENTE = ROOT / "teses_precedentes" / "temas_pendente_verificacao.jsonl"

# === Correcoes do STF (RG) =================================================

TEMA_6_CORRETO = {
    "tema": 6,
    "tese": (
        "A ausencia de inclusao de medicamento nas listas de dispensacao do "
        "Sistema Unico de Saude impede, como regra geral, o fornecimento do "
        "farmaco por decisao judicial, independentemente do custo. "
        "Excepcionalmente, e possivel o fornecimento desde que cumpridos seis "
        "requisitos cumulativos: (i) negativa administrativa; (ii) ilegalidade "
        "do ato da CONITEC, ausencia de pedido de incorporacao ou demora "
        "irrazoavel; (iii) inexistencia de substituto terapeutico nas listas "
        "do SUS; (iv) comprovacao de eficacia e seguranca por evidencias "
        "cientificas de alto nivel; (v) imprescindibilidade clinica; "
        "(vi) incapacidade financeira do paciente."
    ),
    "tipo": "repercussao_geral",
    "leading_case": "RE 566.471",
    "data_julgamento": "2024-09-20",
    "relator": "Min. Marco Aurelio",
    "orgao_julgador": "Plenario",
    "status": "tese_fixada",
    "area_direito": "saude",
    "modulacao_efeitos": True,
    "observacoes": (
        "Art. 196 da CF/88. Caso paradigma: idosa carente do RN, citrato de "
        "sildenafila para cardiomiopatia isquemica e hipertensao pulmonar. "
        "Julgamento concluido em 20/09/2024 (Pleno Virtual, 10x1). Tese "
        "cristalizada na Sumula Vinculante 61/STF (DJe 03/10/2024). "
        "Voto vencedor: Min. Luis Roberto Barroso e Min. Gilmar Mendes."
    ),
}

TEMA_500_CORRETO = {
    "tema": 500,
    "tese": (
        "O Estado nao pode ser obrigado a fornecer medicamento experimental. "
        "A ausencia de registro na ANVISA impede, como regra geral, o "
        "fornecimento de medicamento por decisao judicial. E excepcionalmente "
        "possivel, em caso de mora irrazoavel da ANVISA na apreciacao do "
        "pedido (prazo superior ao da Lei 13.411/2016), desde que presentes "
        "tres requisitos: (i) existencia de pedido de registro no Brasil "
        "(salvo medicamentos orfaos para doencas raras e ultrarraras); "
        "(ii) existencia de registro do medicamento em renomadas agencias de "
        "regulacao no exterior; e (iii) inexistencia de substituto terapeutico "
        "com registro no Brasil. As acoes que demandam medicamento sem "
        "registro na ANVISA devem necessariamente ser propostas contra a Uniao."
    ),
    "tipo": "repercussao_geral",
    "leading_case": "RE 657.718",
    "data_julgamento": "2019-05-22",
    "relator": "Min. Marco Aurelio (redator: Min. Alexandre de Moraes)",
    "orgao_julgador": "Plenario",
    "status": "tese_fixada",
    "area_direito": "saude",
    "modulacao_efeitos": False,
    "observacoes": (
        "Art. 196 da CF/88; Lei 6.360/76; Lei 9.782/99; Lei 13.411/2016. "
        "Acordao publicado no DJe de 09/11/2020."
    ),
}

TEMA_1234_NOVO = {
    "tema": 1234,
    "tese": (
        "1) E da competencia da Justica Federal o julgamento das demandas "
        "que visem ao fornecimento de medicamentos nao incorporados em atos "
        "do SUS e medicamentos oncologicos, quando o valor anual do tratamento "
        "do farmaco ou do principio ativo, com base no Preco Maximo de Venda "
        "ao Governo (PMVG) divulgado pela CMED, for igual ou superior a 210 "
        "salarios minimos. 2) Compete a Justica Estadual o julgamento das "
        "demandas inferiores a esse patamar. 3) Custeio nas acoes da Justica "
        "Estadual segue regime de ressarcimento Fundo a Fundo da Uniao para "
        "Estados/DF/Municipios. 4) Aplica-se as acoes ajuizadas a partir de "
        "19/09/2024 (modulacao)."
    ),
    "tipo": "repercussao_geral",
    "leading_case": "RE 1.366.243",
    "data_julgamento": "2024-09-13",
    "relator": "Min. Gilmar Mendes",
    "orgao_julgador": "Plenario",
    "status": "tese_fixada",
    "area_direito": "saude",
    "modulacao_efeitos": True,
    "observacoes": (
        "Art. 109, I, CF/88. Cristalizado na Sumula Vinculante 60/STF "
        "(DJe 20/09/2024). Tres acordos interfederativos homologados pelo STF. "
        "Embargos de declaracao acolhidos em dez/2024 para integracoes finais. "
        "Aplicacao conjunta com Tema 6 (medicamento nao incorporado) e Tema "
        "500 (medicamento sem registro ANVISA)."
    ),
}

# === Adicoes ao STJ (Repetitivos) ==========================================

TEMA_98_STJ_NOVO = {
    "tema": 98,
    "tese": (
        "E cabivel a imposicao de multa diaria (astreintes) contra a Fazenda "
        "Publica, com fundamento no poder geral de efetividade do juiz, para "
        "compeli-la ao cumprimento de obrigacao de fazer consistente no "
        "fornecimento de medicamento a pessoa desprovida de recursos financeiros."
    ),
    "tipo": "recurso_repetitivo",
    "leading_case": "REsp 1.474.665/RS",
    "data_julgamento": "2017-04-26",
    "relator": "Min. Benedito Goncalves",
    "orgao_julgador": "Primeira Secao",
    "status": "tese_fixada",
    "area_direito": "saude",
    "modulacao_efeitos": False,
    "observacoes": (
        "DJe 22/06/2017 (Informativo STJ 606). Art. 537 do CPC/2015. "
        "Fundamenta astreintes em obrigacoes de fazer relativas a saude "
        "contra entes publicos. Caso paradigma: glaucoma, RS, multa diaria "
        "de meio salario minimo."
    ),
}

TEMA_106_STJ_NOVO = {
    "tema": 106,
    "tese": (
        "A concessao dos medicamentos nao incorporados em atos normativos do "
        "SUS exige a presenca cumulativa dos seguintes requisitos: (i) "
        "comprovacao, por meio de laudo medico fundamentado e circunstanciado, "
        "da imprescindibilidade ou necessidade do medicamento, assim como da "
        "ineficacia, para o tratamento da molestia, dos farmacos fornecidos "
        "pelo SUS; (ii) incapacidade financeira do paciente de arcar com o "
        "custo do medicamento prescrito; (iii) existencia de registro do "
        "medicamento na ANVISA, observados os usos autorizados pela agencia."
    ),
    "tipo": "recurso_repetitivo",
    "leading_case": "REsp 1.657.156/RJ",
    "data_julgamento": "2018-04-25",
    "relator": "Min. Benedito Goncalves",
    "orgao_julgador": "Primeira Secao",
    "status": "tese_fixada",
    "area_direito": "saude",
    "modulacao_efeitos": True,
    "observacoes": (
        "DJe 04/05/2018. Modulacao: aplica-se a processos distribuidos a "
        "partir de 04/05/2018. Base normativa: art. 196 CF/88, Lei 8.080/90. "
        "Complementa o Tema 6 STF (saude). Em sintese, exige tripe: "
        "imprescindibilidade clinica + hipossuficiencia + registro ANVISA."
    ),
}

# === Funcoes ==============================================================


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False))
            f.write("\n")


def main() -> None:
    # STF RG
    rg_rows = load_jsonl(RG)
    pendentes: list[dict] = []
    changes_rg: list[str] = []

    for i, r in enumerate(rg_rows):
        if r.get("tema") == 6 and "566.471" not in (r.get("leading_case") or ""):
            old = dict(r)
            old["_motivo_realocacao"] = (
                "Atribuicao incorreta de Tema 6. Conteudo (RE 566.349/Carmen "
                "Lucia/MP-consumidor) provavelmente pertence a outro tema de "
                "Repercussao Geral — pendente verificacao do numero correto."
            )
            pendentes.append(old)
            rg_rows[i] = TEMA_6_CORRETO
            changes_rg.append("Tema 6 corrigido (RE 566.471)")
        elif r.get("tema") == 500 and "657.718" not in (r.get("leading_case") or ""):
            old = dict(r)
            old["_motivo_realocacao"] = (
                "Atribuicao incorreta de Tema 500. Conteudo (RE 660.861/Dias "
                "Toffoli/1/3 ferias previdenciaria) provavelmente pertence ao "
                "Tema 985 ou similar — pendente verificacao."
            )
            pendentes.append(old)
            rg_rows[i] = TEMA_500_CORRETO
            changes_rg.append("Tema 500 corrigido (RE 657.718)")

    # Adicionar Tema 1234 se ausente
    if not any(r.get("tema") == 1234 for r in rg_rows):
        rg_rows.append(TEMA_1234_NOVO)
        changes_rg.append("Tema 1234 adicionado")

    # Reordenar por numero do tema
    rg_rows.sort(key=lambda x: x.get("tema", 0))
    write_jsonl(RG, rg_rows)

    # STJ Repetitivos — Temas 98 e 106 do dossie estao com leading_case
    # errado (ISS leasing e ISS plano de saude). Os corretos sao: astreintes
    # vs Fazenda (REsp 1.474.665) e medicamentos fora da RENAME (REsp 1.657.156).
    rp_rows = load_jsonl(RP)
    changes_rp: list[str] = []
    for i, r in enumerate(rp_rows):
        if r.get("tema") == 98 and "1.474.665" not in (r.get("leading_case") or ""):
            old = dict(r)
            old["_motivo_realocacao"] = (
                "Atribuicao incorreta de Tema 98/STJ. Conteudo "
                "(REsp 1.111.156/SP/ISS leasing) provavelmente pertence ao "
                "Tema 125/STJ (ISS leasing) — pendente verificacao."
            )
            pendentes.append(old)
            rp_rows[i] = TEMA_98_STJ_NOVO
            changes_rp.append("Tema 98/STJ corrigido (REsp 1.474.665)")
        elif r.get("tema") == 106 and "1.657.156" not in (r.get("leading_case") or ""):
            old = dict(r)
            old["_motivo_realocacao"] = (
                "Atribuicao incorreta de Tema 106/STJ. Conteudo "
                "(REsp 1.102.849/MG/ISS plano de saude) pertence ao "
                "Tema 132/STJ ou similar — pendente verificacao."
            )
            pendentes.append(old)
            rp_rows[i] = TEMA_106_STJ_NOVO
            changes_rp.append("Tema 106/STJ corrigido (REsp 1.657.156)")
    if not any(r.get("tema") == 98 for r in rp_rows):
        rp_rows.append(TEMA_98_STJ_NOVO)
        changes_rp.append("Tema 98/STJ adicionado")
    if not any(r.get("tema") == 106 for r in rp_rows):
        rp_rows.append(TEMA_106_STJ_NOVO)
        changes_rp.append("Tema 106/STJ adicionado")
    rp_rows.sort(key=lambda x: x.get("tema", 0))
    write_jsonl(RP, rp_rows)

    # Pendentes
    if pendentes:
        existing: list[dict] = []
        if PENDENTE.exists():
            existing = load_jsonl(PENDENTE)
        write_jsonl(PENDENTE, existing + pendentes)

    print("=== Resumo das alteracoes ===")
    print(f"STF teses_rg.jsonl: {len(changes_rg)} mudancas")
    for c in changes_rg:
        print(f"  - {c}")
    print(f"STJ repetitivos.jsonl: {len(changes_rp)} mudancas")
    for c in changes_rp:
        print(f"  - {c}")
    print(f"Pendentes movidos: {len(pendentes)} entradas -> {PENDENTE}")


if __name__ == "__main__":
    main()
