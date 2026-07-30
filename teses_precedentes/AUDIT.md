# Auditoria de Teses e Repetitivos — Maio/2026

## Contexto

Durante revisão jurídica do caso *Lourenço Marques v. Distrito Federal* (medicamento Evolocumabe / Tema 6 STF), foram detectadas inconsistências sistemáticas nos arquivos `stf/teses_rg.jsonl` e `stj/repetitivos.jsonl`: o **número do Tema** estava associado ao **leading_case errado**, embora o conteúdo (tese, relator, RE/REsp) fosse internamente coerente.

Hipótese de causa: geração inicial por LLM com hallucination na vinculação número↔caso, sem checagem cruzada contra o portal STF/STJ.

## Correções aplicadas (auditoria 25/05/2026)

| Tema | Antes (dossiê) | Depois (corrigido) | Fonte |
|---|---|---|---|
| **Tema 6/STF** | RE 566.349 (Cármen Lúcia / MP / consumidor) | **RE 566.471** (Marco Aurélio / medicamento alto custo, julg. 20/09/2024) | [portal STF](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=6) |
| **Tema 500/STF** | RE 660.861 (Dias Toffoli / 1/3 férias previdenciária) | **RE 657.718** (Marco Aurélio/Alex. de Moraes / medicamento sem ANVISA) | [portal STF](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=500) |
| **Tema 1234/STF** | — (ausente) | **+RE 1.366.243** (Gilmar Mendes / fluxos interfederativos, julg. 13/09/2024) | [portal STF](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=1234) |
| **Tema 98/STJ** | REsp 1.111.156/SP (ISS leasing) | **REsp 1.474.665/RS** (astreintes vs Fazenda em saúde, Benedito Gonçalves) | [Inf. STJ 606](https://processo.stj.jus.br/jurisprudencia/externo/informativo/?aplicacao=informativo&acao=pesquisar&livre=@cnot%3D016335) |
| **Tema 106/STJ** | REsp 1.102.849/MG (ISS plano de saúde) | **REsp 1.657.156/RJ** (medicamentos fora da RENAME, Benedito Gonçalves) | scon.stj.jus.br |

## Tratamento das entradas antigas

As entradas removidas **não foram descartadas** — foram movidas para `temas_pendente_verificacao.jsonl` com flag `_motivo_realocacao`. O conteúdo de cada uma é válido (existem os REsps/REs citados) mas o **número do Tema atribuído está errado**. Suspeitas iniciais a confirmar:

- RE 566.349 (MP/ACP/consumidor) → pode ser **Tema 4/STF** ou similar
- RE 660.861 (1/3 férias) → pode ser **Tema 985/STF**
- REsp 1.111.156 (ISS leasing) → pode ser **Tema 125/STJ**
- REsp 1.102.849 (ISS planos de saúde) → verificar Tema correto

## Próximos passos sugeridos

1. **Verificar Temas remanescentes em massa**: amostrar 10–15 Temas adicionais do STF e STJ contra o portal oficial para estimar a taxa de erro sistêmico. Se >10% errados, fazer auditoria completa.
2. **Reconciliar entradas pendentes**: atribuir o número correto de Tema às 4 entradas em `temas_pendente_verificacao.jsonl` e reinseri-las nos arquivos principais.
3. **Adicionar metadado de proveniência**: novos campos `fonte_url` e `data_verificacao` para permitir auditorias futuras automatizadas.

## Como reproduzir

```bash
# Auditoria
python scripts/audit_dossie.py

# Aplicar correções (idempotente)
python scripts/apply_corrections.py
```

Backups das versões pré-auditoria: `*.bak-pre-audit` nos diretórios `stf/` e `stj/`.
