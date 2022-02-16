"""
QUESTAO 4 LISTA 7
Ler um formato de número inteiro e verificar se o número corresponde a uma data válida no calendário. Em seguida, escrever "Data Válida, 10 de julho de 2020, p.ex"; senão escrever uma mensagem "Data Inválida".
"""
data = input('Digite uma data no formato DIA/MÊS/ANO: ').replace(" ", "").split("/")

def data_existe(dia, mes, ano):
    def bissexto(ano):
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            return True
        else:
            return False
    if ano > 0 and 0 < mes <= 12 and 0 < dia <= 31:
        if dia <= 28:
                return True
        elif dia == 29 and bissexto(ano):
            return True
        elif dia == 30 and ( mes == 4 or mes == 6 or mes == 9 or mes == 11):
            return True
        elif dia == 31 and mes != 2:
            return True
    return False

if data_existe(int(data[0]), int(data[1]), int(data[2])):
    print('Data Válida')
else:
    print('Data Inválida')
