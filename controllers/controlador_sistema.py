from controllers.controlador_aluno import ControladorAluno
from controllers.controlador_questao import ControladorQuestao
from controllers.controlador_professor import ControladorProfessor
from controllers.controlador_atividadeavaliativa import ControladorAtividadeAvaliativa
from controllers.controlador_orientacao import ControladorOrientacao
from controllers.controlador_curso import ControladorCurso  # Adicionando ControladorCurso
from views.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        # Instância da tela do sistema
        self.__tela_sistema = TelaSistema()

        # Instanciando os controladores
        self.__controlador_curso = ControladorCurso(self)  # Inicializa ControladorCurso
        self.__controlador_alunos = ControladorAluno(self, self.__controlador_curso)
        self.__controlador_questoes = ControladorQuestao(self)
        self.__controlador_professores = ControladorProfessor(self)
        self.__controlador_atividade = ControladorAtividadeAvaliativa(self.__controlador_questoes)
        self.__controlador_orientacao = ControladorOrientacao(self)

    # Propriedades para acessar os controladores no sistema
    @property
    def controlador_alunos(self):
        return self.__controlador_alunos
    
    @property
    def controlador_questoes(self):
        return self.__controlador_questoes

    @property
    def controlador_professores(self):
        return self.__controlador_professores

    @property
    def controlador_atividade(self):
        return self.__controlador_atividade

    @property
    def controlador_orientacao(self):
        return self.__controlador_orientacao
    
    @property
    def controlador_curso(self):
        return self.__controlador_curso

    # Funções para cada opção do menu principal
    def inicializar_sistema(self):
        self.abrir_tela()

    def opcoes_aluno(self):
        self.__controlador_alunos.abrir_tela()

    def opcoes_questao(self):
        self.__controlador_questoes.abre_tela()

    def opcoes_professor(self):
        self.__controlador_professores.abrir_tela()

    def opcoes_atividade(self):
        self.__controlador_atividade.mostrar_menu()

    def opcoes_orientacao(self):
        self.__controlador_orientacao.abre_tela()

    def opcoes_curso(self):  # Função para acessar o menu de cursos
        self.__controlador_curso.abrir_tela()

    def encerrar_sistema(self):
        print("Encerrando o sistema...")
        exit(0)
        
    def abrir_tela(self):
        opcoes = {
            1: self.opcoes_aluno,
            2: self.opcoes_atividade,
            3: self.opcoes_questao,
            4: self.opcoes_professor,
            5: self.opcoes_orientacao,
            6: self.opcoes_curso,  # Adicionando a nova opção de cursos
            0: self.encerrar_sistema
        }

        while True:
            opcao_escolhida = self.__tela_sistema.menu_opcoes()
            funcao_escolhida = opcoes.get(opcao_escolhida)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_sistema.mostra_mensagem("Opção inválida, tente novamente.")