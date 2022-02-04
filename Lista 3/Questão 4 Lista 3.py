"""
QUESTAO 4 LISTA 3
Fazer um algoritmo para ler 10 números inteiros quaisquer e informar quantos e quais são os números primos.
"""
from math import isqrt

def primo(numero):
    if numero == 1:
        return False
    for divisor in range(2, isqrt(numero) + 1):
        if numero % (divisor) == 0:
            return False
    return True

num = []
for index in range(10):
    num.append(int(input(f"Numero {index + 1} = ")))
print("\n")

cont_primo = 0
for i in range(len(num)):
    if primo(num[i]):
        print(f"Numero {i + 1} = {num[i]} é PRIMO")
        cont_primo = cont_primo + 1
    else:
        print(f"Numero {i + 1} = {num[i]} Não é PRIMO")
print(f"\nQuantidade de numeros Primos = {cont_primo}")