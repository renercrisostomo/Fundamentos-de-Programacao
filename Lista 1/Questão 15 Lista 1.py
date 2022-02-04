"""
Questão 15 Lista 1
Faça um algoritmo para calcular e imprimir o An de uma P.G. (Progressão Geométrica), segundo a fórmula: an = a1.qn-1
"""
a1 = int(input("Digite o valor de a1: "))
q = int(input("Digite o valor de q: "))
n = int(input("Digite o valor de n: "))
An = a1 * q ** (n - 1)
print(f"An = {An}")
