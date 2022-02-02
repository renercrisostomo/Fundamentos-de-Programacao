"""
QUESTÃO 1 LISTA 6
Deseja-se atualizar as contas correntes dos clientes de uma agência bancária. É dado o cadastro de 5 clientes contendo para cada um as seguintes informações: o número da conta, nome, saldo e OP (pode ser C ou D).; implemente uma matriz 5 x 5 que mostre o movimento bancário de cada um desses cliente.
"""
matriz=[[],[],[],[],[]]
print("Digite as informações no formato: númerodaConta, nome, saldo, OP")
for cliente in range(len(matriz)):
    matriz[cliente]=((input(f"-Cadastro do cliente {cliente+1}: ")).replace(" ","")).split(",")
for cliente in range(len(matriz)):
    print(matriz[cliente])
