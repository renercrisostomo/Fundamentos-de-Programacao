/******************************************************************************

QUESTAO 9 LISTA 2
Fa�a um algoritmo que leia do teclado um caractere c e dois inteiros n1 e n2. Proceda da seguinte forma utilizando uma estrutura de controle:
Se o caractere for '+', calcule e imprima a soma n1 + n2.
Se o caractere for '-', calcule e imprima a subtra��o n1 - n2.
Se o caractere for '/', calcule e imprima a divis�o n1 / n2.
Se o caractere for '*', calcule e imprima a multiplica��o n1 * n2.
Caso contr�rio, exiba "Opera��o Inv�lida".

*******************************************************************************/

#include <stdio.h>

int main(void)
{
	char c;
	int n1, n2;
	float r;
	
	scanf("%s",&c);
	scanf("%d",&n1);
	scanf("%d",&n2);
	
	switch( c )
    {
        case '+':
        r=n1 + n2;
        printf("%f", r);
        break;

    	case '-':
        r=n1 - n2;
        printf("%f", r);
        break;

    	case '*':
    	r=n1 * n2;
    	printf("%f", r);
        break;

    	case '/':
        if(n2 != 0){
            r= n1 / n2;
            printf("%f", r);
        }
        else{
            printf("Nao existe divisao por 0\n\n");
        }
        break;

    	case '%':
        r=n1 % n2;
        printf("%f", r);
        break;

    	default:
        printf("Operacao invalida\n\n");
    }
    return 0;
}


