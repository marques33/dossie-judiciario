---
name: dossie-legislacao-br
description: Use esta skill quando o usuário pedir legislação federal brasileira (Constituição, códigos, leis ordinárias, leis complementares, decretos-lei, emendas constitucionais) ou legislação local (constituições estaduais, leis orgânicas municipais, ICMS estadual, leis municipais paradigmáticas). Cobre 167 normas em 12 subáreas indexadas em JSONL, com ementa, data, status (vigente/revogado), área temática e URL oficial. Use também quando mencionar leis específicas como CF/88, CC, CPC, CLT, CTN, CDC, LRF, Lei Maria da Penha, LGPD, Reforma Trabalhista, EC 132/2023.
version: 1.0.0
category: legal
tags: [direito, legislacao, codigos, leis, constituicao, dossie-judiciario, brasil]
complexity: intermediate
risk: safe
source: dossie_judiciario
author: renan
date_added: 2026-05-22
---

# Dossiê Judiciário — Legislação Brasileira (Federal + Local)

## Quando usar
- Usuário cita código ou lei pelo nome (Código Civil, CPC, CLT, CTN, CDC, LRF, LGPD, Marco Civil…).
- Usuário cita pelo número (Lei 13.105/2015, EC 132/2023, DL 2.848/1940, LC 87/96…).
- Pergunta sobre status (vigente / revogado / parcialmente revogado).
- Pesquisa de legislação por área (civil, penal, tributária, trabalhista, administrativa, empresarial, constitucional).
- Consulta a legislação estadual ou municipal (CE, LOM, ICMS estadual, leis municipais paradigmáticas como Lei do Silêncio, Lei Cidade Limpa).
- Construção de peça que exija fundamento normativo.

NÃO acione para: jurisprudência (use `dossie-jurisprudencia-br`), súmulas/enunciados (use `dossie-sumulas-enunciados-br`).

## Banco de dados disponível

### Federal — `dossie_judiciario/legislacao_federal/` (86 registros)

| Subdiretório | Arquivo | Qtd | Núcleo |
|---|---|---:|---|
| `codigos/` | `codigos.jsonl` | 17 | CF/88, CC, CPC, CP, CPP, CLT, CTN, CDC, Código Eleitoral, Código Comercial 1850, CPC/1973 (rev.), CC/1916 (rev.), CBA, CTB, Código Florestal, Código de Mineração, Código de Águas |
| `civil/` | `leis_civis.jsonl` | 11 | LINDB, Lei do Divórcio, Lei de Adoção, Maria da Penha, LGPD, Lei de Locações, Lei de Registros Públicos, Estatuto da PCD, LPI, Direitos Autorais, Marco Civil |
| `empresarial/` | `leis_empresariais.jsonl` | 10 | Lei das S.A., Lei de Falências, Simples Nacional, Cooperativas, Franquias, Arbitragem, Mercado de Capitais, Anticorrupção, Nova Lei de Licitações, Concessões |
| `penal/` | `leis_penais.jsonl` | 10 | Hediondos, Drogas, LEP, Desarmamento, Juizados, Lavagem, Organizações Criminosas, Abuso de Autoridade, Crimes Ambientais, Improbidade |
| `tributario/` | `leis_tributarias.jsonl` | 10 | LRF, Simples (ref.), Lei do ISS, Lei Kandir, PIS/COFINS, IRPF, PAF Federal, LEF, MS |
| `trabalho/` | `leis_trabalhistas.jsonl` | 9 | Reforma Trabalhista, FGTS, Benefícios, Custeio, Greve, Doméstico, Temporário, Aprendiz |
| `administrativo/` | `leis_administrativas.jsonl` | 10 | LPA, LAI, Estatuto Servidores, Código de Ética, Agências Reguladoras, Licitações antiga, Pregão, PPPs, CADE, LGT |
| `constitucional/` | `leis_constitucionais.jsonl` | 9 | EC 45 (Reforma Judiciário), EC 95 (Teto), EC 103 (Previdência), EC 132 (Tributária), ADCT, Migração, Ação Popular, ACP, Mandado de Injunção |

### Local — `dossie_judiciario/legislacao_local/` (81 registros)

| Subdiretório | Arquivo | Qtd | Conteúdo |
|---|---|---:|---|
| `constituicoes_estaduais/` | `constituicoes.jsonl` | 27 | CE dos 26 estados + LO do DF |
| `leis_organicas_municipais/` | `principais_capitais.jsonl` | 27 | LOM das 26 capitais + LO de Brasília |
| `legislacao_tributaria_estadual/` | `icms_estados.jsonl` | 12 | Leis de ICMS dos principais entes (SP, RJ, MG, RS, PR, SC, BA, PE, CE, GO, DF, ES) |
| `legislacao_municipal_referencia/` | `leis_municipais_paradigmaticas.jsonl` | 15 | Lei Cidade Limpa (SP 14.223/06), Plano Diretor (SP, RJ), Lei do Silêncio, ZEIS, Outorga Onerosa, Lei do Carro Compartilhado |

## Esquema dos registros

**Federal (`legislacao_federal/*/`):**
```json
{
  "id": "lei_federal_<numero>_<ano>",
  "tipo": "codigo|lei|lei_complementar|decreto_lei|decreto|emenda_constitucional|constituicao",
  "numero": "13.105",
  "ano": 2015,
  "denominacao": "Código de Processo Civil",
  "ementa": "...",
  "data_promulgacao": "YYYY-MM-DD",
  "data_vigencia": "YYYY-MM-DD",
  "status": "vigente|revogado|parcialmente_revogado",
  "area": ["..."],
  "tribunal_referencia": ["STF", "STJ"],
  "observacoes": "...",
  "url_oficial": "https://www.planalto.gov.br/..."
}
```

**Local (`legislacao_local/*/`):**
```json
{
  "id": "constituicao_estadual_sp_1989",
  "ente": "SP",
  "tipo_ente": "estado|municipio|distrito_federal",
  "tipo": "constituicao_estadual|lei_organica|lei_estadual|lei_municipal|lei_complementar_estadual|decreto_estadual",
  "numero": "...",
  "ano": 1989,
  "denominacao": "...",
  "ementa": "...",
  "data_promulgacao": "YYYY-MM-DD",
  "status": "vigente|revogado|parcialmente_revogado",
  "area": ["..."],
  "observacoes": "...",
  "url_oficial": "..."
}
```

## Como consultar

1. **Por número/ano** — grep direto:
   ```bash
   grep -F '"numero": "13.105"' legislacao_federal/*/*.jsonl
   ```
2. **Por denominação** — grep por substring (atenção a acentos):
   ```bash
   grep -i 'Maria da Penha' legislacao_federal/*/*.jsonl
   ```
3. **Por área temática** — busque tokens no array `area`:
   ```bash
   grep -F '"tributário"' legislacao_federal/*/*.jsonl
   ```
4. **Por ente subnacional** — em `legislacao_local/`:
   ```bash
   grep -F '"ente": "SP"' legislacao_local/*/*.jsonl
   ```
5. **Por status** — `"status": "vigente"` ou `"parcialmente_revogado"`.

## Convenções de ID

**Federal:**
- `lei_federal_NNNNN_AAAA` — lei ordinária
- `lei_federal_LCNNN_AAAA` — lei complementar
- `lei_federal_DLNNNNN_AAAA` — decreto-lei
- `lei_federal_DNNNNN_AAAA` — decreto
- `lei_federal_ECNN_AAAA` — emenda constitucional
- `lei_federal_CF88` — Constituição
- `lei_federal_ADCT` — ADCT

**Local:**
- `constituicao_estadual_{uf}_{ano}`
- `lei_organica_{uf|municipio}_{ano}`
- `lei_estadual_{uf}_{numero}_{ano}`
- `lei_municipal_{cidade}_{numero}_{ano}`

## Padrão de resposta esperado

Para cada norma citada, devolva:
1. Denominação + número + ano + tipo.
2. Ementa.
3. Status (sinalizar se revogado/parcialmente).
4. Áreas indexadas.
5. Observações (alterações, EC posteriores, jurisprudência relevante).
6. URL oficial (Planalto para federal; ALEs e Câmaras Municipais para local).

Quando o usuário citar lei revogada, **explicar a substituição** (ex.: CPC/1973 → CPC/2015; CC/1916 → CC/2002; Licitações 8.666/93 → 14.133/2021 com convivência transitória).

## Grafos visuais

- `dossie_judiciario/grafos/mapa_legislacao_federal.md` — árvore Constituição → códigos → leis especiais, por área.
- `dossie_judiciario/grafos/mapa_legislacao_local.md` — federação CE + LOM + ICMS por UF.
- `dossie_judiciario/grafos/cruzamento_leis_jurisprudencia.md` — leis ↔ leading cases que as interpretam.

## Limitações
- Cobertura curatorial (167 normas), não exaustiva. Para leis ordinárias menos centrais, consulte o Planalto.
- Não inclui texto integral — apenas metadados. Para texto, seguir `url_oficial`.
- Dados de março/2026. Conferir alterações posteriores antes de citar em peça.
