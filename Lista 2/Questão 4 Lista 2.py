"""
QUESTAO 4 LISTA 2
Crie um algoritmo que leia 3 números e imprima o maior valor.
"""
num = []
for i in range(3):
    num.append(input(f"Numero {i + 1} = "))
print(f"Maior Valor = {max(num)}")