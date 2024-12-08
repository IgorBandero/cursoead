class ListaModulosVaziaException(Exception):
    def __init__(self):
        super().__init__("NENHUM MÓDULO DISPONÍVEL PARA CURSO!\n")