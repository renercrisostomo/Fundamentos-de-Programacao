"""
QUESTAO 1 LISTA 8
Escreva uma função recursiva em python para mostrar a série fibonacci até o 12º termo.
"""
def fibonacci(numeros = 2, lista = [1, 1]):
    #Retorna n numeros da sequencia fibonacci. Podendo partir de uma sequencia declarada.
    if numeros > len(lista):
        lista.append(lista[-1] + lista[-2])
        fibonacci(numeros - 1)
        return lista
    elif numeros < len(lista):
        lista.insert(0, lista[1] + lista[0])
        fibonacci(numeros + 1)
        return lista
    else:
        return lista

print(fibonacci(12))