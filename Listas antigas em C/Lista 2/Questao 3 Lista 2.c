/*
QUESTAO 3 LISTA 2
Fa�a um algoritmo que leia um valor inteiro e verifica se o valor � par ou �mpar, retornando um valor booleano.
*/

#include <stdio.h>

int main(void)
{
	int x, res;
	printf("Numero = ");
	scanf("%d",&x);
	res=x%2;
	if(res==0){
		printf("PAR");
	}else{
		printf("IMPAR");
	}
	return 0;
}


