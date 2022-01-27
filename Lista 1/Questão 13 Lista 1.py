"""
Questão 13 Lista 1
Fazer um algoritmo para ler dois números inteiros e trocar seus valores (ex.: A e B valor de A passa para o B e valor de B passa para o A) e depois imprimir os novos valores de cada variável.
"""
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = A
A = B
B = C
print(f"A = {A}")
print(f"B = {B}")
