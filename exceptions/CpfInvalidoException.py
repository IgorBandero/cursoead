class CpfInvalidoException(Exception):
    def __init__(self):
        super().__init__("\n\n********* CPF INVÁLIDO! TENTE NOVAMENTE... *********")