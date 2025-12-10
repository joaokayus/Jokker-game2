# Jokker21
-------------------------------------------------------------------------
🎮 Jogo de 21 (Blackjack) com Sistema de Ranking
Um jogo de Blackjack (21) implementado em Python com sistema de ranking persistente, onde os jogadores podem competir contra o dealer e ter suas vitórias e derrotas registradas em um arquivo JSON.
-------------------------------------------------------------------------
✨ Funcionalidades:

🎰 Jogo de 21

•Baralho completo de 52 cartas (4 naipes, 13 valores)

•Sistema de pontuação automático com ajuste inteligente dos Ases (1 ou 11 pontos)

•Turnos interativos: jogador vs dealer
-------------------------------------------------------------------------

Regras oficiais do Blackjack:

•Dealer para em 17 pontos ou mais

•Blackjack (21 com 2 cartas) vence automaticamente

•Estourou (mais de 21 pontos) perde automaticamente
-------------------------------------------------------------------------
🏆 Sistema de Ranking

•Presença de dados em arquivo JSON

•Registro de vitórias e derrotas por jogador

Ranking ordenado por:

•Número de vitórias (maior para menor)

•Saldo (vitórias - derrotas)

•Estatísticas individuais por jogador

•Opção para limpar ranking com confirmação
-------------------------------------------------------------------------
👤 Personalização

•Sistema de nomes para jogadores

•Mensagens personalizadas com o nome do jogador

•Menu interativo com opções claras
-------------------------------------------------------------------------
🚀 Como Executar

Pré-requisitos:

•Python 3.6 ou superior

•Nenhuma biblioteca externa necessária (usa apenas módulos padrão)

Passos para Executar:

•Clone ou baixe o arquivo Jokker21.py

•Abra o terminal/command prompt na pasta do arquivo

Execute o comando:

bash

python Jokker21.py

Alternativamente:

•Execute em qualquer IDE Python (VS Code, PyCharm, etc.)

•Ou execute no IDLE do Python
-------------------------------------------------------------------------
🎯 Regras do Jogo

Objetivo

•Obter uma mão com valor mais próximo de 21 do que o dealer, sem ultrapassar 21 pontos.

Valores das Cartas:

•Cartas numéricas (2-10): Valor equivalente ao número

•Figuras (J, Q, K): 10 pontos cada

•Ás (A): 1 ou 11 pontos (ajustado automaticamente)

Fluxo do Jogo:

•Distribuição inicial: 2 cartas para cada (jogador e dealer)

Turno do jogador:

•Pode "pedir" (receber mais cartas)

•Ou "parar" (manter mão atual)

•Turno do dealer: Automático - para em 17+ pontos

Resultado: Comparação de pontuações

Condições Especiais:

•Blackjack: 21 pontos com 2 cartas - vitória automática

•Estouro: Mais de 21 pontos - derrota automática

•Empate: Mesma pontuação - ninguém ganha ou perde
-------------------------------------------------------------------------
📊 Sistema de Ranking

Estrutura de Dados:

Os dados são armazenados no arquivo ranking_21.json no formato:

json
{
  "João": {
    "vitorias": 5,
    "derrotas": 3
  },
  "Maria": {
    "vitorias": 10,
    "derrotas": 2
  }
}
Como o Ranking é Calculado
Pontuação principal: Número de vitórias

Critério de desempate: Saldo (vitórias - derrotas)

Ordenação: Decrescente (maior para menor)
-------------------------------------------------------------------------
📁 Estrutura do Código

Principais Funções:

1. Funções do Jogo:

•criar_baralho(): Cria e embaralha baralho de 52 cartas

•calcular_pontuacao(mao): Calcula pontos com ajuste de Ases

•turno_jogador(): Gerencia interação do jogador

•turno_dealer(): Lógica automática do dealer

•verificar_vencedor(): Determina resultado da partida

2. Funções do Ranking

•carregar_ranking(): Lê dados do arquivo JSON

•salvar_ranking(): Salva dados no arquivo JSON

•adicionar_vitoria(): Incrementa vitórias do jogador

•adicionar_derrota(): Incrementa derrotas do jogador

•mostrar_ranking(): Exibe ranking formatado

3. Funções de Interface

•mostrar_mao(): Exibe cartas e pontuações

•jogo_21(): Função principal do jogo

•main(): Menu principal do programa

-------------------------------------------------------------------------
Compatibilidade

•Python 3.6+

•Multiplataforma (Windows, macOS, Linux)

•Codificação UTF-8 para suportar acentos e emojis
-------------------------------------------------------------------------
Contribuidores: João Kayus


