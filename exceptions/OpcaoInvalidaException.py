class OpcaoInvalidaException(Exception):
    def __init__(self):
        super().__init__("\n\n******** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... ********")