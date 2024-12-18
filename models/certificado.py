from models.aluno import Aluno
from models.curso import Curso
from datetime import datetime as Date

class Certificado:
    
    def __init__(self, aluno: Aluno, curso: Curso, nota_final: float, data_emissao: Date):
        if isinstance(aluno, Aluno):
            self.__aluno = aluno
        else:
            raise TypeError("Aluno deve ser um objeto da classe Aluno.")

        if isinstance(curso, Curso):
            self.__curso = curso
        else:
            raise TypeError("Curso deve ser um objeto da classe Curso.")

        if isinstance(nota_final, float):
            self.__nota_final = nota_final
        else:
            raise TypeError("Nota final deve ser um número float.")

        if isinstance(data_emissao, Date):
            self.__data_emissao = data_emissao
        else:
            raise TypeError("Data de emissão deve ser uma data do tipo Date.")

    @property
    def aluno(self) -> Aluno:
        return self.__aluno

    @aluno.setter
    def aluno(self, aluno: Aluno):
        if isinstance(aluno, Aluno):
            self.__aluno = aluno
        else:
            raise TypeError("Aluno deve ser um objeto da classe Aluno.")

    @property
    def curso(self) -> Curso:
        return self.__curso

    @curso.setter
    def curso(self, curso: Curso):
        if isinstance(curso, Curso):
            self.__curso = curso
        else:
            raise TypeError("Curso deve ser um objeto da classe Curso.")

    @property
    def nota_final(self) -> float:
        return self.__nota_final

    @nota_final.setter
    def nota_final(self, nota_final: float):
        if isinstance(nota_final, float):
            self.__nota_final = nota_final
        else:
            raise TypeError("Nota final deve ser um número float.")

    @property
    def data_emissao(self) -> Date:
        return self.__data_emissao

    @data_emissao.setter
    def data_emissao(self, data_emissao: Date):
        if isinstance(data_emissao, Date):
            self.__data_emissao = data_emissao
        else:
            raise TypeError("Data de emissão deve ser uma data do tipo Date.")
