"""
QUESTAO 6 LISTA 2
Crie um algoritmo para ler 3 valores float e imprimir o quadrado do 1º + a soma dos outros dois.
"""
num = []
for i in range(3):
    num.append(float(input(f"Numero {i + 1} = ")))
print(f"Resultado = {(num[0] ** 2) + num[1] + num[2]}")