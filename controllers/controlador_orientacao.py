from models.orientacao import Orientacao
from views.tela_orientacao import TelaOrientacao
from controlador_alunos import ControladorAluno
from controlador_professor import ControladorProfessor


class ControladorOrientacao:
    def __init__(self, controlador_sistema):
        self.__orientacoes = []
        self.__tela_orientacao = TelaOrientacao()
        self.__controlador_sistema = controlador_sistema

    def cadastrar_orientacao(self):
        dados_orientacao = self.__tela_orientacao.pega_dados_orientacao()
        aluno = self.__controlador_sistema.controlador_alunos.buscar_aluno_pelo_cpf(dados_orientacao["cpf_aluno"])
        professor = self.__controlador_sistema.controlador_professores.buscar_professor_por_cpf(dados_orientacao["cpf_professor"])
        
        if aluno and professor:
            orientacao = Orientacao(aluno, professor)
            self.__orientacoes.append(orientacao)
            self.__tela_orientacao.mostra_mensagem("Orientação cadastrada com sucesso!")
        else:
            self.__tela_orientacao.mostra_mensagem("Erro: Aluno ou Professor não encontrados.")

    def listar_orientacoes(self):
        if not self.__orientacoes:
            self.__tela_orientacao.mostra_mensagem("Nenhuma orientação cadastrada.")
        else:
            for orientacao in self.__orientacoes:
                dados_orientacao = {
                    "nome_aluno": orientacao.aluno.nome,
                    "cpf_aluno": orientacao.aluno.cpf,
                    "nome_professor": orientacao.professor.nome,
                    "cpf_professor": orientacao.professor.cpf
                }
                self.__tela_orientacao.mostra_orientacao(dados_orientacao)

    def editar_orientacao(self):
        cpf_aluno = self.__tela_orientacao.seleciona_orientacao()
        orientacao = self.buscar_orientacao_por_aluno(cpf_aluno)
        
        if orientacao:
            novos_dados = self.__tela_orientacao.pega_dados_orientacao()
            novo_professor = self.__controlador_sistema.controlador_professores.buscar_professor_por_cpf(novos_dados["cpf_professor"])
            novo_aluno = self.__controlador_sistema.controlador_alunos.buscar_aluno_pelo_cpf(novos_dados["cpf_aluno"])
            
            if novo_aluno and novo_professor:
                orientacao.aluno = novo_aluno
                orientacao.professor = novo_professor
                self.__tela_orientacao.mostra_mensagem("Orientação editada com sucesso!")
            else:
                self.__tela_orientacao.mostra_mensagem("Erro: Aluno ou Professor não encontrados.")
        else:
            self.__tela_orientacao.mostra_mensagem("Orientação não encontrada.")

    def excluir_orientacao(self):
        cpf_aluno = self.__tela_orientacao.seleciona_orientacao()
        orientacao = self.buscar_orientacao_por_aluno(cpf_aluno)
        
        if orientacao:
            self.__orientacoes.remove(orientacao)
            self.__tela_orientacao.mostra_mensagem("Orientação excluída com sucesso!")
        else:
            self.__tela_orientacao.mostra_mensagem("Orientação não encontrada.")

    def listar_orientandos_do_professor(self):
        cpf_professor = input("Informe o CPF do professor: ")
        orientacoes_do_professor = [o for o in self.__orientacoes if o.professor.cpf == cpf_professor]
        
        if orientacoes_do_professor:
            self.__tela_orientacao.mostra_mensagem(f"Orientandos do Professor (CPF {cpf_professor}):")
            for orientacao in orientacoes_do_professor:
                print(f" - Aluno: {orientacao.aluno.nome} (CPF: {orientacao.aluno.cpf})")
        else:
            self.__tela_orientacao.mostra_mensagem("Nenhum orientando encontrado para este professor.")

    def buscar_orientador_do_aluno(self):
        cpf_aluno = input("Informe o CPF do aluno: ")
        orientacao = self.buscar_orientacao_por_aluno(cpf_aluno)
        
        if orientacao:
            self.__tela_orientacao.mostra_mensagem(f"Orientador do Aluno (CPF {cpf_aluno}):")
            print(f"Professor: {orientacao.professor.nome} (CPF: {orientacao.professor.cpf})")
        else:
            self.__tela_orientacao.mostra_mensagem("Orientação não encontrada para este aluno.")

    def buscar_orientacao_por_aluno(self, cpf_aluno):
        for orientacao in self.__orientacoes:
            if orientacao.aluno.cpf == cpf_aluno:
                return orientacao
        return None

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

    def abre_tela(self):
        opcoes = {
            1: self.cadastrar_orientacao,
            2: self.listar_orientacoes,
            3: self.editar_orientacao,
            4: self.excluir_orientacao,
            5: self.listar_orientandos_do_professor,
            6: self.buscar_orientador_do_aluno
        }

        while True:
            opcao = self.__tela_orientacao.mostrar_menu_opcoes()
            funcao_escolhida = opcoes.get(opcao)
            
            if funcao_escolhida:
                funcao_escolhida()
            elif opcao == 0:
                self.voltar()
                break
            else:
                self.__tela_orientacao.mostra_mensagem("Opção inválida. Tente novamente.")
