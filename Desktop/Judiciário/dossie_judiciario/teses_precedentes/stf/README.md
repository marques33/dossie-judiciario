# Teses de Repercussão Geral — STF

## Visão Geral

Banco de teses fixadas pelo Supremo Tribunal Federal sob o regime da repercussão geral (art. 102, §3° CF/88, regulamentado pela Lei 11.418/2006 e pelo CPC/2015, arts. 1.035-1.041).

As teses de repercussão geral têm **eficácia vinculante** e **erga omnes**, obrigando todos os tribunais e juízos do país a aplicar o entendimento fixado pelo STF.

## Arquivo

| Arquivo | Registros |
|---------|-----------|
| `teses_rg.jsonl` | 81 teses |

## Cobertura por Área

| Área | Teses |
|------|-------|
| Tributário | 21 |
| Administrativo | 15 |
| Previdenciário | 8 |
| Penal | 8 |
| Processual Civil | 7 |
| Constitucional | 7 |
| Civil | 7 |
| Trabalhista | 3 |
| Eleitoral | 2 |
| Ambiental | 2 |
| Saúde | 1 |

## Teses de Destaque

| Tema | Caso | Área | Relevância |
|------|------|------|------------|
| 69 | RE 574.706 | Tributário | "Tese do século" — ICMS não integra base PIS/COFINS |
| 698 | RE 709.212 | Trabalhista | FGTS — prescrição quinquenal |
| 786 | RE 1.010.606 | Civil/Constitucional | Direito ao esquecimento não existe no Brasil |
| 505 | RE 635.659 | Penal | Descriminalização do porte de drogas para consumo pessoal |
| 939 | RE 1.017.365 | Constitucional | Marco temporal para demarcação de terras indígenas |
| 809 | RE 593.849 | Tributário | Repetição de indébito em substituição tributária progressiva |
| 80 | RE 377.457 | Previdenciário | Contribuição ao PIS sobre receita das pessoas jurídicas |
| 260 | RE 549.115 | Tributário | COFINS — base de cálculo para empresas financeiras |

## Formato do Registro (JSONL)

```json
{
  "tema": 69,
  "tese": "O ICMS não compõe a base de cálculo para fins de incidência do PIS e da COFINS.",
  "tipo": "repercussao_geral",
  "leading_case": "RE 574.706/PR",
  "data_julgamento": "2017-03-15",
  "relator": "Min. Cármen Lúcia",
  "orgao_julgador": "Plenário",
  "status": "tese_fixada",
  "area_direito": "tributário",
  "modulacao_efeitos": true,
  "observacoes": "Modulação: efeitos a partir de 15/03/2017, ressalvadas ações ajuizadas antes."
}
```

### Campos

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `tema` | int | Número do tema de repercussão geral no STF |
| `tese` | string | Texto da tese fixada |
| `tipo` | string | Sempre `"repercussao_geral"` |
| `leading_case` | string | Processo paradigma (RExt, ARE, etc.) |
| `data_julgamento` | string | Data ISO 8601 (YYYY-MM-DD) |
| `relator` | string | Ministro relator |
| `orgao_julgador` | string | Sempre `"Plenário"` |
| `status` | string | `"tese_fixada"`, `"reconhecida_pendente"` ou `"superado"` |
| `area_direito` | string | Área jurídica principal |
| `modulacao_efeitos` | bool | Se houve modulação de efeitos pelo Plenário |
| `observacoes` | string | Informações complementares, modulação, OJs, etc. |

## Fontes

- Portal do STF — Repercussão Geral: https://portal.stf.jus.br/repercussaogeral/
- Teses STF (por tema): https://jurisprudencia.stf.jus.br/pages/search/
- Dizer o Direito (resumos)
- Buscador Dizer o Direito / JusBrasil
