class ListaCursosVaziaException(Exception):
    def __init__(self):
        super().__init__("\n\n****** NENHUM CURSO DISPONÍVEL PARA MATRÍCULA! *****")