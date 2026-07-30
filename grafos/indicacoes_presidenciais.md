# Grafo de Indicações Presidenciais — Tribunais Superiores

## Relação Presidente → Ministro

```mermaid
graph LR
    subgraph Presidentes
        Lula1[Lula - 1º mandato<br>2003-2006]
        Lula2[Lula - 2º mandato<br>2007-2010]
        Dilma1[Dilma - 1º mandato<br>2011-2014]
        Dilma2[Dilma - 2º mandato<br>2015-2016]
        Temer[Temer<br>2016-2018]
        Bolsonaro[Bolsonaro<br>2019-2022]
        Lula3[Lula - 3º mandato<br>2023-2026]
    end

    subgraph STF
        Barroso[Luís Roberto Barroso]
        Fachin[Edson Fachin]
        Gilmar[Gilmar Mendes]
        Carmen[Cármen Lúcia]
        Toffoli[Dias Toffoli]
        Fux[Luiz Fux]
        Moraes[Alexandre de Moraes]
        Nunes[Nunes Marques]
        Mendonca[André Mendonça]
        Zanin[Cristiano Zanin]
        Dino[Flávio Dino]
    end

    Lula1 --> Barroso
    Dilma1 --> Fachin
    Lula1 --> Toffoli
    Lula2 --> Carmen
    Lula2 --> Fux
    Temer --> Moraes
    Bolsonaro --> Nunes
    Bolsonaro --> Mendonca
    Lula3 --> Zanin
    Lula3 --> Dino
```

## Tabela Detalhada — STF

| Ministro | Indicado por | Ano de Posse | Vaga de |
|---|---|---|---|
| Gilmar Mendes | FHC | 2002 | Néri da Silveira |
| Cármen Lúcia | Lula | 2006 | Nelson Jobim |
| Dias Toffoli | Lula | 2009 | Carlos Alberto Menezes Direito |
| Luiz Fux | Dilma | 2011 | Eros Grau |
| Luís Roberto Barroso | Dilma | 2013 | Ayres Britto |
| Edson Fachin | Dilma | 2015 | Joaquim Barbosa |
| Alexandre de Moraes | Temer | 2017 | Teori Zavascki |
| Nunes Marques | Bolsonaro | 2020 | Celso de Mello |
| André Mendonça | Bolsonaro | 2021 | Marco Aurélio |
| Cristiano Zanin | Lula | 2023 | Ricardo Lewandowski |
| Flávio Dino | Lula | 2023 | Rosa Weber |

## Nós Relacionados
- [Hierarquia do Judiciário](./hierarquia_judiciario.md)
- [STF - Detalhes](../tribunais_superiores/stf/README.md)
- [Especialidades Jurídicas](./especialidades_juridicas.md)
