from models.atividadeavaliativa import AtividadeAvaliativa

class Modulo:
    def __init__(self, codigo: str, nome: str, area: str, carga_horaria: int):
        if isinstance(codigo, str):
            self.__codigo = codigo
        else:
            raise TypeError("Código deve ser uma string.")
        
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("Nome deve ser uma string.")
        
        if isinstance(area, str):
            self.__area = area
        else:
            raise TypeError("Área deve ser uma string.")
        
        if isinstance(carga_horaria, int):
            self.__carga_horaria = carga_horaria
        else:
            raise TypeError("Carga horária deve ser um número inteiro.")
        
        self.__atividades = []
        self.__lista_avaliacoes = []

    @property
    def codigo(self) -> str:
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo: str):
        if not isinstance(codigo, str):
            raise TypeError("O código deve ser uma string.")
        self.__codigo = codigo
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string.")
        self.__nome = nome
    
    @property
    def area(self) -> str:
        return self.__area
    
    @area.setter
    def area(self, area: str):
        if not isinstance(area, str):
            raise TypeError("A área deve ser uma string.")
        self.__area = area
    
    @property
    def carga_horaria(self) -> int:
        return self.__carga_horaria
    
    @carga_horaria.setter
    def carga_horaria(self, carga_horaria: int):
        if not isinstance(carga_horaria, int):
            raise TypeError("A carga horária deve ser um número inteiro.")
        self.__carga_horaria = carga_horaria
    
    @property
    def atividades(self) -> list:
        return self.__atividades
    
    @atividades.setter
    def atividades(self, atividades: list):
        if not isinstance(atividades, list):
            raise TypeError("Atividades deve ser uma lista de objetos AtividadesAvaliativas.")
        self.__atividades = atividades
    
    @property
    def lista_avaliacoes(self) -> list:
        return self.__lista_avaliacoes
    
    @lista_avaliacoes.setter
    def lista_avaliacoes(self, lista_avaliacoes: list):
        if not isinstance(lista_avaliacoes, list):
            raise TypeError("Lista de avaliações deve ser uma lista de números (floats ou inteiros).")
        for avaliacao in lista_avaliacoes:
            if not isinstance(avaliacao, (float, int)):
                raise TypeError("Cada avaliação deve ser um número (float ou int).")
        self.__lista_avaliacoes = lista_avaliacoes

    def adicionar_avaliacao(self, avaliacao: float):
        if not isinstance(avaliacao, (float, int)):
            raise TypeError("A avaliação deve ser um número (float ou int).")
        self.__lista_avaliacoes.append(float(avaliacao))
    
    def avaliacao_media(self) -> float:
        if not self.__lista_avaliacoes:
            return 0.0
        return sum(self.__lista_avaliacoes) / len(self.__lista_avaliacoes)