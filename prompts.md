# Biblioteca de prompts

## Mensagem de orientação após registro de sintoma
Atualizado em: 27/08/2026

Esta é a tarefa que mais importa no projeto agora: é o núcleo do produto (o app conversando com o usuário logo depois que ele registra um sintoma), e ainda não tinha rodado o experimento da semana, então uso esta como a primeira do plano.

### V1 — sem técnica nenhuma
**Prompt:**
"Me ajuda a criar uma mensagem pro app responder quando o usuário registra que está com náusea depois de tomar a caneta emagrecedora."

**Resposta:**
"Olá! Notamos que você está sentindo náusea. Isso é super comum em quem usa Ozempic, Mounjaro ou Wegovy! Tente comer porções menores, evitar frituras, beber bastante água e descansar. Se o incômodo continuar, procure seu médico. Estamos aqui pra te apoiar na sua jornada de emagrecimento!"

**Problema:** tom de vendedor, genérico, não pergunta nem usa a intensidade do sintoma, não referencia o histórico que o usuário acabou de registrar, e "jornada de emagrecimento" soa como propaganda, não como cuidado de saúde — o oposto do que negocio.md pede.

### V2 — briefing completo (Tarefa, Formato, Amostra, Limite)
**Prompt:**
"Você é um redator de comunicação de saúde digital, que escreve para pacientes que podem estar ansiosos, sem soar alarmista nem clínico demais.

TAREFA: escreva a mensagem automática que o app envia logo depois que o usuário registra um sintoma (ex: náusea, intensidade 6/10, no dia seguinte à aplicação da dose).
FORMATO: no máximo 4 frases curtas, tom acolhedor e direto, sem emoji, terminando com uma orientação clara do próximo passo.
AMOSTRA: sem exemplo real ainda — na ausência dele, escreva no tom de 'uma enfermeira de confiança explicando com calma', não de vendedor.
LIMITE: nunca diga se o sintoma é normal ou perigoso, nunca sugira mudar a dose, nunca substitua orientação médica. Termine sempre indicando 'continue monitorando' ou 'fale com seu médico', nunca um diagnóstico."

**Resposta:**
"Registramos sua náusea (intensidade 6/10) de hoje. Isso costuma acontecer nos primeiros dias após a aplicação, então vale continuar monitorando por enquanto: hidrate-se bem e evite refeições muito gordurosas nas próximas horas. Se a náusea piorar, durar mais de 24 horas ou vier acompanhada de outros sintomas, fale com seu médico. Vamos guardar esse registro para você mostrar na sua próxima consulta."

**O que mudou da V1 pra V2:** saiu o tom de vendedor; entrou a referência à intensidade registrada, um critério explícito de quando escalar para o médico, e a menção ao histórico guardado — que é o valor real do produto.

### V3 — reescrita pela IA (meta-prompt)
**Prompt (meta-prompt):**
"Este é um pedido que eu vou usar toda semana: [colei o prompt da V2 aqui]. Critique como um revisor exigente: o que está ambíguo, o que falta, o que sobra? Depois reescreva na melhor versão possível."

**Crítica que veio:**
1. Falta uma regra para quando a intensidade é alta (ex: 9/10) — a mensagem não pode dar a mesma resposta "continue monitorando" para intensidade 3 e para intensidade 9.
2. "Sem exemplo real ainda" é uma instrução vazia dentro do prompt — é informação para mim, não para a IA; melhor tirar.
3. Falta um limite pensando em notificação push (caracteres), não só "4 frases".
4. O prompt não diz o que fazer se o sintoma já dura mais de um dia — só a intensidade não é suficiente como gatilho.

**Prompt V3 (reescrito):**
"Você é um redator de comunicação de saúde digital, tom de enfermeira de confiança: calma, direta, sem soar alarmista nem vendedor.

TAREFA: escreva a mensagem automática que o app envia após o usuário registrar um sintoma com [nome do sintoma] e [intensidade de 0 a 10].
FORMATO: no máximo 300 caracteres, 2 a 4 frases curtas, sem emoji, terminando sempre com uma destas duas ações: 'continue monitorando' ou 'fale com seu médico agora' — nunca as duas juntas, nunca nenhuma diagnose.
REGRA DE ESCALONAMENTO: intensidade de 0 a 6 → 'continue monitorando' + uma dica simples e segura (hidratação, alimentação leve, descanso). Intensidade 7 a 10, ou sintoma que já dura mais de 24h → 'fale com seu médico agora', sem sugerir nenhuma dica antes.
LIMITE: nunca diga se o sintoma é normal ou perigoso, nunca sugira mudar dose, nunca substitua orientação médica."

**Resposta (náusea, intensidade 6/10):**
"Registramos sua náusea (6/10) de hoje. Nessa intensidade, vale continuar monitorando: hidrate-se bem e evite refeições gordurosas nas próximas horas. Guardamos esse registro para sua próxima consulta."

**Resposta (náusea, intensidade 9/10):**
"Registramos sua náusea (9/10) de hoje. Nessa intensidade, o ideal é falar com seu médico agora. Guardamos esse registro para você mostrar a ele."

### Vencedora e por quê
A V3 venceu. Justificativa em uma linha: a V2 tinha um bom tom, mas só a V3 tem uma regra de escalonamento explícita por intensidade — sem isso, o produto daria a mesma resposta para um sintoma leve e para um grave, que é o principal risco do negócio.

### O que aprendi
A amostra (técnica 1) importou menos do que eu esperava: o que realmente mudou a qualidade da resposta foi transformar uma regra de negócio implícita ("nunca dizer se é perigoso") em uma regra operacional explícita ("intensidade X faz Y"). Prompt bom, para este produto, é menos sobre estilo de escrita e mais sobre traduzir a regra de risco em instrução que a IA não pode ignorar.
