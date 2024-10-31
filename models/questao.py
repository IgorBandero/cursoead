class Questao:

    def __init__(self, id: int, enunciado: str, alternativas: list[str], respostas_corretas: list[str]):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError("Id deve ser um número inteiro.")
        
        if isinstance(enunciado, str):
            self.__enunciado = enunciado
        else:
            raise TypeError("Enunciado deve ser uma string.")
        
        if isinstance(alternativas, list) and all(isinstance(alternativa, str) for alternativa in alternativas):
            self.__alternativas = alternativas
        else:
            raise TypeError("Alternativas deve ser uma lista de strings.")
        
        if isinstance(respostas_corretas, list) and all(isinstance(resposta, str) for resposta in respostas_corretas):
            self.__respostas_corretas = respostas_corretas
        else:
            raise TypeError("Respostas corretas deve ser uma lista de strings.")

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError("Id deve ser um número inteiro.")
        
    @property
    def enunciado(self) -> str:
        return self.__enunciado

    @enunciado.setter
    def enunciado(self, enunciado: str):
        if isinstance(enunciado, str):
            self.__enunciado = enunciado
        else:
            raise TypeError("Enunciado deve ser uma string.")

    @property
    def alternativas(self) -> list[str]:
        return self.__alternativas

    @alternativas.setter
    def alternativas(self, alternativas: list[str]):
        if isinstance(alternativas, list) and all(isinstance(alternativa, str) for alternativa in alternativas):
            self.__alternativas = alternativas
        else:
            raise TypeError("Alternativas deve ser uma lista de strings.")

    @property
    def respostas_corretas(self) -> list[str]:
        return self.__respostas_corretas

    @respostas_corretas.setter
    def respostas_corretas(self, respostas_corretas: list[str]):
        if isinstance(respostas_corretas, list) and all(isinstance(resposta, str) for resposta in respostas_corretas):
            self.__respostas_corretas = respostas_corretas
        else:
            raise TypeError("Respostas corretas deve ser uma lista de strings.")

