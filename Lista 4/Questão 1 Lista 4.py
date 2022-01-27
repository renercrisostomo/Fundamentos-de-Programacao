"""
QUESTAO 1 LISTA 4
As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se
forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas,
calcule e escreva o custo total da compra. OBS: experimentar com menos de 12 e com mais de 12 quantidades.
"""
macas=int(input("Numero de Macas: "))
    
if macas<12:
	custo=1.30*macas
else:
	custo=macas
print(f"\nCusto = R$: {custo}")
