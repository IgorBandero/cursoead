from models.Modulo import Modulo
from models.atividadeavaliativa import AtividadeAvaliativa
class Curso:

    def __init__(self, nome: str, descricao: str, carga_horaria: int, min_semestres: int, max_semestres: int, mensalidade: float, modulos: list[Modulo]):
        
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("Nome deve ser uma string.")
        
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TypeError("Descricao deve ser uma string.")
        
        if isinstance(carga_horaria, int):
            self.__carga_horaria = carga_horaria
        else:
            raise TypeError("Carga horária deve ser um inteiro.")
        
        if isinstance(min_semestres, int):
            self.__min_semestres = min_semestres
        else:
            raise TypeError("Minimo de semestres deve ser um inteiro.")
        
        if isinstance(max_semestres, int):
            self.__max_semestres = max_semestres
        else:
            raise TypeError("Máximo de semestres deve ser um inteiro.")
        
        if isinstance(mensalidade, float):
            self.__mensalidade = mensalidade
        else:
            raise TypeError("Mensalidade deve ser um número decimal.")
        
        if isinstance(modulos, list):
            self.__modulos = modulos
        else:
            raise TypeError("Modulos deve ser uma lista de modulos.")

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str):
            raise TypeError("Nome deve ser uma string.")
        self.__nome = nome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if not isinstance(descricao, str):
            raise TypeError("Descricao deve ser uma string.")
        self.__descricao = descricao

    @property
    def carga_horaria(self) -> int:
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, carga_horaria: int):
        if not isinstance(carga_horaria, int):
            raise TypeError("Carga horária deve ser um inteiro.")
        self.__carga_horaria = carga_horaria

    @property
    def min_semestres(self) -> int:
        return self.__min_semestres

    @min_semestres.setter
    def min_semestres(self, min_semestres: int):
        if not isinstance(min_semestres, int):
            raise TypeError("Minimo de semestres deve ser um inteiro.")
        self.__min_semestres = min_semestres

    @property
    def max_semestres(self) -> int:
        return self.__max_semestres

    @max_semestres.setter
    def max_semestres(self, max_semestres: int):
        if not isinstance(max_semestres, int):
            raise TypeError("Máximo de semestres deve ser um inteiro.")
        self.__max_semestres = max_semestres

    @property
    def mensalidade(self) -> float:
        return self.__mensalidade

    @mensalidade.setter
    def mensalidade(self, mensalidade: float):
        if not isinstance(mensalidade, float):
            raise TypeError("Mensalidade deve ser um número decimal (float).")
        self.__mensalidade = mensalidade

    @property
    def modulos(self) -> list[Modulo]:
        return self.__modulos
    
    @modulos.setter
    def modulos(self, modulos: list[Modulo]):
        if not isinstance(modulos, list):
            raise TypeError("Modulos deve ser uma lista de módulos.")
        self.__modulos = modulos

    def adicionar_modulo(self, modulo: Modulo):
        if not isinstance(modulo, Modulo):
            raise TypeError("Modulo deve ser um objeto do tipo Modulo.")
        if modulo not in self.__modulos:
            self.__modulos.append(modulo)

    def remover_modulo(self, modulo: Modulo):
        for item in self.__modulos:
            if(item.codigo == modulo.codigo):
                self.__modulos.remove(item)

    def avaliacao_media_curso(self):
        num_modulos = len(self.__modulos)
        if(num_modulos > 0):
            soma_avaliacoes = 0
            for modulo in self.__modulos:
                soma_avaliacoes += modulo.avaliacao_media()
            return soma_avaliacoes / num_modulos
        return 0