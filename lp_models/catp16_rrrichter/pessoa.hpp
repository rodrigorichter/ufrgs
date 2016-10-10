#pragma once

#include <iostream>
#include <ctime>
#include <cstring>
using namespace std;

class Pessoa {
public:
	enum Sexo {
		INDEFINIDO,
		MASCULINO,
		FEMININO
	};

	Pessoa();

	Pessoa(const Pessoa&);

	Pessoa(char* n, time_t d, Sexo s);

	char* getNome();

	time_t getdtnascimento();

	Sexo getSexo();

	void setNome(char *s);

	void setdtnascimento(time_t d);

	void setSexo(Sexo s);

private:
	char nome[100];
	time_t dtnascimento;
	Sexo sexo;
};