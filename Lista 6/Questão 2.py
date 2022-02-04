"""
QUESTÃO 2 LISTA 6
Deseja-se fazer a emissão da folha de pagamento de uma empresa. Para os 4 funcionários de uma empresa são dadas as seguintes informações: (matrícula, nome, função e salário). Implemente uma matriz 4 x 4 para emissão dessas informações, depois mostre quem ganha o maior e o menor salário.
"""
matriz, salarios = [[], [], [], []], []
print("Digite as informações nessa formatação: matrícula, nome, função, salário")
for funcionario in range(len(matriz)):
    matriz[funcionario] = ((input(f"Funcionario {funcionario + 1}: ")).replace(" ","")).split(",")
    matriz[funcionario][3] = int(matriz[funcionario][3])
    salarios.append(matriz[funcionario][3])  #Adicionando os salarios em outra lista

print("\n[matrícula, nome, função, salário]")
for linha in range(len(matriz)):
    print(matriz[linha])
    if matriz[linha][3] == max(salarios):  #Se o salario for igual ao maior, armazena o nome
        melhorRemunerado = matriz[linha][1]
    elif matriz[linha][3] == min(salarios):  #Se o salario for igual ao menor, armazena o nome
        piorRemunerado = matriz[linha][1]
print(f"Melhor salario: {melhorRemunerado}\nMenor salario: {piorRemunerado}")