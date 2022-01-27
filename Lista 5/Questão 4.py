"""
QUESTÃO 4 LISTA 5
Crie um vetor de inteiros para armazenar a sequência Fibonacci até a 20a. posição.
"""
fibonacci = [1, 1] #Considerando 1 como a 1ª posicao
for posicao in range(2, 20):
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(fibonacci)