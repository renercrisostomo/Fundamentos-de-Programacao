"""
QUESTAO 6 LISTA 8
Faça um programa em python para ler uma matriz em python 3 x 3, informado pelo usuário, que represente uma turma de alunos com suas respectivas notas. Cada linha deverá conter o nome do aluno e duas notas. No final, o programa deverá emitir as seguintes informações:
a) Nome dos alunos com suas médias;
b) A maior e a menor média;
"""
matriz = []
media = []
print('Digite no formato nome, nota1, nota2')
for linha in range(3):
    nome, nota1, nota2 = input(f"-Digite o o nome e as notas do aluno {linha + 1}: ").replace(" ", "").split(",")
    matriz.append([nome, int(nota1), int(nota2)])

for i in range(3):
    aluno = matriz[i][0]
    media.append(sum(matriz[i][1:]) / 2)
    print(f'{aluno}: Média = {media[i]}')

print(f"Maior mádia: {min(media)}\nMenor média: {max(media)}")