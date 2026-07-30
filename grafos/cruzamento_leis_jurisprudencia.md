# Cruzamento Legislação ↔ Jurisprudência

> Grafos Mermaid relacionando os 167 registros de legislação (federal + local) com as 90 decisões emblemáticas.

## 1. Lei → Decisão Paradigmática

```mermaid
graph LR
    CF[CF/88] --> RE466[RE 466343<br/>depositário infiel]
    CF --> ADI4277[ADI 4277<br/>união homoafetiva]
    CF --> ADPF54[ADPF 54<br/>anencefalia]
    CF --> ADI4650[ADI 4650<br/>doação eleitoral PJ]
    CF --> ADPF153[ADPF 153<br/>Lei de Anistia]

    CC[Código Civil 2002] --> REsp1159[REsp 1.159.242<br/>abandono afetivo]
    CC --> RE898[RE 898060<br/>multiparentalidade]
    CC --> RE878[RE 878694<br/>sucessão união]

    CPC[CPC 2015] --> FPPC[Enunciados FPPC<br/>658]
    CPC --> SUM7[Súmula 7 STJ<br/>reexame de prova]

    CP[Código Penal] --> HC84[HC 84078]
    CP --> HC126[HC 126292]
    CP --> ADC43[ADC 43/44/54]

    CLT[CLT] --> ADPF324[ADPF 324<br/>terceirização]
    CLT --> RE958[RE 958252<br/>atividade-fim]
    CLT --> ARE1121[ARE 1121633<br/>negociado x legislado]

    CTN[CTN] --> RE574[RE 574706<br/>Tese do Século]
    CTN --> RE601[RE 601314<br/>sigilo bancário]

    L8429[Lei 8.429/1992<br/>Improbidade] --> RE636886[RE 636886<br/>nepotismo SV 13]
    L7783[Lei 7.783/1989<br/>Greve] --> ADI3014[ADI 3014<br/>greve servidor]
    L13146[Lei 13.146/2015<br/>Estatuto PCD] --> CC

    EC45[EC 45/2004] --> ADI3367[ADI 3367<br/>CNJ]
    L9099[Lei 9.099/1995<br/>Juizados] --> FONAJE[Enunciados FONAJE<br/>326]
    LIN[Lei 11.343/2006<br/>Drogas] --> HC143641[HC 143641<br/>HC coletivo]

    classDef lei fill:#1e40af,color:#fff;
    classDef caso fill:#fef3c7,color:#78350f;
    classDef coletania fill:#bbf7d0,color:#14532d;
    class CF,CC,CPC,CP,CLT,CTN,L8429,L7783,L13146,EC45,L9099,LIN lei;
    class RE466,ADI4277,ADPF54,ADI4650,ADPF153,REsp1159,RE898,RE878,HC84,HC126,ADC43,ADPF324,RE958,ARE1121,RE574,RE601,RE636886,ADI3014,ADI3367,HC143641 caso;
    class FPPC,SUM7,FONAJE coletania;
```

## 2. Trilhas tema → lei → jurisprudência → súmula

### Trilha 1 — Tributário (Tese do Século)

```mermaid
flowchart LR
    A[CF/88<br/>art. 195] --> B[Lei 10.637/2002<br/>PIS não-cum.]
    A --> C[Lei 10.833/2003<br/>COFINS não-cum.]
    A --> D[LC 87/1996<br/>Kandir]
    B --> E[RE 240785<br/>2014]
    C --> E
    D --> E
    E --> F[RE 574706<br/>2017 RG<br/>Tese do Século]
    F --> G[Modulação<br/>EAREsp 2021<br/>marco 15/03/2017]
    G --> H[Impacto<br/>R$ 250 bilhões<br/>compensação tributária]
```

### Trilha 2 — Penal (Presunção de inocência)

```mermaid
flowchart LR
    A[CF/88<br/>art. 5º LVII] --> B[CPP<br/>DL 3.689/1941]
    B --> C[Lei 7.210/1984<br/>LEP]
    A --> D[HC 84078<br/>2009<br/>inconstitucional]
    D -->|overruling| E[HC 126292<br/>2016<br/>constitucional]
    E -->|overruling| F[ADC 43/44/54<br/>2019<br/>inconstitucional]
    F --> G[SV cancelada<br/>posicionamento atual]
```

### Trilha 3 — Família (Multiparentalidade)

```mermaid
flowchart LR
    A[CF/88<br/>art. 226 e 227] --> B[CC/2002<br/>arts. 1.593 ss]
    B --> C[Lei 12.010/2009<br/>Adoção]
    A --> D[REsp 1.159.242<br/>2012<br/>abandono afetivo]
    B --> D
    D --> E[RE 898060<br/>2016 RG<br/>socioafetiva + biológica]
    E --> F[Enunciados<br/>Jornada de Direito Civil]
    F --> G[CNJ Provimento 63/2017<br/>e 83/2019]
```

### Trilha 4 — Trabalhista (Terceirização)

```mermaid
flowchart LR
    A[CF/88<br/>art. 7º] --> B[CLT 1943]
    B --> C[Súmula 331 TST<br/>1993<br/>veda atividade-fim]
    A --> D[Lei 6.019/1974<br/>+ reformas]
    D --> E[Lei 13.429/2017<br/>liberou terceirização]
    E --> F[ADPF 324 + RE 958252<br/>STF 2018<br/>atividade-fim válida]
    F --> G[Lei 13.467/2017<br/>Reforma Trabalhista]
```

## 3. Mapa cruzado por área

```mermaid
graph TB
    subgraph Civil
        CIV_L[CC + LINDB + LGPD + EPCD]
        CIV_J[REsp 1.159.242 · RE 898060 · RE 878694]
        CIV_S[Súm. 7 STJ · 642 enunciados Jornadas]
        CIV_L --> CIV_J --> CIV_S
    end

    subgraph Penal
        PEN_L[CP + CPP + Hediondos + Drogas + LEP]
        PEN_J[HC 84078 → 126292 → ADC 43/44/54 · AP 470 · HC 143641]
        PEN_S[SV 11 + SV 26 · 326 enunciados FONAJE]
        PEN_L --> PEN_J --> PEN_S
    end

    subgraph Tributário
        TRI_L[CTN + LRF + Kandir + ISS + PIS/COFINS]
        TRI_J[RE 574706 · RE 601314 · RE 586482]
        TRI_S[SV 8 · SV 24 · SV 28 · SV 30]
        TRI_L --> TRI_J --> TRI_S
    end

    subgraph Trabalhista
        TRA_L[CLT + Reforma + FGTS + Previdência]
        TRA_J[ADPF 324 · RE 958252 · ARE 1121633 · ADI 5766]
        TRA_S[463 súmulas TST]
        TRA_L --> TRA_J --> TRA_S
    end

    subgraph Administrativo
        ADM_L[Lei 9.784 · LAI · 8.112 · 8.429 · 14.133]
        ADM_J[RE 589998 · RE 636886 · RE 855091]
        ADM_S[SV 13 · SV 21 · SV 33]
        ADM_L --> ADM_J --> ADM_S
    end

    subgraph Constitucional
        CONS_L[CF/88 + EC 45 + EC 95 + EC 103 + EC 132]
        CONS_J[ADI 4650 · ADPF 153 · ADI 3367]
        CONS_S[62 súmulas vinculantes STF]
        CONS_L --> CONS_J --> CONS_S
    end

    classDef l fill:#1e40af,color:#fff;
    classDef j fill:#fef3c7,color:#78350f;
    classDef s fill:#bbf7d0,color:#14532d;
    class CIV_L,PEN_L,TRI_L,TRA_L,ADM_L,CONS_L l;
    class CIV_J,PEN_J,TRI_J,TRA_J,ADM_J,CONS_J j;
    class CIV_S,PEN_S,TRI_S,TRA_S,ADM_S,CONS_S s;
```

## 4. Ciclo normativo-jurisprudencial (modelo simplificado)

```mermaid
flowchart TD
    A[Constituição/Lei] --> B[Aplicação concreta<br/>juízos e tribunais]
    B --> C[Recurso<br/>STF/STJ/TST]
    C --> D{Tese vinculante?}
    D -->|Sim| E[Súmula vinculante<br/>ou repetitivo]
    D -->|Não| F[Acórdão isolado]
    E --> G[Replicação obrigatória<br/>nas instâncias]
    F --> H[Persuasão]
    G --> I[Enunciado<br/>doutrinário FPPC/Jornada]
    H --> I
    I -.->|provoca| A
```

---

## Fonte
Compilação cruzada de:
- `legislacao_federal/` (86) + `legislacao_local/` (81) = 167 normas
- `jurisprudencia/` (90 decisões)
- `sumulas/` (705 súmulas) — STF 62 · STJ 107 · TST 463 · TSE 73
- `enunciados/` (1.744) — Civil 642 · Comercial 118 · FONAJE 326 · FPPC 658

**Skills correspondentes:**
- `skills/dossie-jurisprudencia-br/SKILL.md`
- `skills/dossie-legislacao-br/SKILL.md`
- `skills/dossie-sumulas-enunciados-br/SKILL.md`
