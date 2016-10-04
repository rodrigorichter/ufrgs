
// Multiplicação de matrizes: mulmat_0
//   Matrizes declaradas como globais e não-inicializada (.data não é alocada)

#include <stdio.h>
#include "mulmat.h"

int a[MAXSIZE][MAXSIZE];
int b[MAXSIZE][MAXSIZE];
int c[MAXSIZE][MAXSIZE];

int main(int argc, char *argv[]) {
	
    int i, j, k;

    // Efetua multiplicação em loop infinito

    for(i=0;i<MAXSIZE;i++)
        for(j=0;j<MAXSIZE;j++){
           c[i][j] = 0;
           a[i][j] = a[i][j] + 1;
           b[i][j] = b[i][j] - 1;
        }

    for(i=0;i<MAXSIZE;i++)
        for(j=0;j<MAXSIZE;j++)
	    for(k=0;k<MAXSIZE;k++)
		c[i][j] = c[i][j] + a[i][k] * b[k][j];


    // O programa nunca chega aqui!
}
