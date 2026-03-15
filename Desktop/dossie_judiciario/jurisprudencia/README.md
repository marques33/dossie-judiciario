# Jurisprudência Temática Brasileira

Banco de decisões emblemáticas por área do direito, organizadas em arquivos JSONL temáticos. Cada registro representa um precedente relevante do STF, STJ, TST ou outros tribunais superiores.

## Estrutura

```
jurisprudencia/
├── direitos_fundamentais/       # 15 decisões
├── penal_processual_penal/      # 15 decisões
├── civil_familia/               # 12 decisões
├── tributario/                  # 12 decisões
├── trabalhista/                 # 12 decisões
├── administrativo_publico/      # 12 decisões
└── constitucional_stf/          # 12 decisões
```

**Total: 90 decisões emblemáticas**

---

## Áreas e Destaques

### Direitos Fundamentais (15 registros)
Casos que moldaram a dogmática constitucional brasileira: prisão civil do depositário infiel, uniões homoafetivas, anencefalia, pesquisa com células-tronco, estado de coisas inconstitucional no sistema prisional, direito ao esquecimento e multiparentalidade.

**Destaques**: RE 466343 (status supralegal dos tratados de DH), ADI 4277 (união homoafetiva), ADPF 347 (ECI no sistema prisional)

### Penal e Processual Penal (15 registros)
A histórica trilha de precedentes sobre execução provisória da pena, o julgamento do Mensalão, a colaboração premiada, prova ilícita e prisão domiciliar para gestantes.

**Destaques**: HC 84078 → HC 126292 → ADC 43/44/54 (trilha da presunção de inocência), AP 470 (Mensalão), HC 143641 (habeas corpus coletivo)

### Civil e Família (12 registros)
Casamento homoafetivo, abandono afetivo, multiparentalidade, igualdade sucessória entre cônjuge e companheiro, guarda compartilhada e bem de família do fiador.

**Destaques**: REsp 1.159.242 ("amar é faculdade, cuidar é dever"), RE 878694 (igualdade sucessória), RE 898060 (multiparentalidade)

### Tributário (12 registros)
A "Tese do Século" (ICMS fora da base do PIS/COFINS) e outros leading cases de alto impacto fiscal: sigilo bancário, ISS sobre planos de saúde, guerra fiscal e contribuição previdenciária sobre terço de férias.

**Destaques**: RE 574706 (Tese do Século — R$ 250 bi), RE 601314 (sigilo bancário), RE 586482 (terço de férias)

### Trabalhista (12 registros)
Terceirização irrestrita, Reforma Trabalhista, negociado sobre legislado, FGTS e prescrição trabalhista.

**Destaques**: ADPF 324 + RE 958252 (terceirização irrestrita), ARE 1121633 (negociado/legislado), ADI 5766 (honorários — inconstitucional)

### Administrativo e Público (12 registros)
Responsabilidade civil do Estado, nepotismo, improbidade administrativa, demissão de empregado público e controle judicial da discricionariedade.

**Destaques**: RE 589998 (motivação na demissão de estatal), SV 13 / RE 636886 (nepotismo), RE 855091 (omissão estatal)

### Constitucional — STF (12 registros)
Financiamento eleitoral, Lei da Anistia, criação de municípios, CNJ, impeachment e imunidade parlamentar.

**Destaques**: ADI 4650 (proibição de doações empresariais), ADPF 153 (Lei de Anistia), ADPF 378 (impeachment)

---

## Estrutura dos Registros JSONL

Cada linha de cada arquivo `decisoes.jsonl` é um JSON com os seguintes campos:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | string | Identificador único (`juris_<tribunal>_<área>_<seq>`) |
| `tribunal` | string | STF, STJ, TST, TSE, TRF, etc. |
| `tipo` | string | plenário, turma, acórdão, decisão_monocrática |
| `numero_processo` | string | Numeração oficial do processo |
| `relator` | string | Ministro relator |
| `data_julgamento` | string | ISO 8601 (YYYY-MM-DD) |
| `area` | array | Áreas do direito relacionadas |
| `ementa_resumida` | string | Versão compacta da ementa (até 300 chars) |
| `tese_firmada` | string | Tese jurídica principal (até 400 chars) |
| `leading_case` | boolean | true se estabeleceu precedente paradigmático |
| `overruled` | boolean | true se posteriormente superado |
| `observacoes` | string | Contexto histórico e impacto prático |
| `fonte` | string | URL do portal do tribunal |

---

## Referências Cruzadas

| Processo | Área principal | Também em |
|----------|---------------|-----------|
| RE 898060 | direitos_fundamentais | civil_familia |
| ADI 5938 | direitos_fundamentais | trabalhista |

---

## Fase

Este diretório constitui a **Fase 5** do Dossiê Judiciário, dedicada à jurisprudência temática.

Fases anteriores:
- Fase 1: Súmulas STF e STJ
- Fase 2: Súmulas TST e TSE
- Fase 3: Teses de Repercussão Geral (STF), Repetitivos (STJ) e Repetitivos (TST)
- Fase 4: Enunciados das Jornadas de Direito Comercial
