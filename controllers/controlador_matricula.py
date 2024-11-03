from views.tela_matricula import TelaMatricula
from models.matricula import Matricula
class ControladorMatricula():

    def __init__(self, controlador_sistema, controlador_aluno, controlador_modulo):
        self.__matriculas = []
        self.__tela_matricula = TelaMatricula()
        self.__controlador_aluno = controlador_aluno
        self.__controlador_modulo = controlador_modulo
        self.__controlador_sistema = controlador_sistema

    def matricular_aluno_modulos(self):
        aluno = self.__controlador_aluno.selecionar_aluno()
        if aluno is not None:
            self.__tela_matricula.mostrar_mensagem(f"\nALUNO(A): {aluno.nome} | CURSO: {aluno.matricula.curso.nome} | MATRÍCULA: {aluno.matricula.codigo} | CPF: {aluno.cpf}")
            modulos = self.__controlador_modulo.selecionar_modulos()
            if (modulos is not None):
                for item in modulos:
                    if item not in aluno.matricula.modulos_atuais:
                        aluno.matricula.adicionar_modulo_atual(item)

    def abrir_tela(self):
        menu_opcoes = {1: self.matricular_aluno_modulos, 0: self.voltar}
        while True:
            menu_opcoes[self.__tela_matricula.mostrar_menu_opcoes()]()

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

