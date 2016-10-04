
// Fibonacci.c
//    Realiza o calculo dos n  primeiros termos de um série de
// Fibonacci. O valor de n é passado como parâmetro na lina de
// comando.


#include <stdio.h>
#include <stdlib.h>

long unsigned int count=0;

int fibonacci(long long int num)
{
   char v[256][256]; // É apenas uma alocação de memória, não é
                     // importante para o cálculo
   unsigned int i, j;

   count ++;
   if(num==1 || num==2) {
       return 1;
   }
   else
       return fibonacci(num-1) + fibonacci(num-2);
} 


int main(int argc, char* argv[])
{
   int n,i;

   if ( argc == 2)
       n = (long long int) atoi(argv[1]);
   else
       n = 40; //valor default: 40 termos iniciais

   printf("\nA sequência de Fibonacci é: \n");
   for(i=0; i<n; i++)
       printf("%d ", fibonacci(i+1));
   printf("\n \n");
   printf("numero de vezes que função Fibonacci foi chamada %ld.\n", count);
   exit(0);
}

