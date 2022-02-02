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
matriz=[[],[],[]]

def qmagico(matriz):
    #Verifica se é um quadrado magico
    somaReferencia = 0
    for itens in range(3): #Usando a soma da linha 1 como referencia
        somaReferencia += matriz[0][itens]

    #Verifica a soma das linhas e colunas
    for sequencia in range(3):
        soma1 = soma2 = 0
        for itens in range(3):
            soma1 += matriz[sequencia][itens] #Somando os itens da linha
            soma2 += matriz[itens][sequencia] #Somando os itens da coluna
        if soma1 != somaReferencia or soma2 != somaReferencia:
            return False

    #Verifica a soma das diagonais
    soma1 = soma2 = 0
    for sequencia in range(3):
        soma1 += matriz[sequencia][sequencia] #Somando os itens da diag principal
        soma2 += matriz[sequencia][-(sequencia + 1)] #Somando os itens da diag secundaria
    if soma1 != somaReferencia or soma2 != somaReferencia:
        return False
    return True

#Adicionando itens aleatorios
for linha in range(3):
    for itens in range(3):
        matriz[linha].append(randint(1,99))
for linha in range(3): #Mostra a matriz
    print(matriz[linha])

if qmagico(matriz):
    print("É uma matriz QUADRADO MÁGICO")
else:
    print("NÃO é uma matriz QUADRADO MÁGICO")