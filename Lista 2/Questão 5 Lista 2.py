"""
QUESTAO 5 LISTA 2
Escrever um algoritmo para ler dois valores numéricos e apresentar a diferença do maior pelo menor.
"""
num = []
for i in range(2):
    num.append(int(input(f"Numero {i+1} = ")))
print(f"Diferenca = {abs(num[0]-num[1])}")