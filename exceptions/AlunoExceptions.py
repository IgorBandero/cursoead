class AlunoInvalidoException(Exception):
    def __init__(self):
        super().__init__("\n\n******** ERRO: ALUNO INVÁLIDO PARA CADASTRO! *******")

class AlunoJaRegistradoException(Exception):
    def __init__(self):
        super().__init__("\n\n************ ERRO: ALUNO JÁ CADASTRADO! ************")

class CpfAlunoJaRegistradoException(Exception):
    def __init__(self):
        super().__init__("\n\n*********** ERRO: CPF JÁ CADASTRADO! ************")

class UsuarioAlunoJaRegistradoException(Exception):
    def __init__(self):
        super().__init__("\n\n*********** ERRO: USUÁRIO JÁ CADASTRADO! **********")

class MatriculaJaRegistradaException(Exception):
    def __init__(self):
        super().__init__("\n\n*********** ERRO: MATRÍCULA JÁ CADASTRADA! **********")

class EdicaoAlunoException(Exception):
    def __init__(self):
        super().__init__("\n\n*********** ERRO NA EDIÇÃO DO ALUNO! ***********")

class ListaAlunosVaziaException(Exception):
    def __init__(self):
        super().__init__("\n\n****** NENHUM ALUNO CADASTRADO ATÉ O MOMENTO! *****")

class AlunoNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("\n\n********** ERRO: ALUNO NÃO ENCONTRADO! *********")

class AlunoNaoConcluinteException(Exception):
    def __init__(self):
        super().__init__("\n\n*********** ALUNO NÃO APTO À CONCLUSÃO! ************")

class ListaExAlunosVaziaException(Exception):
    def __init__(self):
        super().__init__("\n\n****** NENHUM ALUNO CONCLUINTE ATÉ O MOMENTO! ******")