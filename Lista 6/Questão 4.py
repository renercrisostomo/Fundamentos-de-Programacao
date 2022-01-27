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
    linha=-1
    for ln in range(len(dados)): #Procurando o Time nos dados e sua Linha
        if dados[ln][0]==nome: #Se achar o time, soma os novos dados
            linha=ln
    if linha==-1:
        dados.append([nome,0,0,0,0,0,0]) #Se não achar o time, adiciona uma nova linha de dados
    
    if marcados>sofridos:
        dados[linha][1]+=2 #Adicionando 2 Pontos de Gol se ganhou
        dados[linha][5]+=1 #Adicionando Vitoria
    elif marcados==sofridos:
        dados[linha][1]+=1 #Adicionando 1 Ponto de Gol se empatou
    
    dados[linha][2]+=marcados #Adicionando Gols Marcados
    dados[linha][3]+=sofridos #Adicionando Gols Sofridos
    dados[linha][4]+=marcados-sofridos #Adicionando Saldo de Gols

#Armazenando o numero de jogos
numjogos=int(input("\nInsira o numero de jogos: "))

#Calculando e armazenando os dados de cada time com base nos resultados
dados=[]
print("\nAdicione os resultados no formato: Time1, Time2, Gols1, Gols2")
for jogo in range(numjogos):
    resultado=((input(f"Resultado do Jogo {jogo+1}: ")).replace(" ","")).split(",")
    #Separando a string do resultado, calculando e armazenando os dados
    adicionarDados(resultado[0], int(resultado[2]), int(resultado[3]))
    adicionarDados(resultado[1], int(resultado[3]), int(resultado[2]))

#Calculando e Adicionando o Gols Avarage
for i in range(len(dados)):
    if dados[i][3]==0:
        dados[i][6]="infinito" #Adicionado Gols Avarage infinito se GS=0
    else:
        dados[i][6]=round(dados[i][2]/dados[i][3], 1) #Adicionado Gols Avarage
print("\n[Nome, PG, GM, GS, S, V, GA]") #Mostrando a Tabela dos dados
for linha in range(len(dados)):
    print(dados[linha]) #Mostrando cada linha

#ITEM B | Classificação: pontos ganhos (PG), saldo de gols (S) e gols marcados (GM)
print("\nClassificacao:")
colunas=[1, 4, 2] #Posição das colunas da classificação (PG, S, GM)
for linha in range(len(dados)): #Classifica a linha atual com relação as linhas anteriores
    for posicao in range(linha):
        for col in range(len(colunas)):
            if dados[linha][colunas[col]]>dados[posicao][colunas[col]]: #Compara dados da coluna
                dados.insert(posicao, dados[linha]) #Se maior, insere a linha de dados na nova posicao
                dados.pop(linha+1) #Remove a linha de dados da antiga posição
                posicao, col=linha, len(colunas)#encerra o for para classificar a linha seguinte

print("\n   [Nome, PG, GM, GS, S, V, GA]") #Mostrando a Tabela dos dados
for linha in range(len(dados)):
    print(f"{linha+1}º {dados[linha]}") #Mostrando cada linha