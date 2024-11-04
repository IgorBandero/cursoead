class NomeCursoJaRegistradoException(Exception):
    def __init__(self):
        super().__init__("\n\n*********** ERRO: NOME JÁ CADASTRADO! **********")
