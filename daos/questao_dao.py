import pickle
from models.questao import Questao

class QuestaoDAO:
    def __init__(self, datasource="questoes.pkl"):
        self.__datasource = datasource
        self.__cache = self.__load()

    def __load(self):
        """
        Carrega os dados do arquivo para o cache.
        """
        try:
            with open(self.__datasource, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            # Retorna um dicionário vazio caso o arquivo não exista ou esteja vazio
            return {}

    def __save(self):
        """
        Salva o cache no arquivo.
        """
        with open(self.__datasource, "wb") as file:
            pickle.dump(self.__cache, file)

    def add(self, questao: Questao):
        """
        Adiciona uma questão ao cache e persiste no arquivo.
        """
        if isinstance(questao, Questao):
            self.__cache[questao.id] = questao
            self.__save()

    def get(self, questao_id):
        """
        Retorna uma questão pelo ID.
        """
        return self.__cache.get(questao_id)

    def get_all(self):
        """
        Retorna todas as questões no cache.
        """
        return list(self.__cache.values())

    def remove(self, questao_id):
        """
        Remove uma questão pelo ID.
        """
        if questao_id in self.__cache:
            del self.__cache[questao_id]
            self.__save()

    def update(self, questao: Questao):
        """
        Atualiza uma questão existente.
        """
        if isinstance(questao, Questao) and questao.id in self.__cache:
            self.__cache[questao.id] = questao
            self.__save()