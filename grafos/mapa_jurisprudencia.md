# Mapa da Jurisprudência Temática Brasileira

> Grafos Mermaid das 90 decisões emblemáticas do STF/STJ/TST catalogadas em `dossie_judiciario/jurisprudencia/`.

## 1. Árvore por Área (90 decisões)

```mermaid
graph TD
    J[Jurisprudência Temática<br/>90 decisões] --> DF[Direitos Fundamentais<br/>15]
    J --> PP[Penal e Processual Penal<br/>15]
    J --> CF[Civil e Família<br/>12]
    J --> TR[Tributário<br/>12]
    J --> TB[Trabalhista<br/>12]
    J --> AD[Administrativo e Público<br/>12]
    J --> CS[Constitucional STF<br/>12]

    DF --> DF1[RE 466343<br/>Depositário infiel]
    DF --> DF2[ADI 4277<br/>União homoafetiva]
    DF --> DF3[ADPF 54<br/>Anencefalia]
    DF --> DF4[ADPF 45<br/>Mínimo existencial]
    DF --> DF5[HC 82424<br/>Caso Ellwanger]

    PP --> PP1[HC 84078<br/>2009]
    PP --> PP2[HC 126292<br/>2016]
    PP --> PP3[ADC 43/44/54<br/>2019]
    PP --> PP4[AP 470<br/>Mensalão]
    PP --> PP5[HC 143641<br/>HC coletivo]

    CF --> CF1[REsp 1.159.242<br/>Abandono afetivo]
    CF --> CF2[RE 898060<br/>Multiparentalidade]
    CF --> CF3[RE 878694<br/>Sucessão união]

    TR --> TR1[RE 574706<br/>Tese do Século]
    TR --> TR2[RE 601314<br/>Sigilo bancário]
    TR --> TR3[RE 240785<br/>ICMS PIS/COFINS]

    TB --> TB1[ADPF 324<br/>Terceirização]
    TB --> TB2[RE 958252<br/>Atividade-fim]
    TB --> TB3[ARE 1121633<br/>Negociado x legislado]
    TB --> TB4[ADI 5766<br/>Honorários]

    AD --> AD1[RE 589998<br/>Demissão empresa pública]
    AD --> AD2[RE 636886<br/>Nepotismo SV 13]
    AD --> AD3[RE 855091<br/>Omissão estatal]
    AD --> AD4[RE 327904<br/>Dupla garantia]

    CS --> CS1[ADI 4650<br/>Doação eleitoral PJ]
    CS --> CS2[ADPF 153<br/>Lei de Anistia]
    CS --> CS3[ADI 3367<br/>CNJ]
    CS --> CS4[RE 197917<br/>Vereadores]

    classDef area fill:#1e40af,color:#fff,stroke:#1e3a8a;
    classDef caso fill:#fef3c7,color:#78350f,stroke:#d97706;
    class DF,PP,CF,TR,TB,AD,CS area;
```

## 2. Trilhas de Overruling (evolução jurisprudencial)

### Presunção de inocência — execução provisória da pena

```mermaid
graph LR
    A[HC 84078<br/>2009<br/>Inconstitucional<br/>execução após 2º grau] -->|overruling| B[HC 126292<br/>2016<br/>Constitucional<br/>execução após 2º grau]
    B -->|overruling| C[ADC 43/44/54<br/>2019<br/>Inconstitucional<br/>execução após 2º grau]
    C --> D[Estado da arte<br/>2026]

    classDef inconst fill:#dcfce7,stroke:#16a34a;
    classDef const fill:#fee2e2,stroke:#dc2626;
    class A,C,D inconst;
    class B const;
```

### Terceirização

```mermaid
graph LR
    S331[Súmula 331 TST<br/>1993<br/>veda na atividade-fim] -->|superada| ADPF324[ADPF 324<br/>2018<br/>libera terceirização irrestrita]
    S331 -->|superada| RE958[RE 958252<br/>2018 RG<br/>tese vinculante]
    ADPF324 --> ATUAL[CLT pós-Reforma 2017<br/>+ tese STF]
    RE958 --> ATUAL
```

### Multiparentalidade e parentalidade socioafetiva

```mermaid
graph LR
    R1159[REsp 1.159.242<br/>STJ 2012<br/>Abandono afetivo<br/>'amar é faculdade, cuidar é dever'] --> RE898[RE 898060<br/>STF 2016 RG<br/>Paternidade socioafetiva<br/>+ biológica simultâneas]
    RE898 --> R1981[REsp 1.981.962<br/>STJ 2022<br/>Multiparentalidade<br/>e sucessão]
```

### Tese do Século (ICMS na base PIS/COFINS)

```mermaid
graph LR
    RE240[RE 240785<br/>2014<br/>precedente isolado] --> RE574[RE 574706<br/>2017 RG<br/>ICMS fora da base<br/>R$ 250 bi]
    RE574 -->|modulação| MOD[EAREsp 1.470.443<br/>2021<br/>marco 15/03/2017]
```

## 3. Linha do Tempo Cronológica

```mermaid
timeline
    title Decisões Emblemáticas — STF/STJ/TST (2001-2021)
    section 2001-2005
        2001 : ADI 1480 (tratados internacionais)
        2003 : HC 82424 (Caso Ellwanger)
        2004 : ADPF 45 (mínimo existencial) : RE 197917 (vereadores)
        2005 : SV 13 (nepotismo)
    section 2006-2010
        2006 : ADI 3367 (CNJ) : RE 327904 (dupla garantia)
        2007 : MS 26602 (fidelidade partidária)
        2008 : RE 466343 (depositário infiel)
        2009 : HC 84078 (presunção de inocência)
        2010 : ADPF 153 (Lei de Anistia) : RE 589998 (demissão estatal)
    section 2011-2015
        2011 : ADI 4277 (união homoafetiva)
        2012 : ADPF 54 (anencefalia) : AP 470 (Mensalão) : REsp 1.159.242 (abandono afetivo)
        2013 : RE 559937 (PIS/COFINS-importação) : RE 562980
        2014 : Início Lava Jato : AP 565 : RE 240785 (ICMS) : RE 613260
        2015 : ADI 4650 (financiamento) : RE 855091 (omissão estatal)
    section 2016-2021
        2016 : HC 126292 (execução provisória) : RE 898060 (multiparentalidade) : REsp 1.526.552 : RE 693456
        2017 : RE 574706 (Tese do Século) : RE 878694 (sucessão) : ADC 41 (cotas) : RE 895759 (terceirização)
        2018 : HC 143641 (HC coletivo) : ADPF 324 + RE 958252 (terceirização)
        2019 : ADC 43/44/54 (execução) : ARE 1121633 (negociado x legislado)
        2020 : RE 636886 (improbidade culposa)
        2021 : ADI 5766 (honorários gratuidade)
```

## 4. Cluster Tribunal × Área

```mermaid
graph TB
    subgraph STF[Supremo Tribunal Federal]
        STF_DF[Direitos<br/>Fundamentais]
        STF_PP[Penal]
        STF_TR[Tributário]
        STF_TB[Trabalhista]
        STF_AD[Administrativo]
        STF_CS[Constitucional]
    end

    subgraph STJ[Superior Tribunal de Justiça]
        STJ_CF[Civil/Família]
        STJ_PP[Processual<br/>Penal]
        STJ_TR[Tributário<br/>infraconst.]
    end

    subgraph TST[Tribunal Superior do Trabalho]
        TST_TB[Trabalhista<br/>infraconst.]
    end

    STF_DF -.->|RE 466343| SV25[SV 25<br/>depositário infiel]
    STF_AD -.->|RE 636886| SV13[SV 13<br/>nepotismo]
    STF_PP -.->|HC 84078<br/>HC 126292<br/>ADC 43/44/54| PRES[Presunção<br/>de inocência]
    STJ_CF -.->|REsp 1.159.242<br/>REsp 1.526.552| FAMILIA[Direito de<br/>família]
    TST_TB -.->|AIRR 10169| FGTS[Prescrição<br/>FGTS]

    classDef trib fill:#1e40af,color:#fff;
    classDef tema fill:#fef3c7,color:#78350f;
    class STF,STJ,TST trib;
    class SV25,SV13,PRES,FAMILIA,FGTS tema;
```

## 5. Referências cruzadas entre áreas

```mermaid
graph LR
    RE898[RE 898060<br/>multiparentalidade] --- DF[Direitos<br/>Fundamentais]
    RE898 --- CF[Civil/Família]

    ADI5938[ADI 5938<br/>gestante/lactante] --- DF
    ADI5938 --- TB[Trabalhista]

    RE636886[RE 636886<br/>nepotismo SV13] --- AD[Administrativo]
    RE636886 --- CS[Constitucional]

    classDef caso fill:#fef3c7,color:#78350f;
    classDef area fill:#1e40af,color:#fff;
    class RE898,ADI5938,RE636886 caso;
    class DF,CF,TB,AD,CS area;
```

## 6. Mapa de Relevância (leading_case × overruled)

```mermaid
quadrantChart
    title Leading Cases por impacto e vigencia
    x-axis Baixo impacto --> Alto impacto
    y-axis Superado --> Vigente
    quadrant-1 Vigente alto impacto
    quadrant-2 Vigente baixo impacto
    quadrant-3 Superado baixo impacto
    quadrant-4 Superado alto impacto
    "RE 574706 Tese do Seculo": [0.95, 0.95]
    "ADI 4277 Uniao homoafetiva": [0.90, 0.95]
    "ADPF 347 ECI prisional": [0.85, 0.90]
    "HC 126292 execucao prov.": [0.85, 0.10]
    "HC 84078 execucao prov.": [0.75, 0.10]
    "ADC 43/44/54": [0.90, 0.95]
    "AP 470 Mensalao": [0.80, 0.85]
    "RE 898060 multiparentalidade": [0.75, 0.90]
    "SV 13 nepotismo": [0.70, 0.90]
    "ADPF 153 Lei Anistia": [0.70, 0.85]
```

---

## Fonte de dados

- `jurisprudencia/direitos_fundamentais/decisoes.jsonl` (15)
- `jurisprudencia/penal_processual_penal/decisoes.jsonl` (15)
- `jurisprudencia/civil_familia/decisoes.jsonl` (12)
- `jurisprudencia/tributario/decisoes.jsonl` (12)
- `jurisprudencia/trabalhista/decisoes.jsonl` (12)
- `jurisprudencia/administrativo_publico/decisoes.jsonl` (12)
- `jurisprudencia/constitucional_stf/decisoes.jsonl` (12)

Gerado a partir de `scripts/_agregado.json` consolidando os 7 JSONLs temáticos.

## Como usar
- **Renderização:** GitHub renderiza Mermaid nativamente; abra este arquivo no repo ou em qualquer leitor Markdown que suporte Mermaid (Obsidian, VSCode com extensão).
- **Edição:** editar diretamente os blocos ` ```mermaid ` neste arquivo.
- **Skill correspondente:** `skills/dossie-jurisprudencia-br/SKILL.md`.
