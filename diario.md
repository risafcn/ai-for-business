# Diário de uso — Claude Code

## 27/08 - construção da base do projeto (problema, contexto, prompts)
Pedi: construir o problema.md, o CLAUDE.md, a pasta contexto/ e o prompts.md do zero, a partir das minhas respostas sobre o problema de acompanhamento de efeitos colaterais de canetas emagrecedoras.

Veio: estrutura completa e organizada, mas a primeira versão do problema.md tratava a persona "Maria" como se fosse uma pessoa real já entrevistada.

Corrigi: deixei explícito que ainda não tenho acesso a um usuário real e pedi para registrar isso como um risco em aberto do projeto, não como algo já resolvido.

## 21/09 - a operação mínima (regras, fonte, rotina, métrica, testes)
Pedi: montar as peças das aulas 11 a 14 a partir do meu contexto/ e problema.md, sem inventar nada sobre o negócio, e rodar de verdade a rotina e os três testes de falha.

Veio: regras.md com 3 regras usando os limites da V3 do prompts.md (intensidade 7, 24h) e o ciclo semanal das medicações (7 dias); dados/fonte.md com a fonte declarada como inventada; automacoes.md com duas execuções (uma disparou, uma calada); testes.md com os três cenários.

Corrigi: no teste 2 a Regra 1 ficou calada quando o registro intenso veio com data em outro formato. A instrução de falha ganhou o "REGISTRO ILEGÍVEL" para isso não passar em silêncio. A métrica ficou na validação (conversas com usuários reais, de 0 para 5 até 31/10), porque as métricas do produto ainda não dão para medir.
