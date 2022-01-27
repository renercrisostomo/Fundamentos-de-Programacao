"""
QUESTAO 1 LISTA 3
Fazer um algoritmo para ler 10 números digitados pelo usuário e depois informar qual maior valor e qual menor valor informado;
"""
num = []
for i in range(10):
    num.append(float(input(f"Numero {i+1} = ")))
print(f"\nMaior numero = {max(num)}\nMenor numero = {min(num)}")