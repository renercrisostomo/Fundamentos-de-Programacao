/******************************************************************************

QUESTAO 3 LISTA 4
Fa�a um algoritmo para ler o saldo de 5 clientes. Depois, dever� realizar opera��es de
d�bito e cr�dito: l� um cr�dito aleat�rio para cada cliente; realizar saque (d�bito qualquer) da
conta de cada cliente; (saldo_atual = cr�dito - d�bito). Tamb�m testar se saldo atual � suficiente para realizar o
saque, confirmando a opera��o, caso positivo, e negando a opera��o, caso negativo, mostrando a mensagem 'Saldo insuficiente'.
No final, dever� exibir o saldo atualizado de cada cliente.

*******************************************************************************/

#include <stdio.h>

int main(void) {
	
	int i, saldo[6], credito, debito=50;
    
    for(i=1; i<=6; ++i){
		printf("Pessoa %d: \n\tSaldo Atual = ", i);
		scanf("%d", &saldo[i]);
	}
	
	for(i=1; i<=6; ++i){
		if(saldo[i]>=debito){
			saldo[i] = credito - debito;
		}
		printf("Pessoa %d: \n\tSaldo Atual = %d", saldo[i], i);
	}
	
    return 0;
}
