#include "pessoa.hpp"

Pessoa::Pessoa() {
	strcpy(nome,"INDEFINIDO");
	time(&dtnascimento);
	sexo = INDEFINIDO;
}

Pessoa::Pessoa(const Pessoa& outra) {
	
}

Pessoa::Pessoa(char* n, time_t d, Sexo s) {
	strcpy(nome, n);
	dtnascimento = d;
	sexo = s;
}

char* Pessoa::getNome() {
	return nome;
}

time_t Pessoa::getdtnascimento() {
	return dtnascimento;
}

Pessoa::Sexo Pessoa::getSexo() {
	return sexo;
}

void Pessoa::setNome(char *s) {
	strcpy(nome,s);
}

void Pessoa::setdtnascimento(time_t d) {
	dtnascimento = d;
}

void Pessoa::setSexo(Sexo s) {
	sexo = s;
}