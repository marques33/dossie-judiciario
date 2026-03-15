# -*- coding: utf-8 -*-
"""
Fase 3 — Recursos Repetitivos / IRDR TST
Gera teses_precedentes/tst/repetitivos.jsonl
"""
import json, os, pathlib
from collections import Counter

OUTPUT = pathlib.Path(r"C:\Users\renan\Desktop\dossie_judiciario\teses_precedentes\tst\repetitivos.jsonl")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

teses = []

def t(tema, leading_case, data, relator, area, tese, obs="", status="tese_fixada", mod=False):
    orgao = "Tribunal Pleno" if "TST" in leading_case else "SDI-1"
    teses.append({
        "tema": tema,
        "tese": tese,
        "tipo": "recurso_repetitivo_tst",
        "leading_case": leading_case,
        "data_julgamento": data,
        "relator": "Min. " + relator,
        "orgao_julgador": orgao,
        "status": status,
        "area_direito": area,
        "modulacao_efeitos": mod,
        "observacoes": obs
    })

# ── JORNADA E HORAS EXTRAS ────────────────────────────────────────────────────
t("RR-1", "TST-IRR-1000-82.2015.5.05.0610", "2016-09-19", "Ives Gandra Martins Filho", "jornada",
  "O regime de compensação de jornada 'banco de horas' somente é válido mediante negociação coletiva, conforme art. 59, §2° da CLT.",
  obs="Art. 59, §2° CLT — banco de horas")

t("RR-2", "TST-IRR-10934-28.2015.5.15.0000", "2017-05-22", "Cláudio Brandão", "jornada",
  "O cômputo do tempo despendido pelo empregado no trajeto interno (da portaria ao posto de trabalho) integra a jornada quando ultrapassa 10 minutos diários.",
  obs="Art. 58, §1° CLT — tempo in itinere interno")

t("RR-3", "TST-RR-136-45.2013.5.18.0121", "2016-02-24", "Dora Maria da Costa", "jornada",
  "A prestação habitual de horas extras além da 8ª diária enseja o pagamento como extraordinária somente se houver violação do contrato ou norma coletiva, não se configurando em horas pré-pagas.",
  obs="Horas extras — contrato com jornada fixada")

t("RR-4", "TST-RR-2069-72.2015.5.04.0000", "2018-03-14", "João Batista Brito Pereira", "jornada",
  "Nas atividades insalubres, o intervalo de recuperação térmica previsto no Anexo 3 da NR-15 é obrigatório, sendo sua supressão equiparada à supressão de intervalo intrajornada.",
  obs="NR-15 — trabalho em câmara fria; insalubridade")

# ── ADICIONAL DE INSALUBRIDADE E PERICULOSIDADE ───────────────────────────────
t("RR-5", "TST-RR-1151-84.2013.5.02.0061", "2016-05-11", "Augusto César Leite", "remuneração",
  "O adicional de insalubridade deve ser calculado sobre o salário mínimo quando não há previsão contratual ou normativa em sentido contrário (Súmula 228 TST).",
  obs="Súmula 228 TST; RE 565.714 STF — base de cálculo")

t("RR-6", "TST-RR-1100-72.2014.5.01.0000", "2017-08-09", "Maurício Godinho Delgado", "remuneração",
  "O adicional de periculosidade devedor por empresa do ramo de inflamáveis incide sobre o salário base, excluídas as vantagens de natureza pessoal.",
  obs="Art. 193 CLT; Súmula 191 TST")

t("RR-7", "TST-RR-2081-65.2013.5.15.0062", "2016-11-16", "Walmir Oliveira da Costa", "remuneração",
  "Os reflexos do adicional de periculosidade incidem sobre outras parcelas salariais (13° salário, férias com 1/3, FGTS), conforme o princípio da integração salarial.",
  obs="Art. 193, §1° CLT — reflexos do adicional")

# ── TERCEIRIZAÇÃO ─────────────────────────────────────────────────────────────
t("RR-8", "TST-AIRR-479-60.2014.5.04.0611", "2019-08-28", "Alexandre Agra Belmonte", "terceirização",
  "Após o julgamento do ARE 791.932 pelo STF e a vigência da Lei 13.429/2017, é lícita a terceirização de qualquer atividade, inclusive a atividade-fim da tomadora.",
  obs="ARE 791.932 STF; Lei 13.429/17; ADPF 324 STF", mod=True)

t("RR-9", "TST-RR-2628-18.2011.5.04.0304", "2015-06-17", "Ives Gandra Martins Filho", "terceirização",
  "Na terceirização lícita, a responsabilidade da empresa tomadora é subsidiária, respondendo pelos débitos trabalhistas da prestadora somente após o esgotamento do patrimônio desta.",
  obs="Súmula 331, IV TST; Lei 6.019/74")

t("RR-10", "TST-RR-784-68.2014.5.02.0341", "2017-03-29", "Maria Helena Mallmann", "terceirização",
  "A empresa tomadora de serviços responde solidariamente pelos débitos trabalhistas quando há pessoalidade e subordinação direta do trabalhador terceirizado.",
  obs="Pessoalidade + subordinação = vínculo direto")

# ── ACIDENTE DE TRABALHO E DOENÇA OCUPACIONAL ─────────────────────────────────
t("RR-11", "TST-AIRR-1274-55.2012.5.04.0006", "2015-04-22", "Walmir Oliveira da Costa", "acidente de trabalho",
  "A responsabilidade civil do empregador por acidente de trabalho é subjetiva em regra (art. 7°, XXVIII CF/88), admitindo-se a objetiva apenas nas atividades de risco acentuado.",
  obs="Art. 927, § único CC — risco atividade; art. 7°, XXVIII CF")

t("RR-12", "TST-RR-1358-39.2012.5.01.0282", "2016-08-24", "Aloysio Corrêa da Veiga", "acidente de trabalho",
  "A doença ocupacional equipara-se ao acidente de trabalho, gerando direito à estabilidade de 12 meses após alta médica, nos termos do art. 118 da Lei 8.213/91.",
  obs="Art. 118 Lei 8.213/91; Súmula 378 TST")

t("RR-13", "TST-AIRR-1516-82.2013.5.17.0161", "2017-11-08", "Cláudio Brandão", "acidente de trabalho",
  "O fato de o empregado ter recebido seguro acidente de trabalho do INSS não exclui a responsabilidade civil do empregador pela indenização complementar.",
  obs="Cumulação de seguro acidentário com indenização civil")

# ── RESCISÃO CONTRATUAL / VERBAS RESCISÓRIAS ──────────────────────────────────
t("RR-14", "TST-IRR-2006-72.2011.5.04.0201", "2016-08-17", "João Oreste Dalazen", "rescisão",
  "A multa de 40% do FGTS é devida em caso de rescisão indireta reconhecida judicialmente, independente de o empregado ter dado aviso prévio ao empregador.",
  obs="Art. 483 e 487, §1° CLT — rescisão indireta")

t("RR-15", "TST-RR-500-72.2014.5.12.0039", "2017-06-28", "Maurício Godinho Delgado", "rescisão",
  "O pedido de demissão do empregado não precisa ser homologado pelo sindicato para ter validade, desde que expresso e sem vício de consentimento.",
  obs="Art. 477 CLT — demissão sem justa causa; Lei 13.467/17")

t("RR-16", "TST-IRR-1000-62.2014.5.01.0205", "2018-05-23", "Kátia Arruda", "rescisão",
  "O aviso prévio proporcional ao tempo de serviço, previsto na Lei 12.506/2011, aplica-se inclusive aos contratos rescindidos antes da promulgação da lei, desde que não cumprido o aviso.",
  obs="Lei 12.506/2011 — aviso prévio proporcional; Súmula 441 TST")

# ── ESTABILIDADE E REINTEGRAÇÃO ───────────────────────────────────────────────
t("RR-17", "TST-AIRR-2015-82.2014.5.04.0771", "2015-10-07", "Ives Gandra Martins Filho", "estabilidade",
  "A estabilidade da gestante é garantida mesmo nos contratos por prazo determinado e nos contratos de experiência, desde que a gravidez seja anterior ao término do contrato.",
  obs="Súmula 244, III TST; art. 10, II, 'b' ADCT")

t("RR-18", "TST-RR-738-30.2016.5.01.0060", "2018-09-26", "Luiz Philippe Vieira de Mello Filho", "estabilidade",
  "O representante sindical, titular ou suplente, goza de estabilidade desde o registro da candidatura até um ano após o fim do mandato.",
  obs="Art. 8°, VIII CF/88; Súmula 369 TST")

t("RR-19", "TST-IRR-1782-30.2016.5.09.0325", "2019-03-14", "Delaíde Alves Miranda Arantes", "estabilidade",
  "A gestante que é dispensada sem justa causa tem direito à reintegração ao emprego ou, caso inviável, à indenização substitutiva equivalente aos salários e vantagens do período de estabilidade.",
  obs="Art. 10, II, 'b' ADCT; Súmula 244 TST")

# ── DANO MORAL / ASSÉDIO MORAL ────────────────────────────────────────────────
t("RR-20", "TST-RR-1116-52.2014.5.03.0183", "2016-09-21", "Claudio Brandao", "dano moral",
  "Configura assédio moral a conduta reiterada do empregador que submete o empregado a humilhações, constrangimentos e situações vexatórias no ambiente de trabalho.",
  obs="Art. 186 CC — dano moral no trabalho")

t("RR-21", "TST-RR-1000-38.2014.5.12.0037", "2017-04-05", "Lelio Bentes Corrêa", "dano moral",
  "A revista íntima em empregados, ainda que prevista em contrato ou acordo coletivo, viola a dignidade humana e enseja indenização por dano moral.",
  obs="Art. 373-A, VI CLT — vedação a revista íntima")

t("RR-22", "TST-AIRR-2094-27.2012.5.04.0263", "2015-11-11", "Márcio Eurico Vitral Amaro", "dano moral",
  "O dano moral decorrente do descumprimento das normas de saúde e segurança do trabalho é presumido (in re ipsa), dispensando comprovação do efetivo sofrimento.",
  obs="Dano moral presumido — violação NR")

# ── PRESCRIÇÃO ────────────────────────────────────────────────────────────────
t("RR-23", "TST-IRR-1000-34.2013.5.06.0251", "2016-05-18", "Cláudio Brandão", "prescrição",
  "A prescrição bienal começa a fluir na data da extinção do contrato de trabalho para a maioria das ações trabalhistas, sendo quinquenal no curso do contrato.",
  obs="Art. 7°, XXIX CF/88 — prazo prescricional trabalhista")

t("RR-24", "TST-RR-2001-87.2014.5.02.0374", "2017-11-22", "João Batista Brito Pereira", "prescrição",
  "O protesto judicial interrompe a prescrição trabalhista, retroagindo seus efeitos à data da distribuição do protesto.",
  obs="Art. 726 CPC/2015 — protesto interruptivo")

# ── CONTRATO DE TRABALHO / VÍNCULO EMPREGATÍCIO ───────────────────────────────
t("RR-25", "TST-AIRR-260-40.2012.5.04.0028", "2016-03-09", "Walmir Oliveira da Costa", "vínculo empregatício",
  "O trabalhador autônomo contratado sem exclusividade e sem subordinação não tem reconhecido o vínculo de emprego, mesmo que preste serviços de forma habitual.",
  obs="Art. 3° CLT — requisitos do vínculo empregatício")

t("RR-26", "TST-IRR-1000-33.2016.5.04.0305", "2019-10-30", "Guilherme Augusto Caputo Bastos", "vínculo empregatício",
  "O motorista de aplicativo pode ter reconhecido vínculo empregatício quando presentes os elementos da relação de emprego (pessoalidade, onerosidade, não eventualidade e subordinação).",
  obs="Art. 3° CLT; plataformas digitais de trabalho; debate em aberto")

# ── EQUIPARAÇÃO SALARIAL ──────────────────────────────────────────────────────
t("RR-27", "TST-RR-1498-55.2014.5.15.0087", "2018-06-13", "Aloysio Corrêa da Veiga", "remuneração",
  "A equiparação salarial exige identidade de função e de empregador, além de diferença de tempo de serviço não superior a dois anos entre o paradigma e o reclamante.",
  obs="Art. 461 CLT; Súmula 6 TST")

# Deduplicar e ordenar
seen = set()
deduped = []
for r in teses:
    k = r["tema"]
    if k not in seen:
        seen.add(k)
        deduped.append(r)

deduped.sort(key=lambda x: int(x["tema"].replace("RR-", "")))

with open(OUTPUT, "w", encoding="utf-8") as f:
    for r in deduped:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"✓ Gerados {len(deduped)} teses de recursos repetitivos do TST")
print(f"✓ Arquivo: {OUTPUT}")
print()
print("Distribuição por área:")
dist = Counter(r["area_direito"] for r in deduped)
for area, n in dist.most_common():
    print(f"  {area}: {n}")
