from pessoa import Pessoa
from matricula import Matricula
from estadoAluno import EstadoAluno
from professor import Professor

class Aluno(Pessoa):

    def __init__(self, nome: str, cpf: str, telefone: str, email: str, usuario: str, senha: str, rua: str, 
                 num_residencia: int, bairro: str, cidade: str, cep: str, matricula: Matricula):

        super().__init__(nome, cpf, telefone, email, usuario, senha, rua, num_residencia, bairro, cidade, cep)

        if isinstance(matricula, Matricula):
            self.__matricula = matricula
        else:
            raise TypeError("Matricula deve ser do tipo Matricula.")

        self.__estado_aluno = EstadoAluno(matricula.curso.carga_horaria)
        self.__orientador = None


    @property
    def matricula(self) -> (Matricula):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula: Matricula):
        if not isinstance(matricula, Matricula):
            raise TypeError("matricula deve ser um objeto do tipo Matricula.")
        self.__matricula = matricula

    @property
    def orientador(self) -> (Professor):
        return self.__orientador
    
    @orientador.setter
    def orientador(self, orientador: Professor):
        if not isinstance(orientador, Professor):
            raise TypeError("Orientador deve ser um objeto do tipo Professor.")
        self.__orientador = orientador

    @property
    def estado_aluno(self) -> (EstadoAluno):
        return self.__estado_aluno
    
    def busca_funcao(self):
        return f"Usuário: ${self.nome} é aluno de ${self.matricula.curso} na universidade."