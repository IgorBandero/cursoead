from endereco import Endereco
from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome: str, cpf: int, telefone: str, email: str, usuario: str, senha: str, rua: str, num_residencia: int, bairro: str, cidade: str, cep: str):
        if isinstance(nome, str):
            self.__nome = nome
        else: 
            raise TypeError("Nome deve ser uma string.")
        if isinstance(cpf, int):
            self.__cpf = cpf
        else: 
            raise TypeError("Cpf deve ser um inteiro.")
        if isinstance(telefone, str):
            self.__telefone = telefone
        else:
            raise TypeError("Telefone deve ser uma string.")
        if isinstance(email, str):
            self.__email = email
        else:
            raise TypeError("Emdereco deve ser uma string.")
        
        self.__endereco = Endereco(rua, num_residencia, bairro, cidade, cep)
        
    @property
    def nome(self) -> (str):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str):
            raise TypeError("Nome deve ser uma string.")
        self.__nome = nome
    
    @property
    def cpf(int) -> (int):
        return self.__cpf  # type: ignore
        
    @cpf.setter
    def cpf(self, cpf: int):
        if not isinstance(cpf, int):
            raise TypeError("Cpf deve ser um inteiro.")
        self.__cpf = cpf

    @property
    def telefone(self) -> (str):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone: str):
        if not isinstance(telefone, str):
            raise TypeError("Telefone deve ser uma string.")
        self.__telefone = telefone

    @property
    def email(self) -> (str):
        return self.__email
    
    @email.setter
    def email(self, email: str):
        if not isinstance(email, str):
            raise TypeError("Email deve ser uma string.")
        self.__email = email

    @property
    def usuario(self) -> (str):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, usuario: str):
        if not isinstance(usuario, str):
            raise TypeError("Usuário deve ser uma string.")
        self.__usuario = usuario

    @property
    def senha(self) -> (str):
        return self.__senha
    
    @senha.setter
    def senha(self, senha: str):
        if not isinstance(senha, str):
            raise TypeError("Senha deve ser uma string.")
        self.__senha = senha
    
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self,rua, num_residencia, bairro, cidade, cep):
        self.__endereco = Endereco(rua, num_residencia, bairro, cidade, cep)
    