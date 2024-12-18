class ListaModulosVaziaException(Exception):
    def __init__(self):
        super().__init__("NENHUM MÓDULO DISPONÍVEL PARA CURSO!\n")

class CodigoModuloJaRegistradoException(Exception):
    def __init__(self):
        super().__init__("ERRO: CÓDIGO DO MÓDULO JÁ CADASTRADO!\n")

class ListaModulosVaziaException(Exception):
    def __init__(self):
        super().__init__("NENHUM MÓDULO CADASTRADO ATÉ O MOMENTO!\n")

class EdicaoModuloException(Exception):
    def __init__(self):
        super().__init__("ERRO NA EDIÇÃO DO MÓDULO!\n")

class ModuloNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("ERRO: MÓDULO NÃO ENCONTRADO!\n")

class ModuloInvalidoException(Exception):
    def __init__(self):
        super().__init__("ERRO: MÓDULO INVÁLIDO PARA CADASTRO!\n")

class ModuloJaCadastradoNoCurso(Exception):
    def __init__(self):
        super().__init__("MÓDULO JÁ CADASTRADO NA LISTA DE MÓDULOS DO CURSO!\n")