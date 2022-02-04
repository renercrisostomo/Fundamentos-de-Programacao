"""
QUESTAO 3 LISTA 4
Faça um algoritmo para ler o saldo de 5 clientes. Depois, deverá realizar operações de débito e crédito: lê um crédito aleatório para cada cliente realizar saque (débito qualquer) da conta de cada cliente (saldo_atual = crédito - débito). Também testar se saldo atual é suficiente para realizar o saque, confirmando a operação, caso positivo, e negando a operação, caso negativo, mostrando a mensagem 'Saldo insuficiente'. No final, deverá exibir o saldo atualizado de cada cliente.
"""
saldo = []
for i in range(6):
		saldo.append(int(input(f"Pessoa {i + 1}: \n\tSaldo Atual = ")))
	
for i in range(6):
	if saldo[i] >= debito:
		saldo[i] = credito - debito
	print(f"Pessoa {saldo[i]}: \n\tSaldo Atual = {i}")
