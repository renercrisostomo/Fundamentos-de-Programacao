"""
QUESTAO 4 LISTA 8
Faça um programa em python que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma. Imprima na tela a matriz, a linha de maior soma e a soma.
"""
def linhaMaiorSoma(matriz):
    #Retorna a linha de maior soma
    maior = 0
    for i in range(3):
        if sum(matriz[i]) > maior:
            maior = sum(matriz[i])
            maiorLinha = f'Linha {i}\nSoma {maior}'
    return max(maiorLinha)

matriz = [[], [], []]
for linha in range(3):
    for itens in range(3):
        matriz[linha].append(int(input(f"-Digite o item {itens + 1} da linha {linha + 1}: ")))

for linha in range(3):
    print(matriz[linha])

print(linhaMaiorSoma(matriz))