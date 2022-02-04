"""
QUESTAO 6 LISTA 3
Fazer um algoritmo para calcular e imprimir a media aritmética de 10 alunos, tendo como dados de entrada 3 notas semestrais. Depois imprimir situação do aluno que deve
obedecer ao seguinte critério: (media maior ou igual a 7, “aprovado”; entre 4 e 6.9, “AF”; menor que 4, “reprovado”), depois imprimir a media geral da turma;
"""
aluno = []
for a in range(len(aluno)):
	print(f"\nAluno(a) {a + 1}:")
	for i in range(3):
		aluno[a].append(float(input(f"\tNota {i + 1} = ")))

for a in range(len(aluno)):
	print(f"\nAluno(a) {a + 1}:")
	media = (aluno[a][0] + aluno[a][1] + aluno[a][2]) / 3
	if media >= 7:
		situacao = " --- Aprovado(a)"
	elif media >= 4:
		situacao = " --- AF"
	else:
		situacao = " --- Reprovado(a)"
	print(f"\tMedia = {media} {situacao}")
	