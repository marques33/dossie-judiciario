# Legislação Local — Dossiê Judiciário

Módulo de legislação estadual e municipal do banco de dados jurídico Dossiê Judiciário.

## Objetivo

Centralizar metadados estruturados de legislação subnacional brasileira — constituições estaduais, leis orgânicas municipais, leis tributárias estaduais e leis municipais paradigmáticas — em formato JSONL para consulta, indexação e integração com sistemas de busca jurídica.

## Estrutura de Diretórios

```
legislacao_local/
├── constituicoes_estaduais/
│   ├── constituicoes.jsonl          (27 registros)
│   └── README.md
├── leis_organicas_municipais/
│   ├── principais_capitais.jsonl    (27 registros)
│   └── README.md
├── legislacao_tributaria_estadual/
│   ├── icms_estados.jsonl           (12 registros)
│   └── README.md
├── legislacao_municipal_referencia/
│   ├── leis_municipais_paradigmaticas.jsonl  (15 registros)
│   └── README.md
└── README.md  (este arquivo)
```

## Total de Registros

| Módulo | Arquivo | Registros |
|--------|---------|-----------|
| Constituições estaduais e Lei Orgânica do DF | `constituicoes_estaduais/constituicoes.jsonl` | 27 |
| Leis Orgânicas das capitais estaduais | `leis_organicas_municipais/principais_capitais.jsonl` | 27 |
| Leis do ICMS dos principais estados | `legislacao_tributaria_estadual/icms_estados.jsonl` | 12 |
| Leis municipais paradigmáticas | `legislacao_municipal_referencia/leis_municipais_paradigmaticas.jsonl` | 15 |
| **Total** | | **81** |

## Estrutura do Registro JSONL

Cada linha é um objeto JSON independente com os seguintes campos:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | string | Identificador único — ver convenção abaixo |
| `ente` | string | Sigla da UF ou identificador do município (ex.: `SP`, `municipio_sao_paulo`) |
| `tipo_ente` | string | `estado`, `municipio` ou `distrito_federal` |
| `tipo` | string | Tipo normativo — ver valores possíveis abaixo |
| `numero` | string | Número da lei ou `s/n` para instrumentos sem numeração |
| `ano` | integer | Ano de promulgação |
| `denominacao` | string | Nome oficial completo |
| `ementa` | string | Ementa resumida |
| `data_promulgacao` | string | Data no formato `YYYY-MM-DD` |
| `status` | string | `vigente`, `revogado` ou `parcialmente_revogado` |
| `area` | array | Tags de área jurídica para indexação e busca |
| `observacoes` | string | Contexto, histórico e notas relevantes |
| `url_oficial` | string | URL do órgão legislativo oficial |

### Valores possíveis para `tipo`

- `constituicao_estadual` — constituição de estado-membro
- `lei_organica` — Lei Orgânica do DF ou de município
- `lei_estadual` — lei ordinária estadual
- `lei_complementar_estadual` — lei complementar estadual ou municipal
- `lei_municipal` — lei ordinária municipal
- `decreto_estadual` — decreto ou decreto-lei estadual/municipal

## Convenção de IDs

| Padrão | Exemplo | Uso |
|--------|---------|-----|
| `constituicao_estadual_{uf}_{ano}` | `constituicao_estadual_sp_1989` | Constituições estaduais |
| `lei_organica_{uf}_{ano}` | `lei_organica_df_1993` | Lei Orgânica do DF |
| `lei_organica_{municipio}_{ano}` | `lei_organica_sao_paulo_1990` | Leis orgânicas municipais |
| `lei_estadual_{uf}_{numero}_{ano}` | `lei_estadual_sp_6374_1989` | Leis estaduais numeradas |
| `lei_municipal_{cidade}_{numero}_{ano}` | `lei_municipal_curitiba_14771_2015` | Leis municipais numeradas |
| `lei_complementar_municipal_{cidade}_{numero}_{ano}` | `lei_complementar_municipal_rj_111_2011` | Leis complementares municipais |
| `decreto_lei_municipal_{cidade}_{numero}_{ano}` | `decreto_lei_municipal_rj_322_1976` | Decretos-lei municipais |

## Limitações

- **Cobertura geográfica:** as leis orgânicas municipais cobrem apenas as 26 capitais estaduais + DF; os demais 5.536 municípios brasileiros não estão cobertos nesta fase
- **Legislação tributária:** apenas ICMS dos 12 estados de maior representatividade; não cobrem IPVA, ITCMD, taxas estaduais, ISS municipal, IPTU, ITBI
- **Atualizações:** os registros refletem o instrumento normativo original; emendas e alterações pontuais não são rastreadas individualmente — consultar as fontes oficiais para texto consolidado
- **URLs:** os links apontam para os portais oficiais das assembleias legislativas e câmaras municipais; a estrutura interna de cada portal pode variar

## Contexto no Dossiê Judiciário

Este módulo complementa:
- `legislacao_federal/` — CF/1988, leis federais, decretos
- `sumulas/` — súmulas do STF, STJ, TST, TSE e TRFs
- `teses_precedentes/` — teses de repercussão geral e recursos repetitivos
- `jurisprudencia/` — acórdãos dos tribunais superiores

## Próximas Expansões Possíveis

- Leis orgânicas dos 100 maiores municípios por população
- Legislação tributária municipal (ISS — LC 116/2003 e leis municipais correlatas)
- Legislação ambiental estadual (principais leis de proteção ambiental por estado)
- Códigos de obras e posturas dos principais municípios
