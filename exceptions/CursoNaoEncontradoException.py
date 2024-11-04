class CursoNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("\n\n********** ERRO: CURSO NÃO ENCONTRADO! *********")


