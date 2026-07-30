# Grafo da Carreira da Magistratura no Brasil

## Progressão na Carreira

```mermaid
graph BT
    subgraph Justica_Estadual[Justiça Estadual]
        JD_Sub[Juiz Substituto<br>Entrada por concurso]
        JD_Tit[Juiz Titular<br>Entrância inicial]
        JD_Ent[Juiz de Entrância<br>Intermediária/Final]
        Des[Desembargador<br>Tribunal de Justiça]

        JD_Sub --> JD_Tit
        JD_Tit --> JD_Ent
        JD_Ent --> |"Merecimento ou<br>Antiguidade"| Des
    end

    subgraph Justica_Federal[Justiça Federal]
        JF_Sub[Juiz Federal Substituto<br>Entrada por concurso]
        JF_Tit[Juiz Federal Titular]
        Des_Fed[Desembargador Federal<br>TRF]

        JF_Sub --> JF_Tit
        JF_Tit --> |"Merecimento ou<br>Antiguidade"| Des_Fed
    end

    subgraph Justica_Trabalho[Justiça do Trabalho]
        JT_Sub[Juiz do Trabalho Substituto<br>Entrada por concurso]
        JT_Tit[Juiz do Trabalho Titular]
        Des_Trab[Desembargador do Trabalho<br>TRT]

        JT_Sub --> JT_Tit
        JT_Tit --> |"Merecimento ou<br>Antiguidade"| Des_Trab
    end

    subgraph Tribunais_Superiores[Tribunais Superiores]
        Min_STJ[Ministro do STJ]
        Min_TST[Ministro do TST]
        Min_STF[Ministro do STF]

        Des --> |"1/3 das vagas"| Min_STJ
        Des_Fed --> |"1/3 das vagas"| Min_STJ
        Des_Trab --> |"4/5 das vagas"| Min_TST
    end

    subgraph Quinto_Constitucional[Quinto Constitucional]
        Adv[Advogado<br>10+ anos OAB]
        MP[Membro do MP<br>10+ anos carreira]

        Adv --> |"1/5 das vagas"| Des
        Adv --> |"1/5 das vagas"| Des_Fed
        Adv --> |"1/5 das vagas"| Des_Trab
        MP --> |"1/5 das vagas"| Des
        MP --> |"1/5 das vagas"| Des_Fed
        MP --> |"1/5 das vagas"| Des_Trab

        Adv --> |"1/3 das vagas"| Min_STJ
        MP --> |"1/3 das vagas"| Min_STJ
        Adv --> |"1/5 das vagas"| Min_TST
    end
```

## Requisitos para Ingresso

### Juiz Substituto (1ª instância)
- Bacharelado em Direito
- 3 anos de atividade jurídica (mínimo)
- Aprovação em concurso público de provas e títulos
- Etapas: prova objetiva, prova discursiva, prova oral, títulos, investigação social

### Desembargador (2ª instância)
- **Por antiguidade**: critério objetivo, o juiz mais antigo na lista
- **Por merecimento**: avaliação de produtividade, presteza, qualidade das decisões
- **Quinto constitucional**: 1/5 das vagas reservadas a advogados e membros do MP

### Ministro (Tribunais Superiores)
- Indicação do Presidente da República
- Aprovação pelo Senado Federal (maioria absoluta para STF)
- Requisitos variam conforme o tribunal

## Garantias Constitucionais

| Garantia | Descrição |
|----------|-----------|
| Vitaliciedade | Após 2 anos, só perde cargo por sentença judicial transitada em julgado |
| Inamovibilidade | Não pode ser removido contra a vontade (salvo interesse público) |
| Irredutibilidade de subsídios | Remuneração não pode ser reduzida |

## Vedações Constitucionais

- Exercer outro cargo (exceto magistério)
- Receber custas ou participação em processos
- Dedicar-se a atividade político-partidária
- Exercer advocacia no juízo de origem (quarentena de 3 anos)

## Aposentadoria

| Modalidade | Requisito |
|------------|-----------|
| Compulsória | 75 anos de idade |
| Voluntária | 62 anos (mulher) / 65 anos (homem) + 25 anos de serviço público |

## Nós Relacionados
- [Hierarquia do Judiciário](./hierarquia_judiciario.md)
- [Estatísticas](./estatisticas_judiciario.md)
- [Indicações Presidenciais](./indicacoes_presidenciais.md)
