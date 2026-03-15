# Dossiê do Judiciário Brasileiro

## Objetivo
Panorama completo do Poder Judiciário brasileiro para trabalho acadêmico sobre o judiciário e digital twins.

## Estrutura Hierárquica

```
Poder Judiciário
├── Tribunais Superiores
│   ├── STF — Supremo Tribunal Federal (11 ministros)
│   ├── STJ — Superior Tribunal de Justiça (33 ministros)
│   ├── TST — Tribunal Superior do Trabalho (27 ministros)
│   ├── TSE — Tribunal Superior Eleitoral (7 ministros)
│   └── STM — Superior Tribunal Militar (15 ministros)
├── Justiça Federal
│   ├── TRF1 — 1ª Região (AC, AM, AP, BA, DF, GO, MA, MG, MT, PA, PI, RO, RR, TO)
│   ├── TRF2 — 2ª Região (ES, RJ)
│   ├── TRF3 — 3ª Região (MS, SP)
│   ├── TRF4 — 4ª Região (PR, RS, SC)
│   ├── TRF5 — 5ª Região (AL, CE, PB, PE, RN, SE)
│   └── TRF6 — 6ª Região (MG) [criado em 2022]
├── Justiça Estadual (27 Tribunais de Justiça)
│   ├── TJAC, TJAL, TJAM, TJAP, TJBA, TJCE, TJDFT
│   ├── TJES, TJGO, TJMA, TJMG, TJMS, TJMT
│   ├── TJPA, TJPB, TJPE, TJPI, TJPR, TJRJ
│   ├── TJRN, TJRO, TJRR, TJRS, TJSC, TJSE, TJSP, TJTO
├── Justiça do Trabalho (24 TRTs)
│   ├── TRT1 (RJ) ... TRT24 (MS)
├── Justiça Eleitoral (27 TREs)
│   ├── TRE-AC ... TRE-TO
└── Justiça Militar
    ├── STM (Superior Tribunal Militar)
    ├── Auditorias Militares da União
    └── Tribunais de Justiça Militar Estaduais (MG, RS, SP)
```

## Formato dos Dados

- **JSONL**: Cada tribunal possui um arquivo `ministros.jsonl` ou `desembargadores.jsonl` com uma linha JSON por magistrado
- **Markdown (README.md)**: Cada tribunal possui um README com visão geral, composição, hierarquia e estrutura
- **Grafos (grafos/)**: Arquivos markdown com relações entre magistrados, tribunais e decisões
- **Enunciados (enunciados/)**: Enunciados de jornadas juridicas e foruns em formato JSONL
- **Sumulas (sumulas/)**: Sumulas vinculantes e ordinarias dos tribunais superiores em formato JSONL

## Campos dos Registros JSONL

```json
{
  "id": "identificador_unico",
  "nome_completo": "",
  "tribunal": "",
  "cargo": "",
  "nascimento": "",
  "naturalidade": "",
  "formacao_academica": [],
  "trajetoria_profissional": [],
  "data_posse": "",
  "indicado_por": "",
  "turma_secao": "",
  "especialidades": [],
  "decisoes_notaveis": [],
  "publicacoes": [],
  "observacoes": ""
}
```

## Fases de Coleta

| Fase | Escopo | Status |
|------|--------|--------|
| 1 | Tribunais Superiores (STF, STJ, TST, TSE, STM) | ✅ 5/5 completos |
| 2 | Justiça Federal (TRF1-TRF6) | ✅ 6/6 completos |
| 3 | Justiça Estadual (27 TJs) | ✅ 27/27 completos |
| 4 | Justiça do Trabalho (24 TRTs) | ✅ 24/24 completos |
| 5 | Justiça Eleitoral (TREs) | ✅ README + 2 JSONLs consolidados + 5 READMEs individuais |
| 6 | Justiça Militar | ✅ README + JSONL (3 TJMs estaduais) |
| 7 | Grafos e relações cruzadas | ✅ 11 grafos Mermaid |
| 8 | Enunciados - Jornadas de Direito Civil (CJF/STJ) | ✅ 642 registros (8 jornadas, ~693 enunciados) |
| 9 | Enunciados - Jornadas de Direito Comercial (CJF/STJ) | ✅ 118 registros (3 jornadas, 115 enunciados) |
| 10 | Enunciados - FONAJE (Juizados Especiais) | ✅ 326 registros (civeis, criminais, fazenda publica) |
| 11 | Enunciados - FPPC (CPC/2015) | ✅ 658 registros (706 enunciados consolidados) |
| 12 | Sumulas Vinculantes do STF | ✅ 62 registros (SV 1 a SV 62) |
| 13 | Sumulas do STJ | ✅ 107 registros (601-676 completas + 31 classicas) |

## Totais

| Metrica | Valor |
|---------|-------|
| Total de arquivos | ~160 |
| Arquivos JSONL — Digital Twins | 65 |
| Arquivos JSONL — Enunciados e Sumulas | 6 |
| Arquivos Markdown | ~90 |
| Magistrados registrados | 1.541 |
| Enunciados e sumulas registrados | 1.913 |
| Tamanho total | ~2,5 MB |

## Cobertura — Digital Twins (Magistrados)

| Ramo | Tribunais | Magistrados |
|------|-----------|-------------|
| Tribunais Superiores | STF (11), STJ (33), TST (26), TSE (11), STM (15) | 96 |
| Justiça Federal | TRF1-TRF6 | ~137 |
| Justiça Estadual | 27 TJs (todos os estados + DF) | ~474 |
| Justiça do Trabalho | 24 TRTs | ~500+ |
| Justiça Eleitoral | 27 TREs (consolidado) | ~190+ |
| Justiça Militar | STM + 3 TJMs estaduais | ~36 |

## Cobertura — Enunciados e Sumulas

| Fonte | Registros | Observacoes |
|-------|-----------|-------------|
| Jornadas de Direito Civil (CJF) | 642 | 8 jornadas (I, III-IX), ~693 enunciados |
| Jornadas de Direito Comercial (CJF) | 118 | 3 jornadas, 115 enunciados |
| FONAJE | 326 | 177 civeis + 132 criminais + 17 fazenda publica |
| FPPC | 658 | Enunciados 1-706 sobre CPC/2015 |
| Sumulas Vinculantes STF | 62 | SV 1 a SV 62 (60 vigentes, 2 canceladas) |
| Sumulas STJ | 107 | 601-676 completas + 31 classicas selecionadas |

## Proximas Fases

| Fase | Escopo | Status |
|------|--------|--------|
| Sumulas TST e TSE | Sumulas do Tribunal Superior do Trabalho e Eleitoral | Pendente |
| Teses Repercussao Geral | Teses do STF em repercussao geral | Pendente |
| Recursos Repetitivos | Teses do STJ em recursos repetitivos | Pendente |
| Legislacao Federal | Codigos e leis estruturantes (metadados) | Pendente |
| Jurisprudencia Tematica | Decisoes emblematicas por area do direito | Pendente |
| Legislacao Local | Legislacao estadual e municipal | Pendente |

## Data de Referencia
Dados coletados entre 12 e 14 de marco de 2026.
