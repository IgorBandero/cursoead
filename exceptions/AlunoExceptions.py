class AlunoInvalidoException(Exception):
    def __init__(self):
        super().__init__("ERRO: ALUNO INVÁLIDO PARA CADASTRO!\n")

class AlunoJaRegistradoException(Exception):
    def __init__(self):
        super().__init__("ERRO: ALUNO JÁ CADASTRADO!\n")

class CpfAlunoJaRegistradoException(Exception):
    def __init__(self):
        super().__init__("ERRO: CPF JÁ CADASTRADO!\n")

class UsuarioAlunoJaRegistradoException(Exception):
    def __init__(self):
        super().__init__("ERRO: USUÁRIO JÁ CADASTRADO!\n")

class MatriculaJaRegistradaException(Exception):
    def __init__(self):
        super().__init__("ERRO: MATRÍCULA JÁ CADASTRADA!\n")

class EdicaoAlunoException(Exception):
    def __init__(self):
        super().__init__("ERRO NA EDIÇÃO DO ALUNO!\n")

class ListaAlunosVaziaException(Exception):
    def __init__(self):
        super().__init__("NENHUM ALUNO CADASTRADO ATÉ O MOMENTO!\n")

class AlunoNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("ERRO: ALUNO NÃO ENCONTRADO!\n")

class AlunoNaoConcluinteException(Exception):
    def __init__(self):
        super().__init__("ALUNO NÃO APTO À CONCLUSÃO!\n")

class ListaExAlunosVaziaException(Exception):
    def __init__(self):
        super().__init__("NENHUM ALUNO CONCLUINTE ATÉ O MOMENTO!\n")

class AlunoSemModulosMatriculadosException(Exception):
    def __init__(self):
        super().__init__("ALUNO SEM MÓDULOS MATRICULADOS!\n")