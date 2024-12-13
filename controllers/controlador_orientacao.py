from models.orientacao import Orientacao
from views.tela_orientacao import TelaOrientacao


class ControladorOrientacao:
    def __init__(self, controlador_sistema):
        self.__orientacoes = []
        self.__tela_orientacao = TelaOrientacao()
        self.__controlador_sistema = controlador_sistema

    def buscar_orientacao_por_cpf_aluno(self, cpf_aluno):
        for orientacao in self.__orientacoes:
            if orientacao.aluno.cpf == cpf_aluno:
                return orientacao
        return None

    def cadastrar_orientacao(self):
        # Obter lista de alunos e professores disponíveis
        alunos_disponiveis = [
            {"cpf": aluno.cpf, "nome": aluno.nome} for aluno in
            self.__controlador_sistema.controlador_alunos.listar_todos_alunos()
        ]
        professores_disponiveis = [
            {"cpf": professor.cpf, "nome": professor.nome} for professor in
            self.__controlador_sistema.controlador_professores.listar_todos_professores()
        ]

        print("Alunos disponíveis para seleção:", alunos_disponiveis)  # Verificar alunos disponíveis
        print("Professores disponíveis para seleção:", professores_disponiveis)  # Verificar professores disponíveis

        if not alunos_disponiveis:
            self.__tela_orientacao.mostrar_mensagem("Não há alunos disponíveis.")
            return

        if not professores_disponiveis:
            self.__tela_orientacao.mostrar_mensagem("Não há professores disponíveis.")
            return

        # Selecionar aluno
        cpf_aluno = self.__tela_orientacao.selecionar_aluno(alunos_disponiveis)
        if not cpf_aluno:
            self.__tela_orientacao.mostrar_mensagem("Seleção de aluno cancelada.")
            return

        # Selecionar professor
        cpf_professor = self.__tela_orientacao.selecionar_professor(professores_disponiveis)
        if not cpf_professor:
            self.__tela_orientacao.mostrar_mensagem("Seleção de professor cancelada.")
            return

        # Debug: Verificar CPFs
        print(f"Aluno CPF selecionado: {cpf_aluno}")
        print(f"Professor CPF selecionado: {cpf_professor}")

        aluno = self.__controlador_sistema.controlador_alunos.buscar_aluno_pelo_cpf(cpf_aluno)
        professor = self.__controlador_sistema.controlador_professores.buscar_professor_por_cpf(cpf_professor)

        # Verificar se aluno e professor foram encontrados
        if not aluno:
            self.__tela_orientacao.mostrar_mensagem("Aluno não encontrado.")
            return

        if not professor:
            self.__tela_orientacao.mostrar_mensagem("Professor não encontrado.")
            return

        # Verificar se já existe a orientação
        for orientacao in self.__orientacoes:
            if orientacao.aluno.cpf == aluno.cpf and orientacao.professor.cpf == professor.cpf:
                self.__tela_orientacao.mostrar_mensagem("Orientação já cadastrada para este aluno e professor.")
                return

        nova_orientacao = Orientacao(aluno, professor)
        self.__orientacoes.append(nova_orientacao)
        self.__tela_orientacao.mostrar_mensagem("Orientação cadastrada com sucesso!")

    def listar_orientacoes(self):
        if not self.__orientacoes:
            self.__tela_orientacao.mostrar_mensagem("Nenhuma orientação cadastrada.")
        else:
            orientacoes = [
                {
                    "nome_aluno": o.aluno.nome,
                    "cpf_aluno": o.aluno.cpf,
                    "nome_professor": o.professor.nome,
                    "cpf_professor": o.professor.cpf,
                }
                for o in self.__orientacoes
            ]
            self.__tela_orientacao.listar_orientacoes(orientacoes)

    def editar_orientacao(self):
        cpf_aluno = self.__tela_orientacao.selecionar_orientacao()
        orientacao = self.buscar_orientacao_por_cpf_aluno(cpf_aluno)

        if orientacao:
            novo_cpf_professor = self.__tela_orientacao.selecionar_orientacao("Digite o CPF do novo professor:")
            professor = self.__controlador_sistema.controlador_professores.buscar_professor_por_cpf(novo_cpf_professor)

            if professor:
                orientacao.professor = professor
                self.__tela_orientacao.mostrar_mensagem("Orientação atualizada com sucesso!")
            else:
                self.__tela_orientacao.mostrar_mensagem("Erro: Professor não encontrado.")
        else:
            self.__tela_orientacao.mostrar_mensagem("Erro: Orientação não encontrada.")

    def excluir_orientacao(self):
        cpf_aluno = self.__tela_orientacao.selecionar_orientacao()
        orientacao = self.buscar_orientacao_por_cpf_aluno(cpf_aluno)

        if orientacao:
            self.__orientacoes.remove(orientacao)
            self.__tela_orientacao.mostrar_mensagem("Orientação excluída com sucesso!")
        else:
            self.__tela_orientacao.mostrar_mensagem("Erro: Orientação não encontrada.")

    def listar_orientandos_do_professor(self):
        cpf_professor = self.__tela_orientacao.selecionar_orientacao("Digite o CPF do professor:")
        orientandos = [
            {"nome_aluno": o.aluno.nome, "cpf_aluno": o.aluno.cpf}
            for o in self.__orientacoes
            if o.professor.cpf == cpf_professor
        ]

        if orientandos:
            for orientando in orientandos:
                self.__tela_orientacao.mostrar_orientacao(orientando)
        else:
            self.__tela_orientacao.mostrar_mensagem("Nenhum orientando encontrado para este professor.")

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {
            1: self.cadastrar_orientacao,
            2: self.listar_orientacoes,
            3: self.editar_orientacao,
            4: self.excluir_orientacao,
            5: self.listar_orientandos_do_professor,
        }

        while True:
            opcao = self.__tela_orientacao.mostrar_menu_opcoes()
            if opcao == 0:
                self.voltar()
                break
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.__tela_orientacao.mostrar_mensagem("Opção inválida. Tente novamente.")

