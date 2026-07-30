---
name: dossie-jurisprudencia-br
description: Use esta skill quando o usuário pedir leading cases, decisões emblemáticas, acórdãos paradigmáticos, jurisprudência temática do STF/STJ/TST por área (direitos fundamentais, penal, civil/família, tributário, trabalhista, administrativo, constitucional) ou quando mencionar processos específicos como ADI 4277, RE 574706, ADPF 153, HC 126292, AP 470. A skill consulta o banco JSONL local de 90 decisões anotadas (id, tese firmada, ementa, leading_case, overruled) no diretório jurisprudencia/.
version: 1.0.0
category: legal
tags: [direito, jurisprudencia, stf, stj, tst, brasil, leading-case, dossie-judiciario]
complexity: intermediate
risk: safe
source: dossie_judiciario
author: renan
date_added: 2026-05-22
---

# Dossiê Judiciário — Jurisprudência Temática (Brasil)

## Quando usar
Acione esta skill em qualquer das situações:
- Usuário pede "leading case", "precedente paradigmático", "acórdão emblemático" sobre uma área do direito brasileiro.
- Usuário cita um número de processo do STF/STJ/TST (ADI, ADPF, ADC, RE, REsp, HC, AP, ARE) e quer contexto.
- Pesquisa por área temática: direitos fundamentais, penal/processual penal, civil/família, tributário, trabalhista, administrativo/público, constitucional STF.
- Construção de peça jurídica que exija precedentes do STF/STJ/TST por tema.
- Trilhas de overruling (evolução jurisprudencial sobre o mesmo tema).

NÃO acione para: legislação federal/estadual (use `dossie-legislacao-br`), súmulas/enunciados (use `dossie-sumulas-enunciados-br`), digital twins de magistrados (consulte diretamente os READMEs dos tribunais).

## Banco de dados disponível

Caminho base: `dossie_judiciario/jurisprudencia/`

| Subdiretório | Decisões | Foco |
|---|---:|---|
| `direitos_fundamentais/decisoes.jsonl` | 15 | RE 466343, ADI 4277, ADPF 347, RE 898060, RE 670422 |
| `penal_processual_penal/decisoes.jsonl` | 15 | HC 84078 → 126292 → ADC 43/44/54, AP 470, HC 143641, HC 152752 |
| `civil_familia/decisoes.jsonl` | 12 | REsp 1.159.242 (abandono afetivo), RE 878694 (sucessão), RE 898060 (multiparentalidade) |
| `tributario/decisoes.jsonl` | 12 | RE 574706 (Tese do Século), RE 601314 (sigilo bancário), RE 586482 (terço de férias) |
| `trabalhista/decisoes.jsonl` | 12 | ADPF 324 + RE 958252 (terceirização), ARE 1121633 (negociado/legislado), ADI 5766 |
| `administrativo_publico/decisoes.jsonl` | 12 | RE 589998, SV 13 / RE 636886 (nepotismo), RE 855091 (omissão estatal), RE 327904 |
| `constitucional_stf/decisoes.jsonl` | 12 | ADI 4650, ADPF 153, ADI 2240, ADI 3367 (CNJ), ADPF 378 (impeachment) |

**Total: 90 decisões emblemáticas.**

## Esquema de cada registro JSONL

```json
{
  "id": "juris_<tribunal>_<area>_<seq>",
  "tribunal": "STF|STJ|TST|TSE",
  "tipo": "plenário|turma|acórdão",
  "numero_processo": "ADI 4277",
  "relator": "Min. Ayres Britto",
  "data_julgamento": "YYYY-MM-DD",
  "area": ["..."],
  "ementa_resumida": "≤300 chars",
  "tese_firmada": "≤400 chars",
  "leading_case": true,
  "overruled": false,
  "observacoes": "Contexto histórico e impacto",
  "fonte": "URL do portal do tribunal"
}
```

## Como consultar (procedimento)

1. **Localizar o arquivo certo** — mapeie a pergunta para um dos 7 subdiretórios. Se o tema cruzar áreas (ex.: multiparentalidade está em `direitos_fundamentais` e referenciada em `civil_familia`), consulte ambos.
2. **Filtrar por tribunal + processo** — use `Grep` no JSONL:
   ```bash
   grep -F '"numero_processo":"ADI 4277"' jurisprudencia/*/decisoes.jsonl
   ```
3. **Filtrar por área temática** — busque pelos tokens em `area`:
   ```bash
   grep -F '"sigilo bancário"' jurisprudencia/tributario/decisoes.jsonl
   ```
4. **Buscar leading cases vivos** — `"leading_case":true` e `"overruled":false`.
5. **Trilhas de overruling** — siga a sequência de `numero_processo` no campo `observacoes` (referências cruzadas em prosa).

## Trilhas jurisprudenciais já mapeadas

- **Execução provisória da pena (presunção de inocência):** HC 84078 (2009, inconst.) → HC 126292 (2016, const.) → ADC 43/44/54 (2019, voltou a inconst.). Arquivo: `penal_processual_penal/decisoes.jsonl`.
- **Terceirização:** Súmula 331 TST → ADPF 324 + RE 958252 (2018, liberou trabalho-fim). Arquivo: `trabalhista/decisoes.jsonl`.
- **Multiparentalidade:** REsp 1.159.242 (abandono afetivo, 2012) → RE 898060 (paternidade socioafetiva + biológica, 2016). Arquivos: `civil_familia` + `direitos_fundamentais`.
- **Tese do Século:** RE 240785 (precedente isolado) → RE 574706 (RG, 2017, modulação 2021). Arquivo: `tributario/decisoes.jsonl`.

## Referências cruzadas explícitas

| Processo | Área principal | Também em |
|---|---|---|
| RE 898060 | direitos_fundamentais | civil_familia |
| ADI 5938 | direitos_fundamentais | trabalhista |
| SV 13 / RE 636886 | administrativo_publico | constitucional_stf |

## Padrões de resposta esperados

Quando o usuário pedir um leading case, devolva:
1. Identificação (processo, tribunal, relator, data).
2. **Tese firmada** (campo `tese_firmada` integral).
3. Ementa resumida.
4. Contexto histórico (campo `observacoes`).
5. Fonte oficial (`fonte`).
6. Se houver overruling ou referência cruzada, citar explicitamente.

Não invente processos. Se a busca não retornar resultado, diga "não consta no dossiê" e sugira ampliar a busca para `teses_precedentes/` (182 teses STF/STJ/TST) ou `sumulas/` (705 súmulas).

## Grafo visual

Consulte `dossie_judiciario/grafos/mapa_jurisprudencia.md` para diagramas Mermaid com: árvore por área, linhas do tempo, trilhas de overruling e clusters tribunal × área.

## Limitações
- Cobertura curatorial (90 decisões), não exaustiva. Para volume maior, partir para `teses_precedentes/`.
- Datas de coleta: março/2026. Verificar atualizações posteriores no portal oficial antes de citar em peça processual.
