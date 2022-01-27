/******************************************************************************

QUESTAO 2 LISTA 4
A jornada de trabalho semanal de um funcion�rio � de 40 horas. O funcion�rio que
trabalhar mais de 40 horas receber� hora extra, cujo c�lculo � o valor da hora regular
com um acr�scimo de 50%. Escreva um algoritmo que leia o n�mero de horas trabalhadas em um m�s,
o sal�rio por hora e escreva o sal�rio total do funcion�rio, que dever� ser acrescido das horas extras,
caso tenham sido trabalhadas, em um total de 10 funcion�rios e depois mostre tamb�m qual destes obteve
maior n�mero de horas trabalhadas. (considere um m�s com 4 semanas exatas).

*******************************************************************************/

#include <stdio.h>

int main(void) {
	
	int i, HorasMes[11], SalarioPorHora, HoraMaior=HorasMes[1];
    float salario[11], SalarioExtra;
    
    printf("Salario por hora = ", SalarioPorHora);
    scanf("%d", &SalarioPorHora);
    SalarioExtra=SalarioPorHora+SalarioPorHora*50/100;
    
    for(i=1; i<=10; ++i){
		printf("Pessoa %d: \n\thoras trabalhadas no mes= ", i);
		scanf("%d", &HorasMes[i]);
		salario[i]=SalarioPorHora*HorasMes[i];
		
		if(HorasMes[i]>160){
			salario[i]+=SalarioExtra*(HorasMes[i]-160);
		}
		printf("\tsalario = %f\n", salario[i]);
	}
	
	for(i=1; i<=10; ++i){
		if(HorasMes[i]>HoraMaior){
			HoraMaior=HorasMes[i];
		}
	}
	printf("\n\nMaior hora = %d\n", HoraMaior);
	
    return 0;
}
