from models.orientacao import Orientacao
from views.tela_orientacao import TelaOrientacao
from daos.orientacao_dao import OrientacaoDAO


class ControladorOrientacao:
    def __init__(self, controlador_sistema):
        self.__orientacao_dao = OrientacaoDAO()
        self.__tela_orientacao = TelaOrientacao()
        self.__controlador_sistema = controlador_sistema

    def buscar_orientacao_por_cpf_aluno(self, cpf_aluno):
        for orientacao in self.__orientacao_dao.get_all():
            if orientacao.aluno.cpf == cpf_aluno:
                return orientacao
        return None

    def cadastrar_orientacao(self):
        # Obter lista de alunos e professores disponíveis
        alunos_disponiveis = [
            {"cpf": aluno.cpf, "nome": aluno.nome}
            for aluno in self.__controlador_sistema.controlador_alunos.listar_todos_alunos()
        ]
        professores_disponiveis = [
            {"cpf": professor.cpf, "nome": professor.nome}
            for professor in self.__controlador_sistema.controlador_professores.listar_todos_professores()
        ]

        if not alunos_disponiveis:
            self.__tela_orientacao.mostrar_mensagem("Não há alunos disponíveis.")
            return

        if not professores_disponiveis:
            self.__tela_orientacao.mostrar_mensagem("Não há professores disponíveis.")
            return

        # Selecionar aluno diretamente
        aluno_selecionado = self.__controlador_sistema.controlador_alunos.selecionar_aluno("Selecione o aluno:")
        if not aluno_selecionado:
            self.__tela_orientacao.mostrar_mensagem("Seleção de aluno cancelada.")
            return

        # Selecionar professor diretamente
        professor_selecionado_dados = self.__tela_orientacao.selecionar_professor(professores_disponiveis)
        if not professor_selecionado_dados:
            self.__tela_orientacao.mostrar_mensagem("Seleção de professor cancelada.")
            return

        # Buscar a instância do professor pela CPF
        professor_selecionado = self.__controlador_sistema.controlador_professores.buscar_professor_por_cpf(
            professor_selecionado_dados["cpf"]
        )
        if not professor_selecionado:
            self.__tela_orientacao.mostrar_mensagem("Erro ao encontrar a instância do professor.")
            return

        # Criar e cadastrar a orientação
        nova_orientacao = Orientacao(aluno_selecionado, professor_selecionado)
        self.__orientacao_dao.add(nova_orientacao)
        self.__tela_orientacao.mostrar_mensagem("Orientação cadastrada com sucesso!")

    def listar_orientacoes(self):
        orientacoes = [
            {
                "nome_aluno": o.aluno.nome,
                "cpf_aluno": o.aluno.cpf,
                "nome_professor": o.professor.nome,
                "cpf_professor": o.professor.cpf,
            }
            for o in self.__orientacao_dao.get_all()
        ]

        if not orientacoes:
            self.__tela_orientacao.mostrar_mensagem("Nenhuma orientação cadastrada.")
        else:
            self.__tela_orientacao.listar_orientacoes(orientacoes)

    def editar_orientacao(self):
        aluno = self.__controlador_sistema.controlador_alunos.selecionar_aluno(
            "Selecione o aluno cuja orientação deseja editar:"
        )
        if not aluno:
            self.__tela_orientacao.mostrar_mensagem("Seleção de aluno cancelada ou aluno não encontrado.")
            return

        orientacao = self.buscar_orientacao_por_cpf_aluno(aluno.cpf)
        if orientacao:
            professores_disponiveis = [
                {"cpf": professor.cpf, "nome": professor.nome}
                for professor in self.__controlador_sistema.controlador_professores.listar_todos_professores()
            ]

            if not professores_disponiveis:
                self.__tela_orientacao.mostrar_mensagem("Não há professores disponíveis para seleção.")
                return

            novo_professor_dados = self.__tela_orientacao.selecionar_professor(professores_disponiveis)
            if not novo_professor_dados:
                self.__tela_orientacao.mostrar_mensagem("Seleção de professor cancelada.")
                return

            novo_professor = self.__controlador_sistema.controlador_professores.buscar_professor_por_cpf(
                novo_professor_dados["cpf"]
            )
            if not novo_professor:
                self.__tela_orientacao.mostrar_mensagem("Erro: Professor não encontrado.")
                return

            orientacao.professor = novo_professor
            self.__orientacao_dao.update(orientacao)
            self.__tela_orientacao.mostrar_mensagem("Orientação atualizada com sucesso!")
        else:
            self.__tela_orientacao.mostrar_mensagem("Erro: Orientação não encontrada.")

    def excluir_orientacao(self):
        cpf_aluno = self.__tela_orientacao.selecionar_orientacao()
        orientacao = self.buscar_orientacao_por_cpf_aluno(cpf_aluno)

        if orientacao:
            self.__orientacao_dao.remove(orientacao)
            self.__tela_orientacao.mostrar_mensagem("Orientação excluída com sucesso!")
        else:
            self.__tela_orientacao.mostrar_mensagem("Erro: Orientação não encontrada.")

    def listar_orientandos_do_professor(self):
        professores_disponiveis = [
            {"cpf": professor.cpf, "nome": professor.nome}
            for professor in self.__controlador_sistema.controlador_professores.listar_todos_professores()
        ]

        if not professores_disponiveis:
            self.__tela_orientacao.mostrar_mensagem("Não há professores disponíveis para seleção.")
            return

        professor_selecionado = self.__tela_orientacao.selecionar_professor(professores_disponiveis)
        if not professor_selecionado:
            self.__tela_orientacao.mostrar_mensagem("Seleção de professor cancelada.")
            return

        orientandos = [
            {"nome": orientacao.aluno.nome, "cpf": orientacao.aluno.cpf}
            for orientacao in self.__orientacao_dao.get_all()
            if orientacao.professor.cpf == professor_selecionado["cpf"]
        ]

        if not orientandos:
            self.__tela_orientacao.mostrar_mensagem("Nenhum orientando encontrado para este professor.")
        else:
            orientandos_formatados = [
                f"Nome: {orientando['nome']} | CPF: {orientando['cpf']}" for orientando in orientandos
            ]
            self.__tela_orientacao.mostrar_lista_orientandos(orientandos_formatados)

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

