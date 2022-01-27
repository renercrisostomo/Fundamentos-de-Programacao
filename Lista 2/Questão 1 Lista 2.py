"""
QUESTAO 1 LISTA 2
Utilize uma estrutura de controle em um algoritmo que imprime a tabuada de 1 a 3.
"""
for i in range(3):
	print(f"TABUADA DO {i+1}\n")
	for j in range(11):
		x=(i+1)*j
		print(f"{i+1} x {j} = {x}\n")
	print("\n\n")