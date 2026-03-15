# Grafo das Reformas do Judiciário Brasileiro

## Linha do Tempo das Principais Reformas

```mermaid
timeline
    title Marcos da Reforma do Judiciário
    1988 : Constituição Federal
         : Estrutura atual do Judiciário
    2004 : EC 45 - Reforma do Judiciário
         : Criação do CNJ
         : Súmula Vinculante
         : Repercussão Geral
    2006 : Início do processo eletrônico
         : Primeiras experiências com PJe
    2009 : Lei 11.419 - Informatização do Processo Judicial
    2015 : CPC/2015 - Novo Código de Processo Civil
         : Precedentes obrigatórios
         : IRDR
    2017 : Reforma Trabalhista (Lei 13.467)
    2019 : Pacote Anticrime (Lei 13.964)
         : Juiz de Garantias
    2022 : Criação do TRF6 (EC 73)
    2024-2026 : Regulamentação IA no Judiciário
              : Resolução CNJ sobre uso de IA
```

## EC 45/2004 — A Grande Reforma

### Principais Inovações

| Inovação | Impacto |
|----------|---------|
| CNJ | Controle externo administrativo |
| Súmula Vinculante | Uniformização de jurisprudência |
| Repercussão Geral | Filtro de recursos no STF |
| Federalização de crimes contra DH | Incidente de deslocamento de competência |
| Quarentena | 3 anos para advogar após deixar cargo |
| Autonomia financeira | PJ com orçamento próprio |
| Justiça itinerante | Obrigatoriedade |
| Câmaras regionais | Descentralização dos TRFs |

## Digitalização do Judiciário

```mermaid
graph TD
    subgraph Evolucao[Evolução Digital]
        P1[Processo Físico<br>Papel] --> P2[Processo Digitalizado<br>Scanner de autos]
        P2 --> P3[Processo Eletrônico<br>PJe e similares]
        P3 --> P4[Judiciário 4.0<br>IA, Analytics, Automação]
        P4 --> P5[Digital Twin<br>Gêmeo Digital do Judiciário]
    end

    subgraph Sistemas[Principais Sistemas]
        PJe[PJe - Processo Judicial Eletrônico<br>CNJ]
        ESAJ[e-SAJ<br>TJSP e outros]
        EPROC[eproc<br>TRF4, TRFs]
        PROJUDI[PROJUDI<br>Justiça Estadual]
        SEI[SEI<br>Administrativo]
    end

    P3 --> PJe
    P3 --> ESAJ
    P3 --> EPROC
    P3 --> PROJUDI
```

## IA no Judiciário

### Sistemas de IA em uso

| Sistema | Tribunal | Função |
|---------|----------|--------|
| VICTOR | STF | Análise de repercussão geral |
| SOCRATES | STJ | Agrupamento de processos repetitivos |
| ATHOS | STJ | Pesquisa jurisprudencial |
| RADAR | TRF3 | Identificação de demandas repetitivas |
| ELIS | TST | Análise de admissibilidade |
| LEIA | TJMG | Leitura de petições iniciais |
| POTI | TJRN | Automação de decisões |
| DRA. LUZIA | TJRO | Análise de processos |
| CLARA | TRF1 | Classificação de processos |

### Regulamentação

- **Resolução CNJ 332/2020**: Ética, transparência e governança na produção e uso de IA
- **Portaria CNJ 271/2020**: Modelo de governança de IA para o Judiciário
- **Resolução CNJ 385/2021**: Criação de núcleos de IA nos tribunais

## Desafios Atuais

1. **Acervo processual**: ~80 milhões de processos pendentes
2. **Morosidade**: Tempo médio até sentença ~2-4 anos (1ª instância)
3. **Acesso à justiça**: Desigualdade regional na distribuição de juízes
4. **Orçamento**: Judiciário consome ~1,3% do PIB
5. **Digitalização desigual**: Sistemas diferentes entre tribunais

## Nós Relacionados
- [CNJ](./estrutura_cnj.md)
- [Digital Twins](./digital_twins_judiciario.md)
- [Estatísticas](./estatisticas_judiciario.md)
- [Hierarquia](./hierarquia_judiciario.md)
