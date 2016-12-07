#include "aluno.hpp"

Aluno::Aluno() {
	strcpy(codigo,"0000000");
	nivel = INDEFINIDO;
}

Aluno::Aluno(char* c, Nivel n) {
	strcpy(codigo, c);
	nivel = n;
}

char* Aluno::getCodigo() {
	return codigo;
}

Aluno::Nivel Aluno::getNivel() {
	return nivel;
}

void Aluno::setCodigo(char* c) {
	strcpy(codigo, c);
}

void Aluno::setNivel(Nivel n) {
	nivel = n;
}