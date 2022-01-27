"""
QUESTAO 3 LISTA 3
A série fibonacci é formada pele seguinte sequência: 1, 1, 2, 3, 5, 8, 13, 13, 21, 34, 55...etc.
Escreva um algoritmo que gere a serie fibonacci até o 12o termo;
"""
sequencia=[1, 1]
for i in range(10):
	sequencia.append(sequencia[i+1]+sequencia[i])
print(sequencia)

