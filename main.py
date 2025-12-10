import random
import json
import os

# Constantes para o arquivo de ranking
RANKING_FILE = "ranking_21.json"

def carregar_ranking():
    """Carrega o ranking do arquivo JSON"""
    if os.path.exists(RANKING_FILE):
        try:
            with open(RANKING_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}

def salvar_ranking(ranking):
    """Salva o ranking no arquivo JSON"""
    with open(RANKING_FILE, 'w', encoding='utf-8') as f:
        json.dump(ranking, f, ensure_ascii=False, indent=2)

def adicionar_vitoria(jogador):
    """Adiciona uma vitória para o jogador"""
    ranking = carregar_ranking()
    
    if jogador not in ranking:
        ranking[jogador] = {"vitorias": 0, "derrotas": 0}
    
    ranking[jogador]["vitorias"] += 1
    salvar_ranking(ranking)

def adicionar_derrota(jogador):
    """Adiciona uma derrota para o jogador"""
    ranking = carregar_ranking()
    
    if jogador not in ranking:
        ranking[jogador] = {"vitorias": 0, "derrotas": 0}
    
    ranking[jogador]["derrotas"] += 1
    salvar_ranking(ranking)

def mostrar_ranking():
    """Mostra o ranking dos jogadores"""
    ranking = carregar_ranking()
    
    if not ranking:
        print("\n📊 Ranking vazio. Jogue algumas partidas para preenchê-lo!")
        return
    
    print("\n" + "="*50)
    print("🏆 RANKING DE JOGADORES 🏆")
    print("="*50)
    
    # Converter para lista e ordenar por vitórias (decrescente)
    ranking_lista = sorted(
        ranking.items(), 
        key=lambda x: (x[1]["vitorias"], -x[1]["derrotas"]), 
        reverse=True
    )
    
    print(f"{'Posição':<10} {'Jogador':<20} {'Vitórias':<10} {'Derrotas':<10} {'Saldo':<10}")
    print("-"*60)
    
    for i, (jogador, dados) in enumerate(ranking_lista, 1):
        saldo = dados["vitorias"] - dados["derrotas"]
        print(f"{i:<10} {jogador:<20} {dados['vitorias']:<10} {dados['derrotas']:<10} {saldo:<10}")
    
    print("="*50)

def limpar_ranking():
    """Limpa todo o ranking"""
    if input("\n⚠️  Tem certeza que deseja limpar todo o ranking? (s/n): ").lower() == 's':
        with open(RANKING_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=2)
        print("✅ Ranking limpo com sucesso!")
    else:
        print("❌ Operação cancelada.")

def criar_baralho():
    naipes = ['♠', '♥', '♦', '♣']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baralho = [(valor,naipe) for naipe in naipes for valor in valores]
    random.shuffle(baralho)
    return baralho

def calcular_pontuacao(mao):
    pontuacao = 0
    ases = 0
    
    for carta in mao:
        valor = carta[0]
        if valor in ['J', 'Q', 'K']:
            pontuacao += 10
        elif valor == 'A':
            ases += 1
            pontuacao += 11
        else:
            pontuacao += int(valor)
    
    while pontuacao > 21 and ases > 0:
        pontuacao -= 10
        ases -= 1
        
    return pontuacao

def dar_carta(baralho):
    """Remove e retorna uma carta do baralho"""
    return baralho.pop() if baralho else None

def mostrar_mao(mao_jogador, mao_dealer, mostrar_todas_dealer=False):
    """Mostra as mãos do jogador e do dealer"""
    print("\n" + "="*40)
    print("Sua mão:", mao_jogador, "- Pontuação:", calcular_pontuacao(mao_jogador))
    
    if mostrar_todas_dealer:
        print("Mão do dealer:", mao_dealer, "- Pontuação:", calcular_pontuacao(mao_dealer))
    else:
        print("Mão do dealer:", [mao_dealer[0], '?'])
    print("="*40)

def turno_jogador(baralho, mao_jogador, mao_dealer, nome_jogador):
    """Gerencia o turno do jogador"""
    while True:
        pontuacao = calcular_pontuacao(mao_jogador)
        mostrar_mao(mao_jogador, mao_dealer)
        
        if pontuacao >= 21:
            break
            
        acao = input(f"\n{nome_jogador}, pedir carta (p) ou Parar (s)? ").lower()
        
        if acao == 'p':
            mao_jogador.append(dar_carta(baralho))
            pontuacao = calcular_pontuacao(mao_jogador)
            if pontuacao >= 21:
                mostrar_mao(mao_jogador, mao_dealer)
                break
        elif acao == 's':
            break
        else:
            print("Ação inválida! Digite 'p' para pedir ou 's' para parar")

def turno_dealer(baralho, mao_dealer, mao_jogador):
    """Gerencia o turno do dealer (computador)"""
    print("\nTurno do dealer...")
    pontuacao = calcular_pontuacao(mao_dealer)
    
    while pontuacao < 17:
        mao_dealer.append(dar_carta(baralho))
        pontuacao = calcular_pontuacao(mao_dealer)
        mostrar_mao(mao_jogador, mao_dealer, mostrar_todas_dealer=True)
        
        if pontuacao >= 21:
            break

def verificar_vencedor(mao_jogador, mao_dealer, nome_jogador):
    """Verifica e retorna o resultado do jogo"""
    pontuacao_jogador = calcular_pontuacao(mao_jogador)
    pontuacao_dealer = calcular_pontuacao(mao_dealer)
    
    print("\n" + "="*50)
    print("RESULTADO FINAL:")
    print(f"{nome_jogador}:", mao_jogador, "- Pontuação:", pontuacao_jogador)
    print("Dealer:", mao_dealer, "- Pontuação:", pontuacao_dealer)
    print("="*50)
    
    if pontuacao_jogador > 21:
        resultado = f"{nome_jogador} estourou! Dealer venceu! 💸"
        vencedor = "dealer"
    elif pontuacao_dealer > 21:
        resultado = f"Dealer estourou! {nome_jogador} venceu! 🎉"
        vencedor = "jogador"
    elif pontuacao_jogador > pontuacao_dealer:
        resultado = f"{nome_jogador} venceu! 🎉"
        vencedor = "jogador"
    elif pontuacao_dealer > pontuacao_jogador:
        resultado = f"Dealer venceu! 💸"
        vencedor = "dealer"
    else:
        resultado = f"Empate! 🤝"
        vencedor = "empate"
    
    print(resultado)
    return vencedor

def distribuir_cartas_iniciais(baralho):
    """Distribui duas cartas para cada jogador"""
    mao_jogador = [dar_carta(baralho), dar_carta(baralho)]
    mao_dealer = [dar_carta(baralho), dar_carta(baralho)]
    return mao_jogador, mao_dealer

def jogo_21():
    """Função principal que executa o jogo de 21"""
    print("\n🎰 BEM-VINDO AO JOGO DE 21! 🎰")
    print("Objetivo: Chegar o mais perto possível de 21 sem estourar!")
    print("Ases valem 1 ou 11 pontos automaticamente")
    print("-" * 50)
    
    # Solicitar nome do jogador
    nome_jogador = input("Digite seu nome: ").strip()
    if not nome_jogador:
        nome_jogador = "Jogador"
    
    while True:
        # Iniciar nova partida
        baralho = criar_baralho()
        mao_jogador, mao_dealer = distribuir_cartas_iniciais(baralho)
        
        # Verificar blackjack inicial
        pontuacao_jogador = calcular_pontuacao(mao_jogador)
        pontuacao_dealer = calcular_pontuacao(mao_dealer)
        
        if pontuacao_jogador == 21 or pontuacao_dealer == 21:
            mostrar_mao(mao_jogador, mao_dealer, mostrar_todas_dealer=True)
            if pontuacao_jogador == 21 and pontuacao_dealer == 21:
                print("Ambos fizeram 21! Empate!")
                vencedor = "empate"
            elif pontuacao_jogador == 21:
                print(f"Blackjack! {nome_jogador} fez 21! 🎉")
                vencedor = "jogador"
                adicionar_vitoria(nome_jogador)
            else:
                print("Dealer fez Blackjack! 💸")
                vencedor = "dealer"
                adicionar_derrota(nome_jogador)
        else:
            # Turno do jogador
            turno_jogador(baralho, mao_jogador, mao_dealer, nome_jogador)
            
            # Turno do dealer (apenas se jogador não estourou)
            if calcular_pontuacao(mao_jogador) <= 21:
                turno_dealer(baralho, mao_dealer, mao_jogador)
            
            # Verificar vencedor
            vencedor = verificar_vencedor(mao_jogador, mao_dealer, nome_jogador)
            
            # Atualizar ranking
            if vencedor == "jogador":
                adicionar_vitoria(nome_jogador)
            elif vencedor == "dealer":
                adicionar_derrota(nome_jogador)
        
        # Mostrar estatísticas do jogador
        ranking = carregar_ranking()
        if nome_jogador in ranking:
            vitorias = ranking[nome_jogador]["vitorias"]
            derrotas = ranking[nome_jogador]["derrotas"]
            saldo = vitorias - derrotas
            print(f"\n📊 Estatísticas de {nome_jogador}:")
            print(f"   Vitórias: {vitorias} | Derrotas: {derrotas} | Saldo: {saldo}")
        
        # Perguntar se quer jogar novamente
        jogar_novamente = input(f"\n{nome_jogador}, quer jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print(f"Obrigado por jogar, {nome_jogador}! 👋")
            break

def main():
    while True:
        print("\n" + "="*50)
        print("🎲 MENU PRINCIPAL - JOGO DE 21 🎲")
        print("="*50)
        print("1. Jogar 21")
        print("2. Ver Ranking")
        print("3. Limpar Ranking")
        print("4. Sair")
        print("-"*50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            jogo_21()
        elif opcao == '2':
            mostrar_ranking()
            input("\nPressione Enter para continuar...")
        elif opcao == '3':
            limpar_ranking()
            input("\nPressione Enter para continuar...")
        elif opcao == '4':
            print("Saindo... Até mais! 👋")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    # Verificar se o arquivo de ranking existe
    if not os.path.exists(RANKING_FILE):
        with open(RANKING_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=2)
    
    main()
    