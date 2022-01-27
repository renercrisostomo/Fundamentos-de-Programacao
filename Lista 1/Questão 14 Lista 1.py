"""
Questão 14 Lista 1
Faça um algoritmo que calcule e imprima o An de uma P.A. (Progressão Aritmética), segundo a fórmula: An = a1 + (n-1) * r.
"""
a1 = int(input("Digite o valor de a1: "))
n = int(input("Digite o valor de n: "))
r = int(input("Digite o valor de r: "))
An = a1+(n-1)*r
print(f"An = {An}")