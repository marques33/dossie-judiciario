# Constituições Estaduais

Registros das constituições dos 26 estados brasileiros e da Lei Orgânica do Distrito Federal.

## Arquivos

| Arquivo | Registros | Descrição |
|---------|-----------|-----------|
| `constituicoes.jsonl` | 27 | Uma entrada por unidade federativa (26 estados + DF) |

## Convenção de IDs

- Estados: `constituicao_estadual_{uf}_{ano}` — ex.: `constituicao_estadual_sp_1989`
- Distrito Federal: `lei_organica_df_{ano}` — ex.: `lei_organica_df_1993`

## Datas de promulgação

A maioria foi promulgada em 05/10/1989, em sincronismo com a CF/1988 (promulgada em 05/10/1988). Exceções:
- MG: 21/09/1989
- RO: 28/09/1989
- AC e RN: 03/10/1989
- RS: 03/10/1989
- AP: 20/12/1991 (ex-território federal)
- RR: 31/12/1991 (ex-território federal)
- DF: 08/06/1993 (Lei Orgânica, nos termos do art. 32 da CF/1988)

## Observações

- O DF não tem constituição estadual; tem Lei Orgânica (CF/1988, art. 32)
- AP e RR foram criados como estados pela CF/1988, mas promulgaram suas constituições apenas em 1991
- As constituições são documentos vivos — passam por emendas frequentes; o campo `status` reflete a validade do instrumento, não de cada dispositivo
