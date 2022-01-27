"""
QUESTÃO 5 LISTA 5
Preencher um vetor com os números 10 a 20, e depois mostrar os elementos pares do vetor de trás para frente.
"""
vetor, pares = [], []

for numero in range(10, 21): #Armazena os numeros de 10 a 20
    vetor.append(numero)
print(vetor)

for itens in range(len(vetor)):
    if vetor[-(itens+1)]%2==0: #Verifica de trás para frente os pares
        pares.append(vetor[-(itens+1)])
print(pares)
