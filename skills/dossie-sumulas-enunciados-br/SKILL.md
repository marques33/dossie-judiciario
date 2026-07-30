---
name: dossie-sumulas-enunciados-br
description: Use esta skill quando o usuário consultar súmulas brasileiras (Súmulas Vinculantes do STF, súmulas do STJ, TST ou TSE) ou enunciados de jornadas e fóruns (Jornadas de Direito Civil/Comercial do CJF/STJ, FONAJE para Juizados Especiais, FPPC sobre CPC/2015). Cobre 705 súmulas e 1.744 enunciados, totalizando 2.449 registros consultáveis. Use quando mencionar "SV 13", "Súmula 331 TST", "Súmula 7 STJ", "Enunciado 4 da Jornada", "Enunciado FONAJE", "FPPC", precedentes consolidados ou orientações sumuladas.
version: 1.0.0
category: legal
tags: [direito, sumulas, enunciados, stf, stj, tst, tse, fonaje, fppc, jornadas-cjf, dossie-judiciario]
complexity: intermediate
risk: safe
source: dossie_judiciario
author: renan
date_added: 2026-05-22
---

# Dossiê Judiciário — Súmulas e Enunciados (Brasil)

## Quando usar
- Usuário cita súmula por número e tribunal ("Súmula Vinculante 13", "Súmula 331 TST", "Súmula 7 STJ").
- Usuário pede orientação consolidada sobre um tema (busca por palavra-chave nas súmulas).
- Usuário cita enunciado de Jornada de Direito Civil ou Comercial (CJF/STJ).
- Usuário cita enunciado FONAJE (Juizados Especiais Cíveis, Criminais ou da Fazenda Pública).
- Usuário cita enunciado FPPC (Fórum Permanente de Processualistas Civis — interpretações do CPC/2015).
- Construção de peça que exija ementa de súmula ou enunciado interpretativo.

NÃO acione para: legislação (use `dossie-legislacao-br`), acórdãos completos / leading cases (use `dossie-jurisprudencia-br`).

## Banco de dados disponível

### Súmulas — `dossie_judiciario/sumulas/` (705 súmulas)

| Tribunal | Arquivo | Qtd | Distribuição por área |
|---|---|---:|---|
| **STF** | `sumulas/stf/sumulas_vinculantes.jsonl` | 62 (SV 1 a SV 62; 60 vigentes, 2 canceladas) | administrativo 16 · tributário 15 · constitucional 10 · penal 10 · trabalhista 4 |
| **STJ** | `sumulas/stj/*.jsonl` | 107 (601-676 completas + 31 clássicas: Súm. 7, 83, 211, 282, 284 etc.) | mista |
| **TST** | `sumulas/tst/*.jsonl` | 463 | Direito do Trabalho 283 · Proc. do Trabalho 172 · Coletivo 7 · Administrativo do Trabalho 1 |
| **TSE** | `sumulas/tse/*.jsonl` | 73 | Direito Eleitoral 73 |

### Enunciados — `dossie_judiciario/enunciados/` (1.744 enunciados)

| Fonte | Arquivo | Qtd | Foco |
|---|---|---:|---|
| **Jornadas de Direito Civil** (CJF) | `enunciados/jornadas_direito_civil/enunciados.jsonl` | 642 | Jornadas I, III-IX — interpretação do CC/2002 |
| **Jornadas de Direito Comercial** (CJF) | `enunciados/jornadas_direito_comercial/enunciados.jsonl` | 118 | 3 jornadas — empresarial, falência, recuperação |
| **FONAJE** | `enunciados/fonaje/enunciados.jsonl` | 326 | 177 cíveis + 132 criminais + 17 fazenda pública — Lei 9.099/95 e 12.153/09 |
| **FPPC** | `enunciados/fppc/enunciados.jsonl` | 658 | Enunciados 1-706 sobre CPC/2015 (FPPC consolidado) |

## Esquemas

**Súmula Vinculante STF:**
```json
{
  "numero": 1,
  "texto": "...",
  "data_aprovacao": "YYYY-MM-DD",
  "status": "vigente|cancelada",
  "area": "tributario|administrativo|constitucional|penal|trabalhista|...",
  "referencia_cf": "Art. 5º, XXXVI"
}
```

**Súmula TST (estrutura típica):**
```json
{
  "numero": "331",
  "tribunal": "TST",
  "texto": "...",
  "area": "Direito do Trabalho",
  "status": "vigente",
  "data_aprovacao": "..."
}
```

**Enunciado (Jornadas/FONAJE/FPPC):**
```json
{
  "numero": "4",
  "fonte": "Jornada de Direito Civil I (CJF)",
  "texto": "...",
  "artigo_referencia": "Art. 1.228 CC/2002",
  "ano": 2002
}
```

(Schemas exatos podem variar entre fontes — verificar a primeira linha do arquivo antes de filtrar.)

## Como consultar

1. **Por número + tribunal** — grep direto:
   ```bash
   grep -F '"numero": 13,' sumulas/stf/sumulas_vinculantes.jsonl
   grep -F '"numero": "331"' sumulas/tst/*.jsonl
   ```
2. **Por palavra-chave no texto** — útil para temas:
   ```bash
   grep -i 'depositário infiel' sumulas/stf/sumulas_vinculantes.jsonl
   ```
3. **Por área** — para SV STF:
   ```bash
   grep -F '"area": "tributario"' sumulas/stf/sumulas_vinculantes.jsonl
   ```
4. **Enunciado por artigo do CC/CPC**:
   ```bash
   grep -F 'Art. 421' enunciados/jornadas_direito_civil/enunciados.jsonl
   ```
5. **Enunciado FPPC sobre artigo do CPC/2015**:
   ```bash
   grep -F '"artigo": "489"' enunciados/fppc/enunciados.jsonl
   ```

## Súmulas Vinculantes do STF — destaques por área

- **Tributário:** SV 8 (prescrição/decadência contribuições), SV 24 (crime tributário pendente de lançamento), SV 28 (depósito prévio inconstitucional), SV 30 (ICMS importação).
- **Administrativo:** SV 13 (nepotismo), SV 21 (depósito prévio em recurso administrativo), SV 33 (mandado de injunção aposentadoria especial).
- **Constitucional/Direitos Fundamentais:** SV 11 (uso de algemas), SV 14 (acesso a inquérito policial), SV 25 (prisão civil depositário infiel).
- **Penal:** SV 26 (LEP — exame criminológico).

## Súmulas STJ — destaques

- **Súm. 7:** "A pretensão de simples reexame de prova não enseja recurso especial."
- **Súm. 83:** "Não se conhece do recurso especial pela divergência, quando a orientação do tribunal se firmou no mesmo sentido da decisão recorrida."
- **Súm. 211:** "Inadmissível recurso especial quanto à questão que, a despeito da oposição de embargos declaratórios, não foi apreciada pelo Tribunal a quo."
- **Súm. 282/284 (STF aplicadas no STJ):** prequestionamento e fundamentação deficiente.

## Padrão de resposta esperado

Para cada súmula/enunciado citado, devolva:
1. Fonte (Tribunal/Jornada/Fórum) + número.
2. **Texto literal** (não parafrasear).
3. Data de aprovação.
4. Status (vigente/cancelada).
5. Área temática.
6. Se for súmula vinculante, referência constitucional (`referencia_cf`).
7. Se for enunciado, artigo de lei correlato.

Quando o usuário pedir "todas as súmulas sobre X", listar de forma estruturada e indicar contagem.

## Grafo visual

Consulte `dossie_judiciario/grafos/mapa_sumulas_enunciados.md` para diagramas Mermaid com: súmulas vinculantes por área constitucional, súmulas TST por matéria e enunciados das Jornadas por artigo do CC.

## Limitações
- Cobertura curatorial de súmulas STJ (107 de 676). Para súmulas STJ não cobertas, consultar https://scon.stj.jus.br/SCON/sumstj/
- Enunciados FPPC foram consolidados de 706 originais → 658 (deduplicação). Verificar consolidação antes de citar.
- Dados de março/2026.
