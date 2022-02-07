"""
QUESTAO 1 LISTA 7
Apresente um programa em python que leia do teclado um caractere c e dois inteiros n1 e n2. Proceda da seguinte forma:

1. Se o caractere for `+`, calcule e imprima a soma `n1 + n2`.

2. Se o caractere for `-`, calcule e imprima a subtração `n1 - n2`.

3. Se o caractere for `/`, calcule e imprima a divisão `n1 / n2`.

4. Se o caractere for `*`, calcule e imprima a multiplicação `n1 * n2`.

Caso contrário, exiba `Operação Inválida`.
"""

n = []
for i in range(2):
    n.append(int(input(f"Numero {i + 1} = ")))
operacao = {
    "+": n[0] + n[1],
    "-": n[0] - n[1],
    "*": n[0] * n[1],
    "/": n[0] / n[1]
}
print(f"Resultado = {operacao[input('Operacao = ')]}")