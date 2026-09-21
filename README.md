# Acompanhamento de efeitos colaterais para usuários de GLP-1

Repositório da disciplina AI for Business, Link School of Business, 2026-2. Aluno: Henrique Guimarães.

O problema: quem usa Mounjaro, Wegovy ou Ozempic fica sozinho com os efeitos colaterais entre uma consulta e outra, sem saber se espera, ajusta algo simples ou procura o médico, e chega na consulta sem histórico organizado. O projeto é um produto que registra sintoma, dose e intensidade, organiza o histórico e orienta o próximo passo, sem nunca substituir a decisão médica.

Estado em 21/09/2026: ainda não há paciente real nem produto. O dado de operação é inventado e declarado como tal; a métrica desta fase é conseguir as primeiras conversas com usuários reais.

## Arquivos

| Arquivo | O que é |
|---|---|
| `problema.md` | O problema, quem sofre, como é hoje, o primeiro experimento e a seção Métrica (Métrica / Alvo / Como confiro) |
| `CLAUDE.md` | Como o Claude deve trabalhar comigo neste projeto: o que pode e o que não pode decidir sozinho |
| `regras.md` | As 3 regras que a operação do piloto segue (gatilho, fonte, condição, ação, quem recebe, se não disparar) e a instrução de falha |
| `automacoes.md` | O que está ligado, a rotina "Checagem do piloto" com o prompt, e a evidência das execuções |
| `testes.md` | Os 3 cenários de falha provocados de propósito (fonte fora do ar, dado sujo, condição que nunca dispara) e o que consertei |
| `prompts.md` | A biblioteca de prompts da NP1: a mensagem de orientação após o registro de sintoma, em 3 versões, e a regra de escalonamento que venceu |
| `rotina.py` | O script que a rotina usa para aplicar as condições do `regras.md` sobre a fonte, com contagem exata de linhas lidas e ignoradas. Rodar: `python rotina.py . AAAA-MM-DD` |
| `diario.md` | Diário de uso do Claude Code: o que pedi, o que veio, o que corrigi |
| `contexto/` | Quem eu sou (`sobre-mim.md`), qual é o negócio (`negocio.md`), quem é o cliente (`cliente.md`) |
| `dados/fonte.md` | A fonte canônica: de onde vem o dado, quem atualiza, quais campos importam e os 3 números com regra de cálculo |
| `dados/amostra.csv` | A amostra de registros de sintoma do piloto. Inventada, declarada como inventada no `fonte.md`; é o que as regras leem |
| `dados/conversas.csv` | A série da métrica do `problema.md`: uma linha por conversa com usuário real. Vazio até a primeira conversa |
| `alertas/` | Os alertas que a rotina escreveu quando alguma regra disparou, um arquivo por dia (`AAAA-MM-DD.md`) |

## O que não está aqui (ainda)

- `painel.html` (aula 12) e a pasta `radar/` (aula 13) não foram feitos. Os 3 números do painel já têm regra de cálculo no `dados/fonte.md`.
- `fake-erp.md` (aula 10) e `.claude/skills/` (aula 8) não existem neste repositório: as regras leem o CSV em `dados/`, não o FakeERP.
