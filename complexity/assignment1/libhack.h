#ifndef __LIB_HACK__ 
#define __LIB_HACK__ 

/*--------------------------------------------
 * LibHack - Simulador de Recrutamento Hacker
 * Autor: Árton Pereira Dorneles
 * E-mail: <arton.dorneles@inf.ufrgs.br>
 * Última modificação: 14/09/2016 
 * Versão 0.2
 * ------------------------------------------*/

#define COMPUTER 'C'
#define SENSOR 'S'
#define DOOR 'D'
#define WALL '#'
#define EMPTY ' '
#define MAX_HACK_ATTEMPTS 3 /*Número máximo de tentativas de hacker algum dispositivo*/
#define SPEED_IMPROVEMENT_FACTOR 4 /*Fator de melhoria na velocidade ao hackear um sensor.*/

/* Estrutura do Problema 1: 
 * Encontrar o número com a maior quantidade de digitos que aparece em a e b*/
typedef struct {
   int n; //Tamanho do problema
   char* a; //String de tamanho n 
   char* b; //String com tamanho n
} Problem1;

/* Estrutura do Problema 2:
 * Encontrar o maior número primo que divide a */
typedef struct {
   int n; //Tamanho do problema
   char* a; //String de tamanho n contendo um número
} Problem2;

/* Ações hacker */
Problem1 inspectComputer(int i, int j); //Obtém o problema para hacker o computador i,j 
Problem2 inspectSensor(int i, int j); //Obtém o problema para hacker o sensor i,j
Problem2 inspectDoor(int i, int j); //Obtém o problema para hacker a porta i,j
int hackComputer(int i, int j, char* key); //Tenta hacker o computador i,j com a chave key. Retorna flag indicando sucesso.
int hackSensor(int i, int j, char* key);//Tenta hacker o sensor i,j com a chave key. Retorna flag indicando sucesso.
int hackDoor(int i, int j, char* key);//Tenta hacker a porta i,j com a chave key. Retorna flag indicando sucesso.

/* Métodos do hacker */
int moveHackerTo(int i, int j); //Move o hacker para posição i,j. Pode demorar dependendo da velocidade.
int getHackerCol(); //Obtém a coluna que o hacker está localizado.
int getHackerRow(); //Obtém a linha que o hacker está localizado.
double getHackerSpeed(); //Obtém a velocidade atual
void hackerSpeak(char* text); //O hacker pode falar em seus momentos de glória, mas até 13 caracteres. Aparece na arena gráfica por um  breve instante em cima do hacker.
void setHackerName(char* name); // Define o nome do hacker (grupo). Obrigatoriamente deve ser chamado antes de readMap(). Usado na arena gráfica para a batalha e ranking.

/* Métodos do mapa */
void setMapSeed(int seed); //Define a semente do mapa. Selecione seed = 0 para mapa aleatório.
int getMapSeed(); //Obtém a semente do mapa. Utilize após uma chamada a readMap().
char** readMap(); //Obtém um ponteiro para a matriz do mapa.
void printMap(); //Imprime o mapa
int getMapRows(); //Obtém número de linhas do mapa.
int getMapCols(); //Obtém número de colunas do mapa.

/* UTILS */
int getDistance(int r1, int c1, int r2, int c2); //Calcula a distância de manhattan entre (r1,c1) e (r2,c2)
void printProblems(); //Usado para fins de debug, caso necessário.

#endif /* __LIB_HACK__ */
