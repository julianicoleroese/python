import random

def jogar_jokenpo():
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

        if escolha_jogador == escolha_computador:
            print("Empate!")

        elif(
            (escolha_jogador=="papel" and escolha_computador =="pedra") or
            (escolha_jogador=="pedra" and escolha_computador =="tesoura") or
            (escolha_jogador=="tesoura" and escolha_computador =="papel") 
        ):
            print("Você ganhou")

        jogar_novamente = input("Deseja jogar novamente?").lower()
        if jogar_novamente != "sim":
            break 

if __name__ == "__main__":
    jogar_jokenpo()

