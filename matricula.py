from datetime import date
from models.curso import Curso
    
class Matricula:
    
    def __init__(self, curso: Curso, codigo: str, data_inicio: date):
        if isinstance(curso, Curso):
            self.__curso = curso
        else:
            raise TypeError("Curso deve ser um objeto do tipo Curso.")
        if isinstance(codigo, str):
            self.__codigo = codigo
        else:
            raise TypeError("Codigo deve ser uma string.")
        if isinstance(data_inicio, date):
            self.__data_inicio = data_inicio
        else:
            raise TypeError("Data_inicio deve ser uma data (Date).")
        self.__data_final = None
        
    @property
    def curso(self) -> (Curso):
        return self.__curso

    @curso.setter
    def curso(self, curso: Curso):
        if not isinstance(curso, Curso):
            raise TypeError("Curso deve ser um objeto do tipo Curso.")
        self.__curso = curso

    @property
    def codigo(self) -> (str):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: str):
        if not isinstance(codigo, str):
            raise TypeError("Codigo deve ser uma string.")
        self.__codigo = codigo
    
    @property
    def data_inicio(self) -> (date):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio: date):
        if not isinstance(data_inicio, date):
            raise TypeError("Data_inicio deve ser uma data (date).")
        self.__data_inicio = data_inicio

    @property
    def data_final(self) -> (date):
        return self.__data_final

    @data_final.setter
    def data_final(self, data_final: date):
        if not isinstance(data_final, date):
            raise TypeError("Data_final deve ser uma data (date).")
        self.__data_final = data_final