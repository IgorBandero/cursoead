
class ProfessorJaRegistradoException(Exception):
    def __init__(self, message="Professor já cadastrado com este CPF."):
        self.message = message
        super().__init__(self.message)
