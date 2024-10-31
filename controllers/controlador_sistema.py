from views.tela_sistema import TelaSistema
from controllers.controlador_alunos import ControladorAluno
from controllers.controllerquestao import ControladorQuestao

class ControladorSistema:

    def __init__(self):
        self.__controlador_alunos = ControladorAluno(self)
        self.__controlador_questoes = ControladorQuestao(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_alunos(self):
        return self.__controlador_alunos
    
    @property
    def controlador_questoes(self):
        return self.__controlador_questoes
    
    def inicializar_sistema(self):
        self.abrir_tela()

    def opcoes_aluno(self):
        self.__controlador_alunos.abrir_tela()

    def opcoes_questao(self):
        self.__controlador_questoes.abre_tela()

    def encerrar_sistema(self):
        exit(0)

    def abrir_tela(self):
        opcoes = {1: self.opcoes_aluno, 3: self.opcoes_questao, 0: self.encerrar_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.menu_opcoes()
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()