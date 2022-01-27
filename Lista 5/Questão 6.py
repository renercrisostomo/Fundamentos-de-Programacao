"""
QUESTÃO 6 LISTA 5
Gerar/Cria um vetor de 10 posições, randomicamente, depois ler um valor e verificar se esse valor está ou não no vetor gerado, mostrando a sua posição;
"""
from random import randint
vetor = []
for i in range(10):
    vetor.append(randint(1, 99)) #Adicionando inteiros randomicamente
print(vetor)

valor=int(input("Digite o valor: "))
if valor in vetor:
    for indice in range(10): #Verifica e mostra a(as) posicao(oes)
        if valor == vetor[indice]:
            print(f"Posição: {indice+1}") #Conciderando posicao=indice+1
else:
    print("Não está no vetor")