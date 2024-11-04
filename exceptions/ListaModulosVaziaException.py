class ListaModulosVaziaException(Exception):
    def __init__(self):
        super().__init__("\n\n****** NENHUM MÓDULO DISPONÍVEL PARA CURSO! ******")