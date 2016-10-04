/*
 * cdata.h: arquivo de inclusão de uso apenas na geração da libpithread
 *
 * Esse arquivo pode ser modificado. ENTRETANTO, deve ser utilizada a TCB fornecida.
 *
 */

#ifndef __cdata__
#define __cdata__

#define	PROCST_CRIACAO	0
#define	PROCST_APTO	1
#define	PROCST_EXEC	2
#define	PROCST_BLOQ	3
#define	PROCST_TERMINO	4

/* NÃO ALTERAR ESSA struct */
typedef struct s_TCB { 
	int		tid; 		// identificador da thread
	int		state;		// estado em que a thread se encontra
					// 0: Criação; 1: Apto; 2: Execução; 3: Bloqueado e 4: Término
        int		ticket;		// 0-255: bilhete de loteria da thread
	ucontext_t 	context;	// contexto de execução da thread (SP, PC, GPRs e recursos) 
} TCB_t; 

//Flag para verificar se o ccreate está sendo chamado na primeira vez
int firstTime = 1;
/*Numero correspondente ao tid de cada thread nova. Começa em 0 e
vai sendo incrementado a cada nova thread criada*/
int tidIndex = 0;
//Declaração de filas
FILA2 fila_aptos;
FILA2 fila_bloqueados;
FILA2 fila_executando;
FILA2 fila_terminados;

#endif

// comando para compilar
//gcc -o filas.c ../bin/support.o -lm