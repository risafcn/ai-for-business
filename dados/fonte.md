# Fonte canônica

Declarada em 21/09/2026 (aula 12). Este arquivo diz de onde vem o dado em que as regras do `regras.md` confiam.

## A situação honesta

O produto ainda não existe e eu ainda não tenho acesso a um paciente real em tratamento com Mounjaro, Wegovy ou Ozempic (ver `problema.md`, seção "Como eu tenho acesso"). Então **não existe dado real de operação hoje**.

Escolhi o caminho 3 do enunciado da NP2: **um CSV com dados inventados, declarados como inventados**. Ele simula o que o piloto vai coletar quando eu tiver os primeiros participantes: cada linha é um registro de sintoma feito por um participante, do jeito que o formulário do piloto vai pedir. Os números, datas, participantes e sintomas foram escritos por mim para testar as regras, e não representam nenhuma pessoa.

Quando o piloto começar, este arquivo continua sendo a fonte canônica, mas passa a ser alimentado pela exportação do formulário, e a amostra inventada sai.

## 1. Qual é a fonte

Um CSV no repositório: `dados/amostra.csv`. Uma linha por registro de sintoma.

Fonte de treino (inventada) enquanto eu não tenho participantes. A fonte real vai ser a exportação do formulário do piloto (Google Forms → Sheets), que eu ainda não criei.

## 2. Onde ela vive

`dados/amostra.csv`, nesta pasta, versionado no Git. Quando duas contas discordarem, vale o que está neste arquivo, no commit mais recente da branch `main`.

## 3. Quem atualiza e com que frequência

- **Quem:** eu (Henrique). Ninguém mais escreve neste arquivo.
- **Hoje:** à mão, quando eu preciso testar uma regra.
- **No piloto:** toda segunda de manhã eu exporto o formulário da semana e faço commit por cima, antes de rodar a rotina das 9h.
- **Como eu percebo que ela está desatualizada:** a data do último registro está a mais de 7 dias de hoje. A Regra 2 do `regras.md` usa exatamente isso.

## 4. Campos, e quais importam para as regras

| Campo | O que é | Usado em |
|---|---|---|
| `data` | Dia do registro, formato AAAA-MM-DD | Regras 1, 2 e 3 |
| `hora` | Hora do registro, HH:MM | Só para o histórico |
| `participante` | Identificador do participante do piloto (USR-001, USR-002...). Nunca nome, telefone ou e-mail | Regra 2 |
| `medicamento` | Mounjaro, Wegovy ou Ozempic | Só para o histórico e o resumo da consulta |
| `dose_mg` | Dose em uso na semana, em mg | Só para o histórico |
| `dias_desde_aplicacao` | Quantos dias se passaram desde a última aplicação (0 = dia da aplicação) | Só para o histórico |
| `sintoma` | nausea, vomito, constipacao, azia, indisposicao, fadiga ou nenhum | Regras 1 e 3 |
| `intensidade` | De 0 a 10, informada pelo participante | Regras 1 e 3 |
| `duracao_horas` | Há quantas horas o sintoma dura no momento do registro | Regras 1 e 3 |
| `orientacao_dada` | O que o produto respondeu: `continue monitorando` ou `fale com seu medico agora` | Regra 3 |

## Regra de sanitização

Nada de nome, telefone, e-mail ou documento entra neste arquivo. Cada participante recebe um identificador sequencial (USR-001, USR-002...), sempre o mesmo para a mesma pessoa. A tabela que liga o identificador à pessoa fica fora do repositório.

## Os 3 números que eu olho (aula 12)

| Tipo | Número | Regra de cálculo |
|---|---|---|
| Volume | Registros de sintoma na semana | Conta as linhas com `data` dentro da semana (segunda a domingo). Linha com `sintoma = nenhum` conta, porque o participante abriu o app e registrou |
| Dinheiro | Receita no mês | **Zero, e declaro zero.** O produto não vende. Quando houver assinatura, será a soma das mensalidades pagas no mês |
| Qualidade | % de registros intensos que receberam "fale com seu medico agora" | Registros com `intensidade >= 7` ou `duracao_horas > 24` que têm `orientacao_dada = fale com seu medico agora`, dividido pelo total de registros com `intensidade >= 7` ou `duracao_horas > 24`. Deve ser 100% sempre; qualquer coisa abaixo é falha do produto (ver Regra 3) |

Os limites 7 e 24h vêm da regra de escalonamento da V3 do `prompts.md`: intensidade de 7 a 10, ou sintoma que já dura mais de 24h, sempre orienta a falar com o médico.

## Outro arquivo nesta pasta

`dados/conversas.csv` é a série da métrica do `problema.md` (conversas com usuários reais). Está vazio, só com o cabeçalho, porque em 21/09 eu ainda não tive nenhuma conversa. Ele não é fonte das regras; a fonte canônica da operação continua sendo o `amostra.csv`.

## O que ainda falta definir

- Criar o formulário real do piloto e conferir se os campos acima são os que o participante consegue preencher em menos de 1 minuto.
- Validar os limites 7 e 24h com um profissional de saúde antes de qualquer uso com pessoa real (compromisso do `problema.md`, pergunta 2 do leitor cético).
