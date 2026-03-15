# Leis Orgânicas Municipais — Capitais Estaduais

Registros das Leis Orgânicas das 26 capitais estaduais brasileiras e do Distrito Federal.

## Arquivos

| Arquivo | Registros | Descrição |
|---------|-----------|-----------|
| `principais_capitais.jsonl` | 27 | Uma entrada por capital estadual + DF |

## Convenção de IDs

- Municípios: `lei_organica_{municipio}_{ano}` — ex.: `lei_organica_sao_paulo_1990`
- Distrito Federal: `lei_organica_brasilia_df_{ano}` (entrada de referência cruzada com `constituicoes_estaduais`)

## Datas de promulgação

As leis orgânicas municipais foram promulgadas em sua maioria entre março e abril de 1990, seguindo o prazo estabelecido pela CF/1988 (art. 11 do ADCT: municípios tinham dois anos a partir da promulgação para elaborar suas leis orgânicas). Datas específicas documentadas:

| Município | Data |
|-----------|------|
| Belo Horizonte | 21/03/1990 |
| Belém | 30/03/1990 |
| Fortaleza | 31/03/1990 |
| Porto Alegre | 03/04/1990 |
| São Paulo | 04/04/1990 |
| Rio de Janeiro | 05/04/1990 |
| Salvador | 05/04/1990 |
| Curitiba | 05/04/1990 |
| Manaus | 05/04/1990 |
| Goiânia | 05/04/1990 |
| Florianópolis | 05/04/1990 |
| Recife | 18/04/1990 |
| Demais capitais | 05/04/1990 (aproximado) |

## Observações

- O DF está registrado aqui (referência cruzada) e em `constituicoes_estaduais/` com o mesmo ID `lei_organica_df_1993`
- Palmas (TO) é a capital mais jovem do Brasil; foi fundada em 1989, portanto sua lei orgânica original é de 1990
- As datas para capitais sem informação precisa usam 05/04/1990 como aproximação; verificar nos sites das câmaras municipais para confirmação
