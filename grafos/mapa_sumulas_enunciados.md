# Mapa de Súmulas e Enunciados

> Grafos Mermaid dos 705 súmulas (STF/STJ/TST/TSE) e 1.744 enunciados (Jornadas/FONAJE/FPPC) catalogados em `dossie_judiciario/sumulas/` e `dossie_judiciario/enunciados/`.

## 1. Visão geral por fonte

```mermaid
graph TD
    R[Súmulas + Enunciados<br/>2.449 registros]

    R --> SU[Súmulas<br/>705]
    R --> EN[Enunciados<br/>1.744]

    SU --> SV[STF — Vinculantes<br/>62 SV 1-62]
    SU --> STJ[STJ<br/>107]
    SU --> TST[TST<br/>463]
    SU --> TSE[TSE<br/>73]

    EN --> JCC[Jornadas Direito Civil<br/>CJF · 642]
    EN --> JCO[Jornadas Direito Comercial<br/>CJF · 118]
    EN --> FNJ[FONAJE<br/>326]
    EN --> FPC[FPPC<br/>658]

    classDef root fill:#7c3aed,color:#fff;
    classDef nivel fill:#1e40af,color:#fff;
    classDef fonte fill:#fef3c7,color:#78350f;
    class R root;
    class SU,EN nivel;
    class SV,STJ,TST,TSE,JCC,JCO,FNJ,FPC fonte;
```

## 2. Súmulas Vinculantes STF — distribuição por área

```mermaid
pie title Súmulas Vinculantes STF (62 registros)
    "Administrativo" : 16
    "Tributário" : 15
    "Constitucional" : 10
    "Penal" : 10
    "Trabalhista" : 4
    "Outras" : 7
```

## 3. SV STF destacadas por área

```mermaid
graph LR
    SV[SV STF 1-62]

    SV --> TRIB[Tributário]
    SV --> ADM[Administrativo]
    SV --> CONS[Constitucional / DF]
    SV --> PEN[Penal]

    TRIB --> SV8[SV 8<br/>Prescrição contribuições<br/>10/05 ANOS — inconst.]
    TRIB --> SV24[SV 24<br/>Crime tributário<br/>pendência de lançamento]
    TRIB --> SV28[SV 28<br/>Depósito prévio<br/>inconstitucional]
    TRIB --> SV30[SV 30<br/>ICMS importação]

    ADM --> SV13[SV 13<br/>Nepotismo]
    ADM --> SV21[SV 21<br/>Depósito recurso adm.]
    ADM --> SV33[SV 33<br/>Aposentadoria especial<br/>MI]

    CONS --> SV11[SV 11<br/>Uso de algemas]
    CONS --> SV14[SV 14<br/>Acesso a inquérito<br/>policial]
    CONS --> SV25[SV 25<br/>Prisão depositário<br/>infiel]

    PEN --> SV26[SV 26<br/>LEP — exame criminológico]

    classDef cat fill:#1e40af,color:#fff;
    classDef sum fill:#fef3c7,color:#78350f;
    class TRIB,ADM,CONS,PEN cat;
    class SV8,SV24,SV28,SV30,SV13,SV21,SV33,SV11,SV14,SV25,SV26 sum;
```

## 4. Súmulas TST — distribuição por subárea trabalhista

```mermaid
pie title Súmulas TST (463 registros)
    "Direito do Trabalho material" : 283
    "Processual do Trabalho" : 172
    "Coletivo do Trabalho" : 7
    "Administrativo do Trabalho" : 1
```

```mermaid
graph TD
    TST[Súmulas TST · 463]
    TST --> MAT[Material 283]
    TST --> PRO[Processual 172]
    TST --> COL[Coletivo 7]

    MAT --> MAT1[Súm. 331<br/>terceirização — atividade-fim<br/>superada]
    MAT --> MAT2[Súm. 51<br/>regulamento mais benéfico]
    MAT --> MAT3[Súm. 277<br/>ultratividade — inconst. ARE 1121633]
    MAT --> MAT4[Súm. 363<br/>contrato nulo Adm. Pública]

    PRO --> PRO1[Súm. 217<br/>depósito recursal]
    PRO --> PRO2[Súm. 422<br/>princípio da dialeticidade]
    PRO --> PRO3[Súm. 393<br/>devolutividade ampla]

    classDef trib fill:#1e40af,color:#fff;
    classDef sub fill:#dc2626,color:#fff;
    classDef sum fill:#fef3c7,color:#78350f;
    class TST trib;
    class MAT,PRO,COL sub;
    class MAT1,MAT2,MAT3,MAT4,PRO1,PRO2,PRO3 sum;
```

## 5. Súmulas STJ — destaques (107 catalogadas)

```mermaid
graph TB
    STJ[Súmulas STJ · 107<br/>601-676 completas + 31 clássicas]

    STJ --> ADM[Admissibilidade<br/>do recurso]
    STJ --> CIV[Civil]
    STJ --> PRO[Processual]
    STJ --> TRI[Tributário]

    ADM --> S7[Súm. 7<br/>reexame de prova]
    ADM --> S83[Súm. 83<br/>orientação no mesmo sentido]
    ADM --> S211[Súm. 211<br/>prequestionamento]

    CIV --> S301[Súm. 301<br/>recusa exame de DNA]
    CIV --> S380[Súm. 380<br/>sociedade de fato]

    PRO --> S568[Súm. 568<br/>relator monocrático]

    TRI --> S554[Súm. 554<br/>parcelamento]

    classDef root fill:#7c3aed,color:#fff;
    classDef cat fill:#1e40af,color:#fff;
    classDef sum fill:#fef3c7,color:#78350f;
    class STJ root;
    class ADM,CIV,PRO,TRI cat;
    class S7,S83,S211,S301,S380,S568,S554 sum;
```

## 6. Súmulas TSE (73 registros)

```mermaid
graph LR
    TSE[Súmulas TSE · 73<br/>100% Direito Eleitoral]

    TSE --> A[Inelegibilidade]
    TSE --> B[Registro de candidatura]
    TSE --> C[Propaganda e prestação de contas]
    TSE --> D[Diplomação]
    TSE --> E[Ações eleitorais<br/>AIJE · AIME · RCED]

    classDef root fill:#7c3aed,color:#fff;
    classDef cat fill:#1e40af,color:#fff;
    class TSE root;
    class A,B,C,D,E cat;
```

## 7. Enunciados das Jornadas de Direito Civil — por jornada

```mermaid
graph TB
    CJF[Jornadas CJF/STJ<br/>de Direito Civil<br/>642 enunciados]

    CJF --> J1[Jornada I<br/>2002 · ~140 enunciados]
    CJF --> J3[Jornada III<br/>2004]
    CJF --> J4[Jornada IV<br/>2006]
    CJF --> J5[Jornada V<br/>2011]
    CJF --> J6[Jornada VI<br/>2013]
    CJF --> J7[Jornada VII<br/>2015]
    CJF --> J8[Jornada VIII<br/>2018]
    CJF --> J9[Jornada IX<br/>2022]

    J1 --> T1[Parte Geral<br/>+ Obrigações]
    J3 --> T2[Direito de Família<br/>+ Sucessões]
    J5 --> T3[Responsabilidade Civil]
    J7 --> T4[Contratos<br/>função social]
    J9 --> T5[Atualizações pós-Estatuto<br/>da PCD e LGPD]

    classDef root fill:#7c3aed,color:#fff;
    classDef jor fill:#1e40af,color:#fff;
    classDef tema fill:#fef3c7,color:#78350f;
    class CJF root;
    class J1,J3,J4,J5,J6,J7,J8,J9 jor;
    class T1,T2,T3,T4,T5 tema;
```

## 8. Enunciados FONAJE — por matéria

```mermaid
pie title Enunciados FONAJE (326)
    "Cíveis (Lei 9.099/95)" : 177
    "Criminais (Lei 9.099/95)" : 132
    "Fazenda Pública (Lei 12.153/09)" : 17
```

## 9. Enunciados FPPC — por bloco do CPC/2015

```mermaid
graph LR
    FPC[FPPC · 658 enunciados<br/>CPC/2015]
    FPC --> A[Parte Geral<br/>normas fundamentais]
    FPC --> B[Tutela de cognição<br/>incluindo IRDR]
    FPC --> C[Tutela provisória]
    FPC --> D[Cumprimento de sentença]
    FPC --> E[Execução]
    FPC --> F[Recursos]
    FPC --> G[Procedimentos especiais]

    classDef root fill:#7c3aed,color:#fff;
    classDef bl fill:#1e40af,color:#fff;
    class FPC root;
    class A,B,C,D,E,F,G bl;
```

## 10. Visão integrada — pirâmide do precedente

```mermaid
graph TD
    A[Constituição Federal] --> B[Súmulas Vinculantes STF<br/>62]
    A --> C[Teses RG STF<br/>81 — em teses_precedentes/]
    A --> D[Súmulas STJ + Repetitivos<br/>107 + 74]
    A --> E[Súmulas TST + Repetitivos<br/>463 + 27]
    A --> F[Súmulas TSE<br/>73]
    A --> G[Enunciados doutrinários<br/>1.744]

    B -.vinculante.-> JU[Juízos e<br/>tribunais inferiores]
    C -.vinculante.-> JU
    D -.persuasivo<br/>forte.-> JU
    E -.persuasivo<br/>forte.-> JU
    F -.persuasivo.-> JU
    G -.doutrinário.-> JU

    classDef cf fill:#7c3aed,color:#fff;
    classDef vin fill:#dc2626,color:#fff;
    classDef per fill:#1e40af,color:#fff;
    classDef dou fill:#fef3c7,color:#78350f;
    classDef ju fill:#bbf7d0,color:#14532d;
    class A cf;
    class B,C vin;
    class D,E,F per;
    class G dou;
    class JU ju;
```

---

## Fonte de dados
- `sumulas/stf/sumulas_vinculantes.jsonl` (62)
- `sumulas/stj/*.jsonl` (107)
- `sumulas/tst/*.jsonl` (463)
- `sumulas/tse/*.jsonl` (73)
- `enunciados/jornadas_direito_civil/enunciados.jsonl` (642)
- `enunciados/jornadas_direito_comercial/enunciados.jsonl` (118)
- `enunciados/fonaje/enunciados.jsonl` (326)
- `enunciados/fppc/enunciados.jsonl` (658)

**Skill correspondente:** `skills/dossie-sumulas-enunciados-br/SKILL.md`.
