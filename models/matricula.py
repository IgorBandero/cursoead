from datetime import date
from models.curso import Curso
from models.Modulo import Modulo
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
        self.__modulos_atuais = []
        self.__modulos_finalizados = []

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

    @property
    def modulos_atuais(self) -> list[Modulo]:
        return self.__modulos_atuais
    
    @modulos_atuais.setter
    def modulos_atuais(self, modulos: list[Modulo]):
        if not isinstance(modulos, list):
            raise TypeError("Modulos_atuais deve ser uma lista de módulos.")
        self.__modulos_atuais = modulos

    def adicionar_modulo_atual(self, modulo: Modulo):
        if not isinstance(modulo, Modulo):
            raise TypeError("Modulo deve ser um objeto do tipo Modulo.")
        if modulo not in self.__modulos_atuais:
            self.__modulos_atuais.append(modulo)

    def remover_modulo_atual(self, modulo: Modulo):
        for item in self.__modulos_atuais:
            if(item.codigo == modulo.codigo):
                self.__modulos_atuais.remove(item)

    @property
    def modulos_finalizados(self) -> list[Modulo]:
        return self.__modulos_finalizados
    
    @modulos_finalizados.setter
    def modulos_finalizados(self, modulos: list[Modulo]):
        if not isinstance(modulos, list):
            raise TypeError("Modulos_finalizados deve ser uma lista de módulos.")
        self.__modulos_finalizados = modulos

    def adicionar_modulos_finalizados(self, modulo: Modulo):
        if not isinstance(modulo, Modulo):
            raise TypeError("Modulo deve ser um objeto do tipo Modulo.")
        if modulo not in self.__modulos_finalizados:
            self.__modulos_finalizados.append(modulo)

    def remover_modulos_finalizados(self, modulo: Modulo):
        for item in self.__modulos_finalizados:
            if(item.codigo == modulo.codigo):
                self.__modulos_finalizados.remove(item)

    def calcular_progresso(self):
        carga_concluida = 0
        if (len(self.__modulos_finalizados) > 0):
            for modulo in self.__modulos_finalizados:
                carga_concluida += modulo.carga_horaria
            return carga_concluida / self.curso.carga_horaria
        else:
            return 0