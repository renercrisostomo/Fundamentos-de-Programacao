"""
QUESTAO 3 LISTA 4
Fa�a um algoritmo para ler o saldo de 5 clientes. Depois, dever� realizar opera��es de
d�bito e cr�dito: l� um cr�dito aleat�rio para cada cliente realizar saque (d�bito qualquer) da
conta de cada cliente (saldo_atual = cr�dito - d�bito). Tamb�m testar se saldo atual � suficiente para realizar o
saque, confirmando a opera��o, caso positivo, e negando a opera��o, caso negativo, mostrando a mensagem 'Saldo insuficiente'.
No final, dever� exibir o saldo atualizado de cada cliente.
"""
saldo=[]
for i in range(6):
		saldo.append(int(input(f"Pessoa {i+1}: \n\tSaldo Atual = ")))
	
for i in range(6):
	if saldo[i]>=debito:
		saldo[i] = credito - debito
	print(f"Pessoa {saldo[i]}: \n\tSaldo Atual = {i}")
