"""
Questão 12 Lista 1
Construa um algoritmo para calcular as raízes de uma equação do 2º. Grau (ax² + bx + c), sendo que A, B, e C são valores fornecidos pelo usuário.
"""
from math import sqrt

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
Delta = B * B - 4 * A * C
if Delta < 0:
	print("NÃO POSSUI VALORES REAIS")
else:
	X1 = (-B + sqrt(Delta)) / 2 * A
	X2 = (-B - sqrt(Delta)) / 2 * A
	print(f"X1 = {X1}")
	print(f"X2 = {X2}")