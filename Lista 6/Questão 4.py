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
#Linhas de Dados:[nome, pontosGol, golsMarcados, golsSofridos, saldodeGols, vitorias, golAvarage]
def adicionarDados(nome, marcados, sofridos):
    #Calcula e adiciona os dados na tabela com base no resultado

    #Seleciona o time nos dados ou adiciona se não existir
    for posicao in range(len(dados)):
        if dados[posicao][0] == nome:
            linha = posicao
            break
        
    if 'linha' not in locals():
        dados.append([nome,0,0,0,0,0,0])
        linha = -1
    
    #Calculando todos os pontos
    if marcados > sofridos:
        dados[linha][1] += 2 #2 Pontos de Gol
        dados[linha][5] += 1 #Vitoria
    elif marcados == sofridos:
        dados[linha][1] += 1 #1 Ponto de Gol
    
    dados[linha][2] += marcados #Gols Marcados
    dados[linha][3] += sofridos #Gols Sofridos
    dados[linha][4] += marcados - sofridos #Saldo de Gols

numjogos = int(input("\nInsira o numero de jogos: "))
dados = []
print("\nAdicione os resultados no formato: Time1, Time2, Gols1, Gols2")

for jogo in range(numjogos):
    resultado = ((input(f"Resultado do Jogo {jogo + 1}: ")).replace(" ","")).split(",")
    adicionarDados(resultado[0], int(resultado[2]), int(resultado[3]))
    adicionarDados(resultado[1], int(resultado[3]), int(resultado[2]))

#Adicionando Gols Avarage
for i in range(len(dados)):
    if dados[i][3] == 0:
        dados[i][6] = "infinito"
    else:
        dados[i][6] = round(dados[i][2] / dados[i][3], 1)

print("\n[Nome, PG, GM, GS, S, V, GA]") 
for linha in range(len(dados)):
    print(dados[linha])

#Classificação: pontos ganhos (PG), saldo de gols (S) e gols marcados (GM)
print("\nClassificacao:")
colunas = [1, 4, 2] #(PG, S, GM)

#Checa de um em um se o cada elemento é maior
for time in range(len(dados)):
    for linha in range(time):
        for elem in range(len(colunas)):
            if dados[time][colunas[elem]] > dados[linha][colunas[elem]]:
                dados.insert(linha, dados[time]) 
                dados.pop(time + 1)
                linha = time  #encerra o for para classificar o proximo time
                break
            elif dados[time][colunas[elem]] < dados[linha][colunas[elem]]:
                dados.insert(linha + 1, dados[time]) 
                dados.pop(time + 1)
                linha = time  #encerra o for para classificar o proximo time
                break

print("\n   [Nome, PG, GM, GS, S, V, GA]")
for linha in range(len(dados)):
    print(f"{linha + 1}º {dados[linha]}")