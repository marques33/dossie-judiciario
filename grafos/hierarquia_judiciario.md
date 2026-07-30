# Grafo Hierárquico do Poder Judiciário Brasileiro

## Nó Raiz: Poder Judiciário

```mermaid
graph TD
    PJ[Poder Judiciário] --> STF[STF]
    PJ --> STJ[STJ]
    PJ --> TST[TST]
    PJ --> TSE[TSE]
    PJ --> STM[STM]
    PJ --> CNJ[CNJ - Conselho Nacional de Justiça]

    STF --> |"Controle de constitucionalidade"| TRFs
    STF --> |"Controle de constitucionalidade"| TJs
    STF --> |"Recurso extraordinário"| STJ
    STF --> |"Recurso extraordinário"| TST
    STF --> |"Recurso extraordinário"| TSE
    STF --> |"Recurso extraordinário"| STM

    STJ --> TRFs[TRFs 1-6]
    STJ --> TJs[TJs 1-27]

    TST --> TRTs[TRTs 1-24]
    TSE --> TREs[TREs 1-27]
    STM --> AudMil[Auditorias Militares]

    TRFs --> JF[Varas Federais]
    TJs --> Comarcas[Comarcas / Varas]
    TRTs --> VT[Varas do Trabalho]
    TREs --> JE[Juntas/Zonas Eleitorais]
    AudMil --> CJM[Circunscrições de Justiça Militar]
```

## Relações de Competência Recursal

| Tribunal Superior | Recebe recursos de | Matéria |
|---|---|---|
| STF | Todos os tribunais | Constitucional |
| STJ | TRFs, TJs | Infraconstitucional federal |
| TST | TRTs | Trabalhista |
| TSE | TREs | Eleitoral |
| STM | Auditorias Militares | Militar |

## Composição por Origem

### STF (11 ministros)
- Indicação: Presidente da República
- Aprovação: Senado Federal (maioria absoluta)
- Requisitos: notável saber jurídico, reputação ilibada, 35-70 anos

### STJ (33 ministros)
- 1/3 dentre desembargadores dos TRFs
- 1/3 dentre desembargadores dos TJs
- 1/3 dentre advogados e membros do MP (alternadamente)

### TST (27 ministros)
- 1/5 dentre advogados e membros do MPT
- 4/5 dentre juízes dos TRTs

### TSE (7 ministros)
- 3 dentre ministros do STF (eleição)
- 2 dentre ministros do STJ (eleição)
- 2 advogados indicados pelo STF e nomeados pelo Presidente

### STM (15 ministros)
- 10 militares (3 Marinha, 3 Exército, 3 Aeronáutica + 1 oficial-general)
- 5 civis (3 advogados, 1 juiz auditor, 1 membro do MPM)

## Nós Relacionados
- [Tribunais Superiores](../tribunais_superiores/)
- [Justiça Federal](../justica_federal/)
- [Justiça Estadual](../justica_estadual/)
- [Justiça do Trabalho](../justica_trabalho/)
- [Justiça Eleitoral](../justica_eleitoral/)
- [Justiça Militar](../justica_militar/)
- [Grafo de Indicações](./indicacoes_presidenciais.md)
- [Grafo de Especialidades](./especialidades_juridicas.md)
