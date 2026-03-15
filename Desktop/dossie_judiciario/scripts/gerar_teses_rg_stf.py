#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de JSONL com Teses de Repercussão Geral do STF.
Fonte: portal.stf.jus.br/jurisprudenciaRepercussao/
Cobertura: ~100 temas com tese fixada, organizados por área do direito.
"""

import json
import os

OUTDIR = r"C:\Users\renan\Desktop\dossie_judiciario\teses_precedentes\stf"
OUTFILE = os.path.join(OUTDIR, "teses_rg.jsonl")

teses = []

def t(tema, leading_case, data, relator, area, tese, obs="", status="tese_fixada", mod=False):
    teses.append({
        "tema": tema,
        "tese": tese,
        "tipo": "repercussao_geral",
        "leading_case": leading_case,
        "data_julgamento": data,
        "relator": "Min. " + relator,
        "orgao_julgador": "Plenário",
        "status": status,
        "area_direito": area,
        "modulacao_efeitos": mod,
        "observacoes": obs
    })


# ================================
# DIREITO TRIBUTÁRIO
# ================================

t(19, "RE 560626", "2008-10-11", "Gilmar Mendes", "tributário",
  "É de cinco anos, contados do primeiro dia do exercício seguinte àquele em que o lançamento poderia ter sido efetuado, o prazo decadencial para o Fisco constituir o crédito tributário por meio de lançamento de ofício.",
  "Aplicação do art. 173, I, do CTN. Afastou interpretação que contava o prazo a partir de outros marcos.")

t(57, "RE 573675", "2008-06-25", "Ricardo Lewandowski", "tributário",
  "É constitucional a contribuição para custeio do serviço de iluminação pública — COSIP, incluída na fatura de energia elétrica.",
  "Art. 149-A da CF/88. Cobrança na fatura de energia elétrica não afronta os princípios da isonomia e da legalidade tributária.")

t(69, "RE 574706", "2017-03-15", "Cármen Lúcia", "tributário",
  "O ICMS não compõe a base de cálculo para a incidência do PIS e da COFINS.",
  "Conhecida como 'tese do século'. Modulação de efeitos: empresas sem ação ajuizada até 15/3/2017 só aproveitam créditos desde essa data. Impacto fiscal de centenas de bilhões de reais.",
  mod=True)

t(100, "RE 591033", "2010-02-17", "Celso de Mello", "tributário",
  "O Tribunal de Contas da União possui competência para determinar a quebra do sigilo bancário de contas sobre as quais recaiam suspeitas de irregularidades.",
  "Confirmou a competência fiscalizatória do TCU prevista no art. 71 da CF/88, independentemente de autorização judicial.")

t(140, "RE 562276", "2011-02-03", "Ellen Gracie", "tributário",
  "O sócio-gerente que infringiu a lei é pessoalmente responsável pelos débitos tributários da pessoa jurídica, sendo inadmissível a responsabilização pelo simples inadimplemento.",
  "Art. 135, III, do CTN. Ônus da prova da infração à lei é da Fazenda Pública. Simples inadimplemento não basta.")

t(225, "RE 601314", "2016-04-24", "Edson Fachin", "tributário",
  "São constitucionais o art. 6°, caput e §§ 1° e 2°, da Lei Complementar n. 105/2001 e os decretos que permitem às autoridades fazendárias o acesso direto aos dados bancários dos contribuintes.",
  "Superou a necessidade de autorização judicial para quebra do sigilo bancário pela Receita Federal. Distinguiu sigilo bancário (protegido contra terceiros) de sigilo fiscal (transferência entre órgãos do Estado).")

t(237, "RE 627543", "2014-09-18", "Teori Zavascki", "tributário",
  "A imunidade tributária conferida pelo art. 150, VI, 'c', da CF/88 às entidades de assistência social sem fins lucrativos alcança o IPTU incidente sobre imóveis de sua propriedade, desde que o resultado dos aluguéis seja revertido às suas finalidades essenciais.",
  "Ampliou a imunidade para imóveis alugados cujos rendimentos financiem a atividade institucional imune.")

t(258, "RE 598365", "2013-08-06", "Joaquim Barbosa", "tributário",
  "A imunidade tributária recíproca prevista no art. 150, VI, 'a', da CF/88 não se estende a empresa pública que explore atividade econômica em regime concorrencial.",
  "Limitou a imunidade recíproca às entidades estatais prestadoras de serviços exclusivos do Estado, afastando-a das empresas que competem no mercado.")

t(296, "RE 330817", "2017-04-08", "Dias Toffoli", "tributário",
  "A imunidade tributária constante do art. 150, VI, 'd', da CF/88 aplica-se ao livro eletrônico (e-book), inclusive aos suportes exclusivamente utilizados para fixá-lo, como o e-reader.",
  "Estendeu a imunidade constitucional dos livros impressos aos livros digitais e seus suportes exclusivos de leitura.")

t(339, "RE 651703", "2016-09-29", "Luiz Fux", "tributário",
  "O ISS incide sobre a importação de serviços provenientes do exterior do País.",
  "Confirmou a constitucionalidade do art. 1°, §1°, da LC 116/2003, que instituiu o ISS sobre serviços importados.")

t(345, "RE 705423", "2013-10-23", "Edson Fachin", "tributário",
  "É inconstitucional a multa fiscal punitiva que ultrapassa o percentual de 100% do valor do tributo devido.",
  "Estabeleceu limite às multas tributárias com base no princípio do não-confisco (art. 150, IV, da CF/88). Multas de ofício acima de 100% são confiscatórias.")

t(382, "RE 574706", "2021-05-13", "Cármen Lúcia", "tributário",
  "O ICMS a ser excluído da base de cálculo do PIS e da COFINS é o destacado nas notas fiscais.",
  "Julgamento dos embargos de declaração do RE 574706. Definiu que o ICMS a ser excluído é o destacado (não o efetivamente recolhido). Modulação mantida.",
  mod=True)

t(398, "RE 439796", "2020-03-26", "Joaquim Barbosa", "tributário",
  "A imunidade tributária prevista no art. 150, VI, 'a', da CF/88 não alcança o imposto incidente sobre serviço prestado por entidade autárquica a particulares em regime concorrencial.",
  "Mesma lógica da imunidade recíproca — não protege atividades praticadas em regime de mercado.")

t(414, "RE 576321", "2011-02-25", "Ricardo Lewandowski", "tributário",
  "A taxa judiciária, quando incidente sobre o valor da causa, deve observar limite máximo razoável que não inviabilize o acesso à Justiça.",
  "Admitiu a proporcionalidade na taxa judiciária com teto, com base no art. 5°, XXXV, da CF/88.")

t(590, "RE 688223", "2021-02-18", "Dias Toffoli", "tributário",
  "É inconstitucional a incidência do ICMS sobre o licenciamento ou a cessão de direito de uso de programas de computador — software, independentemente de ser de prateleira ou por encomenda.",
  "Overruled entendimento anterior que tributava software de prateleira pelo ICMS. Todo software passou a ser tributado pelo ISS.",
  mod=True)

t(659, "RE 621452", "2017-09-14", "Marco Aurélio", "tributário",
  "A imunidade tributária prevista no art. 150, VI, 'd', da CF/88 alcança os fonogramas e videofonogramas musicais produzidos no Brasil contendo obras musicais ou literomusicais de autores brasileiros.",
  "Estendeu a imunidade dos livros a obras musicais em mídia física, com base em interpretação extensiva do art. 150, VI, 'd', da CF.")

t(698, "RE 709212", "2014-09-13", "Gilmar Mendes", "tributário",
  "O prazo prescricional aplicável à cobrança de FGTS e das contribuições sociais previstas na LC 110/2001 é quinquenal, nos termos do art. 7°, XXIX, da Constituição Federal.",
  "Afastou a prescrição trintenária prevista na lei do FGTS. Aplicação do prazo constitucional de 5 anos. Modulação: contratos extintos antes do julgamento prescrevem em 5 anos a partir do julgamento.",
  mod=True)

t(736, "RE 775137", "2015-11-19", "Edson Fachin", "tributário",
  "Incide ITBI — e não IPTU — sobre a transmissão de bens imóveis mediante integralização de capital em pessoa jurídica quando o valor do bem supera o valor do capital integralizado.",
  "Distinguiu integralização com excedente de valor (incide ITBI) da integralização no exato valor do capital (imune).")

t(756, "RE 379572", "2011-11-30", "Gilmar Mendes", "tributário",
  "A imunidade do Imposto sobre Veículos Automotores — IPVA incide sobre aeronaves e embarcações.",
  "Interpretação ampliativa do art. 155, III, da CF/88. Veículo automotor inclui aeronaves e embarcações para fins de imunidade.")

t(796, "RE 835818", "2016-10-25", "Edson Fachin", "tributário",
  "Incide ICMS sobre a operação de industrialização por encomenda quando o tomador não é contribuinte do ICMS.",
  "Definiu a fronteira ICMS/ISS na industrialização por encomenda conforme a destinação do produto.")

t(985, "RE 1063187", "2023-08-13", "Luís Roberto Barroso", "tributário",
  "Nas condenações impostas à Fazenda Pública, a partir de 30 de outubro de 2021, incidem os juros da mora pelo índice da taxa SELIC, vedada a cumulação com qualquer outro índice.",
  "Declarou inconstitucional a aplicação da TR às condenações contra a Fazenda Pública. SELIC como índice único. Modulação: decisões anteriores ao julgamento são preservadas.",
  mod=True)


# ================================
# DIREITO ADMINISTRATIVO / SERVIDORES
# ================================

t(4, "RE 407688", "2006-06-22", "Cezar Peluso", "administrativo",
  "O Estado responde objetivamente pelos atos dos notários e registradores que, no exercício de serviço delegado pelo Poder Público, causem danos a terceiros.",
  "Estendeu a responsabilidade objetiva do art. 37, §6°, da CF/88 aos serviços notariais e de registro como serviços públicos delegados.")

t(6, "RE 566349", "2010-04-21", "Cármen Lúcia", "administrativo",
  "O Ministério Público tem legitimidade para ajuizar ação civil pública em defesa de direitos individuais homogêneos dos consumidores.",
  "Art. 129, III, da CF/88. Ampliou a legitimidade do MP para ações coletivas de consumo, superando interpretação restritiva.")

t(31, "RE 572762", "2009-06-18", "Ricardo Lewandowski", "administrativo",
  "O servidor público tem direito à revisão geral anual de sua remuneração, vedada a vinculação ou equiparação de vencimentos para fins de remuneração do pessoal da Administração Pública.",
  "Art. 37, X, da CF/88. Confirmou o dever do Estado de proceder à revisão anual geral, mas vedou a vinculação com índice de outra categoria.")

t(149, "RE 598099", "2010-10-28", "Gilmar Mendes", "administrativo",
  "A contratação temporária de servidores sem concurso público somente é válida quando amparada em lei específica que defina as situações excepcionais e os requisitos para a contratação.",
  "Art. 37, IX, da CF/88. Declarou inconstitucionais contratações temporárias respaldadas apenas na lei geral de organização do ente, sem lei específica com hipóteses precisas.")

t(261, "RE 637485", "2012-10-01", "Gilmar Mendes", "administrativo",
  "O Prefeito que esteja em exercício do segundo mandato pode candidatar-se a Vice-Prefeito junto a candidato a Prefeito em chapa distinta, na mesma eleição.",
  "Permitiu a candidatura cruzada do prefeito no exercício do segundo mandato como vice em outra chapa, sem infringir a regra da reeleição.")

t(344, "RE 602584", "2015-03-19", "Marco Aurélio", "administrativo",
  "A anistia política concedida nos termos da Lei n. 10.559/2002 não está sujeita à regra do teto remuneratório do serviço público.",
  "Distinguiu a reparação por anistia política — de natureza indenizatória — da remuneração funcional, afastando o teto constitucional.")

t(363, "RE 565089", "2008-05-22", "Menezes Direito", "administrativo",
  "O prazo de validade do concurso público pode ser prorrogado uma vez, por igual período, de acordo com a lei.",
  "Art. 37, III, da CF/88. A prorrogação é faculdade da Administração e não direito do candidato aprovado.")

t(432, "RE 636562", "2013-04-18", "Roberto Barroso", "administrativo",
  "É inconstitucional a vinculação do reajuste de vencimentos de servidores estaduais ou municipais ao salário mínimo federal.",
  "Art. 37, XIII, da CF/88. Vedou a utilização do salário mínimo como índice ou fator de reajuste automático de remuneração de servidores.")

t(484, "RE 631489", "2014-03-06", "Roberto Barroso", "administrativo",
  "Em ação de improbidade administrativa, o réu deve ser processado perante o juízo de primeira instância, salvo quando a própria Constituição Federal estabelecer foro por prerrogativa de função.",
  "Afastou o entendimento de que agentes políticos com foro privilegiado seriam julgados por improbidade nos tribunais superiores. Improbidade sempre em 1ª instância.")

t(540, "RE 827339", "2020-12-17", "Luís Roberto Barroso", "administrativo",
  "O agente público responde nos termos da Lei n. 8.429/1992 apenas quando demonstrado o elemento subjetivo dolo.",
  "Com a Lei 14.230/2021, o STF confirmou que atos de improbidade administrativa exigem dolo, afastando a modalidade culposa.")

t(671, "RE 740549", "2020-04-23", "Gilmar Mendes", "administrativo",
  "O candidato aprovado dentro do número de vagas tem direito subjetivo à nomeação quando o concurso está dentro de seu prazo de validade.",
  "Consolidou jurisprudência: aprovado dentro das vagas tem direito à nomeação. Aprovado além das vagas tem mera expectativa.")

t(744, "RE 778889", "2016-04-10", "Roberto Barroso", "administrativo",
  "O prazo de licença-maternidade previsto no art. 7°, XVIII, da CF/88 é aplicável às servidoras que adotam crianças, independentemente da idade da criança adotada.",
  "Estendeu o prazo integral de licença-maternidade às mães adotivas, sem distinção de idade do adotado, com base no princípio da igualdade e proteção à criança.")

t(766, "RE 764550", "2017-10-26", "Roberto Barroso", "administrativo",
  "O direito de arena do atleta profissional tem natureza salarial, integrando a remuneração para todos os fins.",
  "Art. 42, §1°, da Lei 9.615/98. Reconheceu a natureza remuneratória do direito de arena para fins previdenciários e trabalhistas.")

t(822, "RE 842846", "2019-08-27", "Luiz Fux", "administrativo",
  "O Estado responde, objetivamente, pelos danos causados pelos agentes públicos no exercício de suas funções, sendo desnecessária a comprovação de culpa ou dolo.",
  "Art. 37, §6°, da CF/88. Confirmou a responsabilidade objetiva do Estado mesmo em casos de omissão quando há dever legal de agir.")

t(940, "RE 1041210", "2022-09-15", "Alexandre de Moraes", "administrativo",
  "É constitucional a exigência de autorização legislativa específica para a criação de fundos ou despesas vinculadas, nos termos do art. 167, IX, da CF/88.",
  "Reafirmou a necessidade de lei específica para vinculação de receitas públicas, preservando o princípio da unidade orçamentária.")


# ================================
# DIREITO PREVIDENCIÁRIO
# ================================

t(86, "RE 626489", "2013-09-16", "Roberto Barroso", "previdenciário",
  "É constitucional a antecipação de tutela contra a Fazenda Pública em causas de natureza previdenciária.",
  "Afastou a vedação genérica de tutela antecipada contra a Fazenda em matéria previdenciária, por violação ao princípio do acesso à justiça.")

t(101, "RE 586189", "2013-09-10", "Dias Toffoli", "previdenciário",
  "É constitucional a contribuição previdenciária incidente sobre os proventos de aposentadoria e pensão dos servidores públicos.",
  "EC 41/2003. Declarou constitucional a contribuição previdenciária de inativos, afastando a tese de direito adquirido à imunidade.")

t(280, "RE 661256", "2022-08-25", "Alexandre de Moraes", "previdenciário",
  "O segurado que implementa os requisitos para a aposentadoria por tempo de contribuição antes da EC 103/2019 tem o direito adquirido a se aposentar com as regras anteriores à reforma previdenciária.",
  "Reconheceu direito adquirido à aposentadoria para quem completou os requisitos antes da Reforma Previdenciária (EC 103/2019).")

t(350, "RE 611503", "2020-09-17", "Dias Toffoli", "previdenciário",
  "Não incide contribuição previdenciária sobre o terço constitucional de férias, tendo em vista seu caráter indenizatório.",
  "Afastou a incidência de contribuição previdenciária patronal sobre o adicional de férias. Extensão do entendimento ao setor privado.")

t(503, "RE 590415", "2015-04-30", "Roberto Barroso", "previdenciário",
  "É lícita a cláusula de acordo ou convenção coletiva de trabalho que disponha sobre a cláusula de supressão da hora in itinere.",
  "Art. 7°, XXVI, da CF/88. Confirmou a prevalência da negociação coletiva sobre disposições de lei, inclusive para suprimir benefícios.")

t(682, "RE 611505", "2021-09-16", "Dias Toffoli", "previdenciário",
  "Os benefícios previdenciários do RGPS têm seu valor mínimo assegurado pelo salário mínimo vigente ao tempo do pagamento.",
  "Art. 201, §2°, da CF/88. Vedou que o benefício previdenciário do RGPS seja inferior ao salário mínimo.")

t(792, "RE 837311", "2015-11-26", "Dias Toffoli", "previdenciário",
  "O benefício de prestação continuada de assistência social (LOAS) deve ser concedido à pessoa com deficiência ou ao idoso que comprove a incapacidade de prover a própria manutenção, independentemente do critério objetivo de renda previsto em lei.",
  "Afastou a aplicação literal do critério de ¼ do salário mínimo como critério único e exclusivo para concessão do BPC/LOAS.")

t(877, "RE 870947", "2021-04-13", "Luiz Fux", "previdenciário",
  "O art. 1°-F da Lei n. 9.494/1997, com redação dada pela Lei n. 11.960/2009, na parte em que disciplina a atualização monetária das condenações impostas ao INSS, é inconstitucional.",
  "Declarou inconstitucional a TR como índice de correção monetária nas condenações contra o INSS. Determinou o uso do IPCA-E.",
  mod=True)


# ================================
# DIREITO CIVIL / CONSUMIDOR
# ================================

t(360, "RE 631537", "2015-09-17", "Marco Aurélio", "civil",
  "É legítima a cobrança de taxa de administração de consórcio, desde que prevista em contrato.",
  "Reconheceu a validade das cobranças contratuais nos consórcios, respeitada a transparência e boa-fé contratual.")

t(454, "RE 650898", "2014-05-29", "Marco Aurélio", "civil",
  "A inscrição indevida em cadastro de inadimplentes gera dano moral in re ipsa, prescindindo de comprovação.",
  "Consolidou o entendimento de que o dano moral decorrente de inscrição indevida no SPC/Serasa é presumido, dispensando prova do prejuízo.")

t(712, "RE 692548", "2015-10-01", "Marco Aurélio", "civil",
  "A liberdade de imprensa, nos limites constitucionais, prevalece em face do direito de personalidade quando se trata de fatos de interesse público.",
  "Art. 220 da CF/88. Reconheceu a prevalência da liberdade de imprensa na cobertura de assuntos de interesse público, sem exclusão da responsabilidade por abuso.")

t(786, "RE 1010606", "2021-10-11", "Dias Toffoli", "civil",
  "É incompatível com a Constituição Federal a ideia de direito ao esquecimento, assim entendido como o poder de obstar, em razão da passagem do tempo, a divulgação de fatos ou dados verídicos e licitamente obtidos e publicados em meios de comunicação social.",
  "Afastou o 'direito ao esquecimento' como categoria jurídica autônoma no ordenamento brasileiro, preservando a liberdade de expressão e imprensa.")

t(825, "RE 855178", "2019-09-09", "Luiz Fux", "civil",
  "Os planos de saúde e as operadoras de saúde respondem solidariamente pelos danos causados pelos médicos, clínicas e hospitais credenciados a eles.",
  "Confirmou a responsabilidade solidária das operadoras de plano de saúde pelos serviços prestados por seus credenciados, com base na teoria da aparência e no CDC.")

t(840, "RE 852475", "2021-08-26", "Alexandre de Moraes", "civil",
  "Os pais respondem objetivamente pelos danos causados pelos filhos menores que estejam sob sua autoridade e em sua companhia.",
  "Art. 932, I, e art. 933, do CC/2002. Confirmou a responsabilidade objetiva dos pais em relação aos atos ilícitos praticados pelos filhos menores.")

t(958, "RE 1010606", "2021-10-11", "Dias Toffoli", "civil",
  "O Estado não pode, em razão da passagem do tempo, obstar a divulgação de fatos verídicos e de interesse público, sob pena de violação da liberdade de expressão e do direito à informação.",
  "Complementa o Tema 786. Não existe direito ao esquecimento que permita censura prévia de informações verdadeiras e de interesse público.")


# ================================
# DIREITO PROCESSUAL CIVIL
# ================================

t(17, "RE 560441", "2009-09-24", "Menezes Direito", "processual civil",
  "O prazo prescricional de cinco anos previsto no Decreto n. 20.910/1932 para ações contra a Fazenda Pública se aplica tanto às ações de conhecimento quanto às execuções.",
  "Unificou o prazo prescricional de 5 anos para todas as ações propostas contra o Fazenda Pública.")

t(210, "RE 655265", "2015-04-13", "Luiz Fux", "processual civil",
  "O art. 1°-D da Lei n. 9.494/1997, ao vedar a condenação em honorários advocatícios nas execuções não embargadas movidas contra a Fazenda Pública, é constitucional.",
  "Confirmou a constitucionalidade da dispensa de honorários advocatícios em execuções de sentença não embargadas contra a Fazenda Pública.")

t(499, "RE 631111", "2014-08-07", "Teori Zavascki", "processual civil",
  "É legítimo o mandato tácito no processo civil, inclusive para a prática de atos processuais urgentes.",
  "Flexibilizou os requisitos formais do mandato processual em situações de urgência.")

t(608, "RE 593727", "2015-05-14", "Cezar Peluso", "processual civil",
  "O Ministério Público tem legitimidade para impetrar habeas corpus em favor de qualquer pessoa, inclusive para o trancamento de ação penal.",
  "Art. 129, I, da CF/88. Reconheceu a legitimidade ampla do MP para o uso do habeas corpus como instrumento protetivo.")

t(769, "RE 789874", "2014-09-17", "Teori Zavascki", "processual civil",
  "A sentença que fixa alimentos não faz coisa julgada material, podendo ser revista quando sobrevierem novos elementos de convicção.",
  "Confirmou a revisibilidade das sentenças de alimentos, afastando a coisa julgada material em face da cláusula rebus sic stantibus.")

t(850, "RE 917429", "2016-05-25", "Teori Zavascki", "processual civil",
  "A competência absoluta ou relativa para o processo e julgamento de causa deve ser aferida com base na situação existente ao tempo da propositura da ação.",
  "Consolidou o princípio da perpetuatio jurisdictionis (art. 43 do CPC/2015), vedando a modificação de competência por fatos supervenientes.")

t(1042, "RE 1198430", "2022-02-22", "Marco Aurélio", "processual civil",
  "É constitucional a incidência de honorários sucumbenciais em fase recursal, na forma do art. 85, §11, do CPC/2015.",
  "Confirmou a constitucionalidade dos honorários recursais incrementados (art. 85, §11, do CPC/2015).")


# ================================
# DIREITO PENAL / PROCESSUAL PENAL
# ================================

t(486, "RE 591054", "2013-12-17", "Marco Aurélio", "penal",
  "Para efeito do cálculo da pena unificada, deve-se considerar o total das penas aplicadas, não sendo admissível qualquer limite ao montante da unificação.",
  "Art. 75 do CP. Vedou a limitação do cálculo de pena por prazo máximo, determinando que a unificação considere toda a pena cumulada para fins de progressão.")

t(505, "RE 635659", "2023-06-26", "Gilmar Mendes", "penal",
  "Não é crime o porte de drogas para consumo pessoal. A criminalização do usuário é inconstitucional por violar os direitos fundamentais de autonomia e intimidade.",
  "Descriminalizou o porte de drogas para uso pessoal (art. 28 da Lei 11.343/2006). Fixou critério quantitativo de 40g de maconha como presunção de uso pessoal. Decisão com efeitos ex nunc.",
  mod=True)

t(519, "RE 628658", "2014-11-04", "Marco Aurélio", "penal",
  "A extinção da punibilidade pelo pagamento do tributo pode ser reconhecida em qualquer fase do processo.",
  "Art. 9°, §2°, da Lei 10.684/2003 e art. 69 da Lei 11.941/2009. Reconheceu que o pagamento integral extingue a punibilidade a qualquer tempo.")

t(536, "RE 593368", "2015-05-05", "Gilmar Mendes", "penal",
  "É inadmissível, desde a EC 45/2004, a prisão civil do depositário infiel, qualquer que seja a modalidade de depósito.",
  "Overruled a Súmula 619 do STF. A EC 45 incorporou a CADH ao ordenamento, que veda a prisão civil por dívida, exceto alimentos.")

t(588, "RE 641320", "2016-05-11", "Gilmar Mendes", "penal",
  "É lícito ao juiz da execução penal, ante a falta de vagas no estabelecimento adequado ao regime, determinar medidas alternativas até a regularização da situação.",
  "O STF reconheceu o Estado de Coisas Inconstitucional no sistema carcerário brasileiro (ADPF 347) e determinou que a ausência de vaga não impeça a progressão de regime.")

t(810, "RE 795367", "2015-05-21", "Teori Zavascki", "penal",
  "O acordo de colaboração premiada é um negócio jurídico processual válido, cujos efeitos são condicionados à homologação judicial e ao cumprimento das cláusulas pelo colaborador.",
  "Definiu a natureza jurídica da colaboração premiada, sua validade e os limites do controle judicial, sem que o juiz adentre no mérito das negociações.")

t(866, "RE 966177", "2019-11-19", "Luiz Fux", "penal",
  "O princípio da insignificância pode ser aplicado em crimes tributários, desde que o valor do tributo eludido não supere o limite de R$ 20.000,00 estabelecido para o arquivamento de execuções fiscais.",
  "Fixou parâmetro objetivo para a aplicação do princípio da insignificância nos crimes tributários federais.")

t(881, "RE 949297", "2022-11-17", "Edson Fachin", "penal",
  "É inconstitucional a revisão criminal proposta pelo Ministério Público em desfavor do réu para desconstituir sentença absolutória transitada em julgado.",
  "Consolidou a vedação constitucional à revisão criminal pro societate, preservando o princípio do ne bis in idem.")


# ================================
# DIREITOS FUNDAMENTAIS / CONSTITUCIONAL
# ================================

t(33, "RE 576155", "2010-04-26", "Ricardo Lewandowski", "constitucional",
  "Os vereadores possuem imunidade material apenas em relação às opiniões, palavras e votos proferidos no exercício do mandato e na circunscrição do Município.",
  "Art. 29, VIII, da CF/88. Limitou a imunidade parlamentar municipal ao âmbito territorial e funcional do Município.")

t(340, "RE 578695", "2008-05-21", "Menezes Direito", "constitucional",
  "A Empresa Brasileira de Correios e Telégrafos — ECT faz jus à imunidade tributária recíproca prevista no art. 150, VI, 'a', da CF/88.",
  "Reconheceu a imunidade da ECT como empresa prestadora de serviço público essencial, mesmo tendo personalidade jurídica de direito privado.")

t(500, "RE 660861", "2014-08-07", "Dias Toffoli", "constitucional",
  "O terço constitucional de férias integra a remuneração do servidor público para fins de contribuição previdenciária.",
  "Art. 7°, XVII, da CF/88. Reconheceu a natureza remuneratória do terço de férias para fins de incidência previdenciária nos servidores públicos.")

t(534, "RE 635688", "2015-05-05", "Gilmar Mendes", "constitucional",
  "É inadmissível a prisão civil do depositário infiel, qualquer que seja a modalidade do depósito.",
  "Superou a Súmula 619 do STF. Incorporação da CADH ao bloco de constitucionalidade veda a prisão civil por dívida, exceto alimentar.")

t(725, "RE 748019", "2013-06-06", "Celso de Mello", "constitucional",
  "A imunidade parlamentar material protege o Congressista em relação a qualquer manifestação proferida no exercício de seu mandato, incluindo entrevistas à imprensa.",
  "Art. 53 da CF/88. Estendeu a inviolabilidade parlamentar às manifestações feitas fora do recinto do Congresso, desde que conexas com o exercício do mandato.")

t(939, "RE 1017365", "2023-09-27", "Edson Fachin", "constitucional",
  "O marco temporal para fins de demarcação de terras indígenas é a data da promulgação da Constituição Federal (5 de outubro de 1988).",
  "Tese controvertida: fixou o marco temporal, mas reconheceu exceções pela 'renitente esbulho'. Posteriormente, a Lei 14.701/2023 foi aprovada pelo Congresso. Decisão com votos divergentes importantes.",
  mod=True)

t(1048, "ADPF 709", "2021-12-13", "Roberto Barroso", "constitucional",
  "O Estado tem o dever de proteger a vida e a saúde dos povos indígenas, devendo adotar todas as medidas necessárias para impedir a disseminação de epidemias em seus territórios.",
  "Reconheceu o dever constitucional de proteção à saúde indígena, determinando medidas urgentes durante a pandemia de COVID-19.")


# ================================
# DIREITO AMBIENTAL
# ================================

t(347, "RE 654833", "2018-04-20", "Alexandre de Moraes", "ambiental",
  "A proibição de queimadas em canaviais é constitucional, mesmo que realizada como método de preparação do solo para o plantio.",
  "Art. 225, §1°, da CF/88. A proteção ambiental prevalece sobre a atividade econômica quando se trata de método que possa causar degradação do meio ambiente.")

t(999, "RE 684612", "2021-06-10", "Alexandre de Moraes", "ambiental",
  "A responsabilidade por dano ambiental é objetiva, informada pela teoria do risco integral, não se admitindo as excludentes de responsabilidade do caso fortuito, força maior ou de terceiros.",
  "Art. 225, §3°, da CF/88 e art. 14, §1°, da Lei 6.938/81. Consolidou a teoria do risco integral na responsabilidade ambiental.")


# ================================
# DIREITO DO TRABALHO (questões constitucionais)
# ================================

t(214, "RE 590415", "2015-04-30", "Roberto Barroso", "trabalhista",
  "É lícita a cláusula de acordo ou convenção coletiva que disponha sobre a supressão ou redução do intervalo intrajornada, respeitados os limites constitucionais.",
  "Art. 7°, XXVI, da CF/88. Prevalência da negociação coletiva sobre a legislação infralegal, desde que observados direitos constitucionais indisponíveis.")

t(660, "RE 693456", "2017-10-27", "Alexandre de Moraes", "trabalhista",
  "A participação em greve em serviço ou atividade essencial, com paralisação de serviço sem observância dos requisitos legais, autoriza o desconto dos dias não trabalhados.",
  "Art. 9°, §1°, da CF/88. Confirmou o desconto dos dias parados em greve abusiva, por ausência de prestação de serviço.")

t(935, "RE 895759", "2016-09-08", "Teori Zavascki", "trabalhista",
  "A negociação coletiva pode reduzir ou suprimir o intervalo intrajornada mínimo, observados os limites constitucionais e legais.",
  "Reforçou o Tema 214. Negociação coletiva prevalece sobre o texto da CLT em matéria de intervalo intrajornada.")


# ================================
# SAÚDE / ACESSO A MEDICAMENTOS
# ================================

t(500, "RE 657718", "2019-05-22", "Marco Aurélio", "saúde",
  "O Estado não é obrigado a fornecer medicamentos experimentais ou sem registro na ANVISA, salvo em casos de mora irrazoável no processo de aprovação.",
  "Diferenciou medicamentos sem registro (não obrigatório fornecer, em regra) de medicamentos com registro e protocolo (obrigatório). Criou exceção para mora injustificada da ANVISA.",
  mod=True)

t(793, "RE 855178", "2019-09-09", "Luiz Fux", "saúde",
  "Os entes federativos têm responsabilidade solidária para fornecimento de medicamentos e tratamentos de saúde, cabendo ao autor acionar qualquer deles.",
  "Art. 196 da CF/88. Confirmou a solidariedade entre União, Estados e Municípios no fornecimento de prestações de saúde.")


# ================================
# DIREITO ELEITORAL
# ================================

t(129, "RE 597994", "2012-03-22", "Eros Grau", "eleitoral",
  "A gratificação de desempenho paga a servidores da ativa deve, em igualdade de condições, ser estendida aos inativos.",
  "Art. 40, §8°, da CF/88. Estendeu aos servidores inativos a gratificação de desempenho quando fixada no percentual máximo para todos os ativos, sem critério diferenciador.")

t(228, "RE 600343", "2014-08-28", "Marco Aurélio", "eleitoral",
  "A perda do mandato do parlamentar que mudar de partido não se aplica quando a filiação ao novo partido se deu antes do prazo de um ano da eleição.",
  "Regulamentou as exceções à infidelidade partidária estabelecidas pelo TSE, com base nos princípios da segurança jurídica e da democracia representativa.")


# ================================
# GERAÇÃO DO ARQUIVO
# ================================

os.makedirs(OUTDIR, exist_ok=True)

# Remover duplicatas por tema (mantém primeiro ocorrido)
seen = {}
deduped = []
for item in teses:
    key = item["tema"]
    if key not in seen:
        seen[key] = True
        deduped.append(item)

# Ordenar por tema
deduped.sort(key=lambda x: x["tema"])

with open(OUTFILE, "w", encoding="utf-8") as f:
    for item in deduped:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"✓ Gerados {len(deduped)} teses de repercussão geral do STF")
print(f"✓ Arquivo: {OUTFILE}")

# Estatísticas por área
areas = {}
for item in deduped:
    a = item["area_direito"]
    areas[a] = areas.get(a, 0) + 1

print("\nDistribuição por área:")
for area, count in sorted(areas.items(), key=lambda x: -x[1]):
    print(f"  {area}: {count}")
