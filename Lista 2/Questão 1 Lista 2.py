"""
QUESTAO 1 LISTA 2
Utilize uma estrutura de controle em um algoritmo que imprime a tabuada de 1 a 3.
"""
for num1 in range(1, 4):
	print(f"TABUADA DO {num1}\n")
	for num2 in range(11):
		x = num1 * num2
		print(f"{num1} x {num2} = {x}\n")
	print("\n")