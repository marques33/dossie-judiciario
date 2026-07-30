# Legislação Federal Brasileira — Dossiê Judiciário

## Visão Geral

Este diretório contém metadados estruturados em formato JSONL da **legislação federal brasileira principal**, organizada por área do direito. O objetivo é compor uma base de dados jurídica consultável, integrável com sistemas de busca semântica, RAG e agentes de IA jurídica.

---

## Estrutura de Diretórios

```
legislacao_federal/
├── codigos/                    # Constituição e Códigos principais
│   ├── codigos.jsonl           # 17 registros
│   └── README.md
├── civil/                      # Direito Civil, Família, Propriedade Intelectual
│   ├── leis_civis.jsonl        # 11 registros
│   └── README.md
├── empresarial/                # Direito Empresarial, Societário, Licitações
│   ├── leis_empresariais.jsonl # 10 registros
│   └── README.md
├── penal/                      # Direito Penal especial e Processo Penal
│   ├── leis_penais.jsonl       # 10 registros
│   └── README.md
├── tributario/                 # Direito Tributário Federal
│   ├── leis_tributarias.jsonl  # 10 registros
│   └── README.md
├── trabalho/                   # Direito do Trabalho e Previdenciário
│   ├── leis_trabalhistas.jsonl # 9 registros
│   └── README.md
├── administrativo/             # Direito Administrativo Federal
│   ├── leis_administrativas.jsonl # 10 registros
│   └── README.md
└── constitucional/             # Emendas Constitucionais e Ações Constitucionais
    ├── leis_constitucionais.jsonl # 9 registros
    └── README.md
```

**Total: 86 registros em 8 subdiretórios.**

---

## Formato do Registro JSONL

Cada linha de cada arquivo `.jsonl` é um objeto JSON autônomo com a seguinte estrutura:

```json
{
  "id": "lei_federal_XXXX",
  "tipo": "codigo|lei|decreto_lei|emenda_constitucional|lei_complementar|decreto|constituicao|referencia_interna",
  "numero": "string",
  "ano": 2002,
  "denominacao": "Nome oficial ou consagrado",
  "ementa": "Texto da ementa oficial",
  "data_promulgacao": "YYYY-MM-DD",
  "data_vigencia": "YYYY-MM-DD",
  "status": "vigente|revogado|parcialmente_revogado",
  "area": ["tema1", "tema2"],
  "tribunal_referencia": ["STJ", "STF"],
  "observacoes": "Contexto histórico, alterações, jurisprudência relevante",
  "url_oficial": "https://www.planalto.gov.br/..."
}
```

---

## Índice por Subdiretório

### `codigos/` — Constituição e Códigos

| Lei | Denominação | Status |
|-----|-------------|--------|
| CF/88 | Constituição Federal | vigente |
| Lei 10.406/2002 | Código Civil | vigente |
| Lei 13.105/2015 | Código de Processo Civil | vigente |
| DL 2.848/1940 | Código Penal | vigente |
| DL 3.689/1941 | Código de Processo Penal | vigente |
| DL 5.452/1943 | CLT | vigente |
| Lei 5.172/1966 | Código Tributário Nacional | vigente |
| Lei 8.078/1990 | Código de Defesa do Consumidor | vigente |
| Lei 4.737/1965 | Código Eleitoral | vigente |
| Lei 556/1850 | Código Comercial | parcialmente_revogado |
| Lei 5.869/1973 | CPC/1973 | revogado |
| Lei 3.071/1916 | Código Civil de 1916 | revogado |
| Lei 7.565/1986 | Código Brasileiro de Aeronáutica | vigente |
| Lei 9.503/1997 | Código de Trânsito Brasileiro | vigente |
| Lei 12.651/2012 | Código Florestal | vigente |
| DL 227/1967 | Código de Mineração | vigente |
| Decreto 24.643/1934 | Código de Águas | vigente |

### `civil/` — Direito Civil

| Lei | Denominação | Status |
|-----|-------------|--------|
| DL 4.657/1942 | LINDB | vigente |
| Lei 6.515/1977 | Lei do Divórcio | parcialmente_revogado |
| Lei 12.010/2009 | Lei de Adoção | vigente |
| Lei 11.340/2006 | Lei Maria da Penha | vigente |
| Lei 13.709/2018 | LGPD | vigente |
| Lei 8.245/1991 | Lei de Locações | vigente |
| Lei 6.015/1973 | Lei de Registros Públicos | vigente |
| Lei 13.146/2015 | Estatuto da Pessoa com Deficiência | vigente |
| Lei 9.279/1996 | Lei de Propriedade Industrial | vigente |
| Lei 9.610/1998 | Lei de Direitos Autorais | vigente |
| Lei 12.965/2014 | Marco Civil da Internet | vigente |

### `empresarial/` — Direito Empresarial

| Lei | Denominação | Status |
|-----|-------------|--------|
| Lei 6.404/1976 | Lei das S.A. | vigente |
| Lei 11.101/2005 | Lei de Falências | vigente |
| LC 123/2006 | Simples Nacional | vigente |
| Lei 5.764/1971 | Lei das Cooperativas | vigente |
| Lei 13.966/2019 | Lei de Franquias | vigente |
| Lei 9.307/1996 | Lei de Arbitragem | vigente |
| Lei 6.385/1976 | Lei do Mercado de Capitais | vigente |
| Lei 12.846/2013 | Lei Anticorrupção | vigente |
| Lei 14.133/2021 | Nova Lei de Licitações | vigente |
| Lei 8.987/1995 | Lei de Concessões | vigente |

### `penal/` — Direito Penal

| Lei | Denominação | Status |
|-----|-------------|--------|
| Lei 8.072/1990 | Lei de Crimes Hediondos | vigente |
| Lei 11.343/2006 | Lei de Drogas | vigente |
| Lei 7.210/1984 | Lei de Execução Penal | vigente |
| Lei 10.826/2003 | Estatuto do Desarmamento | vigente |
| Lei 9.099/1995 | Lei dos Juizados Especiais | vigente |
| Lei 9.613/1998 | Lei de Lavagem de Dinheiro | vigente |
| Lei 12.850/2013 | Lei de Organizações Criminosas | vigente |
| Lei 13.869/2019 | Lei de Abuso de Autoridade | vigente |
| Lei 9.605/1998 | Lei de Crimes Ambientais | vigente |
| Lei 8.429/1992 | Lei de Improbidade Administrativa | vigente |

### `tributario/` — Direito Tributário

| Lei | Denominação | Status |
|-----|-------------|--------|
| LC 101/2000 | Lei de Responsabilidade Fiscal | vigente |
| LC 123/2006 | Simples Nacional (ref. cruzada) | vigente |
| LC 116/2003 | Lei do ISS | vigente |
| LC 87/1996 | Lei Kandir (ICMS) | vigente |
| Lei 10.637/2002 | Lei do PIS não-cumulativo | vigente |
| Lei 10.833/2003 | Lei da COFINS não-cumulativa | vigente |
| Lei 9.250/1995 | Lei do IRPF | vigente |
| Decreto 70.235/1972 | PAF Federal | vigente |
| Lei 6.830/1980 | Lei das Execuções Fiscais | vigente |
| Lei 12.016/2009 | Lei do Mandado de Segurança | vigente |

### `trabalho/` — Direito do Trabalho

| Lei | Denominação | Status |
|-----|-------------|--------|
| Lei 13.467/2017 | Reforma Trabalhista | vigente |
| Lei 8.036/1990 | Lei do FGTS | vigente |
| Lei 8.213/1991 | Lei de Benefícios da Previdência | vigente |
| Lei 8.212/1991 | Lei do Custeio da Previdência | vigente |
| Lei 7.783/1989 | Lei de Greve | vigente |
| LC 150/2015 | Lei do Trabalho Doméstico | vigente |
| Lei 6.019/1974 | Lei do Trabalho Temporário | vigente |
| Lei 10.097/2000 | Lei do Aprendiz | vigente |
| CLT Título X | Juizados Especiais do Trabalho | vigente |

### `administrativo/` — Direito Administrativo

| Lei | Denominação | Status |
|-----|-------------|--------|
| Lei 9.784/1999 | Lei do Processo Administrativo Federal | vigente |
| Lei 12.527/2011 | Lei de Acesso à Informação | vigente |
| Lei 8.112/1990 | Estatuto dos Servidores Federais | vigente |
| Decreto 1.171/1994 | Código de Ética do Servidor | vigente |
| Lei 13.848/2019 | Lei das Agências Reguladoras | vigente |
| Lei 8.666/1993 | Lei de Licitações (antiga) | parcialmente_revogado |
| Lei 10.520/2002 | Lei do Pregão | parcialmente_revogado |
| Lei 11.079/2004 | Lei das PPPs | vigente |
| Lei 12.529/2011 | Lei do CADE | vigente |
| Lei 9.472/1997 | Lei Geral de Telecomunicações | vigente |

### `constitucional/` — Direito Constitucional

| Lei | Denominação | Status |
|-----|-------------|--------|
| EC 45/2004 | Reforma do Judiciário | vigente |
| EC 95/2016 | Teto dos Gastos Públicos | vigente |
| EC 103/2019 | Reforma da Previdência | vigente |
| EC 132/2023 | Reforma Tributária | vigente |
| ADCT | Ato das Disposições Constitucionais Transitórias | vigente |
| Lei 13.445/2017 | Lei de Migração | vigente |
| Lei 4.717/1965 | Lei da Ação Popular | vigente |
| Lei 7.347/1985 | Lei da Ação Civil Pública | vigente |
| Lei 13.300/2016 | Lei do Mandado de Injunção | vigente |

---

## Convenções de Nomenclatura de IDs

| Prefixo | Tipo |
|---------|------|
| `lei_federal_NNNNN_AAAA` | Lei ordinária (número_ano) |
| `lei_federal_LCNNN_AAAA` | Lei complementar |
| `lei_federal_DLNNNNN_AAAA` | Decreto-lei |
| `lei_federal_DNNNNN_AAAA` | Decreto |
| `lei_federal_ECNN_AAAA` | Emenda Constitucional |
| `lei_federal_CF88` | Constituição Federal |
| `lei_federal_ADCT` | ADCT |

---

## Fontes

Todos os textos oficiais estão disponíveis no portal do Planalto:
- Leis: https://www.planalto.gov.br/ccivil_03/leis/
- Decretos-lei: https://www.planalto.gov.br/ccivil_03/decreto-lei/
- Leis complementares: https://www.planalto.gov.br/ccivil_03/leis/lcp/
- Emendas Constitucionais: https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/
- Constituição Federal: https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm

---

## Integração com o Dossiê Judiciário

Este módulo integra-se com os demais subdiretórios do projeto:

- `../sumulas/` — Súmulas do STF, STJ, TST, TSE
- `../teses_precedentes/` — Teses de repercussão geral e recursos repetitivos
- `../jurisprudencia/` — Acórdãos e decisões relevantes
- `../enunciados/` — Enunciados das Jornadas de Direito

---

*Dossiê Judiciário — Banco de Dados Jurídico Brasileiro*
*Última atualização: 2025*
