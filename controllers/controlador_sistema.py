from views.tela_sistema import TelaSistema
from controllers.controlador_alunos import ControladorAluno

class ControladorSistema:

    def __init__(self):
        self.__controlador_alunos = ControladorAluno(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_alunos(self):
        return self.__controlador_alunos
    
    def inicializar_sistema(self):
        self.abrir_tela()

    def opcoes_aluno(self):
        self.__controlador_alunos.abrir_tela()

    def encerrar_sistema(self):
        exit(0)

    def abrir_tela(self):
        opcoes = {1: self.opcoes_aluno, 0: self.encerrar_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.menu_opcoes()
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()