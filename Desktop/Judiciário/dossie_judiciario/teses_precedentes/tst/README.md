# Recursos Repetitivos / IRDR — TST

## Visão Geral

Banco de teses fixadas pelo Tribunal Superior do Trabalho sob o regime dos recursos de revista repetitivos e do Incidente de Resolução de Demandas Repetitivas (IRDR), previstos nos arts. 896-B e 896-C da CLT (inseridos pela Lei 13.015/2014) e no art. 15 c/c arts. 976-987 do CPC/2015.

As teses fixadas pelo TST em recursos repetitivos têm **eficácia vinculante** para os Tribunais Regionais do Trabalho e juízos de primeiro grau da Justiça do Trabalho.

## Arquivo

| Arquivo | Registros |
|---------|-----------|
| `repetitivos.jsonl` | 27 teses |

## Cobertura por Área

| Área | Teses |
|------|-------|
| Jornada | 4 |
| Remuneração | 4 |
| Terceirização | 3 |
| Acidente de Trabalho | 3 |
| Rescisão | 3 |
| Estabilidade | 3 |
| Dano Moral | 3 |
| Prescrição | 2 |
| Vínculo Empregatício | 2 |

## Teses de Destaque

| Tema | Caso | Área | Relevância |
|------|------|------|------------|
| RR-1 | TST-IRR-1000-82 | Jornada | Banco de horas exige negociação coletiva |
| RR-5 | TST-RR-1151-84 | Remuneração | Insalubridade calculada sobre salário mínimo |
| RR-8 | TST-AIRR-479-60 | Terceirização | Terceirização da atividade-fim é lícita (pós ADPF 324) |
| RR-17 | TST-AIRR-2015-82 | Estabilidade | Gestante tem estabilidade mesmo em contrato por prazo determinado |
| RR-20 | TST-RR-1116-52 | Dano Moral | Assédio moral — configuração e reparação |
| RR-26 | TST-IRR-1000-33 | Vínculo | Motorista de aplicativo pode ter vínculo reconhecido |

## Formato do Registro (JSONL)

```json
{
  "tema": "RR-8",
  "tese": "Após o julgamento do ARE 791.932 pelo STF e a vigência da Lei 13.429/2017, é lícita a terceirização de qualquer atividade...",
  "tipo": "recurso_repetitivo_tst",
  "leading_case": "TST-AIRR-479-60.2014.5.04.0611",
  "data_julgamento": "2019-08-28",
  "relator": "Min. Alexandre Agra Belmonte",
  "orgao_julgador": "Tribunal Pleno",
  "status": "tese_fixada",
  "area_direito": "terceirização",
  "modulacao_efeitos": true,
  "observacoes": "ARE 791.932 STF; Lei 13.429/17; ADPF 324 STF"
}
```

### Campos

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `tema` | string | Identificador da tese (ex: `"RR-8"`) |
| `tese` | string | Texto da tese fixada |
| `tipo` | string | Sempre `"recurso_repetitivo_tst"` |
| `leading_case` | string | Processo paradigma do TST |
| `data_julgamento` | string | Data ISO 8601 (YYYY-MM-DD) |
| `relator` | string | Ministro relator |
| `orgao_julgador` | string | `"Tribunal Pleno"` ou `"SDI-1"` |
| `status` | string | `"tese_fixada"`, `"reconhecida_pendente"` ou `"superado"` |
| `area_direito` | string | Área jurídica principal |
| `modulacao_efeitos` | bool | Se houve modulação de efeitos |
| `observacoes` | string | Referências a CLT, Súmulas TST, OJs e legislação |

## Fontes

- Jurisprudência TST em Teses: https://www.tst.jus.br/jurisprudencia
- Repetitivos TST: https://www.tst.jus.br/web/guest/repetitivos
- CLT comentada; Dizer o Direito; JusBrasil
