# Direito Tributário — Legislação Federal Brasileira

## Descrição

Este diretório contém metadados estruturados das principais **leis tributárias federais**, incluindo normas gerais, tributos específicos, processo administrativo fiscal e execução fiscal.

## Arquivo

| Arquivo | Registros | Descrição |
|---------|-----------|-----------|
| `leis_tributarias.jsonl` | 10 | Principais leis tributárias federais |

## Conteúdo de `leis_tributarias.jsonl`

| ID | Denominação | Número | Ano | Status |
|----|-------------|--------|-----|--------|
| `lei_federal_LC101_2000` | Lei de Responsabilidade Fiscal | LC 101 | 2000 | vigente |
| `lei_federal_LC123_2006_trib` | Simples Nacional (ref. cruzada) | LC 123 | 2006 | vigente |
| `lei_federal_LC116_2003` | Lei do ISS | LC 116 | 2003 | vigente |
| `lei_federal_LC87_1996` | Lei Kandir (ICMS) | LC 87 | 1996 | vigente |
| `lei_federal_10637_2002` | Lei do PIS não-cumulativo | 10.637 | 2002 | vigente |
| `lei_federal_10833_2003` | Lei da COFINS não-cumulativa | 10.833 | 2003 | vigente |
| `lei_federal_9250_1995` | Lei do IRPF | 9.250 | 1995 | vigente |
| `lei_federal_D70235_1972` | PAF Federal (Decreto) | D 70.235 | 1972 | vigente |
| `lei_federal_6830_1980` | Lei das Execuções Fiscais | 6.830 | 1980 | vigente |
| `lei_federal_12016_2009` | Lei do Mandado de Segurança | 12.016 | 2009 | vigente |

## Referências Cruzadas

- CTN (Lei 5.172/1966): indexado em `../codigos/codigos.jsonl` como `lei_federal_5172_1966`
- LC 123/2006 (Simples Nacional): registro principal em `../empresarial/leis_empresariais.jsonl`
- EC 132/2023 (Reforma Tributária): indexada em `../constitucional/leis_constitucionais.jsonl`

## Observações

O ISS (LC 116/2003) e o ICMS (LC 87/1996) são tributos estaduais/municipais, mas regulamentados por lei complementar federal conforme exigência constitucional, justificando sua inclusão neste diretório.
