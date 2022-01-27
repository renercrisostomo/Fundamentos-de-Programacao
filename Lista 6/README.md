# Lista 6

**Questão 1**

 Deseja-se atualizar as contas correntes dos clientes de uma agência bancária. É dado o cadastro de 5 clientes contendo para cada um as seguintes informações: o número da conta, nome, saldo e OP (pode ser C ou D).; implemente uma matriz 5 x 5 que mostre o movimento bancário de cada um desses cliente.

**Questão 2**

 Deseja-se fazer a emissão da folha de pagamento de uma empresa. Para os 4 funcionários de uma empresa são dadas as seguintes informações: (matrícula, nome, função e salário). Implemente uma matriz 4 x 4 para emissão dessas informações, depois mostre quem ganha o maior e o menor salário.

**Questão 3**

 Dizemos que uma matriz quadrada inteira é um quadrado mágico se a soma dos elementos de cada linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais.
 Exemplo: A matriz
 8| 0|7
 4| 5|6
 3|10|2
 é um quadrado mágico.
 
 Implemente uma matriz quadrada (quadrado mágico), insira valores aleatórios e, depois, mostre a mensagem “É uma matriz QUADRADO MÁGICO” ou “NÃO é uma matriz QUADRADO MÁGICO” e os seus valores.

**Questão 4 | tabela de campeonato de futebol**

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