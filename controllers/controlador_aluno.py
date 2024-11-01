from views.tela_aluno import TelaAluno
from models.aluno import Aluno
from datetime import date

class ControladorAluno():

    def __init__(self, controlador_sistema, controlador_curso):
        self.__alunos = []
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_curso = controlador_curso
        
    def cadastrar_aluno(self):
        num_cursos_disponiveis = len(self.__controlador_curso._ControladorCurso__cursos)
        if (num_cursos_disponiveis == 0):
            self.__tela_aluno.mostrar_mensagem("\n****** ATENÇÃO: Nenhum curso disponível! ******")
            return 
        aluno = self.__tela_aluno.cadastrar_aluno()
        curso = self.__controlador_curso.selecionar_curso()
        if (curso is not None):
            codigo = "24100280"
            data_inicio = date.today()
            aluno_cadastrado = self.buscar_aluno_pelo_cpf(aluno["cpf"])
            if aluno_cadastrado is None:
                novoAluno = Aluno(aluno["nome"], aluno["cpf"], aluno["telefone"], aluno["email"], aluno["usuario"], aluno["senha"], aluno["rua"], aluno["num_residencia"], aluno["bairro"], aluno["cidade"], aluno["cep"], curso, codigo, data_inicio)
                self.__alunos.append(novoAluno)
                print("\nAluno: ", self.__alunos[-1].nome, " cadastrado com sucesso!")
            else:
                self.__tela_aluno.mostrar_mensagem("********* ATENÇÃO: Aluno já cadastrado! *********")

    def buscar_aluno_pelo_cpf(self, cpf: str):
        for aluno in self.__alunos:
            if(aluno.cpf == cpf):
                return aluno
        return None

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        menu_opcoes = {1: self.cadastrar_aluno, 0: self.voltar}

        while True:
            menu_opcoes[self.__tela_aluno.mostrar_menu_opcoes()]()