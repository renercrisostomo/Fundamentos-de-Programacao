/******************************************************************************

QUESTAO 7 LISTA 2
Escreva um algoritmo para ler um n�mero inteiro e verifique se o n�mero corresponde
a um m�s v�lido no calend�rio. Depois escrever o nome do m�s, sen�o escrever uma
mensagem �M�s Inv�lido�.

*******************************************************************************/

#include <stdio.h>

int main(void)
{
	int mes;
	scanf("%d", &mes);
	switch (mes)
	{
		case 1:
		printf("Janeiro");
		break;
		
		case 2:
		printf("Fevereiro");
		break;
		
		case 3:
		printf("Marco");
		break;
		
		case 4:
		printf("Abril");
		break;
		
		case 5:
		printf("Maio");
		break;
		
		case 6:
		printf("Junho");
		break;
		
		case 7:
		printf("Julho");
		break;
		
		case 8:
		printf("Agosto");
		break;
		
		case 9:
		printf("Setembro");
		break;
		
		case 10:
		printf("Outubro");
		break;
		
		case 11:
		printf("Novembro");
		break;
		
		case 12:
		printf("Dezembro");
		break;
		
		default:
		printf("Mes Invalido");
	}

	return 0;
}

