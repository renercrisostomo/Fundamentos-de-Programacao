"""
QUESTAO 3 LISTA 2
Faça um algoritmo que leia um valor inteiro e verifica se o valor é par ou ímpar, retornando um valor booleano.
"""
x = int(input("Numero = "))
res = x % 2
if res==0:
	print("PAR")
else:
    print("IMPAR")