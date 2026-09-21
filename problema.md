# Acompanhamento de efeitos colaterais para usuários de medicamentos GLP-1 (Mounjaro, Wegovy, Ozempic)

## Quem sofre
Persona de trabalho (ainda não é uma pessoa real que eu já entrevistei — ver seção "Como eu tenho acesso"): "Maria", 42 anos, empresária, faz tratamento com Mounjaro sob acompanhamento médico para perda de peso.

Quando aumenta a dose, apresenta náusea, indisposição e alterações intestinais, e não sabe se deve apenas aguardar, mudar a alimentação, conversar com o médico ou procurar atendimento.

## Como é hoje
Hoje, quando apresenta algum sintoma, ela normalmente pesquisa no Google, procura relatos em redes sociais, pergunta para amigos que também usam o medicamento ou manda mensagem para o médico/nutricionista.

O processo leva de alguns minutos a várias horas e frequentemente gera informações contraditórias. Ela pode não saber diferenciar um efeito colateral comum de um sinal que merece avaliação profissional. Quando finalmente conversa com o médico, muitas vezes não tem um histórico organizado de quando os sintomas começaram, qual dose estava usando, o que comeu ou como o sintoma evoluiu.

## O que mudaria
Reduzir para menos de 5 minutos o tempo entre registrar o sintoma e receber uma orientação inicial sobre o próximo passo, além de manter 100% do histórico de sintomas, doses e evolução organizado para apresentar ao profissional de saúde.

Métricas de acompanhamento: redução de mensagens desnecessárias ao médico, percentual de sintomas registrados, tempo entre o sintoma e a orientação, número de usuários que mantêm o acompanhamento ao longo do tratamento.

## Como eu tenho acesso
Hoje não tenho acesso direto a um paciente real em tratamento com essas medicações — este é um ponto em aberto do projeto, e estou registrando isso em vez de esconder.

O plano é conseguir os primeiros contatos através de comunidades online de pacientes (grupos de Facebook, Reddit, fóruns sobre Mounjaro/Wegovy/Ozempic) e, se possível, através de um médico ou nutricionista disposto a indicar pacientes para uma conversa curta.

Até validar isso, a "Maria" usada acima é uma persona de trabalho, construída a partir de relatos públicos comuns sobre o tema — não uma pessoa real que eu já conheço.

## Por que eu escolhi
Escolhi esse problema porque percebi que o uso das canetas emagrecedoras aumentou muito e existe uma dificuldade prática durante o tratamento: entre uma consulta e outra, o paciente frequentemente fica sozinho para lidar com os efeitos colaterais. É um problema recorrente, fácil de observar e que permite testar uma solução com usuários reais assim que eu conseguir acesso a eles.

## O resultado que eu quero
Reduzir para menos de 5 minutos o tempo entre o usuário registrar um sintoma e receber uma orientação inicial sobre o próximo passo (monitorar, ajustar algo simples, ou procurar o médico).

Manter 100% do histórico de sintomas, doses e evolução organizado e pronto para ser mostrado ao profissional de saúde na consulta seguinte.

Prazo: ter uma primeira versão testável (mesmo que manual, tipo formulário) até outubro, com essas métricas medidas num piloto pequeno.

## Métrica

Atualizado em 21/09/2026 (aula 13).

As métricas do produto que eu listei acima (tempo até a orientação, % do histórico organizado, mensagens ao médico evitadas) ainda não dão para medir: não existe produto nem participante. O número que mais dói hoje é outro, e vem do "Primeiro experimento" logo abaixo: **eu ainda não conversei com nenhum usuário real dessas medicações.** Sem isso, o problema inteiro é hipótese. Então a métrica desta fase é a da validação, e as do produto ficam para quando o piloto existir (NP3).

| Métrica | Alvo | Como confiro |
|---|---|---|
| Conversas com usuários reais de Mounjaro, Wegovy ou Ozempic sobre o que fazem com um efeito colateral entre consultas (número de pessoas diferentes) | De 0 para 5 até 31/10/2026 | Toda segunda, antes de rodar a rotina, conto as linhas de `dados/conversas.csv`, que eu mesmo atualizo a cada conversa (data, canal, identificador USR, se confirmou ou não o padrão descrito em "Como é hoje") |

Por que 5 e por que 31/10: são o critério de sucesso e o prazo que eu mesmo escrevi no "Primeiro experimento" e em "O resultado que eu quero" (piloto até outubro). Conversa conta quando a pessoa usa uma das três medicações e responde à pergunta sobre o que faz entre consultas; comentário solto em post não conta. O ponto de partida é 0 porque, em 21/09, eu ainda não publiquei a pergunta nas comunidades.

## O plano antes do prompt
**Observar:** quais sintomas os usuários de GLP-1 mais relatam, em que dia do ciclo de aplicação eles aparecem, e como essas pessoas hoje decidem se "esperam" ou "procuram ajuda".

**Decidir:** quais sintomas/intensidades geram cada uma das três orientações possíveis — "continue monitorando", "ajuste algo simples" ou "fale com seu médico" — sempre sem dar diagnóstico.

**Executar sozinho (o produto/IA):** registrar dose, sintoma, intensidade e contexto (alimentação, tempo desde a aplicação); organizar o histórico; identificar padrões ao longo das semanas; gerar o resumo estruturado para a consulta.

**O que fica comigo/com o médico:** qualquer decisão clínica — mudar dose, diagnosticar a causa do sintoma, decidir suspender o tratamento. O produto nunca decide isso.

## Primeiro experimento
Como ainda não tenho acesso a um paciente real (ver "Como eu tenho acesso"), o primeiro experimento não é técnico: é validar se a dor é real e do jeito que estou descrevendo.

Esta semana: publicar uma pergunta em 2 comunidades online de usuários de Mounjaro/Wegovy/Ozempic (grupos de Facebook, subreddits como r/Ozempic, ou fóruns de pacientes) perguntando como decidem se um efeito colateral é "normal" e o que fazem hoje entre consultas.

Critério de sucesso: pelo menos 5 respostas que confirmem o padrão descrito (pesquisa no Google/redes sociais, incerteza sobre quando procurar o médico, falta de histórico organizado).

## Perguntas de um leitor cético (v3)
**1. Sem acesso a um paciente real ainda, como você sabe que o problema é exatamente esse, e não outra coisa (ex: medo de efeito colateral grave, não falta de acompanhamento)?**
Não sei com certeza ainda. É uma hipótese baseada em relatos públicos e no crescimento do uso dessas medicações. É exatamente o que o primeiro experimento (comunidades online) serve para confirmar ou derrubar antes de construir qualquer coisa.

**2. Como o produto evita ser interpretado como um serviço médico, já que fala sobre sintomas e diz quando "procurar o médico"?**
O produto nunca vai dizer se o sintoma é perigoso ou normal, nem sugerir mudança de dose — só organiza informação e sinaliza "continue monitorando" ou "fale com seu médico" com base em regras simples de intensidade/duração, não em diagnóstico. Ainda preciso validar essas regras com um profissional de saúde antes de qualquer versão real em uso.

**3. Por que alguém pagaria por isso (B2C) em vez de simplesmente perguntar de graça ao médico ou pesquisar no Google?**
Porque o problema não é falta de informação, é falta de organização e de resposta rápida entre consultas — o Google dá informação genérica e contraditória, e o médico não está disponível na hora. Ainda não testei se as pessoas pagariam por isso; é uma pergunta em aberto que quero validar no primeiro experimento e nas próximas conversas com usuários reais.
