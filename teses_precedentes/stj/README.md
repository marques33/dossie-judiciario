# Recursos Repetitivos — STJ

## Visão Geral

Banco de teses fixadas pelo Superior Tribunal de Justiça sob o regime dos recursos repetitivos (arts. 1.036-1.041 do CPC/2015; art. 543-C do CPC/1973).

As teses fixadas em recursos repetitivos têm **caráter vinculante** para os tribunais de segundo grau e juízos de primeiro grau (art. 927, III CPC/2015), orientando a resolução em massa de demandas idênticas.

## Arquivo

| Arquivo | Registros |
|---------|-----------|
| `repetitivos.jsonl` | 74 teses |

## Cobertura por Área

| Área | Teses |
|------|-------|
| Tributário | 14 |
| Administrativo | 11 |
| Consumidor | 9 |
| Previdenciário | 8 |
| Processual Civil | 8 |
| Civil | 6 |
| Penal | 5 |
| Empresarial | 5 |
| Trabalhista | 3 |
| Imobiliário | 3 |
| Saúde | 2 |

## Teses de Destaque

| Tema | Caso | Área | Relevância |
|------|------|------|------------|
| 228 | REsp 1.228.104 | Consumidor | Responsabilidade objetiva de banco por fraudes de terceiros |
| 295 | REsp 1.280.825 | Civil | Dano moral in re ipsa por anotação indevida em cadastro de inadimplentes |
| 313 | REsp 1.300.903 | Empresarial | Penhora do bem de família do fiador em locação comercial |
| 340 | REsp 1.347.077 | Tributário | Indenização por dano moral não integra base do IR |
| 430 | REsp 1.525.510 | Empresarial | Stay period de 180 dias na recuperação judicial é improrrogável |
| 471 | REsp 1.591.141 | Empresarial | Dissolução irregular autoriza redirecionamento da execução fiscal |
| 479 | REsp 1.624.003 | Consumidor | Vício do serviço — responsabilidade do fornecedor |
| 534 | REsp 1.693.528 | Previdenciário | Desaposentação — vedação ao duplo benefício |

## Formato do Registro (JSONL)

```json
{
  "tema": 228,
  "tese": "As instituições financeiras respondem objetivamente pelos danos causados por fraudes ou delitos praticados por terceiros...",
  "tipo": "recurso_repetitivo",
  "leading_case": "REsp 1.228.104/SP",
  "data_julgamento": "2012-03-14",
  "relator": "Min. Luis Felipe Salomão",
  "orgao_julgador": "STJ",
  "status": "tese_fixada",
  "area_direito": "consumidor",
  "modulacao_efeitos": false,
  "observacoes": "Súmula 479 STJ; art. 14 CDC; fortuito interno"
}
```

### Campos

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `tema` | int | Número do tema no sistema de repetitivos do STJ |
| `tese` | string | Texto da tese fixada |
| `tipo` | string | Sempre `"recurso_repetitivo"` |
| `leading_case` | string | Processo paradigma (REsp, AREsp, etc.) |
| `data_julgamento` | string | Data ISO 8601 (YYYY-MM-DD) |
| `relator` | string | Ministro relator |
| `orgao_julgador` | string | `"Corte Especial"` ou `"STJ"` (turma/seção) |
| `status` | string | `"tese_fixada"`, `"reconhecida_pendente"` ou `"superado"` |
| `area_direito` | string | Área jurídica principal |
| `modulacao_efeitos` | bool | Se houve modulação de efeitos |
| `observacoes` | string | Súmulas relacionadas, artigos legais, notas |

## Fontes

- Pesquisa de Jurisprudência em Teses STJ: https://www.stj.jus.br/repetitivos/
- Repetitivos e IACs STJ: https://www.stj.jus.br/sites/portalp/Jurisprudencia/Repetitivos-e-IAC
- Dizer o Direito
- JusBrasil / InfoJus
