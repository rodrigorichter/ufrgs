#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

int main()
{
    char SegundoNumero[] = "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111";
    char PrimeiroNumero[] = "2";
    char Resultado[2000];
    Multiplica(PrimeiroNumero,SegundoNumero,Resultado);
    printf("%s\n",Resultado);
    return 0;
}