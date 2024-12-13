import pickle
import os

class ProfessorDAO:
    def __init__(self, filepath="professores.pkl"):
        self.__filepath = filepath
        self.__cache = {}
        self.__load()

    def __load(self):
        if os.path.exists(self.__filepath):
            with open(self.__filepath, "rb") as file:
                self.__cache = pickle.load(file)
        else:
            self.__cache = {}

    def __save(self):
        with open(self.__filepath, "wb") as file:
            pickle.dump(self.__cache, file)

    def add(self, professor):
        if professor.cpf in self.__cache:
            raise ValueError("Professor já registrado com esse CPF.")
        self.__cache[professor.cpf] = professor
        self.__save()

    def update(self, professor):
        if professor.cpf not in self.__cache:
            raise ValueError("Professor não encontrado.")
        self.__cache[professor.cpf] = professor
        self.__save()

    def remove(self, cpf):
        if cpf in self.__cache:
            del self.__cache[cpf]
            self.__save()

    def get(self, cpf):
        return self.__cache.get(cpf)

    def get_all(self):
        return list(self.__cache.values())