import random

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

def turno_jogador(baralho, mao_jogador, mao_dealer):
    """Gerencia o turno do jogador"""
    while True:
        pontuacao = calcular_pontuacao(mao_jogador)
        mostrar_mao(mao_jogador, mao_dealer)
        
        if pontuacao >= 21:
            break
            
        acao = input("\nPedir carta (p) ou Parar (s)? ").lower()
        
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

def verificar_vencedor(mao_jogador, mao_dealer):
    """Verifica e retorna o resultado do jogo"""
    pontuacao_jogador = calcular_pontuacao(mao_jogador)
    pontuacao_dealer = calcular_pontuacao(mao_dealer)
    
    print("\n" + "="*50)
    print("RESULTADO FINAL:")
    print("Sua mão:", mao_jogador, "- Pontuação:", pontuacao_jogador)
    print("Mão do dealer:", mao_dealer, "- Pontuação:", pontuacao_dealer)
    print("="*50)
    
    if pontuacao_jogador > 21:
        return "Você estourou! Dealer venceu! 💸"
    elif pontuacao_dealer > 21:
        return "Dealer estourou! Você venceu! 🎉"
    elif pontuacao_jogador > pontuacao_dealer:
        return "Você venceu! 🎉"
    elif pontuacao_dealer > pontuacao_jogador:
        return "Dealer venceu! 💸"
    else:
        return "Empate! 🤝"

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
    
    while True:
        
        baralho = criar_baralho()
        mao_jogador, mao_dealer = distribuir_cartas_iniciais(baralho)
        
        
        pontuacao_jogador = calcular_pontuacao(mao_jogador)
        pontuacao_dealer = calcular_pontuacao(mao_dealer)
        
        if pontuacao_jogador == 21 or pontuacao_dealer == 21:
            mostrar_mao(mao_jogador, mao_dealer, mostrar_todas_dealer=True)
            if pontuacao_jogador == 21 and pontuacao_dealer == 21:
                print("Ambos fizeram 21! Empate!")
            elif pontuacao_jogador == 21:
                print("Blackjack! Você fez 21! 🎉")
            else:
                print("Dealer fez Blackjack! 💸")
        else:
           
            turno_jogador(baralho, mao_jogador, mao_dealer)
            
            
            if calcular_pontuacao(mao_jogador) <= 21:
                turno_dealer(baralho, mao_dealer, mao_jogador)
            
            
            resultado = verificar_vencedor(mao_jogador, mao_dealer)
            print(resultado)
        
        
        jogar_novamente = input("\nQuer jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! 👋")
            break


def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Jogar 21")
        print("2. Sair")
       
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            jogo_21()

        elif opcao == '2':
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
