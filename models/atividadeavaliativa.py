from models.questao import Questao

class AtividadeAvaliativa:

    def __init__(self, id: int, questoes: list[Questao], nota_maxima: float):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError("ID deve ser um número inteiro.")

        if isinstance(questoes, list) and all(isinstance(questao, Questao) for questao in questoes):
            self.__questoes = questoes
        else:
            raise TypeError("Questões deve ser uma lista de objetos Questao.")
        
        if isinstance(nota_maxima, float):
            self.__nota_maxima = nota_maxima
        else:
            raise TypeError("Nota máxima deve ser um valor float.")

    @property
    def id(self) -> int:
        return self.__id

    @property
    def questoes(self) -> list[Questao]:
        return self.__questoes

    @questoes.setter
    def questoes(self, questoes: list[Questao]):
        if isinstance(questoes, list) and all(isinstance(questao, Questao) for questao in questoes):
            self.__questoes = questoes
        else:
            raise TypeError("Questões deve ser uma lista de objetos Questao.")

    @property
    def nota_maxima(self) -> float:
        return self.__nota_maxima

    @nota_maxima.setter
    def nota_maxima(self, nota_maxima: float):
        if isinstance(nota_maxima, float):
            self.__nota_maxima = nota_maxima
        else:
            raise TypeError("Nota máxima deve ser um valor float.")
