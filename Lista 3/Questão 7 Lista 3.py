"""
QUESTAO 7 LISTA 3
Faça um algoritmo para ler o peso e altura de 10 pessoas, em seguida, deve-se exibir
o resultado, conforme os dados da tabela abaixo.
"""
imc=[]
for i in range(10):
	imc.append(float(input(f"Pessoa {i}: \n\tIMC= ")))

print("\nClassificacao:")
for i in range(10):
	print("\n\tPessoa %d: ", i)
	if imc[i]>=40:
		print("Obesidade Grau III ou Morbida")
	elif imc[i]>=35:
		print("Obesidade Grau II")
	elif imc[i]>=30:
		print("Obesidade Grau I")
	elif imc[i]>=25:
		print("Sobrepeso")
	elif imc[i]>=18.5:
		print("Peso Normal")
	else:
		print("Abaixo do Peso")
