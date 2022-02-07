"""
QUESTAO 1 LISTA 8
Escreva uma função recursiva em python para mostrar a série fibonacci até o 12o. termo.
"""

fibonacci = [1, 1]  #Considerando 1 como a 1ª posicao
for posicao in range(2, 20):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci)