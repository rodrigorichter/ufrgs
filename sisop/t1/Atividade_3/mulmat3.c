

// Multiplicação de matrizes: multmat_3
//    Matrizes declaradas ponteiros e alocadas dinamicamente

#include <stdio.h>
#include <stdlib.h>
#include "mulmat.h"

int main(int argc, char *argv[]) {

   int *a, *b, *c;
   int i, j, k;

// aloca dinamicamente a área para as matrizes

    a = (int *)malloc(sizeof(int)*MAXSIZE*MAXSIZE);
    b = (int *)malloc(sizeof(int)*MAXSIZE*MAXSIZE);
    c = (int *)malloc(sizeof(int)*MAXSIZE*MAXSIZE);

    if (a == NULL || b == NULL || c == NULL) {
           printf("Erro de alocação de memória para as matrizes!!\n");
           exit(0);
    }

// multiplica as matrizes

    for(i=0;i<MAXSIZE;i++)
        for(j=0;j<MAXSIZE;j++) {
           *(int *)(c + i*MAXSIZE + j) = 0;
           *(int *)(a + i*MAXSIZE + j) = *(int *)(a + i*MAXSIZE + j) + 1;
           *(int *)(b + i*MAXSIZE + j) = *(int *)(b + i*MAXSIZE + j) - 1;
         }
  
    for(;;) 
	for(i=0;i<MAXSIZE;i++)
            for(j=0;j<MAXSIZE;j++)
	       for(k=0;k<MAXSIZE;k++)
                   *(int *)(c + i*MAXSIZE+j) =  *(int *)(c + i*MAXSIZE+j) + 
                                                *(int *)(a + i*MAXSIZE+k) * 
                                                *(int *)(b + k*MAXSIZE+i);

}
