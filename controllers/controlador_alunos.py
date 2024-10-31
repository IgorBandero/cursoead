from views.tela_aluno import TelaAluno
from models.aluno import Aluno
from models.curso import Curso

class ControladorAluno():

    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_aluno = TelaAluno()

    def cadastrar_aluno(self):
        aluno = self.__tela_aluno.cadastrar_aluno()
        aluno_cadastrado = self.buscar_aluno_pelo_cpf(aluno["cpf"])
        if aluno_cadastrado is None:
            curso = Curso(aluno["curso"], "Curso da Universidade", 3500, 8, 16, 750.00)
            novoAluno = Aluno(aluno["nome"], aluno["cpf"], aluno["telefone"], aluno["email"], aluno["usuario"], aluno["senha"], aluno["rua"], aluno["num_residencia"], aluno["bairro"], aluno["cidade"], aluno["cep"], curso, aluno["codigo"], aluno["data_inicio"])
            self.__alunos.append(novoAluno)
            print(self.__alunos[0])
        else:
            self.__tela_aluno.mostrar_mensagem("ATENCAO: Aluno já cadastrado!")

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