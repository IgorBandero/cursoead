from daos.dao import DAO
from models.Modulo import Modulo

class ModuloDAO(DAO):
    def __init__(self):
        super().__init__("modulos.pkl")

    def add(self, modulo: Modulo):
        if((modulo is not None) and isinstance(modulo, Modulo) and isinstance(modulo.codigo, str)):
            super().add(modulo.codigo, modulo)

    def update(self, modulo: Modulo):
        if((modulo is not None) and isinstance(modulo, Modulo) and isinstance(modulo.codigo, str)):
            super().update(modulo.codigo, modulo)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)