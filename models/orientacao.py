from models.aluno import Aluno
from models.professor import Professor
class Orientacao:
    def __init__(self, aluno: Aluno, professor: Professor):
        self.aluno = aluno  # Chamando diretamente o setter para validação
        self.professor = professor  # Chamando diretamente o setter para validação

    @property
    def aluno(self) -> Aluno:
        return self.__aluno
    
    @aluno.setter
    def aluno(self, aluno: Aluno):
        if not isinstance(aluno, Aluno):
            raise TypeError("aluno deve ser uma instância da classe Aluno.")
        self.__aluno = aluno

    @property
    def professor(self) -> Professor:
        return self.__professor
    
    @professor.setter
    def professor(self, professor: Professor):
        if not isinstance(professor, Professor):
            raise TypeError("professor deve ser uma instância da classe Professor.")
        self.__professor = professor
