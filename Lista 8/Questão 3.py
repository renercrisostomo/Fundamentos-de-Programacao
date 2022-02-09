"""
QUESTAO 3 LISTA 8
Escreva uma função em python para calcular e informar o MDC (Máximo Divisor Comum) de um número qualquer informado pelo usuário.
"""
from math import factorial

def mdc(lista):
    return factorial(lista)

numeros = input(f"Numeros (num1, num2...): ").replace(" ", "").split(",")
for item in range(len(numeros)):
    numeros[item] = int(numeros[item])

print(factorial(12))