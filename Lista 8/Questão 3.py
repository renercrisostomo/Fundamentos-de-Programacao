"""
QUESTAO 3 LISTA 8
Escreva uma função em python para calcular e informar o MDC (Máximo Divisor Comum) de um número qualquer informado pelo usuário.
"""
def adicionarPrimo(listaPrimos):
    prox = listaPrimos[-1] + 1
    while True:
        for primo in range(len(listaPrimos)):
            if prox % listaPrimos[primo] == 0:
                prox += 1
                break
        else:
            break
    listaPrimos.append(prox)
    return listaPrimos

def mdc_function(listaNumeros):
    if len(listaNumeros) == 1:
        return listaNumeros [0]
        
    divisores = []
    listaPrimos = [2]
    listaDeUms = []
    for item in range(len(numeros)):
        listaDeUms.append(1)

    while listaNumeros != listaDeUms:
        naoDivididos = 0
        for numero in range(len(listaNumeros)):
            if listaNumeros[numero] % listaPrimos[-1] == 0:
                listaNumeros[numero] /= listaPrimos[-1]
            else:
                naoDivididos += 1  #Conta quantos não foram divididos pelo divisor primo

        if naoDivididos == 0:
            divisores.append(listaPrimos[-1])  #Adiciona o Divisor Comum
        elif naoDivididos == len(listaNumeros):
            listaPrimos = adicionarPrimo(listaPrimos)  #Adiciona mais um divisor primo

    mdc = 1
    for numero in divisores:  #Multiplica os divisores para encontrar o Máximo Divisor Comum
        mdc *= numero

    return mdc

numeros = input(f"Numeros (num1, num2...): ").replace(" ", "").split(",")
for item in range(len(numeros)):
    numeros[item] = int(numeros[item])

print(f'O MDC é igual a: {mdc_function(numeros)}')