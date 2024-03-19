import random

def jogar_jokenpo():
    derrotas = 0
    vitorias = 0
    opcoes = ["pedra","papel","tesoura"]
    print("Bem-vindo ao jogo Jokenpô!")
    print("Escolha um: pedra, papel ou tesoura.")

    while True:
        escolha_jogador = input("Faça sua escolha:").lower()
        if escolha_jogador not in opcoes:
            print("Escolha inválida, tente outra vez.")
            continue

        escolha_computador = random.choice(opcoes)
        print(f"Computador escolheu: {escolha_computador}")

        resultado = define_vencedor(escolha_jogador, escolha_computador)
        print(resultado)

        if resultado == "Você ganhou!":
            vitorias += 1
        elif resultado == "Você perdeu!":
            derrotas += 1
        print(f"Você tem {vitorias} vitórias, e {derrotas} derrotas.")

        jogar_novamente = input("Deseja jogar novamente?").lower()
        if jogar_novamente != "sim":
            break 

def define_vencedor(escolha_jogador , escolha_computador):
        if escolha_jogador == escolha_computador:
            return"Empate!"
        elif(
            (escolha_jogador=="papel" and escolha_computador =="pedra") or
            (escolha_jogador=="pedra" and escolha_computador =="tesoura") or
            (escolha_jogador=="tesoura" and escolha_computador =="papel") 
        ):
            return"Você ganhou!"
        else:
            return"Você perdeu!"

if __name__ == "__main__":
    jogar_jokenpo()

