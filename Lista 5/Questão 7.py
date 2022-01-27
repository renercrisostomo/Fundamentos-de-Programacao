"""
QUESTÃO 7 LISTA 5
Gerar/Cria um vetor de 10 posições, randomicamente, depois contar quantos pares e quantos ímpares existem no vetor;
"""
from random import randint
vetor = []
for i in range(10):
    vetor.append(randint(1, 99)) #Adicionando inteiros randomicamente
print(vetor)

cont_par=0
for i in range(10):
    if vetor[i-1]%2==0: #Contando os numeros pares
        cont_par+=1
print(f"{cont_par} par(es) e {len(vetor)-cont_par} impar(es)") #Impares=total-pares