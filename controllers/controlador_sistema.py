from views.tela_sistema import TelaSistema
from controllers.controlador_aluno import ControladorAluno
from controllers.controlador_questao import ControladorQuestao
from controllers.controlador_atividadeavaliativa import ControladorAtividadeAvaliativa
from controllers.controlador_professor import ControladorProfessor 
from controllers.controlador_curso import ControladorCurso

class ControladorSistema:

    def __init__(self):
        self.__controlador_questao = ControladorQuestao(self)  
        self.__controlador_atividade = ControladorAtividadeAvaliativa(self.__controlador_questao)  
        self.__controlador_professor = ControladorProfessor(self) 
        self.__controlador_curso = ControladorCurso(self) 
        self.__controlador_aluno = ControladorAluno(self, self.__controlador_curso)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_aluno(self):
        return self.__controlador_aluno
    
    @property
    def controlador_questao(self):
        return self.__controlador_questao

    @property
    def controlador_atividade(self):
        return self.__controlador_atividade

    @property
    def controlador_professor(self):
        return self.__controlador_professor
    
    @property
    def controlador_curso(self):
        return self.__controlador_curso

    def inicializar_sistema(self):
        self.abrir_tela()

    def opcoes_aluno(self):
        self.__controlador_aluno.abrir_tela()

    def opcoes_questao(self):
        self.__controlador_questao.abre_tela()

    def opcoes_atividade(self):
        self.__controlador_atividade.mostrar_menu()

    def opcoes_professor(self):
        self.__controlador_professor.abrir_tela()  

    def opcoes_curso(self):
        self.__controlador_curso.abrir_tela() 

    def encerrar_sistema(self):
        exit(0)

    def abrir_tela(self):
        opcoes = {
            1: self.opcoes_aluno,
            2: self.opcoes_atividade,
            3: self.opcoes_questao,
            4: self.opcoes_professor,
            5: self.opcoes_curso,
            0: self.encerrar_sistema
        }

        while True:
            opcao_escolhida = self.__tela_sistema.menu_opcoes()
            funcao_escolhida = opcoes.get(opcao_escolhida)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                print("Opção inválida, tente novamente.")