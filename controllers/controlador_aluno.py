from views.tela_aluno import TelaAluno
from models.aluno import Aluno
from models.matricula import Matricula
from datetime import date
import random
class ControladorAluno():

    def __init__(self, controlador_sistema, controlador_curso):
        self.__alunos = []
        self.__tela_aluno = TelaAluno()
        self.__controlador_curso = controlador_curso
        self.__controlador_sistema = controlador_sistema

    def cadastrar_aluno(self):
        num_cursos_disponiveis = len(self.__controlador_curso._ControladorCurso__cursos)
        if (num_cursos_disponiveis == 0):
            self.__tela_aluno.mostrar_mensagem("\n****** NENHUM CURSO DISPONÍVEL PARA MATRÍCULA! ******")
            return
        aluno = self.__tela_aluno.cadastrar_aluno()
        if (aluno is not None):
            self.__tela_aluno.mostrar_mensagem("Curso: ")
            curso = self.__controlador_curso.selecionar_curso()
            if (curso is not None):
                codigo = self.gerar_codigo_matricula()
                data_inicio = date.today()
                aluno_cadastrado = self.buscar_aluno_pelo_cpf(aluno["cpf"])
                if aluno_cadastrado is None:
                    novoAluno = Aluno(aluno["nome"], aluno["cpf"], aluno["telefone"], aluno["email"], aluno["usuario"], aluno["senha"], aluno["rua"], aluno["num_residencia"], aluno["bairro"], aluno["cidade"], aluno["cep"], curso, codigo, data_inicio)
                    self.__alunos.append(novoAluno)
                    print("\nAluno: ", self.__alunos[-1].nome, " cadastrado(a) com sucesso!")
                else:
                    self.__tela_aluno.mostrar_mensagem("********* ATENÇÃO: Aluno já cadastrado! *********")
            else:
                self.__tela_aluno.mostrar_mensagem("\n****** ATENÇÃO: Curso inválido! ******")
        else:
            self.__tela_aluno.mostrar_mensagem("\n************* ERRO NO CADASTRO DE ALUNO ************")

    def editar_aluno(self):
        aluno = self.selecionar_aluno()
        if(aluno is not None):
            self.mostrar_aluno(aluno)
            while(True):
                campo, info_atualizada = self.__tela_aluno.editar_aluno()
                if info_atualizada is not None:
                    for item in self.__alunos:
                        if(item.cpf == aluno.cpf):
                            if campo == 1:
                                item.nome = info_atualizada
                            elif campo == 2:
                                for caso in self.__alunos:
                                    if caso.cpf == info_atualizada:
                                        print("\n*********** ERRO: CPF JÁ CADASTRADO! ***********")
                                        return
                                item.cpf = info_atualizada
                            elif campo == 3:
                                item.telefone = info_atualizada
                            elif campo == 4:
                                item.email = info_atualizada
                            elif campo == 5:
                                for caso in self.__alunos:
                                    if caso.usuario == info_atualizada:
                                        print("\n*********** ERRO: USUÁRIO JÁ CADASTRADO! ***********")
                                        return
                                item.usuario = info_atualizada
                            elif campo == 6:
                                item.rua = info_atualizada
                            elif campo == 7:
                                item.num_residencia = info_atualizada
                            elif campo == 8:
                                item.bairro = info_atualizada
                            elif campo == 9:
                                item.cidade = info_atualizada
                            elif campo == 10:
                                item.cep = info_atualizada
                            elif campo == 11:
                                novo_curso = self.__controlador_curso.selecionar_curso()
                                print("NOVO CURSO: ", novo_curso.nome)
                                if (novo_curso is not None):
                                    item.matricula.curso = novo_curso
                            elif campo == 12:
                                for caso in self.__alunos:
                                    if caso.matricula.codigo == info_atualizada:
                                        print("\n*********** ERRO: MATRICULA JÁ CADASTRADA! ***********")
                                        return
                                item.matricula = Matricula(aluno.matricula.curso, info_atualizada, aluno.matricula.data_inicio)
                            elif campo == 13:
                                while(True):
                                    self.__tela_aluno.mostrar_mensagem("\nInforme a senha atual... ")
                                    senha_atual = input("Digite a senha atual: ")
                                    if senha_atual == aluno.senha:
                                        self.__tela_aluno.mostrar_mensagem("\nInforme a nova senha... ")
                                        nova_senha = self.__tela_aluno.cadastrar_senha()
                                        item.senha = nova_senha
                                    else:
                                        self.__tela_aluno.mostrar_mensagem("\n****************** SENHA INCORRETA! ******************")
                            self.mostrar_aluno(aluno)
                else:
                    self.__tela_aluno.mostrar_mensagem("\n************* ERRO: Edição não concluída *************")
                continuar = self.__tela_aluno.continuar_edicao()
                if not continuar:
                    break

    def excluir_aluno(self):
        aluno = self.selecionar_aluno()
        if(aluno is not None):
            excluir = self.__tela_aluno.excluir_aluno({"nome": aluno.nome, "curso": aluno.matricula.curso.nome})
            if (excluir):
                self.__alunos.remove(aluno)
                self.__tela_aluno.mostrar_mensagem(f"\nAluno: {aluno.nome} foi removido da lista de alunos da universidade.")
            else:
                self.__tela_aluno.mostrar_mensagem("\n*************** EXCLUSÃO CANCELADA ****************")

    def listar_alunos(self):
        if(len(self.__alunos) == 0):
            self.__tela_aluno.mostrar_mensagem("\n****** NENHUM ALUNO CADASTRADO ATÉ O MOMENTO! ******")
            return
        print("\n----------------- LISTA DE ALUNOS ------------------\n")
        for indice, aluno in enumerate(self.__alunos):
            self.__tela_aluno.mostrar_opcao_aluno({"indice": indice, "nome": aluno.nome, "cpf": aluno.cpf, "matricula": aluno.matricula.codigo, "curso": aluno.matricula.curso.nome})

    def buscar_aluno(self):
        aluno = self.selecionar_aluno()
        if aluno is not None:
            self.mostrar_aluno(aluno)

    def mostrar_aluno(self, aluno):
        self.__tela_aluno.mostrar_aluno({"nome": aluno.nome, "cpf": aluno.cpf, "telefone": aluno.telefone, "email": aluno.email, "usuario": aluno.usuario, "rua": aluno.endereco.rua, "num_residencia": aluno.endereco.num_residencia, "bairro": aluno.endereco.bairro, "cidade": aluno.endereco.cidade, "cep": aluno.endereco.cep, "curso": aluno.matricula.curso.nome, "codigo": aluno.matricula.codigo, "data_inicio": aluno.matricula.data_inicio})

    def selecionar_aluno(self):
        self.__tela_aluno.mostrar_mensagem("\n----------------- SELECIONAR ALUNO -----------------")
        tipo_consulta = self.__tela_aluno.selecionar_aluno(len(self.__alunos))
        if tipo_consulta == "Buscar pelo cpf":
            aluno = self.selecionar_aluno_pelo_cpf()
            if(aluno is not None):
                return aluno
            else:
                self.__tela_aluno.mostrar_mensagem("\n********* ATENÇÃO: Aluno não encontrado! *********")
        elif tipo_consulta == "Selecionar da lista":
            self.listar_alunos()
            indice_aluno_escolhido = self.__tela_aluno.selecionar_aluno_na_lista(len(self.__alunos))
            if (indice_aluno_escolhido is not None):
                aluno = self.__alunos[indice_aluno_escolhido]
                if(aluno is not None):
                    return aluno
                else:
                    self.__tela_aluno.mostrar_mensagem("\n********* ATENÇÃO: Aluno não encontrado! *********")

    def selecionar_aluno_pelo_cpf(self):
        cpf = self.__tela_aluno.buscar_aluno_pelo_cpf()
        if (cpf is not None):
            aluno = self.buscar_aluno_pelo_cpf(cpf)
            if(aluno is not None):
                return aluno

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
        menu_opcoes = {1: self.cadastrar_aluno, 2: self.editar_aluno, 3: self.excluir_aluno, 4: self.listar_alunos, 5: self.buscar_aluno, 0: self.voltar}
        while True:
            menu_opcoes[self.__tela_aluno.mostrar_menu_opcoes()]()
