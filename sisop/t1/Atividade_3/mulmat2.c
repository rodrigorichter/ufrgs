
// Multiplicação de matrizes: mulmat2.c
//    Matrizes alocadas no corpo da função main.

#include <stdio.h>
#include "mulmat.h"


int main(int argc, char *argv[]) {
	
    int i, j, k;
    int a[MAXSIZE][MAXSIZE]={1};
    int b[MAXSIZE][MAXSIZE]={2};
    int c[MAXSIZE][MAXSIZE]={3};

    // Efetua multiplicação em loop infinito

    for(i=0;i<MAXSIZE;i++)
        for(j=0;j<MAXSIZE;j++)
           c[i][j] = 0;

    for(;;)
     for(i=0;i<MAXSIZE;i++)
            for(j=0;j<MAXSIZE;j++)
	       for(k=0;k<MAXSIZE;k++)
		   c[i][j] = a[i][k] * b[k][j];

    // O programa nunca chega aqui!
}
