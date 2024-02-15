nome = input ("Escreva seu nome")
try:
    idade = int (input("Escreva a sua idade"))
except ValueError:
    print("você não digitou um numérico")
#idade = int(idade)
print(f"Olá {nome}, você tem {idade} anos.")