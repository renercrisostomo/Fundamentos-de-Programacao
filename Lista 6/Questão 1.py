"""
QUESTÃO 1 LISTA 6
Deseja-se atualizar as contas correntes dos clientes de uma agência bancária. É dado o cadastro de 5 clientes contendo para cada um as seguintes informações: o número da conta, nome, saldo e OP (pode ser C ou D).; implemente uma matriz 5 x 5 que mostre o movimento bancário de cada um desses cliente.
"""
matriz=[
    ['Conta1', 'José', -1000.0],
    ['Conta2', 'Maria', 2000.0],
    ['Conta3', 'Marcos', 0.0],
    ['Conta4', 'Carina', 30.0],
    ['Conta5', 'Rosa', -6.0]]

print("Digite as informações no formato: OP, Valor")
for conta in range(len(matriz)):
    print(f"\n{matriz[conta][0]}:\nCliente: {matriz[conta][1]} | Saldo: {matriz[conta][2]}")
    op, valor = input(f"Tipo(D ou C) e Valor da operação: ").replace(" ", "").split(",")
    matriz[conta].append(f"{op}: {valor}")
    valor = float(valor)
    if op.capitalize() == "C":
        valor *= -1
    matriz[conta].append(matriz[conta][2] + valor)

print("\n[Nº Conta, Cliente, Saldo, Operação, S.Atualizado]")
for conta in range(len(matriz)):
    print(matriz[conta])
