"""
QUESTÃO 4 LISTA 6 | TABELA DE CAMPEONATO DE FUTEBOL
Um campeonato de futebol foi disputado por N times identificados pelos seus nomes. Para cada time são considerados os seguintes dados:
PG - número de pontos ganhos (2 por vitória, 1 por empate, 0 por derrota)
GM - número de gols marcados
GS - número de gols sofridos (gols difíceis de marcar)
S - saldo de gols (GM - GS para os não atletas)
V - número de vitórias
GA - gol average (GM / GS, cuidado se GS = 0 )

(a) Dados os resultados de m jogos, imprima uma tabela com todos os dados (PG, GM, GS, S, V, GA, igual àquela que sai no jornal) dos n times. Cada resultado é representado na forma (t1,t2,n1,n2) cuja interpretação é a seguinte: no jogo t1 x t2 (times), o resultado foi n1 x n2 (placar);
Exemplo: (São Paulo, Milan, 3, 2) que foi o placar da vitória que deu ao São Paulo o BICAMPEONATO MUNDIAL.

(b) Com os mesmos dados do item (a), imprima a classificação dos times no campeonato (do primeiro para o último). A classificação é pelo número de pontos ganhos (PG) e em segundo lugar pelo saldo de gols (S). Se houver empate segundo os dois critérios, classifique os times envolvidos pelo maior número de gols marcados no campeonato.
"""

def adicionarDados(nome, marcados, sofridos):
    #Calcula e adiciona os pontos na tabela de dados
    #[nome, pontosGanhos, golsMarcados, golsSofridos, saldoGols, vitorias, golAvarage]

    #Seleciona o time nos dados ou adiciona se não existir
    for posicao in range(len(dados)):
        if dados[posicao][0] == nome:
            linha = posicao
            break
    else:
        dados.append([nome, 0, 0, 0, 0, 0, 0])
        linha = -1
    
    #Calculando todos os pontos
    if marcados > sofridos:
        dados[linha][1] += 2  #2 Pontos ganhos
        dados[linha][5] += 1  #Vitoria
    elif marcados == sofridos:
        dados[linha][1] += 1  #1 Ponto ganho
    
    dados[linha][2] += marcados  #Gols Marcados
    dados[linha][3] += sofridos  #Gols Sofridos
    dados[linha][4] += marcados - sofridos  #Saldo de Gols

numjogos = int(input("\nInsira o numero de jogos: "))
dados = []
print("\nAdicione os resultados no formato: Time1, Time2, Gols1, Gols2")

for jogo in range(numjogos):
    Time1, Time2, Gols1, Gols2 = input(f"Resultado do Jogo {jogo + 1}: ").replace(" ", "").split(",")
    adicionarDados(Time1, int(Gols1), int(Gols2))
    adicionarDados(Time2, int(Gols2), int(Gols1))

#Adicionando Gols Avarage
for i in range(len(dados)):
    if dados[i][3] == 0:
        dados[i][6] = "infinito"
    else:
        dados[i][6] = round(dados[i][2] / dados[i][3], 1)

print("\n[Nome, PG, GM, GS, S, V, GA]")
for linha in range(len(dados)):
    print(dados[linha])

#Classificação em: pontosGanhos, saldoGols, golsMarcados
print("\nClassificacao:")
colunas = [2, 4, 1]
for coluna in range(len(colunas)):
    dados.sort(key=lambda i: i[(coluna)], reverse=True)

print("\n   [Nome, PG, GM, GS, S, V, GA]")
for linha in range(len(dados)):
    print(f"{linha + 1}º {dados[linha]}")