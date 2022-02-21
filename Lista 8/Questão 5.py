"""
QUESTAO 5 LISTA 8
Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Faça um programa em python que leia os nomes e os tempos (em segundos) de cada volta de cada corredor e guarde as informações em uma matriz. Ao final, o programa deve informar:
a) De quem foi a melhor volta da prova e em que volta;
b) Classificação final em ordem (1º o campeão);
c) Qual foi a volta com a média mais rápida.
"""
print('Digite no formato nome, nota1, nota2')
for linha in range(5):
    for tempos in range(10):
        nome, tempo1, tempo2, 3, 4, = input(f"-Digite o o nome e as notas do aluno {linha + 1}: ").replace(" ", "").split(",")
        matriz.append([nome, int(nota1), int(nota2)])