from daos.dao import DAO
from models.certificado import Certificado

class CertificadoDAO(DAO):
    def __init__(self):
        super().__init__("certificados.pkl")

    def add(self, certificado: Certificado):
        if((certificado is not None) and isinstance(certificado, Certificado) and isinstance(certificado.aluno.nome, str)):
            super().add(certificado.aluno.nome, certificado)

    def update(self, certificado: Certificado):
        if((certificado is not None) and isinstance(certificado, Certificado) and isinstance(certificado.aluno.nome, str)):
            super().update(certificado.aluno.nome, certificado)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)