"""
QUESTAO 7 LISTA 2
Escreva um algoritmo para ler um número inteiro e verifique se o número corresponde a um mês válido no calendário. Depois escrever o nome do mês, senão escrever uma mensagem “Mês Inválido”.
"""
mes = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

try:
    print(mes[int(input("Numero do mes = "))-1])
except:
    print("Mes Invalido")

