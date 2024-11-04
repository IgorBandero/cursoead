class CursoInvalidoException(Exception):
    def __init__(self):
        super().__init__("\n\n******** ERRO: CURSO INVÁLIDO PARA CADASTRO! *******")

class CursoJaRegistradoException(Exception):
    def __init__(self):
        super().__init__("\n\n************ ERRO: CURSO JÁ CADASTRADO! ************")

class CursoNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("\n\n********** ERRO: CURSO NÃO ENCONTRADO! *********")

class ListaCursosVaziaException(Exception):
    def __init__(self):
        super().__init__("\n\n****** NENHUM CURSO DISPONÍVEL PARA MATRÍCULA! *****")

class NomeCursoJaRegistradoException(Exception):
    def __init__(self):
        super().__init__("\n\n*********** ERRO: NOME JÁ CADASTRADO! **********")

class EdicaoCursoException(Exception):
    def __init__(self):
        super().__init__("\n\n*********** ERRO NA EDIÇÃO DO CURSO! ***********")