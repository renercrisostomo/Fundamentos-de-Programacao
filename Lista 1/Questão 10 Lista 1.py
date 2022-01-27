"""
Questão 10 Lista 1
Faça um algoritmo para ler 3 números inteiros, depois calcular e imprimir a média aritmética destes.
"""
numeros=[]
for numero in range(1, 4):
	numeros.append(int(input(f"{numero}º número: ")))
print(f"\nMédia = {sum(numeros)/len(numeros)}")
