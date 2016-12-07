// Só funciona no C++11
// compilar com -std=c++11

#include <ctime>
#include <string>
#include <iostream>

using namespace std;

class Pessoa{
	public:
		enum Sexo { INDEFINIDO, MASCULINO, FEMININO };
		
		Pessoa(); // Construtor padrão		
		Pessoa(std::string, Sexo, time_t); // Construtor alternativo				
		Pessoa(const Pessoa& outra); // // construtor de cópia		
		
		Pessoa& operator=(const Pessoa& outra);
		
		time_t get_dtnascimento() const;		
		void set_dtnascimento(time_t dtnascimento);

		std::string get_nome() const;		
		void set_nome(std::string nome);
		
		Sexo get_sexo() const;
		void set_sexo(Sexo sexo);
		
		virtual std::string toString();		
		
	private:
		time_t dtnascimento;
		std::string nome;
		Sexo sexo;	
};

// Construtor padrão (inicializa atributos com valores default)
// Perceba que ele usa a técnica de delegating constructor (c++11)
// para chamar o construtor alternativo, passando os valores default para os atributos 
Pessoa::Pessoa() : Pessoa("Indefinido", INDEFINIDO, time(0))
{			
	cout << "Construtor Pessoa() chamado"<< endl;
}	

// Construtor alternativo
Pessoa::Pessoa(std::string nome, Pessoa::Sexo sexo, time_t dtnascimento)
   : nome(nome),                 // ":" introduz lista de inicializadores de atributos 			   
	 sexo(sexo),                 // esta lista eh opcional (e a inicializacao poderia ser
     dtnascimento(dtnascimento)  // feita dentro das chaves
			                     // mais detalhes em:
							     // http://en.cppreference.com/w/cpp/language/initializer_list
{			
	cout << "Construtor alternativo de Pessoa chamado" << endl;
}

/* 
// Uma alternativa para os dois acima seria criar um construtor com valores default:
Pessoa(std::string nome = nome, sexo=INDEFINIDO, dtnascimento = time(0)){			
	// o problema é fazer isso funcionar para funções!
}

// outra seria especificar um método privado para a inicialização
// o qual seria chamado por todos os construtores!

*/

// construtor de cópia
Pessoa::Pessoa(const Pessoa& outra) 
   : nome(outra.nome), 
	 dtnascimento(outra.dtnascimento),
	 sexo(outra.sexo)
{
	cout << "Construtor de cópia chamado" << endl;
	// este eh soh um exemplo e pode nao funcionar como esperado
	// substitua pelo seu codigo
}						
		
// Operador de atribuição sobrecarregado para receber uma pessoa
Pessoa& Pessoa::operator=(const Pessoa& outra){
	// este eh soh um exemplo e pode nao funcionar como esperado
	// substitua pelo seu codigo
	this->nome = outra.nome;
	this->dtnascimento = outra.dtnascimento;
	this->sexo = outra.sexo;
	cout << "Operator= chamado" << endl;			
	return *this;
}

time_t Pessoa::get_dtnascimento() const{
	return this->dtnascimento;
}

void Pessoa::set_dtnascimento(time_t dtnascimento){
	this->dtnascimento = dtnascimento;
}

std::string Pessoa::get_nome() const{
	return this->nome;
}

void Pessoa::set_nome(std::string nome){
	this->nome = nome;
}

Pessoa::Sexo Pessoa::get_sexo() const{
	return this->sexo;
}

void Pessoa::set_sexo(Pessoa::Sexo sexo){
	this->sexo = sexo;
}

std::string Pessoa::toString(){
			time_t dtnascimento = this->get_dtnascimento();			
			std::string tmp = "Pessoa{\n\tNome: ";
			
			std::string sexos[] = { "Indefinido", "Masculino", "Feminino" };
			
			tmp.append(this->get_nome());
			tmp.append("\n\tSexo: ");
			tmp.append(sexos[this->get_sexo()]);
			tmp.append("\n\tNascimento: ");
			tmp.append(ctime(&dtnascimento));
			tmp.append("}\n");
			
			return tmp;
		}

// sobrecarga do operador << usado em cout
// Permite imprimir strings representativas para a enumeração Sexo
// Do contrário, imprimiria um número inteiro correspondente a cada valor de sexo 
std::ostream& operator<<(std::ostream& os, Pessoa::Sexo s)
{
    switch(s) {
         case Pessoa::INDEFINIDO : os << "INDEFINIDO"; break;
         case Pessoa::MASCULINO  : os << "MASCULINO"; break;
         case Pessoa::FEMININO   : os << "FEMININO"; break;
         default                 : os.setstate(std::ios_base::failbit);
    }
    return os;
}

class Aluno: public Pessoa{
	public:
		enum Nivel { INDEFINIDO, GRADUACAO, ESPECIALIZACAO, MESTRADO, DOUTORADO };		
		
		Aluno();
		
		Aluno(std::string, Sexo, time_t, std::string, Nivel);
		
		Aluno(const Aluno& outro);
		
		Aluno& operator=(const Aluno& outro);
		
		const std::string get_codigo() const;		
		void set_codigo(std::string codigo);
		
		const Nivel get_nivel() const;		
		void set_nivel(Nivel nivel); 
		
		std::string toString();
		
	private:				
		std::string codigo;		
		Nivel nivel;	
};

// Construtor padrão
Aluno::Aluno() : codigo("INDEFINIDO"),  nivel(Aluno::INDEFINIDO){			  
	cout << "Construtor Aluno() chamado"<< endl;
}	

// construtor de cópia
Aluno::Aluno(const Aluno& outro){			
	set_nome(outro.get_nome());
	set_dtnascimento(outro.get_dtnascimento());
	set_sexo(outro.get_sexo());
	set_codigo(outro.get_codigo());
	set_nivel(outro.get_nivel());
	cout << "Construtor de cópia de Aluno chamado" << endl;
}		

// Construtor alternativo
Aluno::Aluno(std::string nome, Sexo sexo, time_t dtnascimento, std::string codigo, Nivel nivel){	
	this->set_nome(nome);
	this->set_sexo(sexo);
	this->set_dtnascimento(dtnascimento);
	this->set_codigo(codigo);
	this->set_nivel(nivel);
	cout << "Construtor Alternativo Aluno() chamado"<< endl;
}

// Operador de atribuição sobrecarregado para receber uma pessoa
Aluno& Aluno::operator=(const Aluno& outro){
	set_nome(outro.get_nome());
	set_dtnascimento(outro.get_dtnascimento());
	set_sexo(outro.get_sexo());
	this->codigo = outro.get_codigo();
	this->nivel = outro.get_nivel();
	
	cout << "Operator=(Aluno) chamado" << endl;
	
	return *this;
}

const std::string Aluno::get_codigo() const{
	return this->codigo;
}

void Aluno::set_codigo(std::string codigo){
	this->codigo = codigo;
}

const Aluno::Nivel Aluno::get_nivel() const{
	return this->nivel;
}

void Aluno::set_nivel(Nivel nivel){
	this->nivel = nivel;
}

std::string Aluno::toString(){
	time_t dtnascimento = this->get_dtnascimento();			
	std::string tmp = "Aluno{\n\tNome: ";
	
	std::string sexos[] = { "Indefinido", "Masculino", "Feminino" };
	std::string niveis[] = { "Indefinido", "Graduacao", "Especializacao", "Mestrado", "Doutorado" };
	
	tmp.append(this->get_nome());
	tmp.append("\n\tSexo: ");
	tmp.append(sexos[this->get_sexo()]);
	tmp.append("\n\tNascimento: ");
	tmp.append(ctime(&dtnascimento));
	tmp.append("\n\tCodigo: ");
	tmp.append(this->get_codigo());
	tmp.append("\n\tNivel: ");
	tmp.append(niveis[this->get_nivel()]);
	tmp.append("\n}\n");
	
	return tmp;
}
		
std::ostream& operator<<(std::ostream& os, Aluno::Nivel n){
    switch(n) {
         case Aluno::INDEFINIDO     : os << "INDEFINIDO"; break;
         case Aluno::GRADUACAO      : os << "GRADUACAO"; break;
         case Aluno::ESPECIALIZACAO : os << "ESPECIALIZACAO"; break;
		 case Aluno::MESTRADO       : os << "MESTRADO"; break;
		 case Aluno::DOUTORADO      : os << "DOUTORADO"; break;
         default                    : os.setstate(std::ios_base::failbit);
    }
    return os;
}

int main() {
	Pessoa* p1 = new Pessoa("Ana Paula", Pessoa::FEMININO, time(0));
	Pessoa* p2 = new Aluno("Jose Silva", Pessoa::FEMININO, time(0), "01001010", Aluno::GRADUACAO);
	cout << p1->toString();
	cout << p2->toString();

	/*
	O código original chama o toString de pessoa porque ocorreu um 
	upcast de aluno para pessoa, então o programa dá prioridade
	para os métodos de Pessoa, já que em C++, o padrão é static
	binding. Para isso, precisamos usar dynamic binding, e para isso
	é só transformar o toString da classe base em virtual.
	*/

	return 0;
}