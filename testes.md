# Testes de falha

Testado em 21/09/2026, entre 19:48 e 19:49, sobre a rotina "Checagem do piloto" (`automacoes.md`), as regras do `regras.md` e a fonte `dados/amostra.csv` (inventada, ver `dados/fonte.md`). Cada teste foi provocado de propósito e a fonte foi restaurada ao final (conferi que o arquivo voltou idêntico ao original).

## Cenário 1 · A fonte saiu do ar

**O que eu testei:** renomeei `dados/amostra.csv` para `dados/amostra_OLD.csv` e rodei a rotina duas vezes: uma com o `regras.md` sem a instrução de falha (o estado "antes"), outra com a instrução.

**O que aconteceu:**

Antes (sem a instrução): a rotina não achou o arquivo e seguiu com o que tinha. Devolveu isto:

```
Fonte nao encontrada em dados/amostra.csv.
Regra 1: nao disparou, 0 registros olhados. Regra 2: nao disparou, 0 participantes. Regra 3: nao disparou.
```

Três "não disparou" com cara de dia normal. Se isso chegasse na segunda de manhã, eu leria como "está tudo bem no piloto" e o arquivo simplesmente não existia.

Depois (com a instrução no `regras.md`):

```
FONTE INDISPONÍVEL: dados/amostra.csv não existe. Parei. Nada foi estimado.
```

**O que eu consertei:** acrescentei ao `regras.md` a seção "Instrução de falha": se a fonte não existir ou vier vazia, escrever "FONTE INDISPONÍVEL" e parar; nunca inventar número; sempre dizer quantas linhas leu e quantas ignorou. A mesma frase entrou no prompt da rotina, no `automacoes.md`. Plano B: se um dia a rotina devolver "FONTE INDISPONÍVEL", eu abro o `dados/amostra.csv` à mão e refaço a exportação do formulário antes de rodar de novo.

## Cenário 2 · Chegou dado inesperado

**O que eu testei:** devolvi o nome da fonte e estraguei 3 linhas de propósito: a linha 5 ficou com `intensidade` vazia, a linha 11 ficou com `intensidade = -3`, e a linha 19 (justamente o registro de vômito 8/10 de 20/09, o que faz a Regra 1 disparar) ficou com a data em outro formato: `20/09/2026` em vez de `2026-09-20`. Rodei a rotina com data de execução 21/09.

**O que aconteceu:** a rotina avisou que ignorou as 3 linhas, com o motivo de cada uma, e não inventou nenhum número:

```
Execução em 21/09/2026. Linhas lidas: 19. Ignoradas: 3.
  - linha 5 ignorada: intensidade '' não é inteiro
  - linha 11 ignorada: intensidade -3 fora de 0 a 10
  - linha 19 ignorada: data '20/09/2026' fora do formato AAAA-MM-DD

Regra 1 · Sintoma intenso em D-1 (2026-09-20): não disparou. 1 registro(s) de D-1 olhados, maior intensidade: 0.
```

O problema real apareceu aqui: a Regra 1 ficou **calada**. O registro intenso existia, mas com a data ilegível ele saiu da conta, e o resultado foi "maior intensidade: 0". Ou seja, a rotina fez o que eu mandei (ignorar linha suja e avisar), e mesmo assim eu perderia o sintoma mais importante do dia se não lesse a lista de ignoradas com atenção.

**O que eu consertei:** acrescentei ao `regras.md` (Instrução de falha) que uma linha ignorada com data igual a D-1 ou com data ilegível não pode deixar a Regra 1 calada: a rotina escreve "REGISTRO ILEGÍVEL" com o conteúdo bruto da linha e trata como alerta para eu conferir à mão. Rodei de novo com as mesmas 3 linhas estragadas:

```
Regra 1 · Sintoma intenso em D-1 (2026-09-20): REGISTRO ILEGÍVEL. 1 linha(s) que podem ser de D-1 não puderam ser lidas; trato como alerta para eu conferir à mão:
  - linha 19: data '20/09/2026' fora do formato AAAA-MM-DD · conteúdo bruto: 20/09/2026,08:40,USR-002,Wegovy,0.5,4,vomito,8,3,fale com seu medico agora
```

Agora ela acusa. Depois restaurei a fonte original e conferi que a execução normal voltou a disparar a Regra 1 com o USR-002.

## Cenário 3 · A condição nunca dispara

**O que eu testei:** a Regra 3 (escalonamento falhou) nunca disparou nas execuções registradas no `automacoes.md`, e, pelo desenho, ela **não deve** disparar nunca: ela só acende quando o produto responde "continue monitorando" a um sintoma com intensidade 7 ou mais, ou que dura mais de 24h, e a regra de escalonamento da V3 do `prompts.md` proíbe exatamente isso. Então "calada" pode ser "o produto está escalando certo" ou "a regra está quebrada e não enxerga a falha". De fora, é igual.

Para diferenciar, forcei o dado: troquei, no registro de vômito 8/10 do USR-002 em 20/09, a `orientacao_dada` de `fale com seu medico agora` para `continue monitorando`, e rodei a rotina.

**O que aconteceu:** a Regra 3 disparou na hora, com o registro certo:

```
Regra 3 · Escalonamento falhou: DISPAROU. 1 registro(s):
  - USR-002 · vomito · intensidade 8/10 · dura 3h · orientação dada: 'continue monitorando'. O produto respondeu 'continue monitorando' a um sintoma que devia escalar.
```

Depois desfiz a troca e a Regra 3 voltou a ficar calada com "1 registro intenso olhado; 100% receberam 'fale com seu medico agora'".

**O que eu consertei / plano B:** a regra não estava quebrada, e agora eu sei disso porque a forcei uma vez. Para não depender da memória, ficou combinado: (1) o campo "Se não disparar" da Regra 3 sempre grava quantos registros intensos foram olhados, então "calada com 0 intensos olhados" e "calada com 3 intensos olhados, 100% escalados" são leituras diferentes; (2) uma vez por mês, na primeira segunda, eu repito este teste forçado e anoto a data no `automacoes.md`. Se um dia a regra forçada não disparar, aí sim ela quebrou.

## O que os três testes me ensinaram

O conserto nos três casos foi uma frase de instrução, não código. O que muda o comportamento da rotina é ela ser obrigada a dizer o que não conseguiu ler, e eu ser obrigado a tratar "não consegui ler" como alerta, não como silêncio.
