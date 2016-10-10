#include <iostream>
#include <ctime>
#include <cstring>
using namespace std;

#include "pessoa.hpp"
#include "aluno.hpp"

int main() {
	cout << "pessoa com construtor padrao:" << endl;
	Pessoa p1;
	cout << "Nome: " << p1.getNome() << endl;
	cout << "Data: " << p1.getdtnascimento() << endl;
	cout << "Sexo: " << p1.getSexo() << endl;

	cout << "pessoa com construtor alternativo:" << endl;
	time_t t;
	time(&t);
	Pessoa p2("Wives", t, Pessoa::MASCULINO);
	cout << "Nome: " << p2.getNome() << endl;
	cout << "Data: " << p2.getdtnascimento() << endl;
	cout << "Sex0: " << p2.getSexo() << endl;

	Pessoa p10;
	Pessoa p20 = p10;
	Pessoa p30;
	p30 = p10; 

	cout << "aluno com construtor padrao:" << endl;
	Aluno a1;
	cout << "Codigo: " << a1.getCodigo() << endl;
	cout << "Nivel: " << a1.getNivel() << endl;

	cout << "aluno com construtor alternativo:" << endl;
	Aluno a2("0217445",Aluno::GRADUACAO);
	cout << "Codigo: " << a2.getCodigo() << endl;
	cout << "Nivel: " << a2.getNivel() << endl;

	return 0;
}