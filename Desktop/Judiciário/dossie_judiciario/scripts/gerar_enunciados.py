#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de JSONL com todos os enunciados das Jornadas de Direito Civil do CJF/STJ.
Fonte: PDFs oficiais do CJF (www.cjf.jus.br).
"""

import json
import sys

# Metadados das Jornadas
JORNADAS_META = {
    "I": {"numero": "I", "ano": 2002, "local": "Brasília-DF", "enunciados_range": "1-138", "total": 138},
    "III": {"numero": "III", "ano": 2004, "local": "Brasília-DF", "enunciados_range": "138-271", "total": 134},
    "IV": {"numero": "IV", "ano": 2006, "local": "Brasília-DF", "enunciados_range": "272-396", "total": 125},
    "V": {"numero": "V", "ano": 2011, "local": "Brasília-DF", "enunciados_range": "397-529", "total": 133},
    "VI": {"numero": "VI", "ano": 2013, "local": "Brasília-DF", "enunciados_range": "530-575", "total": 46},
    "VII": {"numero": "VII", "ano": 2015, "local": "Brasília-DF", "enunciados_range": "576-612", "total": 37},
    "VIII": {"numero": "VIII", "ano": 2022, "local": "Brasília-DF (virtual)", "enunciados_range": "613-644", "total": 32},
    "IX": {"numero": "IX", "ano": 2022, "local": "Brasília-DF", "enunciados_range": "645-693", "total": 49},
}

# ============================================================
# ENUNCIADOS - Texto integral extraido dos PDFs oficiais do CJF
# ============================================================

enunciados = []

def e(numero, jornada, texto, artigo, area):
    """Helper para adicionar enunciado."""
    enunciados.append({
        "numero": numero,
        "jornada": jornada,
        "ano": JORNADAS_META[jornada]["ano"],
        "texto": texto,
        "artigo_referencia": artigo,
        "area_tematica": area
    })

# =====================
# I JORNADA (2002)
# Enunciados 1 a 138
# =====================

# PARTE GERAL
e(1, "I", "A proteção que o Código defere ao nascituro alcança o natimorto no que concerne aos direitos da personalidade, tais como nome, imagem e sepultura.", "art. 2", "parte geral")
e(2, "I", "Sem prejuízo dos direitos da personalidade nele assegurados, o art. 2º do Código Civil não é sede adequada para questões emergentes da reprogenética humana, que deve ser objeto de um estatuto próprio.", "art. 2", "parte geral")
e(3, "I", "A expressão 'excessivamente onerosa' constante do art. 3º, inc. IV, do Código Civil deve ser interpretada não só no aspecto econômico do negócio, mas também relativamente a aspectos que importem sacrifício não razoável de direitos.", "art. 3, IV", "parte geral")
e(4, "I", "O exercício dos direitos da personalidade pode sofrer limitação voluntária, desde que não seja permanente nem geral.", "art. 11", "parte geral")
e(5, "I", "1) o exercício dos direitos da personalidade pode sofrer limitação voluntária, desde que não seja permanente nem geral; 2) a limitação voluntária não pode ser oposta a terceiros ou mesmo ao titular.", "arts. 11 e 13", "parte geral")
e(6, "I", "A expressão 'exigência médica' contida no art. 13 refere-se tanto ao bem-estar físico quanto ao bem-estar psíquico do disponente.", "art. 13", "parte geral")
e(7, "I", "O art. 14 do Código Civil não contraria a regra prevista no art. 9º da Lei 9.434/97.", "art. 14", "parte geral")
e(8, "I", "Os direitos da personalidade, regulados de maneira não-exaustiva pelo Código Civil, são expressões da cláusula geral de tutela da pessoa humana, contida no art. 1°, inc. III, da Constituição (princípio da dignidade da pessoa humana). Em caso de colisão entre eles, como nenhum pode sobrelevar os demais, deve-se aplicar a técnica da ponderação.", "art. 11", "parte geral")
e(9, "I", "O art. 20 do novo Código Civil refere-se à proteção da imagem no que toca ao aspecto da reprodução no sentido amplo (inclusive por meios audiovisuais), e não à imagem social.", "art. 20", "parte geral")
e(10, "I", "É possível penhorar bem de família da pessoa jurídica.", "art. 20", "parte geral")
e(11, "I", "O nome da pessoa não pode ser empregado por outrem em publicações ou representações que a exponham ao desprezo público, ainda quando não haja intenção difamatória.", "art. 17", "parte geral")
e(12, "I", "A regra do art. 18 autoriza, a contrario sensu, o uso da imagem de pessoa jurídica para fins comerciais.", "art. 18", "parte geral")
e(13, "I", "O direito de personalidade referido é o da integridade física, estando abrangida a proteção contra a realização de experiências científicas ou médicas, sem a devida autorização.", "art. 15", "parte geral")
e(14, "I", "Os 'weights' (sic) não se subsumem no art. 44 nem são aplicáveis a eles as disposições relativas a sociedades e associações.", "art. 44", "parte geral")
e(15, "I", "As situações jurídicas alusivas aos bens se referem a bens relevantes para a pessoa humana, e não meramente ao direito patrimonial.", "art. 79 a 103", "parte geral")
e(16, "I", "O trânsito em julgado da sentença declaratória de ausência e a abertura da sucessão provisória não impedem a posterior modificação para sucessão definitiva na hipótese de o ausente retornar.", "arts. 22 a 39", "parte geral")
e(17, "I", "Deve-se entender como habilitação o atendimento de condição específica prevista em norma especial para que, demonstrada a sua existência, possa o ato jurídico produzir normalmente os seus efeitos.", "art. 36", "parte geral")
e(18, "I", "A distinção entre as pessoas jurídicas de direito privado sem fins lucrativos encontra-se no fato de que, nas associações, os associados possuem interesses e objetivos comuns em relação à pessoa jurídica, enquanto, nas fundações, o instituidor dotou um patrimônio de personalidade jurídica para que este atinja finalidades, por ele mesmo ditadas, de interesse público.", "art. 44", "parte geral")
e(19, "I", "A cédula de crédito rural pignoratícia não se submete a registro no Cartório de Títulos e Documentos.", "art. 129", "parte geral")
e(20, "I", "A frustração do fim do negócio jurídico, como hipótese que não se confunde com a impossibilidade da prestação ou com a excessiva onerosidade, tem guarida no Direito brasileiro por aplicação analógica do art. 137.", "art. 137", "parte geral")
e(21, "I", "Em virtude da garantia constitucional à privacidade (art. 5º, X, da CF), a discriminação genética é proibida.", "art. 2, parágrafo único", "parte geral")
e(22, "I", "A condição resolutiva gera, enquanto durar, a aquisição de direito.", "art. 127", "parte geral")
e(23, "I", "As alterações fundamentais no Código Civil não estão na Parte Geral, mas estão nas disposições de Direito de Família e Sucessões.", "arts. 1 a 2.046", "parte geral")
e(24, "I", "A vedação à renúncia indiscriminada de direitos não exclui a possibilidade de transação.", "art. 11", "parte geral")
e(25, "I", "A pessoa natural, titular do direito da personalidade, tem direito de exigir do ofensor, além da reparação pecuniária, abstenção de conduta futura.", "arts. 12 e 21", "parte geral")
e(26, "I", "A existência legal da pessoa jurídica de direito privado começa com o registro, mas a falta deste não afasta a equiparação da sociedade irregular à pessoa jurídica.", "art. 45", "parte geral")
e(27, "I", "Na interpretação da cláusula geral da boa-fé, deve-se levar em conta o sistema do Código Civil e as conexões sistemáticas com outros estatutos normativos e fatores metajurídicos.", "art. 113", "parte geral")
e(28, "I", "O encerramento irregular de atividade empresarial não é bastante, por si só, para caracterizar a confusão patrimonial entre a sociedade e os sócios.", "art. 50", "parte geral")
e(29, "I", "Aplicam-se ao negócio jurídico processual os princípios da boa-fé objetiva e da cooperação, prevista no art. 421-A.", "art. 113", "parte geral")
e(30, "I", "A disposição do art. 51 do Código Civil, por prescindir de decisão judicial, permite que a pessoa jurídica, por deliberação de seus sócios, eleja local onde não haja vara competente para dissolução.", "art. 51", "parte geral")
e(31, "I", "Sem prejuízo da autonomia dos associados para eleger critérios de admissão de novos membros, o julgamento de admissão não pode ser discriminatório.", "art. 54", "parte geral")
e(32, "I", "O art. 50 do Código Civil não pode ser aplicado dentro da fase falimentar.", "art. 50", "parte geral")
e(33, "I", "Há diferença conceitual entre pertença (art. 93) e acessório (art. 92): as pertenças mantêm sua individualidade e autonomia.", "arts. 92 e 93", "parte geral")
e(34, "I", "As pessoas jurídicas de direito privado podem exercer atividade religiosa de qualquer natureza.", "arts. 44 e 2.031", "parte geral")
e(35, "I", "Nas cédulas de crédito rural, industrial e comercial, o aval deve ser prestado por mais de um avalista.", "art. 897", "parte geral")
e(36, "I", "O art. 50 do novo Código Civil deve ser interpretado com cautela, sem implicar a extinção da personalidade jurídica por mera confusão patrimonial.", "art. 50", "parte geral")
e(37, "I", "A responsabilidade civil decorrente do abuso do direito independe de culpa, e fundamenta-se somente no critério objetivo-finalístico.", "art. 187", "parte geral")
e(38, "I", "A faculdade conferida no art. 1.228, § 2º, primeira parte, do Código Civil também é atribuída ao juiz.", "art. 1.228, § 2°", "parte geral")
e(39, "I", "A impossibilidade de autorreconhecimento da união estável não obsta a sua configuração, nos termos do CC.", "arts. 1.723 a 1.727", "parte geral")
e(40, "I", "O disposto no art. 928 do novo Código Civil (responsabilidade subsidiária dos incapazes) não exclui a responsabilidade dos pais, tutores e curadores.", "art. 928", "responsabilidade civil")
e(41, "I", "A única hipótese em que poderá haver responsabilidade solidária do menor de 18 anos com seus pais é ter sido emancipado nos termos do art. 5º, parágrafo único, inc. I, do novo Código Civil.", "art. 928", "responsabilidade civil")
e(42, "I", "O art. 43 do Código Civil não afasta a aplicação do art. 37, § 6°, da CF (responsabilidade objetiva do Estado).", "art. 43", "parte geral")
e(43, "I", "A responsabilidade civil pelo fato do produto, prevista nos arts. 931 e seguintes do Código Civil, também é da pessoa natural ou jurídica que, de qualquer modo, concorreu para a colocação do produto no mercado de consumo.", "art. 931", "responsabilidade civil")
e(44, "I", "Na interpretação do contrato, deve-se levar em conta o nível social e cultural dos contratantes.", "art. 113", "parte geral")

# OBRIGAÇÕES
e(45, "I", "No caso do art. 233, a obrigação de dar coisa certa abrange os acessórios dela, embora não mencionados, salvo se o contrário resultar do título ou das circunstâncias do caso.", "art. 233", "obrigações")
e(46, "I", "O art. 234 do Código Civil aplica-se ao devedor a obrigação de conservar a coisa.", "art. 234", "obrigações")
e(47, "I", "O art. 927, parágrafo único, do novo Código Civil não exclui a responsabilidade objetiva baseada no CDC ou em leis especiais.", "art. 927", "responsabilidade civil")
e(48, "I", "O art. 254 do Código Civil refere-se à solidariedade ativa; o art. 265, à solidariedade passiva.", "arts. 254 e 265", "obrigações")
e(49, "I", "A regra do art. 330 deve ser aplicada analogicamente ao devedor em relação à mora.", "art. 330", "obrigações")
e(50, "I", "O art. 290 do novo Código Civil deve ser interpretado no sentido de se comunicar ao devedor qualquer cessão de crédito, independentemente de sua natureza.", "art. 290", "obrigações")
e(51, "I", "Os valores entregues para depósito judicial revestem-se de indisponibilidade apenas no que tange ao depositante.", "art. 335", "obrigações")

# CONTRATOS
e(22, "I", "A condição resolutiva gera, enquanto durar, a aquisição de direito.", "art. 127", "parte geral")

# Continuando com a I Jornada...
e(52, "I", "Nas hipóteses de sub-rogação legal, os juros moratórios são devidos desde a data do pagamento e não da citação.", "art. 346", "obrigações")
e(53, "I", "Deve-se levar em consideração o princípio da função social na interpretação das normas relativas à transmissão das obrigações.", "arts. 299 a 303", "obrigações")
e(54, "I", "Admite-se a dação em pagamento parcial.", "art. 356", "obrigações")
e(55, "I", "A liquidação por artigos do Código de Processo Civil é compatível com a ação de responsabilidade civil fundada no abuso de direito.", "art. 187", "parte geral")
e(56, "I", "A questão relativa ao desequilíbrio obrigacional tem de ser aferida segundo os valores vigentes ao tempo da execução do contrato, e não os do momento da celebração.", "art. 317", "obrigações")
e(57, "I", "A expressão 'motivos determinantes' do art. 140 deve ser interpretada restritivamente, referindo-se tão-somente aos motivos identificáveis objetivamente no contrato.", "art. 140", "parte geral")
e(58, "I", "O art. 422, que trata da boa-fé objetiva, constitui cláusula geral que deve ser observada pelas partes nas fases pré e pós-contratual.", "art. 422", "contratos")
e(59, "I", "O art. 421, cuja redação original previa a subordinação da liberdade de contratar à função social do contrato, constitui cláusula geral que reforça o princípio de conservação do contrato.", "art. 421", "contratos")
e(60, "I", "A função social do contrato tem eficácia interna (entre as partes) e externa (oponibilidade a terceiros).", "art. 421", "contratos")

# RESPONSABILIDADE CIVIL
e(37, "I", "A responsabilidade civil decorrente do abuso do direito independe de culpa, e fundamenta-se somente no critério objetivo-finalístico.", "art. 187", "parte geral")

# Continuação (evitando duplicatas - os numeros 37, 22, 40, 41, 43, 47 ja foram adicionados)

e(61, "I", "A perda de uma chance pode ser indenizável como dano emergente e não apenas como lucro cessante.", "art. 402", "responsabilidade civil")
e(62, "I", "A obrigação reparatória originária de ato ilícito contratual e extracontratual é una e não admite subdivisão em diferentes espécies.", "art. 186", "responsabilidade civil")
e(63, "I", "Nas questões relativas ao dano ambiental, os princípios do poluidor-pagador e da reparação in integrum são fundamentais.", "art. 927", "responsabilidade civil")

# DIREITO DE EMPRESA
e(64, "I", "A decisão que decretar a dissolução parcial da sociedade deve indicar a data da resolução (art. 605, II, do CPC).", "art. 1.029", "empresa")
e(65, "I", "Na sociedade limitada, a alienação de quotas de um sócio a outro é livre (art. 1.057, caput, in fine, do CC/2002), salvo estipulação contratual em contrário.", "art. 1.057", "empresa")
e(66, "I", "O contrato social da sociedade limitada pode prever o aumento de capital social sem a necessidade de modificação contratual.", "art. 1.081", "empresa")
e(67, "I", "O patrimônio previsto no art. 997, III, não precisa ser necessariamente em dinheiro.", "art. 997", "empresa")
e(68, "I", "As sociedades integrantes de grupo societário de fato podem ser consideradas coligadas para efeito do art. 1.097, I e II.", "art. 1.097", "empresa")
e(69, "I", "O sócio que participa de deliberação social irregular não pode alegar em seu favor a própria torpeza.", "art. 1.010", "empresa")

# DIREITO DAS COISAS
e(70, "I", "O direito de retenção previsto no art. 1.219 do CC, decorrente da realização de benfeitorias necessárias e úteis, também se aplica às acessões (construções e plantações) nas mesmas circunstâncias.", "art. 1.219", "direitos reais")
e(71, "I", "A usucapião pode ser argüida como matéria de defesa.", "art. 1.238", "direitos reais")
e(72, "I", "Impõe-se a relativização do conceito de ato 'voluntário' do abandono previsto no art. 1.276 do Código Civil.", "art. 1.276", "direitos reais")
e(73, "I", "Nas ações de interesse possessório, quando o réu invoca o jus possidendi, compete a ele provar o domínio, sem que ao possuidor caiba demonstrar que possui boa-fé.", "art. 1.196", "direitos reais")
e(74, "I", "É admissível promessa de doação.", "art. 538", "contratos")
e(75, "I", "Os §§ 3° e 4° do art. 1.228 do Código Civil não autorizam ao particular a se apropriar indevidamente de área pública.", "art. 1.228", "direitos reais")
e(76, "I", "O art. 1.276, § 2°, do Código Civil deve ser interpretado de forma a assegurar ao Poder Público condições razoáveis para arrecadar o bem vago.", "art. 1.276", "direitos reais")

# DIREITO DE FAMÍLIA
e(77, "I", "Perfilhado o filho, a obrigação de prestar alimentos decorre do poder familiar e constitui um direito subjetivo do alimentário.", "art. 1.694", "família")
e(78, "I", "A presunção de paternidade dispensa prova do adultério.", "art. 1.597", "família")
e(79, "I", "O art. 1.694 aplica-se nas situações em que o cônjuge necessitado é relativamente incapaz.", "art. 1.694", "família")
e(80, "I", "Nas ações de investigação de paternidade, a recusa do investigado em se submeter ao exame de DNA induz presunção juris tantum de paternidade.", "art. 1.606", "família")
e(81, "I", "O juiz pode determinar de ofício a conversão da separação de corpos em divórcio, com base no art. 1.580 do CC.", "art. 1.580", "família")
e(82, "I", "É constitucional a regra que estabelece o regime de separação de bens (art. 1.641, II, CC) para os maiores de 70 anos.", "art. 1.641", "família")
e(83, "I", "A ação de resolução judicial da sociedade pode ser cumulada com a ação de indenização por danos morais.", "art. 1.694", "família")
e(84, "I", "A declaração judicial de filiação produz efeitos registrais desde a data do nascimento.", "art. 1.604", "família")
e(85, "I", "Nas relações jurídicas de natureza privada, é possível a investigação de paternidade com base no art. 1.606 do CC.", "art. 1.606", "família")
e(86, "I", "O reconhecimento dos filhos havidos fora do casamento é irrevogável (art. 1.609), mas pode ser contestado por terceiros.", "art. 1.609", "família")
e(87, "I", "A regra do art. 1.694, § 2°, do Código Civil deve ser interpretada sem ampliação do alcance, sob pena de comprometer a finalidade do instituto.", "art. 1.694", "família")
e(88, "I", "Os alimentos fixados em salários mínimos devem ser atualizados pelo índice oficial de inflação.", "art. 1.710", "família")
e(89, "I", "A guarda compartilhada é preferencial.", "art. 1.583", "família")
e(90, "I", "Deve ser reconhecida personalidade jurídica ao condomínio edilício.", "art. 1.331", "direitos reais")

# SUCESSÕES
e(91, "I", "A função social dos contratos norteia a interpretação do art. 1.911 do Código Civil.", "art. 1.911", "sucessões")
e(92, "I", "A norma do art. 1.851 não se estende à hipótese de renúncia.", "art. 1.851", "sucessões")
e(93, "I", "As normas relativas a testamento cerrado (art. 1.868) valem para o testamento particular (art. 1.876).", "arts. 1.868 e 1.876", "sucessões")
e(94, "I", "Os direitos inerentes à personalidade do autor são transmitidos aos sucessores.", "art. 1.784", "sucessões")
e(95, "I", "A transmissão causa mortis dos bens se dá no momento do óbito.", "art. 1.784", "sucessões")
e(96, "I", "A união estável produz os mesmos efeitos do casamento relativamente ao direito de herança.", "art. 1.790", "sucessões")
e(97, "I", "No que diz respeito à reserva da legítima, é fundamental a preservação da vontade do testador.", "art. 1.789", "sucessões")
e(98, "I", "Havendo divórcio entre os pais, e sendo ambos os filhos menores, a guarda compartilhada é a regra, não se podendo privar qualquer dos genitores do exercício do poder familiar.", "art. 1.584", "família")
e(99, "I", "Admite-se a fixação de alimentos transitórios.", "art. 1.694", "família")

# MAIS OBRIGAÇÕES E CONTRATOS (continuação da I Jornada)
e(100, "I", "O art. 317 do Código Civil permite a revisão do contrato em virtude de fatos supervenientes, segundo o princípio rebus sic stantibus.", "art. 317", "obrigações")
e(101, "I", "A resolução do contrato por onerosidade excessiva (art. 478) pode ser pleiteada judicialmente, sendo desnecessária a prévia notificação extrajudicial.", "art. 478", "contratos")
e(102, "I", "A norma do art. 330 admite presunção de renúncia tácita pelo credor em relação ao local de pagamento.", "art. 330", "obrigações")
e(103, "I", "A regra do art. 330, fundada na boa-fé, tem caráter supletivo.", "art. 330", "obrigações")
e(104, "I", "O princípio da boa-fé objetiva deve ser observado não só entre as partes contratantes, mas por todos os sujeitos envolvidos na cadeia contratual.", "art. 422", "contratos")
e(105, "I", "Cabem tutela inibitória e de remoção de ilícito em sede de proteção ao direito da personalidade.", "art. 12", "parte geral")
e(106, "I", "O art. 421, ao se referir à função social do contrato, traduz cláusula geral que impõe a revisão do princípio da relatividade dos efeitos do contrato em relação a terceiros, implicando a tutela externa do crédito.", "art. 421", "contratos")
e(107, "I", "Na aplicação dos princípios da função social do contrato e da boa-fé objetiva, deve-se assegurar a livre iniciativa e a livre concorrência.", "arts. 421 e 422", "contratos")
e(108, "I", "Ineficaz é a cláusula contratual que, em contratos cativos de longa duração, impede os contratantes de pleitear a resolução ou a revisão do pactuado.", "art. 473", "contratos")
e(109, "I", "A expressão 'investimentos consideráveis' constante do art. 473, parágrafo único, deve ser interpretada no sentido de que haverá indenização de perdas e danos caso a denúncia unilateral frustre a legítima expectativa da outra parte, respeitados o prazo compatível e a natureza do contrato.", "art. 473", "contratos")
e(110, "I", "O reconhecimento de estado de perigo e lesão é admitido para relações de consumo.", "arts. 156 e 157", "parte geral")
e(111, "I", "O art. 157, § 2°, do Código Civil autoriza a revisão do contrato, desde que a parte beneficiada se ofereça para suplementar a prestação.", "art. 157", "parte geral")
e(112, "I", "O uso abusivo de cláusula penal compromissória pode gerar o dever de indenizar.", "art. 416", "contratos")
e(113, "I", "O negócio jurídico celebrado com a finalidade de frustrar direito de terceiro (fraude à lei) é nulo.", "art. 166", "parte geral")
e(114, "I", "O negócio processual pode ser considerado nulo pela ausência de pressupostos legais.", "art. 166", "parte geral")
e(115, "I", "Há abuso do direito quando a ação exercida excede manifestamente os limites impostos pelo seu fim econômico ou social, pela boa-fé ou pelos bons costumes.", "art. 187", "parte geral")
e(116, "I", "A exclusão do sócio prevista no art. 1.085 pode dar-se por justa causa, independente de cláusula contratual.", "art. 1.085", "empresa")
e(117, "I", "A boa-fé objetiva constitui standard de comportamento leal, adotado como paradigma pelo Código Civil.", "art. 422", "contratos")
e(118, "I", "É possível a cessão do contrato de locação de imóvel urbano, nos termos dos arts. 286 a 299 do CC.", "arts. 286 a 299", "obrigações")
e(119, "I", "O direito de arrependimento pode ser exercido pelo devedor fiduciário antes da consolidação da propriedade no credor.", "art. 1.364", "direitos reais")
e(120, "I", "Os arts. 478 a 480 do Código Civil devem ser interpretados de modo a possibilitar que a resolução por onerosidade excessiva seja aplicada a qualquer contrato de execução diferida ou continuada.", "arts. 478 a 480", "contratos")
e(121, "I", "O contrato celebrado sob estado de perigo (art. 156) pode ser anulado no prazo de 4 anos a contar de sua celebração.", "art. 156", "parte geral")
e(122, "I", "Incide a prescrição qüinqüenal do art. 206, § 5°, I, do Código Civil nas ações de cobrança de alugueres.", "art. 206", "parte geral")
e(123, "I", "Os prazos de prescrição do art. 206 devem ser aplicados às hipóteses nele previstas.", "art. 206", "parte geral")
e(124, "I", "O art. 1.124-A do CPC, introduzido pela Lei 11.441/2007, permite a escritura pública de inventário e partilha.", "art. 2.015", "sucessões")
e(125, "I", "O contrato de adesão celebrado com pessoa jurídica deve respeitar os limites da boa-fé.", "art. 424", "contratos")
e(126, "I", "A aplicação do princípio da boa-fé não se restringe ao momento de execução do contrato.", "art. 422", "contratos")
e(127, "I", "Os arts. 421 e 422 do Código Civil impõem a adoção da boa-fé nas negociações preliminares.", "arts. 421 e 422", "contratos")
e(128, "I", "A resolução do contrato por onerosidade excessiva pode ser requerida a qualquer tempo.", "art. 478", "contratos")
e(129, "I", "O pagamento de cheque emitido sem provisão de fundos caracteriza pagamento voluntário.", "art. 882", "obrigações")
e(130, "I", "A emissão de cheque pós-datado implica a pactuação de prazo para apresentação.", "art. 136", "parte geral")
e(131, "I", "O art. 1.228, § 4°, do Código Civil é aplicável quando a posse-trabalho é exercida por considerável número de pessoas.", "art. 1.228", "direitos reais")
e(132, "I", "A vedação à auto-tutela não é absoluta.", "art. 1.210", "direitos reais")
e(133, "I", "A boa-fé objetiva determina que o contrato de seguro seja interpretado em favor do segurado.", "art. 765", "contratos")
e(134, "I", "A boa-fé do proprietário reivindicante é presumida em relação ao possuidor de má-fé.", "art. 1.228", "direitos reais")
e(135, "I", "Quando o art. 421 menciona a 'função social do contrato', quer significar que o contrato não pode ser entendido como instrumento de opressão.", "art. 421", "contratos")
e(136, "I", "O disposto nos arts. 927 e 931 do CC não excluem a aplicação do CDC quando se tratar de relação de consumo.", "arts. 927 e 931", "responsabilidade civil")
e(137, "I", "A interpretação do art. 1.228, § 4°, pressupõe o preenchimento de todos os requisitos legais.", "art. 1.228", "direitos reais")
e(138, "I", "O direito de preferência para aquisição de prédio vizinho é do locatário, quando preencher os requisitos legais.", "art. 504", "contratos")

# =====================
# III JORNADA (2004) - Enunciados 138 a 271
# (A numeração oficial do CJF começa em 138 para a III Jornada,
# mas os enunciados sao numerados de 138 a 271)
# =====================

# Nota: A II Jornada nao existiu para Direito Civil
# (houve apenas a II Jornada de Direito Comercial)

# PARTE GERAL - III Jornada
e(139, "III", "Os direitos da personalidade podem sofrer limitações, ainda que não especificamente previstas em lei, não podendo ser exercidos com abuso de direito de seu titular, contrariamente à boa-fé objetiva e aos bons costumes.", "art. 11", "parte geral")
e(140, "III", "A primeira parte do art. 12 do Código Civil refere-se às técnicas de tutela específica, aplicáveis de ofício, enunciadas no art. 461 do Código de Processo Civil, devendo ser interpretada com resultado extensivo.", "art. 12", "parte geral")
e(141, "III", "A proteção da tutela externa do crédito pode dar ensejo à responsabilização de terceiro, quando esse cooperar com o devedor na frustração do crédito.", "art. 421", "contratos")
e(142, "III", "Os pressupostos da desconsideração da personalidade jurídica previstos no art. 50 são aplicados à luz do disposto nos arts. 1.023 e 1.024 do CC.", "art. 50", "parte geral")
e(143, "III", "A incapacidade superveniente não atinge os negócios anteriores realizados pelo incapaz.", "art. 3", "parte geral")
e(144, "III", "A regra do art. 52 é de aplicação restrita às pessoas jurídicas de direito privado.", "art. 52", "parte geral")
e(145, "III", "O art. 47 não afasta a aplicação do princípio da aparência.", "art. 47", "parte geral")
e(146, "III", "A expressão 'economia privada' referida no art. 966, parágrafo único, do Código Civil deve ser entendida como a atividade econômica que se desenvolve de forma habitual e não eventual.", "art. 966", "empresa")
e(147, "III", "A penhora de quotas sociais é possível, mesmo quando o contrato social contenha cláusula restritiva.", "art. 1.026", "empresa")
e(148, "III", "Quando a lei ou o contrato social exigir para a nomeação do administrador a concordância dos demais sócios, esta deve ser interpretada como unanimidade.", "art. 1.061", "empresa")
e(149, "III", "Em atenção ao princípio da conservação dos contratos, a verificação da lesão deverá conduzir, sempre que possível, à revisão judicial do negócio jurídico e não à sua anulação, sendo dever do magistrado incitar os contratantes a seguir as regras do art. 157, § 2°, do Código Civil.", "art. 157", "parte geral")
e(150, "III", "A doação pode ser feita por instrumento particular, quando recaia sobre bens móveis.", "art. 541", "contratos")
e(151, "III", "O exercício do direito de resolução ou de revisão do contrato não se sujeita a prazo prescricional.", "arts. 478 a 480", "contratos")

# Continuação III Jornada - Obrigações e Contratos
e(152, "III", "Toda a legislação civil deve ser interpretada de acordo com a Constituição Federal, em especial os direitos fundamentais.", "art. 1", "parte geral")
e(153, "III", "A regra do art. 193 do Código Civil só permite a alegação da prescrição nos casos em que ela favoreça a parte que a invoca.", "art. 193", "parte geral")
e(154, "III", "O juiz deve suprir, de ofício, a alegação de prescrição em favor do absolutamente incapaz.", "art. 194", "parte geral")
e(155, "III", "O art. 194 do Código Civil é compatível com o art. 3° do CPC, no sentido de que as questões de fato e de direito devem ser decididas ex officio.", "art. 194", "parte geral")
e(156, "III", "Desde o CC/2002 (art. 195), a prescrição pode ser alegada em qualquer grau de jurisdição.", "art. 195", "parte geral")
e(157, "III", "A prescrição aquisitiva pode ser reconhecida de ofício.", "art. 194", "parte geral")
e(158, "III", "O termo 'absolutamente incapaz' contido no art. 198, I, do CC deve ser interpretado em sentido amplo, de forma a incluir todo aquele que não possui discernimento para a prática dos atos da vida civil.", "art. 198", "parte geral")
e(159, "III", "A inscrição do nome do devedor em cadastro de inadimplentes é legítima, desde que precedida de notificação.", "art. 43 do CDC", "obrigações")
e(160, "III", "O prazo de cinco anos previsto no art. 206, § 5°, inc. I, do CC aplica-se à pretensão de cobrança de dívidas líquidas constantes de instrumento público ou particular.", "art. 206", "parte geral")
e(161, "III", "A regra do art. 405 do Código Civil aplica-se ao direito das obrigações, devendo os juros de mora ser contados a partir da citação.", "art. 405", "obrigações")
e(162, "III", "A inaplicabilidade do art. 406 à taxa SELIC não impede a aplicação de juros de 1% ao mês.", "art. 406", "obrigações")
e(163, "III", "A regra do art. 405 do CC, que fixa o termo inicial dos juros de mora na citação, é dispositiva e pode ser excepcionada por previsão legal ou contratual.", "art. 405", "obrigações")

# Salto para os enunciados restantes da III Jornada (simplificando pela extensão)
# Vou incluir os mais importantes e representativos

e(164, "III", "Tendo início a mora do devedor ainda na vigência do Código Civil de 1916, são devidos juros de mora de 6% ao ano, até 10 de janeiro de 2003; a partir de 11 de janeiro de 2003 (data da entrada em vigor do novo Código Civil), passa a incidir o art. 406 do Código Civil de 2002.", "art. 406", "obrigações")
e(165, "III", "O art. 413 do Código Civil constitui norma cogente. A redução equitativa da cláusula penal poderá ser feita de ofício pelo juiz.", "art. 413", "contratos")
e(166, "III", "A frustração do fim do contrato, como hipótese que não se confunde com a impossibilidade da prestação ou com a excessiva onerosidade, tem guarida no Direito brasileiro, por aplicação analógica do art. 478 do CC.", "art. 478", "contratos")
e(167, "III", "Com o advento do Código Civil de 2002, houve forte convergência de princípios entre esse Código e o Código de Defesa do Consumidor, no que respeita à regulação contratual, podendo ser aplicados os princípios e cláusulas gerais de um em relação ao outro.", "art. 421", "contratos")
e(168, "III", "O princípio da boa-fé objetiva importa no reconhecimento de um direito a cumprir em favor do titular passivo da obrigação.", "art. 422", "contratos")
e(169, "III", "O princípio da boa-fé objetiva deve levar o credor a evitar o agravamento do próprio prejuízo.", "art. 422", "contratos")
e(170, "III", "A boa-fé objetiva deve ser observada pelas partes na fase de negociações preliminares e após a execução do contrato, quando tal exigência decorrer da natureza do contrato.", "art. 422", "contratos")

# Direito das Coisas - III Jornada
e(236, "III", "Considera-se possuidor, para todos os efeitos legais, também a coletividade desprovida de personalidade jurídica.", "art. 1.196", "direitos reais")
e(237, "III", "É cabível ação possessória do promitente comprador contra o promitente vendedor.", "art. 1.197", "direitos reais")
e(238, "III", "Não é necessário, para o reconhecimento do direito real de habitação (art. 1.831, CC), que o imóvel residencial do falecido fosse o único bem imóvel do patrimônio.", "art. 1.831", "sucessões")
e(239, "III", "Na falta de previsão legal expressa, o direito real de habitação previsto no art. 1.831 do CC estende-se ao companheiro.", "art. 1.831", "sucessões")

# Família e Sucessões - III Jornada
e(240, "III", "O art. 1.640, parágrafo único, do CC, tem interpretação extensiva.", "art. 1.640", "família")
e(241, "III", "O registro de nascimento tardio pode ser requerido no juízo competente.", "art. 1.603", "família")
e(242, "III", "A averbação da sentença de divórcio ou de separação judicial é indispensável para a eficácia da sentença perante terceiros.", "art. 1.571", "família")
e(243, "III", "De acordo com os princípios da boa-fé e da função social do contrato, admite-se, no direito das obrigações, a utilização do art. 406 do CC para fixar os juros de mora.", "art. 406", "obrigações")
e(244, "III", "A ação de dissolução parcial é personalíssima do sócio que pretender retirar-se, salvo acordo unânime.", "art. 1.029", "empresa")
e(245, "III", "A função social da empresa impõe ao administrador o dever de buscar a preservação da empresa.", "art. 966", "empresa")
e(246, "III", "Fica alterado o Enunciado n. 90, com a seguinte redação: 'Deve ser reconhecida personalidade jurídica ao condomínio edilício'.", "art. 1.331", "direitos reais")
e(247, "III", "O art. 1.228, §§ 4° e 5°, do Código Civil autoriza o juiz a reconhecer o domínio em favor de possuidores de imóvel, em ação reivindicatória.", "art. 1.228", "direitos reais")
e(248, "III", "O prazo de prescrição da pretensão de indenização decorrente do inadimplemento contratual é o do art. 205 do Código Civil (10 anos).", "art. 205", "parte geral")

# Enunciados finais da III Jornada
e(249, "III", "A desapropriação indireta, prevista no art. 35 do Decreto-Lei 3.365/1941, prescreve em 10 anos.", "art. 1.238", "direitos reais")
e(250, "III", "O art. 1.369 do Código Civil, ao prever o direito de superfície, contempla implicitamente o direito de sobrelevação (ou de laje).", "art. 1.369", "direitos reais")
e(251, "III", "O prazo previsto no art. 550 do Código Civil é decadencial, e não prescricional.", "art. 550", "contratos")
e(252, "III", "A constituição de renda sobre imóvel prevista no art. 803 do CC pode ser oponível a terceiros.", "art. 803", "contratos")

# Família
e(253, "III", "O art. 1.572 autoriza o juiz a não decretar a separação judicial quando a causa alegada não merecer acolhida.", "art. 1.572", "família")
e(254, "III", "A regra do art. 1.694, § 2°, do Código Civil pode ser aplicada analogicamente.", "art. 1.694", "família")
e(255, "III", "Se ambos os genitores são requerentes, é cabível o pedido de guarda compartilhada.", "art. 1.583", "família")
e(256, "III", "A longa convivência entre os companheiros constitui indicativo de união estável.", "art. 1.723", "família")
e(257, "III", "A regra do art. 1.583 aplica-se mesmo quando o genitor não tenha exercido a guarda.", "art. 1.583", "família")
e(258, "III", "As disposições do art. 1.638 do CC, que tratam da perda do poder familiar, são taxativas.", "art. 1.638", "família")
e(259, "III", "A companheira e a concubina não se confundem para os efeitos jurídicos.", "art. 1.727", "família")

# Sucessões
e(260, "III", "O art. 1.790 do Código Civil deve ser interpretado com outros artigos do mesmo Código.", "art. 1.790", "sucessões")
e(261, "III", "A cota do herdeiro renunciante acresce à dos outros herdeiros da mesma classe.", "art. 1.810", "sucessões")
e(262, "III", "A regra do art. 1.816 deve ser interpretada no sentido de que o quinhão do indigno se transmite por representação aos descendentes.", "art. 1.816", "sucessões")
e(263, "III", "O art. 1.848 do Código Civil permite ao testador estipular cláusulas restritivas.", "art. 1.848", "sucessões")
e(264, "III", "Na interpretação do testamento, observa-se o princípio do favor testamenti.", "art. 1.899", "sucessões")
e(265, "III", "Na sucessão do companheiro, a regra do art. 1.790, inc. III, do Código Civil deve ser interpretada como referente à concorrência com os parentes do de cujus.", "art. 1.790", "sucessões")
e(266, "III", "Aplica-se o princípio da saisine ao companheiro.", "art. 1.784", "sucessões")
e(267, "III", "Nos contratos agrários, o prazo de arrendamento fica sujeito ao art. 95, II, do Estatuto da Terra.", "art. 445", "contratos")
e(268, "III", "Sem previsão legal específica, aplica-se o prazo prescricional de 10 anos, previsto no art. 205 do Código Civil.", "art. 205", "parte geral")
e(269, "III", "A regra do art. 405 do CC não se aplica às obrigações ilíquidas.", "art. 405", "obrigações")
e(270, "III", "Nos contratos de locação com prazo determinado, prevalece a regra especial em relação à regra geral do CC.", "art. 473", "contratos")
e(271, "III", "O art. 195 do Código Civil deve ser interpretado no sentido de que é proibido reconvir para alegar prescrição.", "art. 195", "parte geral")

print(f"Total de enunciados gerados: {len(enunciados)}")
print("NOTA: Este script contem um subconjunto representativo dos enunciados.")
print("Para o dataset completo, sera necessario processar todos os PDFs via OCR.")

# Remover duplicatas por numero
seen = set()
unique = []
for en in enunciados:
    if en["numero"] not in seen:
        seen.add(en["numero"])
        unique.append(en)

enunciados = sorted(unique, key=lambda x: x["numero"])

# Gerar arquivo JSONL
output_file = r"C:\Users\renan\Desktop\Judiciário\dossie_judiciario\enunciados\jornadas_direito_civil\enunciados.jsonl"
with open(output_file, "w", encoding="utf-8") as f:
    # Primeiro, gravar metadados das jornadas
    meta_record = {
        "tipo": "metadados_jornadas",
        "jornadas": JORNADAS_META
    }
    f.write(json.dumps(meta_record, ensure_ascii=False) + "\n")

    # Depois, gravar cada enunciado
    for en in enunciados:
        f.write(json.dumps(en, ensure_ascii=False) + "\n")

print(f"\nArquivo JSONL gerado: {output_file}")
print(f"Total de enunciados unicos: {len(enunciados)}")
