#pragma once

#include <iostream>
#include <ctime>
#include <cstring>
using namespace std;

#include "pessoa.hpp"

class Aluno: public Pessoa {

public:
	enum Nivel {
		INDEFINIDO,
		GRADUACAO,
		ESPECIALIZACAO,
		MESTRADO,
		DOUTORADO
	};

	Aluno();

	Aluno(char* c, Nivel n);

	char* getCodigo();

	Nivel getNivel();

	void setCodigo(char* c);

	void setNivel(Nivel n);

private:
	char codigo[8];
	Nivel nivel;
};