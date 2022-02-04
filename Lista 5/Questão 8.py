"""
QUESTÃO 8 LISTA 5
Gerar/Cria um vetor de 10 posições, randomicamente, depois contar quantos valores repetidos existem no vetor gerado, imprimindo-os se houver;
"""
from random import randint

vetor = []
for i in range(10):
    vetor.append(randint(1, 99))  #Adicionando inteiros randomicamente
print(vetor)

vetor.sort()  #Ordena para Verificar de dois em dois se são iguais 
cont_igual = 0
for i in range(10):
    if vetor[i - 1] == vetor[i]:
        cont_igual += 1
    elif cont_igual > 0:
        print(f"{vetor[i - 1]} apareceu {cont_igual + 1} vezes")
        cont_igual = 0