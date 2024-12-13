import pickle
from models.orientacao import Orientacao


class OrientacaoDAO:
    def __init__(self, filepath="orientacoes.pkl"):
        """
        Inicializa a DAO de Orientação, carregando os dados do arquivo, se existente.
        :param filepath: Caminho do arquivo onde os dados são persistidos.
        """
        self.__filepath = filepath
        self.__orientacoes = self.__load()

    def __load(self):
        """
        Carrega os dados do arquivo de persistência.
        :return: Lista de orientações carregadas.
        """
        try:
            with open(self.__filepath, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def __save(self):
        """
        Salva os dados no arquivo de persistência.
        """
        with open(self.__filepath, "wb") as file:
            pickle.dump(self.__orientacoes, file)

    def add(self, orientacao: Orientacao):
        """
        Adiciona uma nova orientação à lista e salva os dados.
        :param orientacao: Objeto Orientacao a ser adicionado.
        """
        self.__orientacoes.append(orientacao)
        self.__save()

    def remove(self, orientacao: Orientacao):
        """
        Remove uma orientação existente da lista e salva os dados.
        :param orientacao: Objeto Orientacao a ser removido.
        """
        self.__orientacoes.remove(orientacao)
        self.__save()

    def update(self, orientacao: Orientacao):
        """
        Atualiza uma orientação existente na lista e salva os dados.
        :param orientacao: Objeto Orientacao atualizado.
        """
        index = self.__orientacoes.index(orientacao)
        self.__orientacoes[index] = orientacao
        self.__save()

    def get_all(self):
        """
        Retorna todas as orientações armazenadas.
        :return: Lista de objetos Orientacao.
        """
        return self.__orientacoes