'''
QUESTAO 5 LISTA 3
Faça um algoritmo que leia a data de nascimento de 10 pessoas, depois calcule a idade de cada uma, informando-a. E, por último, mostre qual a pessoa mais jovem e a mais velha do grupo.
'''
#include <time.h>

int data[11][3], Idade[11], dias[11], Velho=0, Novo=0, i
time_t mytime
mytime = time(NULL)
struct tm tm = *localtime(&mytime)
data[0][0] = tm.tm_mday
data[0][1] = tm.tm_mon + 1
data[0][2] = tm.tm_year + 1900
print(f"Data Atual: {data[0][0]}/{data[0][1]}/{data[0][2]}\n")
dias[0] = 365*data[0][2] + 30*data[0][1] + data[0][0]

print("\nData de Nascimento:")
for i in range(1, 11):
	data[i][0]=int(input(f"\n\tPessoa {i} = Dia: "))
	data[i][1]=int(input("\t\t   Mes: "))
	data[i][2]=int(input("\t\t   Ano: "))
	dias[i] = 365*data[i][2] + 30*data[i][1] + data[i][0]
	Idade[i] =(dias[0]-dias[i])/365

print("\nIdades:")
int dias_menor=dias[0]-dias[1], dias_maior=dias[0]-dias[1]
for i in range(1, 11):
	print(f"\n\tPessoa {i} = {Idade[i]} ano(s)")
	dias[i] = dias[0]-dias[i]
	if dias[i]>dias_maior:
		dias_maior=dias[i]
		Velho=i
		
	if dias[i]<dias_menor:
		dias_menor=dias[i]
		Novo=i
	
print("\n\nMais Velha = Pessoa {}\nMais Nova = Pessoa {}", Velho, Novo)
