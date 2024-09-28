from aluno import Aluno
from professor import Professor

class Orientacao:
    def __init__(self, aluno: Aluno, professor: Professor):
        self.__aluno = aluno
        self.__professor = professor

    @property
    def aluno(self):
        return self.__aluno
    
    @aluno.setter
    def aluno(self, aluno: Aluno):
        if not isinstance(aluno, Aluno):
            raise TypeError("aluno deve ser uma instancia da classe Aluno.")
        self.__aluno = Aluno
    
    @property
    def aluno(self):
        return self.__aluno
    
    @aluno.setter
    def aluno(self, aluno: Aluno):
        if not isinstance(aluno, Aluno):
            raise TypeError("aluno deve ser uma instancia da classe Aluno.")
        self.__aluno = aluno

    @property
    def professor(self):
        return self.__professor
    
    @professor.setter
    def professor(self, professor: Professor):
        if not isinstance(professor, Professor):
            raise TypeError("professor deve ser uma instancia da classe Professor.")
        self.__professor = professor