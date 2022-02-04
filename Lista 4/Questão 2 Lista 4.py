"""
QUESTAO 2 LISTA 4
A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas, em um total de 10 funcionários e depois mostre também qual destes obteve maior número de horas trabalhadas. (considere um mês com 4 semanas exatas).
"""
SalarioPorHora = int(input("Salario por hora = "))
SalarioExtra = SalarioPorHora + SalarioPorHora * 50 / 100
HorasMes, salario = [], []
for i in range(10):
	HorasMes.append(int(input(f"Pessoa {i}: \n\thoras trabalhadas no mes= ")))
	salario.append(SalarioPorHora * HorasMes[i])
	
	if HorasMes[i] > 160:
		salario[i] += SalarioExtra * (HorasMes[i] - 160)
	print(f"\tsalario = {salario[i]}\n")

for i in range(10):
	if HorasMes[i] > HoraMaior:
		HoraMaior = HorasMes[i]
print(f"\n\nMaior hora = {HoraMaior}\n")