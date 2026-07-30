# Direito do Trabalho — Legislação Federal Brasileira

## Descrição

Este diretório contém metadados estruturados das principais **leis trabalhistas e previdenciárias** brasileiras, complementando a CLT (indexada em `../codigos/`).

## Arquivo

| Arquivo | Registros | Descrição |
|---------|-----------|-----------|
| `leis_trabalhistas.jsonl` | 9 | Principais leis trabalhistas e previdenciárias extravagantes |

## Conteúdo de `leis_trabalhistas.jsonl`

| ID | Denominação | Número | Ano | Status |
|----|-------------|--------|-----|--------|
| `lei_federal_13467_2017` | Lei da Reforma Trabalhista | 13.467 | 2017 | vigente |
| `lei_federal_8036_1990` | Lei do FGTS | 8.036 | 1990 | vigente |
| `lei_federal_8213_1991` | Lei de Benefícios da Previdência | 8.213 | 1991 | vigente |
| `lei_federal_8212_1991` | Lei do Custeio da Previdência | 8.212 | 1991 | vigente |
| `lei_federal_7783_1989` | Lei de Greve | 7.783 | 1989 | vigente |
| `lei_federal_LC150_2015` | Lei do Trabalho Doméstico | LC 150 | 2015 | vigente |
| `lei_federal_6019_1974` | Lei do Trabalho Temporário | 6.019 | 1974 | vigente |
| `lei_federal_10097_2000` | Lei do Aprendiz | 10.097 | 2000 | vigente |
| `lei_federal_CLT_JET` | Juizados Especiais do Trabalho (CLT) | CLT Título X | 1943 | vigente |

## Referências Cruzadas

- CLT (DL 5.452/1943): indexada em `../codigos/codigos.jsonl` como `lei_federal_DL5452_1943`
- EC 103/2019 (Reforma da Previdência): indexada em `../constitucional/leis_constitucionais.jsonl`

## Observações

O processo trabalhista e os Juizados Especiais do Trabalho são disciplinados diretamente pela CLT (Título X, arts. 651-910), sem lei processual própria separada — diferentemente da Justiça Comum e da Justiça Federal. Há um registro explicativo (`lei_federal_CLT_JET`) para orientação em buscas.
