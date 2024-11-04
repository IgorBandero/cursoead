
class ProfessorNaoEncontradoException(Exception):
    def __init__(self, message="Professor não encontrado."):
        self.message = message
        super().__init__(self.message)

