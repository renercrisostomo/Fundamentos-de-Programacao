"""
QUESTAO 2 LISTA 7
Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito, conforme a tabela abaixo:

Média | Conceito
de 0,0 a 4,9  | D
de 5,0 a 6,9  | C
de 7,0 a 8,9  | B
de 9,0 a 10,0 | A
"""
def conceito(media):
    if media > 10 or media < 0:
        return "Por favor, insira a media com numeros de 0 a 10 e tente novamente."
    elif media >= 9:
        return "Conceito: A"
    elif media >= 7:
        return "Conceito: B"
    elif media >= 5:
        return "Conceito: C"
    else:
        return "Conceito: D"

media = float(input("Media = "))
print(conceito(media))