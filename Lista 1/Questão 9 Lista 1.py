"""
Questão 9 Lista 1
Faça um algoritmo para ler um número inteiro, depois calcular e imprimir a sua raiz quadrada e sua potenciação.
"""
from math import sqrt
numero=int(input("Digite o numero: "))
raiz = sqrt(numero)
print(f"raiz quadrada = {raiz}")
potencia = numero**2
print(f"Quadrado = {potencia}")
