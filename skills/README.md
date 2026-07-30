# Skills do Dossiê Judiciário

Skills no padrão Claude Code (frontmatter YAML + corpo Markdown) que ensinam o Claude a consultar o banco JSONL deste dossiê.

## Skills disponíveis

| Skill | Cobertura | Registros |
|---|---|---:|
| [`dossie-jurisprudencia-br`](dossie-jurisprudencia-br/SKILL.md) | 90 decisões emblemáticas STF/STJ/TST em 7 áreas + trilhas de overruling | 90 |
| [`dossie-legislacao-br`](dossie-legislacao-br/SKILL.md) | Legislação federal (86) + local (81) — códigos, leis ordinárias, complementares, ECs, CEs, LOMs | 167 |
| [`dossie-sumulas-enunciados-br`](dossie-sumulas-enunciados-br/SKILL.md) | Súmulas STF/STJ/TST/TSE (705) + enunciados Jornadas/FONAJE/FPPC (1.744) | 2.449 |

**Total mapeado: 2.706 registros.**

## Como ativar

### Opção A — Como skills do projeto (recomendado)
As skills já vivem em `dossie_judiciario/skills/`. Para o Claude usá-las automaticamente em qualquer sessão dentro deste diretório, basta ter o Claude Code rodando aqui (ele varre `./skills/*/SKILL.md` automaticamente em projetos com diretório `.claude/`).

Se quiser tornar explícito:
```bash
mkdir -p .claude/skills
# As skills já estão em skills/ — basta apontar
```

### Opção B — Globais para o usuário
Copiar para `~/.claude/skills/`:

```powershell
Copy-Item -Recurse skills/dossie-* "$env:USERPROFILE\.claude\skills\"
```

Depois disso, qualquer conversa que mencionar "leading case", "Súmula Vinculante", "CC/2002", etc., o Claude poderá invocar essas skills mesmo fora do diretório do dossiê.

## Anatomia de uma skill (padrão usado aqui)

```markdown
---
name: dossie-jurisprudencia-br
description: <quando o Claude deve usar esta skill — campo crítico para auto-discovery>
version: 1.0.0
category: legal
tags: [...]
complexity: intermediate
risk: safe
source: dossie_judiciario
author: renan
date_added: 2026-05-22
---

# Título

## Quando usar
## Banco de dados disponível
## Esquema dos registros
## Como consultar (comandos exemplo)
## Padrão de resposta esperado
## Grafos visuais
## Limitações
```

A skill **não** carrega os JSONLs no contexto — ela ensina o Claude onde procurar e como filtrar (Grep no JSONL, ID conventions, áreas indexadas). Isso preserva contexto e mantém o dado como fonte de verdade.

## Grafos correspondentes

| Grafo | Skill |
|---|---|
| `../grafos/mapa_jurisprudencia.md` | dossie-jurisprudencia-br |
| `../grafos/mapa_legislacao_federal.md` | dossie-legislacao-br |
| `../grafos/mapa_legislacao_local.md` | dossie-legislacao-br |
| `../grafos/mapa_sumulas_enunciados.md` | dossie-sumulas-enunciados-br |
| `../grafos/cruzamento_leis_jurisprudencia.md` | todas |

## Pipeline de manutenção

Quando novos registros forem adicionados a `jurisprudencia/`, `legislacao_*/`, `sumulas/` ou `enunciados/`:

1. Atualizar a fase correspondente no `../README.md`.
2. Rodar `python scripts/agregar_metadados.py` (gera `scripts/_agregado.json`).
3. Atualizar a contagem na tabela acima e nas SKILLs afetadas (campo `description` no frontmatter + tabela "Banco de dados disponível").
4. Atualizar o grafo correspondente em `../grafos/` (totais nos `pie` e nós dos `graph`).
