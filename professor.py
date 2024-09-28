from pessoa import Pessoa
from orientacao import Orientacao

class Professor(Pessoa):
    def __init__(self, nome: str, cpf: int, telefone: str, email: str, usuario: str, senha: str, formacao: str, especialidade: str, rua: str, num_residencia: int, bairro: str, cidade: str, cep: str):

        super().__init__(nome, cpf, telefone, email, usuario, senha, rua, num_residencia, bairro, cidade, cep)
        
        if isinstance(formacao, str):
            self.__formacao = formacao
        else:
            raise TypeError("Formação deve ser uma string.")
        
        if isinstance(especialidade, str):
            self.__especialidade = especialidade
        else:
            raise TypeError("Especialidade deve ser uma string.")
        
        self.__orientandos = []
    
    @property
    def formacao(self) -> str:
        return self.__formacao
    
    @formacao.setter
    def formacao(self, formacao: str):
        if not isinstance(formacao, str):
            raise TypeError("Formação deve ser uma string.")
        self.__formacao = formacao

    @property
    def especialidade(self) -> str:
        return self.__especialidade
    
    @especialidade.setter
    def especialidade(self, especialidade: str):
        if not isinstance(especialidade, str):
            raise TypeError("Especialidade deve ser uma string.")
        self.__especialidade = especialidade

    
    def adicionar_orientando(self, orientacao: Orientacao):
        if not isinstance(orientacao, Orientacao):
            raise TypeError("orientacao deve ser uma instancia da de Orientacao.")
        self.__orientandos.append(orientacao)

    def listar_orientandos(self):
        if not self.__orientandos:
            return f"O professor {self.nome} não possui orientandos."
        
        orientandos_str = f"O professor {self.nome} possui os seguintes orientandos:\n"
        for orientacao in self.__orientandos:
            orientandos_str += f" - {orientacao.aluno.nome}\n"
        
        return orientandos_str
    
    def mostra_funcao(self):
        return f"Usuário:{self.nome} é professor de {self.especialidade} na universidade."