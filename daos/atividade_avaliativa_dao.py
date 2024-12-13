import pickle
from models.atividadeavaliativa import AtividadeAvaliativa

class AtividadeAvaliativaDAO:
    def __init__(self, filepath="atividades.pkl"):
        self.__filepath = filepath
        self.__atividades = self.__load()

    def __load(self):
        try:
            with open(self.__filepath, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def __save(self):
        with open(self.__filepath, "wb") as file:
            pickle.dump(self.__atividades, file)

    def add(self, atividade: AtividadeAvaliativa):
        """
        Adiciona uma nova atividade avaliativa ao DAO.
        """
        self.__atividades.append(atividade)
        self.__save()

    def remove(self, atividade: AtividadeAvaliativa):
        """
        Remove uma atividade avaliativa existente do DAO.
        """
        self.__atividades.remove(atividade)
        self.__save()

    def update(self, atividade: AtividadeAvaliativa):
        """
        Atualiza uma atividade avaliativa existente com base em seu ID.
        """
        for index, a in enumerate(self.__atividades):
            if a.id == atividade.id:
                self.__atividades[index] = atividade
                self.__save()
                return
        raise ValueError(f"Atividade com ID {atividade.id} não encontrada.")

    def get(self, atividade_id: int):
        """
        Busca uma atividade avaliativa pelo seu ID.
        """
        for atividade in self.__atividades:
            if atividade.id == atividade_id:
                return atividade
        return None

    def get_all(self):
        """
        Retorna todas as atividades avaliativas.
        """
        return self.__atividades