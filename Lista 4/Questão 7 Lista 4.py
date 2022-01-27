"""
QUESTAO 7 LISTA 4
A prefeitura de uma cidade deseja fazer uma pesquisa para coletar dados sobre o salário e número de filhos de cada habitante. Faça um algoritmo para ler os dados de 5 habitantes e escrever:
a) Média de salário da população
b) Média do número de filhos
c) Percentual de pessoas com salário menor que R$ 1000,00.
"""
Dados,MenoresQue1000=[[],[]],0
for i in range(4):
	Dados[0].append(int(input(f"Pessoa {i+1}: \n\tSalario = ")))
	Dados[1].append(int(input("\tNumero de Filhos = ")))
	if Dados[0][-1]<1000:
		MenoresQue1000+=1
MenoresQue1000*=100/5

print(f"\n\tMedia Salarial = {sum(Dados[0])/len(Dados[0])}")
print(f"\n\tMedia do numero de Filhos = {sum(Dados[1])/len(Dados[1])}")
print(f"\n\tPercentual de salarios menores que 1000 = {MenoresQue1000}")
