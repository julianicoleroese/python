import random 
numero_secreto =  random.randint(1, 10)
tentativa = 0
max_tentativa = 5
while tentativa < max_tentativa:
    palpite = int(input("Digite seu palpite"))
    tentativa += 1
    if palpite == numero_secreto:
        print("Parabéns")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior")
    else:
        print("Tente um número menor")
        
    if tentativa < max_tentativa:
        print(f"Você tem {max_tentativa-tentativa} tentativas")
    else:
        print(f"Você não acertou, o número era {numero_secreto}")
        
print ("Fim de jogo")
        
        
    
    