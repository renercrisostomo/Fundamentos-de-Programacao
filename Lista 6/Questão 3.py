"""
QUESTÃO 3 LISTA 6
Dizemos que uma matriz quadrada inteira é um quadrado mágico se a soma dos elementos de cada linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais.
Exemplo: A matriz
8| 0|7
4| 5|6
3|10|2
é um quadrado mágico.

Implemente uma matriz quadrada (quadrado mágico), insira valores aleatórios e, depois, mostre a mensagem “É uma matriz QUADRADO MÁGICO” ou “NÃO é uma matriz QUADRADO MÁGICO” e os seus valores.
"""
from random import randint

matriz=[[], [], []]

def qmagico(matriz):
    #Verifica se é um quadrado magico

    somaRef = sum(matriz[0])
    for i in range(3):
        soma = 0
        for itens in range(3):
            soma += matriz[itens][i]  #Soma coluna
        if soma != somaRef  or somaRef != sum(matriz[i]):  #Soma linha
            return False

    soma = soma2 = 0
    for i in range(3):
        soma += matriz[i][i]  #Soma diagonal principal
        soma2 += matriz[i][ -(i + 1)]  #Soma diagonal secundaria
    if soma != somaRef  or somaRef != soma2:
        return False
    return True

for linha in range(3):
    for itens in range(3):
        matriz[linha].append(randint(1, 99))
        
for linha in range(3):  #Mostra a matriz
    print(matriz[linha])

if qmagico(matriz):
    print("É uma matriz QUADRADO MÁGICO")
else:
    print("NÃO é uma matriz QUADRADO MÁGICO")