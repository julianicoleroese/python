#solicitar 2 números, selecionar uma das 4 operações(adicao,subtracao,multiplicacao,divisao) e usar os dois numero solicitados

operacao = input("Digite qual operação deseja: +,-,*,/")

num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))


def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não pode ser dividido por zero"
    else:
        return num1 / num2

if (operacao == "+"):
    print(adicao(num1, num2))
elif (operacao == "-"):
    print(subtracao(num1, num2))
elif (operacao == "*"):
    print(multiplicacao(num1, num2))
elif (operacao == "/"):
    print(divisao(num1, num2))
else:
    print("Sua operação foi inválida, tente usar +,-,*,/.")