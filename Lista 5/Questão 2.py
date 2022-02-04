"""
QUESTÃO 2 LISTA 5
Preencher um primeiro vetor com o quadrado dos números pares do intervalo 2 a 20. Preencher um segundo vetor com os números de 10 a 19. Mostrar a soma dos dois vetores.
"""
primeiro_vetor, segundo_vetor, soma = [], [],[]

for i in range(2, 21, 2):
    primeiro_vetor.append(i * i)
for i in range(10, 20, 1):
    segundo_vetor.append(i)
for i in range(0, 10, 1):
    soma.append(primeiro_vetor[i] + segundo_vetor[i])

print(primeiro_vetor)
print(segundo_vetor)
print(soma)