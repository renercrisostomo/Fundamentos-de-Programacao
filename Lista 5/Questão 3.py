"""
QUESTÃO 3 LISTA 5
Gerar um vetor de 10 elementos. Em seguida, verifique quantos números primos existem no vetor, imprimindo-os.
"""
from math import isqrt
from random import randint

def primo(numero):
    if numero==1:
        return False
    for divisor in range(2, isqrt(numero)+1):
        if numero%(divisor)==0:
            return False
    return True

aleatorio, primos = [], []
for i in range(10):
    aleatorio.append(randint(1,99))
print(aleatorio)

for i in range(10):
    if primo(aleatorio[i]): #Verifica se é primo
        primos.append(aleatorio[i])
print(f"{len(primos)} primo(s): {primos}")