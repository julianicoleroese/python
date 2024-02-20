#solicitar 2 numeros pro usuario, converter pra flowt, fazer a somar e exibir pro usuario

try:
    a = float (input ("Escreva um numero"))
    b = float (input ("Escreva um numero"))
except ValueError:
    print("Tente Novamente")
soma = a + b 
print(f"Soma de {a} e {b} é igual a:{soma}")