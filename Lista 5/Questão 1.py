"""
QUESTÃO 1 LISTA 5
Gerar um vetor aleatório de 10 posições, em seguida ordená-lo de forma crescente e, depois, decrescente.
"""
from random import randint

aleatorio = []
for posicoes in range(10):
    aleatorio.append(randint(1,99))
print(aleatorio)

aleatorio.sort()
print(aleatorio)

aleatorio.sort(reverse=True)
print(aleatorio)