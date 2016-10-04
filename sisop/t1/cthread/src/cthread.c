#include	<sys/time.h>
#include	<stdio.h>
#include	<pthread.h>
#include	<stdlib.h>
#include	<string.h>
#include 	<ucontext.h>
#include	"../include/support.h"
#include	"../include/cdata.h"

/* criação de thread: É inicializado um pthread e um TCB.
O pthread é o espaço de memória aonde vai ficar a thread em si,
e o pthread_create é a chamada do SO que vai criar a thread.
o TCB é a estrutura que vai armazenar as informações dessa thread, e 
vai passar para a biblioteca support, que administra a fila.
*/
int ccreate (void* (*start)(void*), void *arg) {
	if (FirstTime) {
		CreateFila2(fila_aptos);
		CreateFila2(fila_bloqueados);
		CreateFila2(fila_executando);
		CreateFila2(fila_terminados);

		TCB_t *main_tcb;
		main_tcb = (TCB_t *)malloc(sizeof(TCB_t));
		
		getcontext(&(main_tcb->context));

		main_tcb->tid = tidIndex;
		tidIndex++;
		//main_tcb->context.uc_stack.ss_sp = malloc(SIGSTKSZ);
		//main_tcb->context.uc_stack.ss_size = SIGSTKSZ;
		//nao sei se precisa fazer isso ou nao

		AppendFila2(fila_aptos, tcb_main);

		firstTime = 0;
	}

	ucontext_t main_context;
	TCB_t *tcb;

	tcb = (TCB_t *)malloc(sizeof(TCB_t));

	getcontext(&main_context);
	getcontext(&(tcb->context));

	tcb->tid = tidIndex;
	tidIndex++;
	tcb->state = PROCST_CRIACAO;
	tcb->ticket = Random2();

	tcb->context.uc_link		  = &main_context;
	tcb->context.uc_stack.ss_sp   = malloc(SIGSTKSZ);
	tcb->context.uc_stack.ss_size = SIGSTKSZ;

	makecontext(&(tcb->context),(void (*)(void)) start, 1, arg);
	AppendFila2(fila_aptos, tcb);

	return tcb->tid;
}

int cyield(void) {
	return -1;
}

int cjoin(int tid)  {
	FirstFila2(fila_terminados);
	int threadTerminou = 0;
	TCB_t *tcb;

	while (threadTerminou == 0) {
		tcb = GetAtIteratorFila2(fila_terminados);
		if (tcb != NULL) {
			if (tcb->tid == tid) threadTerminou = 1;
		}

		NextFila2(fila_terminados);

	}
	return 0;

}

int csem_init(csem_t *sem, int count) {
	return -1;
}

int cwait(csem_t *sem) {
	return -1;
}

int csignal(csem_t *sem) {
	return -1;
}

int cidentify(char *name, int size) {
	return -1;
}