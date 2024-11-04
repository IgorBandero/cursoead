class CursoInvalidoException(Exception):
    def __init__(self):
        super().__init__("\n\n******** ERRO: CURSO INVÁLIDO PARA CADASTRO! *******")
