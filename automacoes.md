# Automações

O que está ligado neste projeto, o que roda e quando. Criado em 21/09/2026: eu não tinha este arquivo desde a aula 9, então ele nasce aqui com a rotina das aulas 11 a 14.

## Regras ligadas

- Arquivo das regras: `regras.md` (3 regras: sintoma intenso em D-1, participante parou de registrar, escalonamento falhou)
- Fonte que elas leem: `dados/amostra.csv` (inventado, declarado em `dados/fonte.md`)
- Como roda: **à mão, no Claude**, toda segunda de manhã depois de eu atualizar a fonte. A Regra 1 e a Regra 3 estão escritas para rodar todo dia às 8h, mas enquanto o piloto não começa eu rodo as três juntas na segunda.
- **Status: rodada à mão (a função de agendar não está disponível na minha conta).**

## Rotina · Checagem do piloto

- **Nome:** Checagem do piloto
- **Horário previsto:** todo dia às 8h (Regras 1 e 3) e toda segunda às 9h (Regra 2). Hoje: à mão, toda segunda.
- **Onde roda:** Claude, na pasta do repositório, lendo `regras.md` e `dados/amostra.csv`. Para a contagem ser exata e repetível, a checagem usa o script `rotina.py` (na raiz), que aplica literalmente as condições do `regras.md`. Rodar: `python rotina.py . AAAA-MM-DD`, onde a data é o dia da execução.
- **Condição que ela checa:** as três do `regras.md`. Regra 1: algum registro de D-1 com `intensidade >= 7` ou `duracao_horas > 24`. Regra 2: algum participante com último registro há mais de 7 dias. Regra 3: algum registro intenso de D-1 sem `orientacao_dada = fale com seu medico agora`.
- **Saída:** o alerta em `alertas/AAAA-MM-DD.md` quando dispara; uma linha na tabela de execuções abaixo sempre, disparando ou não.

### O prompt que ela roda (colado inteiro)

```
Leia o regras.md e o dados/fonte.md desta pasta. Depois abra o dados/amostra.csv
e aplique as três regras do regras.md com a data de execução de hoje.

Antes de qualquer conta: se o dados/amostra.csv não existir ou vier vazio,
escreva "FONTE INDISPONÍVEL" e pare. Nunca invente número. Me diga quantas
linhas leu e quantas ignorou, e por quê (data fora de AAAA-MM-DD, intensidade
fora de 0 a 10, duração negativa ou vazia). Se uma linha ignorada puder ser de
ontem, escreva "REGISTRO ILEGÍVEL" com o conteúdo bruto dela e trate como alerta.

Para cada regra me diga: disparou ou não, e qual foi o número que decidiu.
Se disparou, escreva o alerta pronto em alertas/AAAA-MM-DD.md, com participante,
medicamento, dose, sintoma, intensidade, duração e orientação dada, sem JSON.
Se não disparou, escreva a linha do campo "Se não disparar" da regra.
Use o rotina.py para a contagem: python rotina.py . AAAA-MM-DD.
```

### Evidência de execução

**Execução 1 · 21/09/2026 às 19:48 · data de execução 21/09 (D-1 = 20/09)**

Resultado devolvido:

```
Execução em 21/09/2026. Linhas lidas: 19. Ignoradas: 0.

Regra 1 · Sintoma intenso em D-1 (2026-09-20): DISPAROU. 1 registro(s):
  - USR-002 · Wegovy 0.5 mg · vomito · intensidade 8/10 · dura 3h · orientação dada: fale com seu medico agora

Regra 2 · Participante parou de registrar: DISPAROU. 1 participante(s):
  - USR-003 · último registro em 10/09 · há 11 dias

Regra 3 · Escalonamento falhou: não disparou. 1 registro(s) intenso(s) em D-1 olhado(s); 100% receberam 'fale com seu medico agora'.
```

Alerta gerado: `alertas/2026-09-21.md`.

**Execução 2 · 21/09/2026 às 19:48 · data de execução 14/09 (D-1 = 13/09), para ver a rotina calada**

Rodada no mesmo momento, com a data de referência de uma semana antes, sobre o mesmo arquivo. Resultado devolvido:

```
Execução em 14/09/2026. Linhas lidas: 19. Ignoradas: 0.

Regra 1 · Sintoma intenso em D-1 (2026-09-13): não disparou. 1 registro(s) de D-1 olhados, maior intensidade: 3.

Regra 2 · Participante parou de registrar: não disparou. 3 participantes olhados, último registro mais antigo: 2026-09-10.

Regra 3 · Escalonamento falhou: não disparou. 0 registro(s) intenso(s) em D-1 olhado(s); 100% receberam 'fale com seu medico agora'.
```

Nada a reportar. Nenhum alerta gerado.

### Execuções

| Data e hora da execução | Data de referência | Regra | Fonte | Linhas lidas / ignoradas | Disparou? | Número que decidiu |
|---|---|---|---|---|---|---|
| 21/09/2026 19:48 | 21/09 (D-1 = 20/09) | 1 · Sintoma intenso | dados/amostra.csv | 19 / 0 | sim | USR-002, vômito, intensidade 8 |
| 21/09/2026 19:48 | 21/09 | 2 · Participante parou | dados/amostra.csv | 19 / 0 | sim | USR-003, 11 dias sem registro |
| 21/09/2026 19:48 | 21/09 (D-1 = 20/09) | 3 · Escalonamento falhou | dados/amostra.csv | 19 / 0 | não | 1 registro intenso, 100% escalado |
| 21/09/2026 19:48 | 14/09 (D-1 = 13/09) | 1 · Sintoma intenso | dados/amostra.csv | 19 / 0 | não | maior intensidade em 13/09: 3 |
| 21/09/2026 19:48 | 14/09 | 2 · Participante parou | dados/amostra.csv | 19 / 0 | não | registro mais antigo: 10/09 (4 dias) |
| 21/09/2026 19:48 | 14/09 (D-1 = 13/09) | 3 · Escalonamento falhou | dados/amostra.csv | 19 / 0 | não | 0 registros intensos em 13/09 |

As execuções dos testes de falha (fonte renomeada, dado sujo, regra forçada) estão no `testes.md`, com hora.

## Painel

Não fiz o `painel.html` da aula 12. Os 3 números que ele mostraria estão definidos com regra de cálculo no `dados/fonte.md`; o painel fica para a próxima semana e não vale ponto na NP2.

## O que aprendi

- A rotina calada e a rotina quebrada são iguais vistas de fora. O campo "Se não disparar" e a coluna "Linhas lidas / ignoradas" são o que separa uma da outra.
- Enquanto o dado é inventado, a rotina só prova que a regra funciona. O que ela não prova é que os limites 7 e 24h são os certos para uma pessoa real; isso continua dependendo de validação com um profissional de saúde.
