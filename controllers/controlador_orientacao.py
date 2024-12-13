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

        print("Alunos disponíveis:", alunos_disponiveis)
        print("Professores disponíveis:", professores_disponiveis)

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

        print(f"Aluno selecionado: {aluno_selecionado.nome}")
        print(f"Professor selecionado: {professor_selecionado.nome}")

        # Criar e cadastrar a orientação
        nova_orientacao = Orientacao(aluno_selecionado, professor_selecionado)
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
        # Selecionar aluno da lista
        aluno = self.__controlador_sistema.controlador_alunos.selecionar_aluno(
            "Selecione o aluno cuja orientação deseja editar:")
        if not aluno:
            self.__tela_orientacao.mostrar_mensagem("Seleção de aluno cancelada ou aluno não encontrado.")
            return

        # Buscar a orientação pelo CPF do aluno selecionado
        orientacao = self.buscar_orientacao_por_cpf_aluno(aluno.cpf)

        if orientacao:
            # Selecionar o novo professor da lista
            professores_disponiveis = [
                {"cpf": professor.cpf, "nome": professor.nome} for professor in
                self.__controlador_sistema.controlador_professores.listar_todos_professores()
            ]

            if not professores_disponiveis:
                self.__tela_orientacao.mostrar_mensagem("Não há professores disponíveis para seleção.")
                return

            novo_professor_dados = self.__tela_orientacao.selecionar_professor(professores_disponiveis)
            if not novo_professor_dados:
                self.__tela_orientacao.mostrar_mensagem("Seleção de professor cancelada.")
                return

            # Buscar a instância do novo professor pelo CPF selecionado
            novo_professor = self.__controlador_sistema.controlador_professores.buscar_professor_por_cpf(
                novo_professor_dados["cpf"])
            if not novo_professor:
                self.__tela_orientacao.mostrar_mensagem("Erro: Professor não encontrado.")
                return

            # Atualizar a orientação com o novo professor
            orientacao.professor = novo_professor
            self.__tela_orientacao.mostrar_mensagem("Orientação atualizada com sucesso!")
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
        # Obter a lista de professores disponíveis
        professores_disponiveis = [
            {"cpf": professor.cpf, "nome": professor.nome}
            for professor in self.__controlador_sistema.controlador_professores.listar_todos_professores()
        ]

        if not professores_disponiveis:
            self.__tela_orientacao.mostrar_mensagem("Não há professores disponíveis para seleção.")
            return

        # Selecionar professor
        professor_selecionado = self.__tela_orientacao.selecionar_professor(professores_disponiveis)
        if not professor_selecionado:
            self.__tela_orientacao.mostrar_mensagem("Seleção de professor cancelada.")
            return

        # Obter os orientandos do professor selecionado
        orientandos = [
            {"nome": orientacao.aluno.nome, "cpf": orientacao.aluno.cpf}
            for orientacao in self.__orientacoes
            if orientacao.professor.cpf == professor_selecionado["cpf"]
        ]

        if not orientandos:
            self.__tela_orientacao.mostrar_mensagem("Nenhum orientando encontrado para este professor.")
            return

        # Exibir a lista de orientandos
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

