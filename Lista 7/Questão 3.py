"""
QUESTAO 3 LISTA 7
Crie uma função em python que receba 3 números e retorne em forma crescente.
"""
def cresente(num1, num2, num3):
    numeros = [int(num1), int(num2), int(num3)]
    return sorted(numeros)

num1 = input("numero1 = ")
num2 = input("numero2 = ")
num3 = input("numero3 = ")
print(cresente(num1, num2, num3))