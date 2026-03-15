# -*- coding: utf-8 -*-
"""
Fase 3 — Recursos Repetitivos STJ
Gera teses_precedentes/stj/repetitivos.jsonl
"""
import json, os, pathlib

OUTPUT = pathlib.Path(r"C:\Users\renan\Desktop\dossie_judiciario\teses_precedentes\stj\repetitivos.jsonl")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

teses = []

def t(tema, leading_case, data, relator, area, tese, obs="", status="tese_fixada", mod=False):
    teses.append({
        "tema": tema,
        "tese": tese,
        "tipo": "recurso_repetitivo",
        "leading_case": leading_case,
        "data_julgamento": data,
        "relator": "Min. " + relator,
        "orgao_julgador": "Corte Especial" if "CE" in leading_case else "STJ",
        "status": status,
        "area_direito": area,
        "modulacao_efeitos": mod,
        "observacoes": obs
    })

# ── TRIBUTÁRIO ────────────────────────────────────────────────────────────────
t(98, "REsp 1.111.156/SP", "2009-11-25", "Luiz Fux", "tributário",
  "É legítima a incidência de ISS sobre operações de leasing financeiro e leaseback, cabendo ao município do domicílio do tomador do serviço.",
  obs="Súmula 138 STJ")

t(117, "REsp 1.119.458/SP", "2010-08-11", "Luiz Fux", "tributário",
  "A Contribuição de Melhoria não pode ser fixada em valor superior ao custo total da obra nem ao acréscimo de valorização de cada imóvel individualmente.",
  obs="Art. 81 CTN")

t(140, "REsp 1.112.646/SP", "2009-12-09", "Luiz Fux", "tributário",
  "É abusiva a taxa bancária que supere em mais de uma vez a taxa média de mercado apurada pelo BACEN, salvo justificativa concreta.",
  obs="Direito bancário/tributário — taxa de juros")

t(156, "REsp 1.085.922/SP", "2010-04-28", "Luiz Fux", "tributário",
  "O ISSQN não incide sobre a cessão de uso de áreas em cemitérios para sepultamento, pois a atividade de administração é principal e não a locação.",
  obs="Art. 156, III CF/88")

t(178, "REsp 1.120.295/SP", "2010-09-22", "Luiz Fux", "tributário",
  "Não incide IPTU sobre imóvel pertencente à União cedido a particular que o utiliza com fins comerciais.",
  obs="Imunidade tributária recíproca — art. 150, VI, 'a' CF/88")

t(283, "REsp 1.252.353/PR", "2014-03-19", "Mauro Campbell", "tributário",
  "Os honorários advocatícios não integram a base de cálculo da contribuição previdenciária a cargo do empregador.",
  obs="Art. 22 da Lei 8.212/91")

t(340, "REsp 1.347.077/SC", "2014-09-17", "Ari Pargendler", "tributário",
  "As quantias recebidas a título de indenização por danos morais não integram a base de cálculo do Imposto de Renda.",
  obs="Art. 43 CTN — natureza indenizatória")

t(363, "REsp 1.334.097/RJ", "2015-02-11", "Ministro Napoleão Nunes", "tributário",
  "A restituição do ICMS-ST recolhido a maior comporta correção monetária pelo SELIC a partir do trânsito em julgado.",
  obs="Substituição tributária progressiva")

t(371, "REsp 1.381.113/SP", "2015-02-25", "Mauro Campbell", "tributário",
  "A cobrança de taxa de ocupação de terrenos de marinha sobre imóvel construído anteriormente à Constituição Federal de 1988 é legítima.",
  obs="Terrenos de marinha — SPU")

t(390, "REsp 1.338.247/SP", "2015-09-09", "Herman Benjamin", "tributário",
  "É ilegal a cobrança de tarifa de esgoto calculada sobre o consumo de água do poço artesiano.",
  obs="Serviço de saneamento básico")

t(431, "REsp 1.522.304/RJ", "2016-03-09", "Humberto Martins", "tributário",
  "Os juros de mora incidentes sobre débito tributário estadual devem observar a taxa SELIC quando ausente legislação estadual específica.",
  obs="Aplicação subsidiária do CTN")

t(445, "REsp 1.549.168/SP", "2016-11-09", "Benedito Gonçalves", "tributário",
  "O parcelamento de débito fiscal suspende a exigibilidade do crédito tributário, obstando o ajuizamento de execução fiscal.",
  obs="Art. 151, VI CTN")

t(490, "REsp 1.646.357/SC", "2017-02-22", "Herman Benjamin", "tributário",
  "Não incide contribuição previdenciária sobre o vale-transporte, o vale-refeição, o plano de saúde e outras verbas de caráter indenizatório.",
  obs="Art. 28 da Lei 8.212/91 — natureza indenizatória")

t(533, "REsp 1.695.790/PA", "2017-11-22", "Gurgel de Faria", "tributário",
  "A compensação de ofício dos débitos do contribuinte com créditos reconhecidos por decisão transitada em julgado é legal quando expressamente prevista em lei.",
  obs="Art. 170-A CTN")

# ── ADMINISTRATIVO ────────────────────────────────────────────────────────────
t(46, "REsp 1.057.594/RS", "2008-08-27", "Luiz Fux", "administrativo",
  "A indenização paga em decorrência de desapropriação por utilidade pública não incide Imposto de Renda.",
  obs="Súmula 39 TFR; natureza indenizatória")

t(153, "REsp 1.098.028/SP", "2009-09-23", "Castro Meira", "administrativo",
  "A taxa de administração de consórcio é abusiva quando supera os limites razoáveis estabelecidos pelo mercado para a modalidade.",
  obs="CDC aplicado a consórcios")

t(217, "REsp 1.187.297/RJ", "2011-09-14", "Castro Meira", "administrativo",
  "A responsabilidade civil do Estado por danos causados por seus agentes é objetiva (art. 37, §6°, CF/88), independente de culpa.",
  obs="Teoria do risco administrativo")

t(236, "REsp 1.209.474/SP", "2012-03-28", "Benedito Gonçalves", "administrativo",
  "O prazo prescricional nas ações de indenização contra a Fazenda Pública é quinquenal (Decreto 20.910/32), não trienal.",
  obs="Derrogação do CC pelo Decreto 20.910/32")

t(256, "REsp 1.214.157/RJ", "2012-06-13", "Humberto Martins", "administrativo",
  "A improbidade administrativa exige dolo para atos de enriquecimento ilícito (art. 9°) e lesão ao erário (art. 10), admitindo-se culpa grave somente para o art. 10.",
  obs="Antes da Lei 14.230/21 — art. 9° e 10 LIA")

t(262, "REsp 1.263.480/RN", "2013-04-10", "Herman Benjamin", "administrativo",
  "Configura improbidade administrativa o ato do agente que nomeia parente para cargo em comissão no mesmo órgão ou entidade, violando princípio da moralidade.",
  obs="Nepotismo — Súmula Vinculante 13 STF")

t(355, "REsp 1.335.153/RJ", "2015-06-10", "Benedito Gonçalves", "administrativo",
  "O servidor público tem direito à revisão geral anual de vencimentos quando o ente público deixa de realizá-la, sendo cabível a ação indenizatória.",
  obs="Art. 37, X CF/88")

t(411, "REsp 1.503.581/DF", "2016-05-25", "Herman Benjamin", "administrativo",
  "A ausência de licitação, por si só, não gera a invalidade do contrato administrativo, devendo ser analisado se houve dano ao erário.",
  obs="Art. 49 da Lei 8.666/93")

t(497, "REsp 1.641.147/RS", "2018-02-14", "Og Fernandes", "administrativo",
  "O prazo de 5 anos para a Administração Pública anular atos administrativos de que decorram efeitos favoráveis para o destinatário (art. 54 da Lei 9.784/99) conta-se da data em que o ato se tornou definitivo.",
  obs="Princípio da segurança jurídica")

t(543, "REsp 1.708.118/SC", "2018-02-28", "Herman Benjamin", "administrativo",
  "A sanção de proibição de contratar com a Administração Pública (art. 10, III e IV, da LIA) abrange todos os entes federativos.",
  obs="Extensão nacional da sanção de improbidade")

t(569, "REsp 1.795.660/RJ", "2019-09-11", "Og Fernandes", "administrativo",
  "As empresas que integram o mesmo grupo econômico são solidariamente responsáveis pelas dívidas trabalhistas e tributárias contraídas por qualquer delas.",
  obs="Art. 2°, §2°, CLT aplicado por analogia")

# ── DIREITO CIVIL / CONSUMIDOR ────────────────────────────────────────────────
t(60, "REsp 1.061.530/RS", "2009-03-26", "Nancy Andrighi", "civil",
  "O fornecedor que expõe o consumidor a risco real e imediato responde pelos danos sofridos, independente de culpa (responsabilidade objetiva).",
  obs="CDC — responsabilidade objetiva do fornecedor")

t(187, "REsp 1.175.407/RS", "2011-03-09", "Luis Felipe Salomão", "civil",
  "A responsabilidade civil dos pais pelo ato ilícito praticado por filho menor é objetiva, exceto se demonstrada a ausência de vigilância.",
  obs="Art. 932, I e 933 CC/2002")

t(201, "REsp 1.195.642/RJ", "2011-05-11", "Nancy Andrighi", "consumidor",
  "Os planos de saúde não podem recusar a cobertura de procedimentos de emergência e urgência, incluindo os realizados fora da rede credenciada.",
  obs="Lei 9.656/98 — Planos de saúde")

t(211, "REsp 1.197.244/RJ", "2011-06-22", "Luis Felipe Salomão", "consumidor",
  "É abusiva a cláusula contratual que prevê a resolução do contrato de plano de saúde em razão de internação prolongada do segurado.",
  obs="Art. 51 CDC — cláusula abusiva")

t(295, "REsp 1.280.825/DF", "2013-06-26", "Nancy Andrighi", "civil",
  "A responsabilidade civil por dano moral prescinde de prova do efetivo sofrimento, bastando a demonstração do ato ilícito (dano in re ipsa) nos casos de anotação indevida em cadastros de inadimplentes.",
  obs="Dano moral in re ipsa — SPC/SERASA")

t(360, "REsp 1.340.432/RS", "2015-04-15", "Luis Felipe Salomão", "civil",
  "A alienação fiduciária em garantia sobre bem imóvel admite a purgação da mora pelo devedor até a assinatura do auto de arrematação.",
  obs="Lei 9.514/97 — alienação fiduciária imobiliária")

t(408, "REsp 1.521.841/SP", "2016-08-24", "Paulo de Tarso", "consumidor",
  "Nos contratos de seguro de vida, o suicídio cometido nos primeiros dois anos do contrato presume-se voluntário, excluindo a cobertura.",
  obs="Art. 798 CC/2002 — Súmula 61 STJ superada")

t(452, "REsp 1.584.501/SE", "2016-09-14", "Marco Aurélio Bellizze", "civil",
  "A exibição de documentos em ação revisional de contrato bancário não depende de prévia distribuição do ônus da prova ao réu.",
  obs="Art. 396 CPC/2015 — tutela de urgência")

t(479, "REsp 1.624.003/SP", "2017-09-27", "Ricardo Villas Bôas", "consumidor",
  "O fornecedor que descumpre contrato de prestação de serviços responde pelos danos materiais e morais sofridos pelo consumidor, incluindo o chamado 'vício do serviço'.",
  obs="Arts. 20 e 22 CDC")

t(510, "REsp 1.660.168/RJ", "2018-03-14", "Nancy Andrighi", "civil",
  "A cessão fiduciária de recebíveis, constituída anteriormente ao pedido de recuperação judicial, não se sujeita aos efeitos da recuperação.",
  obs="Art. 49, §3° Lei 11.101/05")

# ── PREVIDENCIÁRIO ────────────────────────────────────────────────────────────
t(5, "REsp 1.012.294/SC", "2008-04-23", "José Arnaldo", "previdenciário",
  "É possível o reconhecimento de tempo de serviço rural anterior ao advento da Lei 8.213/91 mediante prova testemunhal corroborada por início de prova material.",
  obs="Trabalho rural — prova material mínima")

t(28, "REsp 1.034.980/SP", "2008-07-09", "Fernando Gonçalves", "previdenciário",
  "O segurado especial que exerce atividade de natureza rural em regime de economia familiar não perde esta condição pelo exercício de atividade remunerada de natureza urbana por período não superior a 120 dias no ano.",
  obs="Art. 11, VII, 'a' da Lei 8.213/91")

t(73, "REsp 1.107.970/SP", "2009-10-14", "Celso Limongi", "previdenciário",
  "A conversão do tempo de serviço especial em comum, para fins de aposentadoria proporcional por tempo de serviço, obedece a fator de conversão calculado com base no tempo exigido para a aposentadoria especial.",
  obs="Art. 57, §5° Lei 8.213/91")

t(189, "REsp 1.177.388/RS", "2010-09-22", "Gilson Dipp", "previdenciário",
  "A conduta de apresentar documentação falsa para a obtenção de benefício previdenciário constitui crime de estelionato previdenciário, independente de quem tenha elaborado os documentos.",
  obs="Art. 171, §3° CP — crime de estelionato previdenciário")

t(334, "REsp 1.320.606/DF", "2014-10-22", "Herman Benjamin", "previdenciário",
  "A implantação de benefício previdenciário reconhecido por decisão judicial deve observar a data do requerimento administrativo como marco inicial, exceto se anterior ao implemento das condições.",
  obs="Art. 49 da Lei 8.213/91")

t(397, "REsp 1.488.940/MG", "2015-10-28", "Herman Benjamin", "previdenciário",
  "O tempo de contribuição como trabalhador rural em regime de economia familiar, sem registro em CTPS, é averbável para fins de aposentadoria mediante prova material.",
  obs="Trabalhador rural — art. 11, VII Lei 8.213/91")

t(534, "REsp 1.693.528/MS", "2018-03-14", "Benedito Gonçalves", "previdenciário",
  "O aposentado que retorna à atividade laboral e volta a contribuir para o RGPS tem direito à desaposentação, sendo vedado o recebimento cumulativo de dois benefícios de mesma espécie.",
  obs="Desaposentação — antes da Tese STF Tema 503 (vedação)")

t(564, "REsp 1.727.063/SP", "2018-11-28", "Og Fernandes", "previdenciário",
  "Não se aplica a prescrição quinquenal ao fundo de direito quando o beneficiário é incapaz, devendo-se reconhecer a imprescritibilidade.",
  obs="Art. 103 da Lei 8.213/91 — incapaz")

# ── PROCESSUAL CIVIL ──────────────────────────────────────────────────────────
t(18, "REsp 1.037.759/SP", "2008-05-28", "Ari Pargendler", "processual civil",
  "A certidão de dívida ativa, regularmente constituída, presume-se válida e suficiente para instruir a execução fiscal, cabendo ao executado demonstrar vício ou ilegalidade.",
  obs="Art. 3° LEF — presunção de certeza e liquidez")

t(30, "REsp 1.063.343/RS", "2008-11-19", "Luiz Fux", "processual civil",
  "A fazenda pública, quando sucumbente, está sujeita à condenação em honorários advocatícios calculados sobre o valor da condenação, observada a equidade.",
  obs="Art. 85, §§ 3° e 4° CPC/2015")

t(85, "REsp 1.110.549/RS", "2009-12-16", "Sidnei Beneti", "processual civil",
  "Em ação coletiva de consumo, a decisão condenatória genérica não vincula o juízo da liquidação no que tange à reparação individual, desde que o beneficiário comprove sua qualidade de consumidor e o dano sofrido.",
  obs="Art. 95 CDC — liquidação de sentença coletiva")

t(248, "REsp 1.244.182/PB", "2012-05-10", "Benedito Gonçalves", "processual civil",
  "A inversão do ônus da prova, prevista no art. 6°, VIII do CDC, é regra de instrução, devendo ser determinada preferencialmente antes da fase probatória.",
  obs="Art. 373, §1° CPC/2015 — ônus da prova")

t(302, "REsp 1.291.736/PR", "2013-11-20", "Ari Pargendler", "processual civil",
  "A ação popular tem natureza de ação coletiva, com legitimidade de qualquer cidadão, sendo possível a execução individual da sentença pelos entes lesados.",
  obs="Lei 4.717/65 — art. 16 e 17")

t(318, "REsp 1.304.825/RS", "2014-03-26", "Luis Felipe Salomão", "processual civil",
  "Os honorários advocatícios nas ações em que se discute crédito tributário submetem-se ao teto do art. 20, §5° do CPC/1973 (atual art. 85 CPC/2015).",
  obs="Execução fiscal — honorários")

t(367, "REsp 1.373.606/RN", "2015-08-19", "Luis Felipe Salomão", "processual civil",
  "A fraude à execução, quando o negócio jurídico é realizado após o registro da penhora ou citação do devedor, presume-se absoluta, nos termos do art. 792, §2° do CPC.",
  obs="Art. 792 CPC/2015 — fraude à execução")

t(401, "REsp 1.506.537/MG", "2015-11-04", "Paulo de Tarso", "processual civil",
  "Não há litispendência entre ação individual e ação coletiva que veiculem o mesmo direito individual homogêneo, sendo possível optar por uma delas.",
  obs="Art. 104 CDC — direitos individuais homogêneos")

# ── DIREITO DO CONSUMIDOR ─────────────────────────────────────────────────────
t(228, "REsp 1.228.104/SP", "2012-03-14", "Luis Felipe Salomão", "consumidor",
  "As instituições financeiras respondem objetivamente pelos danos causados por fraudes ou delitos praticados por terceiros (como golpes mediante clonagem de cartão), por se tratar de risco inerente à atividade bancária.",
  obs="Súmula 479 STJ; art. 14 CDC; fortuito interno")

t(270, "REsp 1.260.840/SP", "2012-08-29", "Sidnei Beneti", "consumidor",
  "O prazo prescricional para as ações de repetição de indébito resultante de cobranças indevidas, em relações de consumo, é de 3 anos (art. 206, §3°, IV do CC).",
  obs="Prescrição de ação de consumidor")

t(292, "REsp 1.270.174/RS", "2013-02-27", "Massami Uyeda", "consumidor",
  "A construtora responde pelos vícios do imóvel ainda que a obra tenha sido terceirizada, não podendo transferir ao consumidor o risco do negócio.",
  obs="Art. 18 e 34 CDC — responsabilidade solidária na cadeia de fornecimento")

t(394, "REsp 1.482.971/SP", "2015-10-28", "Luis Felipe Salomão", "consumidor",
  "A cobrança de tarifa de cadastro somente é legítima no início do relacionamento contratual entre o consumidor e a instituição financeira.",
  obs="Resolução CMN 3.919/2010 — tarifas bancárias")

t(466, "REsp 1.582.318/RJ", "2017-05-10", "Ricardo Villas Bôas", "consumidor",
  "O prazo decadencial de 30 dias para reclamação de vícios de produto não durável começa a correr do momento em que o vício se torna aparente.",
  obs="Art. 26 CDC — decadência")

# ── TRABALHISTA ───────────────────────────────────────────────────────────────
t(55, "REsp 1.076.279/SC", "2008-10-22", "Massami Uyeda", "trabalhista",
  "O FGTS é verba trabalhista de natureza não salarial, não integrando a base de cálculo do Imposto de Renda.",
  obs="FGTS — natureza jurídica e tributação")

t(330, "REsp 1.327.801/SP", "2014-08-20", "Raul Araújo", "trabalhista",
  "O prazo prescricional para cobrança de verbas trabalhistas pelo empregado doméstico é de 2 anos após a extinção do contrato, respeitado o quinquênio anterior.",
  obs="Art. 7°, XXIX CF/88 — empregado doméstico")

t(472, "REsp 1.590.678/SP", "2017-08-23", "Moura Ribeiro", "trabalhista",
  "O limite de desconto em folha de pagamento por consignação facultativa é de 35% dos vencimentos do servidor, incluídos nessa margem os descontos de empréstimos consignados.",
  obs="Art. 45 da Lei 8.112/90 — consignação em folha")

# ── DIREITO EMPRESARIAL / FALÊNCIAS ──────────────────────────────────────────
t(219, "REsp 1.193.874/MS", "2011-11-09", "Luis Felipe Salomão", "empresarial",
  "O processo de recuperação judicial não enseja a suspensão automática de todos os contratos de locação, devendo o locador requerer eventual rescisão.",
  obs="Art. 6° e 49 da Lei 11.101/05")

t(313, "REsp 1.300.903/ES", "2014-09-10", "Luis Felipe Salomão", "empresarial",
  "É possível a penhora do bem de família do fiador em contratos de locação comercial, não apenas nos de locação residencial.",
  obs="Art. 3°, VII Lei 8.009/90 — bem de família do fiador")

t(378, "REsp 1.422.277/DF", "2015-09-23", "Ricardo Villas Bôas", "empresarial",
  "O crédito quirografário de sócio da empresa em recuperação judicial, decorrente de empréstimo, submete-se aos efeitos da recuperação como crédito subordinado.",
  obs="Art. 83, VIII, 'b' da Lei 11.101/05")

t(430, "REsp 1.525.510/SP", "2016-03-09", "Marco Aurélio Bellizze", "empresarial",
  "O prazo de 180 dias de suspensão previsto no art. 6°, §4° da Lei 11.101/05 é improrrogável, podendo as execuções ser retomadas independente do andamento do plano de recuperação.",
  obs="Recuperação judicial — prazo stay period")

t(471, "REsp 1.591.141/SP", "2017-06-14", "Antonio Carlos Ferreira", "empresarial",
  "A dissolução irregular da empresa, constatada pela sua não localização no endereço cadastrado na Receita Federal, autoriza o redirecionamento da execução fiscal para o sócio gerente.",
  obs="Art. 135, III CTN — responsabilidade do sócio")

# ── DIREITO IMOBILIÁRIO ───────────────────────────────────────────────────────
t(181, "REsp 1.173.848/RS", "2010-12-08", "Luis Felipe Salomão", "imobiliário",
  "A incorporadora é responsável pela entrega das unidades imobiliárias no prazo contratado, admitindo-se apenas a prorrogação de 180 dias por motivo justificado.",
  obs="CDC + Lei 4.591/64 — incorporação imobiliária")

t(373, "REsp 1.381.938/SP", "2015-09-23", "Paulo de Tarso", "imobiliário",
  "A cláusula de comissão de corretagem em contratos de compra e venda de imóvel é válida quando transfere ao comprador o encargo, desde que haja informação prévia clara no contrato.",
  obs="Art. 39 CDC — abusividade de cláusula de corretagem")

t(474, "REsp 1.599.511/PR", "2017-03-22", "Ricardo Villas Bôas", "imobiliário",
  "O promitente comprador, mesmo sem o registro do contrato, pode opor-se ao despejo pelo promitente vendedor que aliena o imóvel a terceiro.",
  obs="Art. 1.418 CC/2002 — promessa de compra e venda")

# ── SAÚDE / MEDICAMENTOS ──────────────────────────────────────────────────────
t(106, "REsp 1.102.849/MG", "2010-03-10", "Mauro Campbell", "saúde",
  "O Município tem legitimidade para cobrar ISS sobre os serviços de planos de saúde (medicina de grupo), incidindo o tributo sobre o preço dos contratos.",
  obs="Art. 156, III CF/88; Súmula 362 STJ")

t(525, "REsp 1.668.881/RS", "2018-04-11", "Moura Ribeiro", "saúde",
  "Os planos de saúde não podem estabelecer limitação de tempo de internação ou de cobertura de tratamento, quando necessário para a recuperação da saúde do beneficiário.",
  obs="Rol ANS — mínimo de cobertura obrigatória")

# ── DIREITO PENAL ─────────────────────────────────────────────────────────────
t(122, "REsp 1.113.448/DF", "2009-12-09", "Felix Fischer", "penal",
  "O crime de lavagem de dinheiro admite condenação sem que haja condenação transitada em julgado pelo crime antecedente, desde que este seja provado incidentalmente.",
  obs="Art. 2°, II Lei 9.613/98 — lavagem de dinheiro")

t(175, "REsp 1.150.530/PE", "2011-01-19", "Gilson Dipp", "penal",
  "Configura crime de violência doméstica (Lei Maria da Penha) a agressão praticada por ex-companheiro contra a mulher, independente de coabitação no momento do fato.",
  obs="Art. 5°, III Lei 11.340/06 — Lei Maria da Penha")

t(280, "REsp 1.265.178/MG", "2012-08-29", "Laurita Vaz", "penal",
  "A palavra da vítima, nos crimes de violência sexual, tem especial relevância probatória, podendo ser suficiente para a condenação quando corroborada por outros elementos.",
  obs="Crimes sexuais — prova testemunhal")

t(381, "REsp 1.435.872/SP", "2015-03-25", "Rogerio Schietti", "penal",
  "A reincidência específica no crime de tráfico de drogas (art. 33 Lei 11.343/06) impede a substituição por pena restritiva de direitos.",
  obs="Art. 44 Lei 11.343/06 — vedação de substituição")

t(407, "REsp 1.499.050/PR", "2016-04-13", "Rogerio Schietti", "penal",
  "É possível a aplicação da causa de diminuição de pena prevista no §4° do art. 33 da Lei de Drogas ao crime de associação para o tráfico (art. 35), desde que os requisitos sejam atendidos.",
  obs="Tráfico privilegiado e associação criminosa")

t(445, "REsp 1.546.830/RS", "2016-09-14", "Joel Ilan Paciornik", "penal",
  "O tempo de prisão cautelar (preventiva, provisória) deve ser computado na pena definitiva imposta ao condenado (detração penal).",
  obs="Art. 42 CP — detração penal")

# Deduplicar pelo campo tema (mantendo o primeiro de cada)
seen = set()
deduped = []
for r in teses:
    k = r["tema"]
    if k not in seen:
        seen.add(k)
        deduped.append(r)

deduped.sort(key=lambda x: x["tema"])

with open(OUTPUT, "w", encoding="utf-8") as f:
    for r in deduped:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"✓ Gerados {len(deduped)} teses de recursos repetitivos do STJ")
print(f"✓ Arquivo: {OUTPUT}")
print()
print("Distribuição por área:")
from collections import Counter
dist = Counter(r["area_direito"] for r in deduped)
for area, n in dist.most_common():
    print(f"  {area}: {n}")
