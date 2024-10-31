from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: str, email: str, usuario: str, senha: str, formacao: str, especialidade: str, rua: str, num_residencia: int, bairro: str, cidade: str, cep: str):
        super().__init__(nome, cpf, telefone, email, usuario, senha, rua, num_residencia, bairro, cidade, cep)
        
        if isinstance(formacao, str):
            self.__formacao = formacao
        else:
            raise TypeError("Formação deve ser uma string.")
        
        if isinstance(especialidade, str):
            self.__especialidade = especialidade
        else:
            raise TypeError("Especialidade deve ser uma string.")
    
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

    def mostra_funcao(self):
        return f"Professor de {self.especialidade} com formação em {self.formacao}."

