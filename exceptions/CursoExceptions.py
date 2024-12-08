class CursoInvalidoException(Exception):
    def __init__(self):
        super().__init__("ERRO: CURSO INVÁLIDO PARA CADASTRO!\n")

class CursoJaRegistradoException(Exception):
    def __init__(self):
        super().__init__("ERRO: CURSO JÁ CADASTRADO!\n")

class CursoNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("ERRO: CURSO NÃO ENCONTRADO!\n")

class ListaCursosVaziaException(Exception):
    def __init__(self):
        super().__init__("NENHUM CURSO DISPONÍVEL!\n")

class NomeCursoJaRegistradoException(Exception):
    def __init__(self):
        super().__init__("ERRO: NOME JÁ CADASTRADO!\n")

class EdicaoCursoException(Exception):
    def __init__(self):
        super().__init__("ERRO NA EDIÇÃO DO CURSO!\n")