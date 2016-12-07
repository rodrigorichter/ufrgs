#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "libhack.h"
#include "header.h"

typedef struct elementPosition {
    int row;
    int col;
    int distanceFromHacker;
    int hasBeenHacked;
} epos;

int main(int argc, char** argv) {
	if (argc > 1) {
	  setMapSeed(atoi(argv[1]));
	}

	setHackerName("Cypherpunks");
	char** map = readMap();
	printMap();
	hackerSpeak("Easy peasy");
	printf("Hacker Info:  Position = (%d,%d)  Speed = %1.0f\n",getHackerRow(),getHackerCol(),getHackerSpeed());

	int mapCols = getMapCols();
	int mapRows = getMapRows();
	Problem2 doorProblem;
	Problem1 computerProblem;
	Problem2 sensorProblem;
	char computersAnswers[100][1000];
	int amountOfComputers = 0;
    epos elementsPosition[1000];
    int amountOfElements = 0;
    printf("Map Size: (%d,%d)\n",mapRows,mapCols);

    // olha no mapa para descobrir quais sao, onde estao e a qual a distancia do hacker
    amountOfElements = 0;
    for (int i = 0; i < mapRows; i++) {
        for (int j = 0; j < mapCols; j++) {
            if (map[i][j] == COMPUTER || map[i][j] == SENSOR) {
                elementsPosition[amountOfElements].hasBeenHacked = 0;
                elementsPosition[amountOfElements].row = i;
                elementsPosition[amountOfElements].col = j;

                int d = getDistance(i,j, getHackerRow(),getHackerCol());
                elementsPosition[amountOfElements].distanceFromHacker = d;
                amountOfElements++;
            }
        }
    }

    // faz o algoritmo de selecionar o elemento mais perto e hackear ele, para cada elemento.
    for (int iterations=0;iterations<amountOfElements;iterations++) {

        // ve qual é o elemento mais perto do hacker nesse instante
        int closestElementIndex = 0;
        for (int i=0;i<amountOfElements;i++) {
            int d = getDistance(elementsPosition[i].row,elementsPosition[i].col, getHackerRow(),getHackerCol());
            elementsPosition[i].distanceFromHacker = d;

            if ((   elementsPosition[i].distanceFromHacker <= elementsPosition[closestElementIndex].distanceFromHacker && elementsPosition[i].hasBeenHacked == 0) || elementsPosition[closestElementIndex].hasBeenHacked == 1) {
                closestElementIndex = i;
            }
        }

        // vai até esse elemento e hackeia
        int targetRow = elementsPosition[closestElementIndex].row;
        int targetCol = elementsPosition[closestElementIndex].col;

        if (map[targetRow][targetCol] == SENSOR) {
            printf("Found a sensor. Lets go to it!\n");
            printf("Coordinates: %d,  %d\n",targetRow,targetCol);
            moveHackerTo(targetRow,targetCol);
            printf("Reached it. Lets hack.\n");
            printMap();
            sensorProblem = inspectSensor(targetRow,targetCol);

            long int a = atol(sensorProblem.a);
            char key[sensorProblem.n];
            int Maior_Divisor = Fatoracao(a);

            sprintf(key, "%d",Maior_Divisor);
            hackSensor(targetRow,targetCol,key);
            elementsPosition[closestElementIndex].hasBeenHacked = 1;
            printf("The sensor is hacked! Im feeling FAST, is this sensor made by Redbull?\n");
        }

        if (map[targetRow][targetCol] == COMPUTER) {
            printf("Found a computer. Lets go to it!\n");
            printf("Coordinates: %d,  %d\n",targetRow,targetCol);
            moveHackerTo(targetRow,targetCol);
            printf("Reached it. Lets hack.\n");
            printMap();
            computerProblem = inspectComputer(targetRow,targetCol);

            int Tamanho = computerProblem.n;
            printf("Size of the problem: %d\n",Tamanho);

            char *key = (char *)calloc(800,sizeof(char));
            //EncontraChave(computerProblem.a,computerProblem.b,Tamanho, key);
            matcher(computerProblem.a,computerProblem.b,key,Tamanho);

            hackComputer(targetRow,targetCol,key);
            strcpy(computersAnswers[amountOfComputers],key);
            printf("Computer is hacked! The key is: %s\n",computersAnswers[amountOfComputers]);

            amountOfComputers++;
            elementsPosition[closestElementIndex].hasBeenHacked = 1;
        }  
    }

    // vai até a porta e hackeia ela
    int doorCol = -1;
    int doorRow = -1;

    for (int i = 0; i < mapRows; i++) {
        for (int j = 0; j < mapCols; j++) {
            if (map[i][j] == DOOR) {
                doorCol = j;
                doorRow = i;
                break;
            }
        }
    }

    printf("The exit door is located at (%d,%d). Lets go there\n",doorRow,doorCol);

    moveHackerTo(doorRow,doorCol);
    printf("Reached it. Lets hack.");
    printMap();
    doorProblem = inspectDoor(doorRow,doorCol);

    int possibleAnswer;
    char possibleAnswerStr[20];
    
    for (int i=0;i<amountOfComputers;i++) {
        for (int j=0;j<amountOfComputers;j++) {
            possibleAnswer = MultiplicaEZ(computersAnswers[i],computersAnswers[j]);
            printf("Found a possible answer, but is it the right one?\n");

            sprintf(possibleAnswerStr,"%d",possibleAnswer);
        	if (strncmp(possibleAnswerStr,doorProblem.a,2) == 0) {
        		printf("Yes, it is. Lets finish this. Evil corp is OVER.\n");

        		if (biggest(computersAnswers[i],computersAnswers[j]) == 0) {
                    hackDoor(doorRow,doorCol,computersAnswers[i]);
                    printf("Door is hacked! easy peasy lemon squeezy\n");
                    return 0;
                }
                if (biggest(computersAnswers[i],computersAnswers[j]) == 1) {
                    hackDoor(doorRow,doorCol,computersAnswers[j]);
                    printf("Door is hacked! easy peasy lemon squeezy\n");
                    return 0;
                }
        	}
        	printf("Nah, it isnt. Lets try another one.\n");
		}
	}
	return 0;
}

void ComputaPrefixo(char PREFIXO[],int TAMANHO, int *FuncaoPrefixo)
{
    int m = TAMANHO;
    int k,q;

    k = 0;
    FuncaoPrefixo[0] = 0;
    for(q=1; q<TAMANHO; q++)
    {
        while(k>0 && ((PREFIXO[k])!= (PREFIXO[q])))
        {
            k = FuncaoPrefixo[k-1];
        }
        if(PREFIXO[k]==PREFIXO[q])
            k++;
        FuncaoPrefixo[q]=k;
    }
}

int KMP_Matcher(char TEXTO[],char PADRAO[], int *FuncaoPrefixo)
{
    int n = strlen(TEXTO);
    int m = strlen(PADRAO);
    ComputaPrefixo(PADRAO,m, FuncaoPrefixo);
    int num_caracteres,IndiceTexto,ACHOU = 0;

    num_caracteres = 0;
    for(IndiceTexto=0; IndiceTexto<n; IndiceTexto++)
    {
        while(num_caracteres>0 &&(PADRAO[num_caracteres]!=TEXTO[IndiceTexto]))
            num_caracteres = FuncaoPrefixo[num_caracteres-1];
        if(PADRAO[num_caracteres]==TEXTO[IndiceTexto])
            num_caracteres++;
        if(num_caracteres == m)
        {
            ACHOU = 1;
            num_caracteres = FuncaoPrefixo[num_caracteres-1];
        }
    }
    return ACHOU;
}

void EncontraChave(char TEXTO1[],char TEXTO2[],int TAMANHO, char *Chave)
{
    int TAMANHO_STRING = TAMANHO;
    char SUB_STRING[800];
    int FuncaoPrefixo[1000];
    int TAMANHO_SUBSTRING;
    int TAM_PADRAO_ATUAL = 0;
    int i,j,k;

    TAMANHO_SUBSTRING = 3;
    while(TAMANHO_SUBSTRING<=800) {
        i=0;
        printf("vamo q vamo%d\n",TAMANHO_SUBSTRING);
        while(i+TAMANHO_SUBSTRING<=TAMANHO_STRING)
        {
            for(k=0,j=1; j<=TAMANHO_SUBSTRING; i++,j++,k++)
            {
                SUB_STRING[k] = TEXTO2[i];
            }
            SUB_STRING[k] = '\0';
            if((TAMANHO_SUBSTRING>TAM_PADRAO_ATUAL)&&(KMP_Matcher(TEXTO1,SUB_STRING, FuncaoPrefixo)))
            {
                TAM_PADRAO_ATUAL = TAMANHO_SUBSTRING;
                strcpy(Chave,SUB_STRING);
                printf("string: %s\n", SUB_STRING);
            }
            i = (i-TAMANHO_SUBSTRING)+1;
        }
        TAMANHO_SUBSTRING++;
    }
}

int Fatoracao(long int n)
{
    long int numero = n;
    int divisor = 1;
    long int resto;
    int i=2;

    while(numero!=1)
    {
        resto = numero%i;
        if(resto==0)
        {
            divisor = i;
            numero/=i;
        }
        else
            i++;
    }
    return divisor;
}

void Multiplica(char Multiplicando[],char Multiplicador[],char Produto[])
{
    char Buffer[2001];

    int digito,j,resto=0,i=0;
    long int Parcial,Quociente = 0;
    long int Auxiliar1 = atol(Multiplicando);
    int Tamanho_string = strlen(Multiplicador);

    Tamanho_string--;
    while(Tamanho_string!=-1)
    {
        digito = Multiplicador[Tamanho_string]-48;
        Parcial = Auxiliar1*digito;
        Parcial = Parcial+Quociente;
        Quociente = Parcial/10;
        resto = Parcial%10;
        Buffer[i] = resto+48;
        i++;
        Tamanho_string--;
    }
    while(Quociente>=10)
    {
        resto = Quociente%10;
        Quociente = Quociente/10;
        Buffer[i] = resto+48;
        i++;
    }
    if(Quociente>0)
    {
        Buffer[i] = Quociente+48;
        i++;
    }
    Buffer[i] = '\0'; // Obtem a "string" de forma inversa
    Tamanho_string = strlen(Buffer); // eh preciso inverter os caracteres
    for(i=0,j=Tamanho_string-1; i<Tamanho_string; i++,j--)
    {
        Produto[i] = Buffer[j];
    }
    Produto[i]='\0';
}

int MultiplicaEZ(char m1[],char m2[]) {
	char subm1[5];
	strncpy(subm1,m1,4);
	subm1[4] = '\0';

	char subm2[5];
	strncpy(subm2,m2,4);
	subm2[4] = '\0';

	int im1 = atoi(subm1);
	int im2 = atoi(subm2);

	return (im1*im2);
}

int biggest(char s1[], char s2[]) {
    int l1 = strlen(s1);
    int l2 = strlen(s2);

    if (l1 > l2) return 0;
    if (l1 < l2) return 1;
    if (l2 == l1) {
        for (int i=0;i<l1;i++) {
            if (s1[i] > s2[i]) return 0;
            if (s1[i] < s2[i]) return 1;
        }
    }

    return -1;
}

void matcher(char s1[],char s2[],char *Chave,int size) {
	char subs[2000];
	char subs2[2000];
	int biggestMatch = 0;
	int i,j,k;

	for (j=0;j<size;j++) {
		for (k=0;k<size;k++) {
			if (s1[j] == s2[k]) {
				i=0;
				while (s1[j+i] == s2[k+i]) {
					subs[i] = s1[j+i];
					i++;
				}
				subs[i] = '\0';
				if (strlen(subs) > biggestMatch) {
					biggestMatch = strlen(subs);
					strcpy(subs2,subs);
				}		
			}
		}
	}

	strcpy(Chave,subs2);
}