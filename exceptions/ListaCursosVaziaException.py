class ListaCursosVaziaException(Exception):
    def __init__(self):
        super().__init__("Nenhum curso disponível para matrícula!")