"""
QUESTAO 1 LISTA 8
Escreva uma função recursiva em python para mostrar a série fibonacci até o 12º termo.
"""
def fibonacci(n):
    if n < 20:
        lista.append(lista[-1] + lista[-2])
        fibonacci(n + 1)
        return lista
lista = [1, 1]  #Considerando 1 como a 1ª posicao
print(fibonacci(2))