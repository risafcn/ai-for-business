# Regras da operação

Regras do piloto de acompanhamento de efeitos colaterais para usuários de Mounjaro, Wegovy e Ozempic. Escritas em 21/09/2026 (aula 11). Todas leem a mesma fonte: `dados/amostra.csv` (ver `dados/fonte.md`).

Os números das condições (intensidade 7, duração 24h) vêm da regra de escalonamento da V3 do `prompts.md`, que é a regra de risco do produto. Os 7 dias da Regra 2 vêm do ciclo semanal das três medicações (uma aplicação por semana): um participante que passou uma aplicação inteira sem registrar nada saiu do acompanhamento.

Nenhuma regra decide nada clínico. Elas avisam a mim, o fundador, para eu agir na operação do piloto. Quem decide sobre dose, diagnóstico ou tratamento é o médico do participante.

## Instrução de falha (vale para todas as regras)

Se a fonte `dados/amostra.csv` não existir ou vier vazia, escreva "FONTE INDISPONÍVEL" e pare. Nunca invente número. Sempre me diga quantas linhas leu e quantas ignorou, e por quê. Uma linha é ignorada quando `data` não está no formato AAAA-MM-DD, quando `intensidade` não é um inteiro de 0 a 10, ou quando `duracao_horas` é negativa ou vazia; linha ignorada é listada no resultado com o motivo.

Acrescentado depois do teste 2 do `testes.md` (21/09): se uma linha ignorada tiver `data` = D-1 ou uma data que não dá para ler, a Regra 1 não pode ficar calada. Escreva "REGISTRO ILEGÍVEL" com o conteúdo bruto da linha e trate como alerta, porque pode ser um sintoma intenso que eu não vi.

## Regra 1 · Sintoma intenso registrado no dia anterior

- **Nome:** Sintoma intenso registrado no dia anterior
- **Gatilho:** tempo. Todo dia às 8h.
- **Fonte:** `dados/amostra.csv`, linhas com `data` = ontem (D-1).
- **Condição:** existe pelo menos 1 registro em D-1 com `intensidade >= 7` OU `duracao_horas > 24`.
- **Ação:** escrever um alerta em `alertas/AAAA-MM-DD.md` com, para cada registro: participante, medicamento, dose, sintoma, intensidade, duração e a orientação que o produto deu.
- **Quem recebe:** eu (Henrique). Nos 10 minutos seguintes eu mando uma mensagem ao participante confirmando que ele viu a orientação "fale com seu medico agora" e pergunto se conseguiu falar com o médico. Se não conseguiu, eu anoto no histórico dele para a próxima consulta.
- **Se não disparar:** gravar no `automacoes.md` a data, quantas linhas de D-1 foram lidas e a maior intensidade encontrada.

## Regra 2 · Participante parou de registrar

- **Nome:** Participante parou de registrar
- **Gatilho:** tempo. Toda segunda às 9h, depois de eu atualizar a fonte.
- **Fonte:** `dados/amostra.csv`, a data do último registro de cada `participante`.
- **Condição:** existe pelo menos 1 participante cujo último registro tem mais de 7 dias (contando até a data da execução).
- **Ação:** escrever um alerta em `alertas/AAAA-MM-DD.md` listando cada participante parado, a data do último registro e há quantos dias.
- **Quem recebe:** eu (Henrique). Nos 10 minutos seguintes eu mando uma mensagem curta ao participante perguntando se ele quer continuar no piloto e o que atrapalhou registrar (o `contexto/cliente.md` lista os motivos prováveis: registrar é complicado, resposta genérica, não percebeu benefício). A resposta vai para o `contexto/cliente.md`.
- **Se não disparar:** gravar no `automacoes.md` a data, quantos participantes foram olhados e a data do registro mais antigo entre os "últimos registros".

## Regra 3 · Escalonamento falhou

- **Nome:** Escalonamento falhou
- **Gatilho:** tempo. Todo dia às 8h, junto com a Regra 1.
- **Fonte:** `dados/amostra.csv`, linhas com `data` = ontem (D-1).
- **Condição:** existe pelo menos 1 registro em D-1 com `intensidade >= 7` OU `duracao_horas > 24` cuja `orientacao_dada` é diferente de `fale com seu medico agora`.
- **Ação:** escrever um alerta em `alertas/AAAA-MM-DD.md` com o registro completo e a frase "o produto respondeu 'continue monitorando' a um sintoma que devia escalar".
- **Quem recebe:** eu (Henrique). Nos 10 minutos seguintes eu paro o envio automático de orientações do piloto, mando ao participante a orientação correta à mão e abro uma correção no `prompts.md` (a regra de escalonamento da V3 quebrou).
- **Se não disparar:** gravar no `automacoes.md` a data, quantos registros intensos foram olhados e que 100% deles receberam "fale com seu medico agora". Esta regra deve ficar calada sempre; ela existe para pegar o dia em que o produto falhar. Como distinguir "calada porque está tudo bem" de "calada porque quebrou" está no `testes.md`, cenário 3.
