from views.tela_sistema import TelaSistema
from controllers.controlador_alunos import ControladorAluno
from controllers.controlador_questao import ControladorQuestao
from controllers.controlador_atividadeavaliativa import ControladorAtividadeAvaliativa
from controllers.controlador_professor import ControladorProfessor 

class ControladorSistema:

    def __init__(self):
        self.__controlador_alunos = ControladorAluno(self)
        self.__controlador_questoes = ControladorQuestao(self)  
        self.__controlador_atividade = ControladorAtividadeAvaliativa(self.__controlador_questoes)  
        self.__controlador_professor = ControladorProfessor(self) 
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_alunos(self):
        return self.__controlador_alunos
    
    @property
    def controlador_questoes(self):
        return self.__controlador_questoes

    @property
    def controlador_atividade(self):
        return self.__controlador_atividade

    @property
    def controlador_professor(self):
        return self.__controlador_professor

    def inicializar_sistema(self):
        self.abrir_tela()

    def opcoes_aluno(self):
        self.__controlador_alunos.abrir_tela()

    def opcoes_questao(self):
        self.__controlador_questoes.abre_tela()

    def opcoes_atividade(self):
        self.__controlador_atividade.mostrar_menu()

    def opcoes_professor(self):
        self.__controlador_professor.abrir_tela()  

    def encerrar_sistema(self):
        exit(0)

    def abrir_tela(self):
        opcoes = {
            1: self.opcoes_aluno,
            2: self.opcoes_atividade,
            3: self.opcoes_questao,
            4: self.opcoes_professor,
            0: self.encerrar_sistema
        }

        while True:
            opcao_escolhida = self.__tela_sistema.menu_opcoes()
            funcao_escolhida = opcoes.get(opcao_escolhida)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                print("Opção inválida, tente novamente.")