"""
QUESTAO 2 LISTA 8
Escreva uma função em python que, a partir de um vetor de cédulas [2, 5, 10, 20, 50, 100, 200], seja capaz de calcular e informar a menor quantidade de cédulas em um determinado saque. (P.ex.: “se a pessoa for sacar 250 reais, deverá obter 2 cédulas, uma de 200 e outra de 50”).
"""

def escolherCedulas(valor):
    cedulas = [2, 5, 10, 20, 50, 100, 200]
    escolhidas = []
    for cedula in range(-1, -(len(cedulas) + 1), -1):
        if valor // cedulas[cedula] != 0:
            escolhidas.append(f"{valor // cedulas[cedula]} x {cedulas[cedula]}")
            valor %= cedulas[cedula]
    return escolhidas

valor = int(input("digite o valor: "))
cedulas = escolherCedulas(valor)
for cedula in range(len(cedulas)):
    print(cedulas[cedula])