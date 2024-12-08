class OpcaoInvalidaException(Exception):
    def __init__(self):
        super().__init__("OPÇÃO INVÁLIDA! TENTE NOVAMENTE...\n")