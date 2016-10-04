#include <stdio.h>
#include <sys/time.h>
#include <sys/resource.h>
 
int contador = 0;
 
void funcao_recursiva(void){
    int i, j;

    i = j; /*operação sem sentido. É apenas para consumir memória */

    printf("chamando pela %d vez\n",++contador);
    funcao_recursiva();
}
  
int main() {
    struct rlimit rlim;

    getrlimit(RLIMIT_STACK, &rlim);
    printf("\nSoft limite da pilha (bytes): %d  (%d KB)\n", (unsigned int)rlim.rlim_cur, 
           (unsigned int)rlim.rlim_cur/1024);
    printf("Hard limite da pilha (bytes): %ld\n", (unsigned long int)rlim.rlim_max);
    printf ("Pressione ENTER para continuar...\n"); getchar();
    funcao_recursiva();
}
