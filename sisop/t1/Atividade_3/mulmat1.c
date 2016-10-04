
// Multiplicação de matrizes: multmat_1
//    Matrizes declaradas como globais e inicializadas (área .data alocada)

#include <stdio.h>
#include "mulmat.h"

int a[MAXSIZE][MAXSIZE]={1};
int b[MAXSIZE][MAXSIZE]={2};
int c[MAXSIZE][MAXSIZE]={3};

int main(int argc, char *argv[]) {
	
    int i, j, k;

    // Efetua multiplicação em loop infinito

    for(i=0;i<MAXSIZE;i++)
        for(j=0;j<MAXSIZE;j++) {
           c[i][j] = 0;
           a[i][j] = a[i][j];
           b[i][j] = b[i][j];
        }

    for(;;) {
	for(i=0;i<MAXSIZE;i++)
            for(j=0;j<MAXSIZE;j++)
	       for(k=0;k<MAXSIZE;k++)
		   c[i][j] = c[i][j] + a[i][k] * b[k][j];
    }

    // O programa nunca chega aqui!
}
