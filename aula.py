from questao import Questao

class Aula:

    def __init__(self, tema: str, videos: list[str], textos: list[str], exercicios: list[Questao]):

        if isinstance(tema, str):
            self.__tema = tema
        else:
            raise TypeError("Tema deve ser uma string.")
        
        if isinstance(videos, list) and all(isinstance(video, str) for video in videos):
            self.__videos = videos
        else:
            raise TypeError("Videos deve ser uma lista de strings.")
        
        if isinstance(textos, list) and all(isinstance(texto, str) for texto in textos):
            self.__textos = textos
        else:
            raise TypeError("Textos deve ser uma lista de strings.")
        
        if isinstance(exercicios, list) and all(isinstance(exercicio, Questao) for exercicio in exercicios):
            self.__exercicios = exercicios
        else:
            raise TypeError("Exercícios deve ser uma lista de objetos Questao.")

    @property
    def tema(self) -> str:
        return self.__tema

    @tema.setter
    def tema(self, tema: str):
        if isinstance(tema, str):
            self.__tema = tema
        else:
            raise TypeError("Tema deve ser uma string.")

    @property
    def videos(self) -> list[str]:
        return self.__videos

    @videos.setter
    def videos(self, videos: list[str]):
        if isinstance(videos, list) and all(isinstance(video, str) for video in videos):
            self.__videos = videos
        else:
            raise TypeError("Videos deve ser uma lista de strings.")

    @property
    def textos(self) -> list[str]:
        return self.__textos

    @textos.setter
    def textos(self, textos: list[str]):
        if isinstance(textos, list) and all(isinstance(texto, str) for texto in textos):
            self.__textos = textos
        else:
            raise TypeError("Textos deve ser uma lista de strings.")

    @property
    def exercicios(self) -> list[Questao]:
        return self.__exercicios

    @exercicios.setter
    def exercicios(self, exercicios: list[Questao]):
        if isinstance(exercicios, list) and all(isinstance(exercicio, Questao) for exercicio in exercicios):
            self.__exercicios = exercicios
        else:
            raise TypeError("Exercícios deve ser uma lista de objetos Questao.")