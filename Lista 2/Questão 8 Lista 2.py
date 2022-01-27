"""
QUESTAO 8 LISTA 2
Faça um algoritmo que recebe a média final de um aluno e imprima o seu conceito, conforme a tabela abaixo:

Média | Conceito
de 0,0 a 4,9  | D
de 5,0 a 6,9  | C
de 7,0 a 8,9  | B
de 9,0 a 10,0 | A
"""
media=input("Media = ")
media=float(media)
if media>10 or media<0:
    print("Por favor, insira a media com numeros de 0 a 10 e tente novamente.")
elif media>=9:
    print("Conceito: A")
elif media>=7:
    print("Conceito: B")
elif media>=5:
    print("Conceito: C")
else:
    print("Conceito: D")