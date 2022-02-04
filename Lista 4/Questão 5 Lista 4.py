"""
QUESTAO 5 LISTA 4
O sistema do governo quer verificar um grupo de empregados apto para a aposentadoria ou não. Para estar em condições, os seguintes requisitos devem ser satisfeitos: - Ter no mínimo 65 anos de idade e ter trabalhado no mínimo 35 anos é homens ter 60 anos de idade e ter trabalhado 30 anos - mulheres. Com base nessas informações, faça um algoritmo que leia (para 6 empregados): o nome, sexo, ano de nascimento e os anos de contribuições. O programa deverá escrever: nome, idade, sexo e o tempo de trabalho de cada empregado com a mensagem 'Apto para aposentadoria' ou 'Não apto para aposentadoria'.
"""
nome, idade, sexo, tempoDeTrabalho = [], [], [], []
for i in range(6):
	nome.append(int(input(f"Pessoa {i + 1}: \n\tNome: ")))
	idade.append(int(input("\tIdade: ")))
	sexo.append(int(input("\tSexo(M|F): ")))
	tempoDeTrabalho.append(int(input("\tTempo de Trabalho: ")))
	
for i in range(6):
	print(f"\n\nPessoa {i + 1}: \n\tNome: {nome[i]} Idade: {idade[i]} Sexo: {sexo[i]} Tempo de Trabalho: {tempoDeTrabalho[i]}\n")
	
	if sexo[i] == "M" and idade[i] >= 65 and tempoDeTrabalho[i] >= 35 or sexo[i] == "F" and idade[i] >= 60 and tempoDeTrabalho[i] >= 30:
		print("Apto para aposentadoria")
	else:
		print("Nao apto para aposentadoria")
