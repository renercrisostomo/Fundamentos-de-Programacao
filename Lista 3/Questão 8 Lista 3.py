"""
QUESTAO 8 LISTA 3
Construa um algoritmo para ler salarios de 10 funcionários de uma empresa e depois calcular e informar:
	- maior salario
	- menor salario
	- media salarial
	- imposto de renda, levando em consideração (até R$ 1.500 – isento maior que R$ 1.500 e menor ou
	  igual a R$ 2.000 – descontar 10% maior que R$ 2.000 – descontar 15%)
	- salário liquido a receber
"""
salario=[]
for i in range(10):
	salario.append(int(input(f"Pessoa {i}: \n\tSalario= ")))

print(f"\n\nMaior salario = {max(salario)}\nMenor salario = {min(salario)}\n\nMedia salarial = {sum(salario)/len(salario)}\n")
print("\nImposto de Renda:")
for i in range(10):
	print(f"\n\tPessoa {i}: ")
	if salario[i]>2000:
		print("descontar 15%")
		salario[i]=salario[i]*75/100
	elif salario[i]>1500:
		print("descontar 10%")
		salario[i]=salario[i]*90/100
	else: print("isento")

print("\n\nSalario liquido:")
for i in range(10):
	print(f"\n\tPessoa {i}: = {salario[i]}")
