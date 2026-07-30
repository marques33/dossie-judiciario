# Mapa da Legislação Local (Estadual + Municipal)

> Grafos Mermaid dos 81 registros catalogados em `dossie_judiciario/legislacao_local/`.

## 1. Estrutura Federativa

```mermaid
graph TD
    BR[República Federativa<br/>do Brasil]
    BR --> UN[União<br/>CF/88]
    BR --> ED[26 Estados<br/>+ DF]
    BR --> MU[5.570 Municípios]

    ED --> CE[Constituições Estaduais<br/>27 registros]
    ED --> ICMS[Leis de ICMS<br/>12 registros]
    MU --> LOM[Leis Orgânicas Municipais<br/>27 capitais]
    MU --> LMP[Leis Municipais<br/>Paradigmáticas<br/>15 registros]

    classDef root fill:#7c3aed,color:#fff;
    classDef ente fill:#1e40af,color:#fff;
    classDef norma fill:#fef3c7,color:#78350f;
    class BR root;
    class UN,ED,MU ente;
    class CE,ICMS,LOM,LMP norma;
```

## 2. Distribuição geográfica — CEs por região

```mermaid
graph TB
    subgraph N[Norte 7]
        N1[AC] --- N2[AM] --- N3[AP] --- N4[PA] --- N5[RO] --- N6[RR] --- N7[TO]
    end
    subgraph NE[Nordeste 9]
        NE1[AL] --- NE2[BA] --- NE3[CE] --- NE4[MA] --- NE5[PB]
        NE6[PE] --- NE7[PI] --- NE8[RN] --- NE9[SE]
    end
    subgraph CO[Centro-Oeste 3 + DF]
        CO1[GO] --- CO2[MT] --- CO3[MS] --- CO4[DF<br/>LO 1993]
    end
    subgraph SE[Sudeste 4]
        SE1[ES] --- SE2[MG] --- SE3[RJ] --- SE4[SP]
    end
    subgraph SU[Sul 3]
        SU1[PR] --- SU2[RS] --- SU3[SC]
    end

    classDef ufN fill:#fde68a,color:#78350f;
    classDef ufNE fill:#fbcfe8,color:#831843;
    classDef ufCO fill:#bfdbfe,color:#1e3a8a;
    classDef ufSE fill:#bbf7d0,color:#14532d;
    classDef ufSU fill:#fecaca,color:#7f1d1d;
    class N1,N2,N3,N4,N5,N6,N7 ufN;
    class NE1,NE2,NE3,NE4,NE5,NE6,NE7,NE8,NE9 ufNE;
    class CO1,CO2,CO3,CO4 ufCO;
    class SE1,SE2,SE3,SE4 ufSE;
    class SU1,SU2,SU3 ufSU;
```

## 3. Capitais — Leis Orgânicas (27 registros)

```mermaid
graph LR
    LOM[Leis Orgânicas das Capitais]
    LOM --> N[Norte]
    LOM --> NE[Nordeste]
    LOM --> CO[Centro-Oeste]
    LOM --> SE[Sudeste]
    LOM --> SU[Sul]

    N --> N_C[Rio Branco · Manaus · Macapá<br/>Belém · Porto Velho · Boa Vista · Palmas]
    NE --> NE_C[Maceió · Salvador · Fortaleza<br/>São Luís · João Pessoa · Recife<br/>Teresina · Natal · Aracaju]
    CO --> CO_C[Goiânia · Cuiabá · Campo Grande<br/>+ Brasília LO/DF 1993]
    SE --> SE_C[Vitória · Belo Horizonte<br/>Rio de Janeiro · São Paulo]
    SU --> SU_C[Curitiba · Porto Alegre · Florianópolis]
```

## 4. ICMS estadual (12 leis catalogadas)

```mermaid
graph TD
    KAN[Lei Kandir<br/>LC 87/1996<br/>Federal]
    KAN --> SP[SP — Lei 6.374/1989]
    KAN --> RJ[RJ — Lei 2.657/1996]
    KAN --> MG[MG — Lei 6.763/1975]
    KAN --> RS[RS — Lei 8.820/1989]
    KAN --> PR[PR — Lei 11.580/1996]
    KAN --> SC[SC — Lei 10.297/1996]
    KAN --> BA[BA — Lei 7.014/1996]
    KAN --> PE[PE — Lei 15.730/2016]
    KAN --> CE[CE — Lei 12.670/1996]
    KAN --> GO[GO — Lei 11.651/1991]
    KAN --> DF[DF — Lei 1.254/1996]
    KAN --> ES[ES — Lei 7.000/2001]

    classDef fed fill:#1e40af,color:#fff;
    classDef est fill:#fef3c7,color:#78350f;
    class KAN fed;
    class SP,RJ,MG,RS,PR,SC,BA,PE,CE,GO,DF,ES est;
```

## 5. Leis municipais paradigmáticas (15 registros) — eixos temáticos

```mermaid
graph LR
    LMP[Leis Municipais Paradigmáticas]
    LMP --> URB[Urbanismo / Cidade]
    LMP --> AMB[Ambiental / Convivência]
    LMP --> TRIB[Tributária / Fiscal]
    LMP --> MOB[Mobilidade]

    URB --> U1[Lei Cidade Limpa<br/>São Paulo · Lei 14.223/2006]
    URB --> U2[Plano Diretor Estratégico<br/>São Paulo · Lei 16.050/2014]
    URB --> U3[Outorga Onerosa]
    URB --> U4[ZEIS — Zonas Especiais]
    URB --> U5[Plano Diretor RJ]

    AMB --> A1[Lei do Silêncio<br/>diversos municípios]
    AMB --> A2[Lei Antifumo]
    AMB --> A3[Lei dos Sacolas Verdes]

    TRIB --> T1[IPTU progressivo<br/>função social]
    TRIB --> T2[ITBI municipal]

    MOB --> M1[Lei do Carro Compartilhado]
    MOB --> M2[Faixa Azul / Faixa Exclusiva]
    MOB --> M3[Zona Maxima/Mínima de Operação]
```

## 6. Federação normativa — fluxo hierárquico

```mermaid
graph TD
    CF[CF/88<br/>art. 22-30] --> CE[Constituições<br/>Estaduais]
    CF --> LOM[Leis Orgânicas<br/>Municipais]
    CE --> LECT[Leis estaduais ordinárias]
    LOM --> LMUN[Leis municipais ordinárias]

    LECT --> ICMSL[Leis de ICMS]
    LECT --> ORGEST[Lei Orgânica do MP estadual]
    LECT --> CARR[Estatuto de Carreira]
    LMUN --> URBAN[Plano Diretor]
    LMUN --> CODMUN[Código Tributário Municipal]
    LMUN --> POSTURAS[Posturas / Silêncio / Antifumo]

    classDef fed fill:#7c3aed,color:#fff;
    classDef est fill:#1e40af,color:#fff;
    classDef mun fill:#10b981,color:#fff;
    classDef norma fill:#fef3c7,color:#78350f;
    class CF fed;
    class CE,LECT,ICMSL,ORGEST,CARR est;
    class LOM,LMUN,URBAN,CODMUN,POSTURAS mun;
```

## 7. Cobertura por categoria (81 normas)

```mermaid
pie title Legislação Local por categoria
    "Constituições Estaduais + DF" : 27
    "Leis Orgânicas das Capitais" : 27
    "Leis de ICMS estaduais" : 12
    "Leis Municipais Paradigmáticas" : 15
```

---

## Fonte de dados
- `legislacao_local/constituicoes_estaduais/constituicoes.jsonl` (27)
- `legislacao_local/leis_organicas_municipais/principais_capitais.jsonl` (27)
- `legislacao_local/legislacao_tributaria_estadual/icms_estados.jsonl` (12)
- `legislacao_local/legislacao_municipal_referencia/leis_municipais_paradigmaticas.jsonl` (15)

**Skill correspondente:** `skills/dossie-legislacao-br/SKILL.md`.
