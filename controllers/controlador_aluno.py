from views.tela_aluno import TelaAluno
from models.aluno import Aluno
from datetime import date
import random

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

        try:
            cpf = int(aluno["cpf"])
        except ValueError:
            self.__tela_aluno.mostrar_mensagem("Erro: CPF deve ser um número inteiro válido.")
            return

        curso = self.__controlador_curso.selecionar_curso()
        if (curso is not None):
            codigo = self.gerar_codigo_matricula()
            data_inicio = date.today()
            aluno_cadastrado = self.buscar_aluno_pelo_cpf(aluno["cpf"])
            if aluno_cadastrado is None:
                novoAluno = Aluno(aluno["nome"], aluno["cpf"], aluno["telefone"], aluno["email"], aluno["usuario"], aluno["senha"], aluno["rua"], aluno["num_residencia"], aluno["bairro"], aluno["cidade"], aluno["cep"], curso, codigo, data_inicio)
                self.__alunos.append(novoAluno)
                print("\nAluno: ", self.__alunos[-1].nome, " cadastrado com sucesso!")
            else:
                self.__tela_aluno.mostrar_mensagem("********* ATENÇÃO: Aluno já cadastrado! *********")
        else:
            self.__tela_aluno.mostrar_mensagem("\n****** ATENÇÃO: Curso inválido! ******")

    def excluir_aluno(self):
        aluno = self.selecionar_aluno()
        if(aluno is not None):
                self.__alunos.remove(aluno)
                self.__tela_aluno.mostrar_mensagem(f"\nAluno: {aluno.nome} foi removido da lista de alunos da universidade.")

    def selecionar_aluno(self):
        print("\nSelecione o aluno:")
        self.listar_alunos()
        indice_aluno_escolhido = self.__tela_aluno.selecionar_aluno(len(self.__alunos))
        if (indice_aluno_escolhido is not None):
            aluno = self.__alunos[indice_aluno_escolhido]
            if(aluno is not None):
                return aluno
            else:
                self.__tela_aluno.mostrar_mensagem("********* ATENÇÃO: Aluno não encontrado! *********")

    def listar_alunos(self):
        print("\n")
        if(len(self.__alunos) == 0):
            self.__tela_aluno.mostrar_mensagem("******* NENHUM ALUNO CADASTRADO ATÉ O MOMENTO! *******")
        for indice, aluno in enumerate(self.__alunos):
            self.__tela_aluno.mostrar_opcao_aluno({"indice": indice, "nome": aluno.nome, "matricula": aluno.matricula.codigo, "curso": aluno.matricula.curso.nome})

    def buscar_aluno_pelo_cpf(self, cpf):
        for aluno in self.__alunos:
            if aluno.cpf == cpf:
                return aluno
        return None
    
    def gerar_codigo_matricula(self):
        data = date.today()
        ano = data.strftime('%Y')
        semestre = "100" if data.month in [1, 2, 3, 4, 5, 6] else "200"
        numero = random.randint(1, 9999)
        numero = str(numero).zfill(4)
        return ano+semestre+numero

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        menu_opcoes = {1: self.cadastrar_aluno, 2: self.excluir_aluno, 3: self.listar_alunos, 0: self.voltar}

        while True:
            menu_opcoes[self.__tela_aluno.mostrar_menu_opcoes()]()
