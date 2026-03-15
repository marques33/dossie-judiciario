# Códigos — Legislação Federal Brasileira

## Descrição

Este diretório contém os metadados estruturados dos principais **Códigos** do ordenamento jurídico brasileiro, incluindo a Constituição Federal, códigos vigentes, revogados e parcialmente revogados.

## Arquivo

| Arquivo | Registros | Descrição |
|---------|-----------|-----------|
| `codigos.jsonl` | 17 | Principais códigos e consolidações legislativas do direito brasileiro |

## Conteúdo de `codigos.jsonl`

| ID | Denominação | Número | Ano | Status |
|----|-------------|--------|-----|--------|
| `lei_federal_CF88` | Constituição Federal | CF/88 | 1988 | vigente |
| `lei_federal_10406_2002` | Código Civil | 10.406 | 2002 | vigente |
| `lei_federal_13105_2015` | Código de Processo Civil | 13.105 | 2015 | vigente |
| `lei_federal_DL2848_1940` | Código Penal | DL 2.848 | 1940 | vigente |
| `lei_federal_DL3689_1941` | Código de Processo Penal | DL 3.689 | 1941 | vigente |
| `lei_federal_DL5452_1943` | CLT | DL 5.452 | 1943 | vigente |
| `lei_federal_5172_1966` | Código Tributário Nacional | 5.172 | 1966 | vigente |
| `lei_federal_8078_1990` | Código de Defesa do Consumidor | 8.078 | 1990 | vigente |
| `lei_federal_4737_1965` | Código Eleitoral | 4.737 | 1965 | vigente |
| `lei_federal_556_1850` | Código Comercial | 556 | 1850 | parcialmente_revogado |
| `lei_federal_5869_1973` | CPC/1973 | 5.869 | 1973 | revogado |
| `lei_federal_3071_1916` | Código Civil de 1916 | 3.071 | 1916 | revogado |
| `lei_federal_7565_1986` | Código Brasileiro de Aeronáutica | 7.565 | 1986 | vigente |
| `lei_federal_9503_1997` | Código de Trânsito Brasileiro | 9.503 | 1997 | vigente |
| `lei_federal_12651_2012` | Código Florestal | 12.651 | 2012 | vigente |
| `lei_federal_DL227_1967` | Código de Mineração | DL 227 | 1967 | vigente |
| `lei_federal_D24643_1934` | Código de Águas | D 24.643 | 1934 | vigente |

## Formato dos Registros

Cada linha é um objeto JSON com os campos:

- `id`: identificador único no banco
- `tipo`: `constituicao`, `codigo`, `decreto_lei`, `decreto`
- `numero`: número da lei/decreto
- `ano`: ano de promulgação
- `denominacao`: nome oficial ou consagrado
- `ementa`: texto da ementa oficial
- `data_promulgacao`: data no formato ISO 8601 (YYYY-MM-DD)
- `data_vigencia`: data de início da vigência
- `status`: `vigente`, `revogado`, `parcialmente_revogado`
- `area`: lista de temas relevantes para busca semântica
- `tribunal_referencia`: tribunais que aplicam este diploma com frequência
- `observacoes`: contexto histórico e alterações relevantes
- `url_oficial`: link para texto compilado no Planalto
