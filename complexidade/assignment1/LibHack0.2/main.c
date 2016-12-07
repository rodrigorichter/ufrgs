//Código de exemplo - Trabalho 1
//Você pode modificar esse arquivo à vontade.

#include <stdio.h>
#include <stdlib.h>
#include "libhack.h"

int main(int argc, char** argv) {
   
   if (argc > 1) {
      setMapSeed(atoi(argv[1])); //Você pode passar a semente do mapa por parâmetro.
   }

   setHackerName("The Homeless Hacker"); //É obrigatório definir o nome do hacker antes de chamar readMap (nome do seu grupo).

   char** map = readMap(); //O mapa é lido para a variável map como uma matriz 2D de caracteres.
   printMap(); //Imprime o mapa

   hackerSpeak("Let's rock!"); //Na arena, essa função vai mostrar um balão de fala em cima do hacker. Use sabiamente. 

   printf("Hacker Info:  Position = (%d,%d)  Speed = %1.0f\n",getHackerRow(),getHackerCol(),getHackerSpeed()); 

   int cols = getMapCols();
   int rows = getMapRows();

   printf("Map Size: (%d,%d)\n",rows,cols); 

   printf("I'm looking for the exit door...\n"); 
   //Procurando a posição da porta usando o mapa lido.
   //Você poderá fazer algo semelhante, possivelmente de forma mais eficiente, para procurar computadores e sensores.
   int doorCol = -1;
   int doorRow = -1;
   for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
         if (map[i][j] == DOOR) {
             doorCol = j;
             doorRow = i;
             break;
         }  
      }
   }
   printf("The exit door is located at (%d,%d)\n",doorRow,doorCol);

   int d = getDistance(doorRow,doorCol, getHackerRow(),getHackerCol()); //Você pode usar essa função para avaliar a distância.
   printf("Distance to the exit door: %d\n",d);
   if (d<=4) {
      printf("It's close!\n");
      printf("I'm going to get the door today!\n"); 
   } else {
      printf("It's a long way to the top!\n");
      printf("Walking slowly to the door...\n"); 
   }
   moveHackerTo(doorRow,doorCol); //Movendo até a porta.

   printf("Inspecting door...\n");
   Problem2 doorProblem = inspectDoor(doorRow,doorCol); //Inspecionando a porta para ter acesso ao problema.

   printf("Door inspected. Problem size = %d!\n",doorProblem.n); 
   if (doorProblem.n > 9) {
       printf("Ouch! Should I hack this door now? Maybe later!\n"); 
       hackerSpeak("Maybe later!");  
   } else {
       hackerSpeak("Too easy!");  
   }

   printf("Walking to the center...\n"); //Andando meio perdido pelo mapa.
   moveHackerTo(rows/2,cols/2);
   printMap();
   printf("What should I do next? Should I stay or should I go?\n");
   hackerSpeak("I'm thinking!");  

   //Aqui você deve incluir sua estratégia para se mover e hackear os computadores/sensores descobrindo as chaves dos problemas

   printf("Walking to the exit door...\n"); 
   moveHackerTo(doorRow,doorCol); //Eventualmente, você vai se mover até a porta e hackeá-la para completar a missão.
   printMap();
   printf("Hacking door key...\n"); 
   char doorKey[] = "???????"; //Você precisa descobrir essa chave para abrir a porta.
   if (hackDoor(doorRow,doorCol,doorKey)) {
      hackerSpeak("Oh yeahhh!"); 
   } else {
      printf("It is still locked!\n"); 
      hackerSpeak("Help!!!"); 
   }
   return 0;
}
