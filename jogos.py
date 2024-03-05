import forca
import adivinhacao

def escolha_jogos():

    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("=-Escolha o Jogo-=")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("(1)Forca,(2)Adivinhacão")

    jogo = int(input("Selecione o Jogo:"))

    if(jogo == 1): 
        print("Jogo da Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo da Adivinhação")
        adivinhacao.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()
