# exceptions/ListaProfessoresVaziaException.py

class ListaProfessoresVaziaException(Exception):
    def __init__(self, message="Nenhum professor cadastrado."):
        self.message = message
        super().__init__(self.message)

