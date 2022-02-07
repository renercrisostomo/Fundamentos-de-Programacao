"""
QUESTAO 5 LISTA 7
Dado os índices de massa corporal e sua classificação, conforme tabela abaixo, crie uma função em python para ler os valores (peso e altura) de uma pessoa e mostrar seu IMC, CLASSIFICAÇÃO e OBESIDADE.

IMC                 | CLASSIFICAÇÂO   | OBESIDADE (GRAU)
--------------------|-----------------|------------------
MENOR QUE QUE 18,5  | MAGREZA         | 0
ENTRE 18,5 E 24,9   | NORMAL          | 0
ENTRE 25,0 E 29,9   | SOBREPESO       | I
ENTRE 30,0 E 39,9   | OBESIDADE       | II
MAIOR QUE 40,0      | OBESIDADE GRAVE | III
"""

def classificacaoCorporal (peso, altura):
    print(f"\nIMC, CLASSIFICAÇÂO, OBESIDADE (GRAU)")
    imc = peso / altura ** 2
    if imc >= 40:
        print(f"{round(imc, 2)}, OBESIDADE GRAVE, III")
    elif imc >= 30:
        print(f"{round(imc, 2)}, OBESIDADE, II")
    elif imc >= 25:
        print(f"{round(imc, 2)}, SOBREPESO, I")
    elif imc >= 18.5:
        print(f"{round(imc, 2)}, NORMAL, 0")
    else:
        print(f"{round(imc, 2)}, MAGREZA, 0")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite seu altura (m): "))
classificacaoCorporal (peso, altura)