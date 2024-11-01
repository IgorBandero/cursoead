from models.Modulo import Modulo
from certificado import Certificado

class EstadoAluno:
    
    def __init__(self, carga_obrigatoria: int):
        if isinstance(carga_obrigatoria, int):
            self.__carga_obrigatoria = carga_obrigatoria
            self.__modulos_atuais = []
            self.__modulos_finalizados = []
            self.__certificados = []
            self.__progresso = 0
        else: 
            raise TypeError("Carga_obrigatoria deve ser um inteiro.")
        
    @property
    def modulos_atuais(self) -> (list[Modulo]):
        return self.__modulos_atuais 

    @modulos_atuais.setter
    def modulos_atuais(self, modulos_atuais: list[Modulo]):
        if not isinstance(modulos_atuais, list):
            raise TypeError("Modulos_atuais deve ser uma lista.")
        for modulo in modulos_atuais:
            self.__modulos_atuais.adicionar_modulo_atual(modulo)
    
    @property
    def progresso(self) -> (float):
        return self.__progresso
    
    @progresso.setter
    def progresso(self, progresso: float):
        if not isinstance(progresso, float):
            raise TypeError("Progresso deve ser um número float.")
        self.__progresso = progresso
            
    @property
    def modulos_finalizados(self) -> (list[Modulo]):
        return self.__modulos_finalizados 

    @modulos_finalizados.setter
    def modulos_finalizados(self, modulos_finalizados: list[Modulo]):
        if not isinstance(modulos_finalizados, list):
            raise TypeError("Modulos_finalizados deve ser uma lista.")
        for modulo in modulos_finalizados:
            self.adicionar_modulo_finalizado(modulo)
    
    @property
    def certificados(self) -> (list[Certificado]):
        return self.__certificados 

    @certificados.setter
    def certificados(self, certificados: list[Certificado]):
        if not isinstance(certificados, list):
            raise TypeError("Certificados deve ser uma lista.")
        for certificado in certificados:
            self.__certificados.adicionar_certificado(certificado)

    def adicionar_modulo_atual(self, modulo: Modulo):
        if not isinstance(modulo, Modulo):
            raise TypeError("Modulo deve ser um objeto do tipo Modulo.")
        if modulo not in self.__modulos_atuais:
            self.__modulos_atuais.append(modulo)

    def remover_modulo_atual(self, modulo: Modulo):
        for item in self.__modulos_atuais:
            if(item.codigo == modulo.codigo):
                self.__modulos_atuais.remove(modulo)

    def adicionar_modulo_finalizado(self, modulo: Modulo):
        if not isinstance(modulo, Modulo):
            raise TypeError("Modulo deve ser um objeto do tipo Modulo.")
        if modulo not in self.__modulos_finalizados:
            self.__modulos_finalizados.append(modulo)
            self.__progresso = self.calcular_progresso()

    def remover_modulo_finalizado(self, modulo: Modulo):
        for item in self.__modulos_finalizados:
            if(item.codigo == modulo.codigo):
                self.__modulos_finalizados.remove(modulo)
                self.__progresso = self.calcular_progresso()

    def adicionar_certificado(self, certificado: Certificado):
        if not isinstance(certificado, Certificado):
            raise TypeError("Certificado deve ser um objeto do tipo Certificado.")
        self.__certificados.append(certificado)

    def calcular_progresso(self):
        carga_cursada = 0
        if (len(self.__modulos_finalizados) > 0):
            for modulo in self.__modulos_finalizados:
                carga_cursada += modulo.num_residencia
            return (carga_cursada / self.__carga_obrigatoria)*100
        return 0