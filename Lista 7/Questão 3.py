"""
QUESTAO 3 LISTA 7
Crie uma função em python que receba 3 números e retorne em forma crescente.
"""
def cresente(num1, num2, num3):
    numeros = [num1, num2, num3]
    for num in range(3):
        for linha in range(num):
            if numeros[num] != numeros[linha]:
                if numeros[num] > numeros[linha]:
                    numeros.insert(linha, numeros[num]) 
                else:
                    numeros.insert(linha + 1, numeros[num])
                numeros.pop(num + 1)
                break
    return numeros

num1 = input("numero1 = ")
num2 = input("numero2 = ")
num3 = input("numero3 = ")
print(cresente(num1, num2, num3))