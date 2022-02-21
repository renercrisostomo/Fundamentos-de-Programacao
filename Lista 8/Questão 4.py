"""
QUESTAO 4 LISTA 8
Faça um programa em python que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma. Imprima na tela a matriz, a linha de maior soma e a soma.
"""

matriz = []
print('Digite no formato num1, num2, num3')
for linha in range(3):
    num1, num2, num3 = input(f"-Digite o itens da linha {linha + 1}: ").replace(" ", "").split(",")
    matriz.append([int(num1), int(num2), int(num3)])

for linha in range(3):
    print(matriz[linha])

maior = 0
for i in range(3):
    if sum(matriz[i]) > maior:
        LinhaMaiorSoma = sum(matriz[i])
        indiceMaiorSoma = i

print(f'Linha {indiceMaiorSoma}\nSoma {LinhaMaiorSoma}')