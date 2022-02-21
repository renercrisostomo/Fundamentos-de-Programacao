"""
QUESTAO 1 LISTA 8
Escreva uma função recursiva em python para mostrar a série fibonacci até o 12º termo.
"""
def fibonacci(final):
    if final - 2 > 0:
        lista.append(lista[-1] + lista[-2])
        fibonacci(final - 1)
        return lista
lista = [1, 1]  #Conciderando 1 como a 1ª posição
print(fibonacci(12))