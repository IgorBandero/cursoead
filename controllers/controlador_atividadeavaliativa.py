from models.questao import Questao
from models.atividadeavaliativa import AtividadeAvaliativa
from views.TelaAtividadeAvaliativa import TelaAtividadeAvaliativa
from daos.atividade_avaliativa_dao import AtividadeAvaliativaDAO



class ControladorAtividadeAvaliativa:
    def __init__(self, controlador_questao, controlador_aluno, controlador_sistema):
        self.__atividade_dao = AtividadeAvaliativaDAO()  # DAO para persistência
        self.__tela_atividade = TelaAtividadeAvaliativa()
        self.__controlador_questao = controlador_questao
        self.__controlador_aluno = controlador_aluno
        self.__controlador_sistema = controlador_sistema
        self.__id_atual = self.__gerar_proximo_id()  # Para IDs únicos
        self.__notas_atividade = {}

    def __gerar_proximo_id(self):
        """
        Gera o próximo ID único baseado nas atividades persistidas.
        """
        atividades = self.__atividade_dao.get_all()
        if atividades:
            return max(atividade.id for atividade in atividades) + 1
        return 1

    def cadastrar_atividade(self):
        dados_atividade = self.__tela_atividade.pega_dados_atividade()

        if dados_atividade:
            quantidade_questoes = dados_atividade.get("quantidade_questoes", 0)

            if quantidade_questoes <= 0:
                self.__tela_atividade.mostra_mensagem("Quantidade de questões inválida.")
                return

            questoes_selecionadas = self.selecionar_questoes_existentes(quantidade_questoes)
            if not questoes_selecionadas:
                self.__tela_atividade.mostra_mensagem("Atividade não pode ser criada sem questões.")
                return

            atividade = AtividadeAvaliativa(
                id=self.__id_atual,
                questoes=questoes_selecionadas,
                nota_maxima=dados_atividade["nota_maxima"]
            )
            self.__atividade_dao.add(atividade)  # Salva no DAO
            self.__id_atual += 1
            self.__tela_atividade.mostra_mensagem("Atividade cadastrada com sucesso!")

    def listar_atividades(self):
        atividades = self.__atividade_dao.get_all()

        if not atividades:
            self.__tela_atividade.mostra_mensagem("Nenhuma atividade cadastrada.")
            return

        lista_dados_atividades = [
            {
                "id": atividade.id,
                "nota_maxima": atividade.nota_maxima,
                "questoes": [
                    {
                        "enunciado": questao.enunciado,
                        "alternativas": questao.alternativas,
                        "respostas_corretas": questao.respostas_corretas
                    }
                    for questao in atividade.questoes
                ]
            }
            for atividade in atividades
        ]
        self.__tela_atividade.listar_atividades(lista_dados_atividades)

    def selecionar_atividade(self):
        atividades = self.__atividade_dao.get_all()

        if not atividades:
            self.__tela_atividade.mostra_mensagem("Nenhuma atividade cadastrada.")
            return None

        lista_atividades = [{"id": atividade.id, "nota_maxima": atividade.nota_maxima} for atividade in atividades]
        id_atividade = self.__tela_atividade.seleciona_atividade(lista_atividades)

        if id_atividade:
            return self.__atividade_dao.get(id_atividade)
        return None

    def editar_atividade(self):
        atividade = self.selecionar_atividade()
        if atividade:
            dados_atividade = {
                "nota_maxima": atividade.nota_maxima,
                "questoes": [
                    {
                        "id": questao.id,
                        "enunciado": questao.enunciado,
                        "alternativas": questao.alternativas,
                        "respostas_corretas": questao.respostas_corretas
                    }
                    for questao in atividade.questoes
                ]
            }

            dados_atualizados = self.__tela_atividade.editar_atividade(dados_atividade)
            if dados_atualizados:
                atividade.nota_maxima = dados_atualizados["nota_maxima"]
                atividade.questoes = [
                    Questao(
                        id=questao["id"],
                        enunciado=questao["enunciado"],
                        alternativas=questao["alternativas"],
                        respostas_corretas=questao["respostas_corretas"]
                    )
                    for questao in dados_atualizados["questoes"]
                ]
                self.__atividade_dao.update(atividade)
                self.__tela_atividade.mostra_mensagem("Atividade atualizada com sucesso!")

    def remover_atividade(self):
        atividade = self.selecionar_atividade()
        if atividade:
            confirmacao = self.__tela_atividade.excluir_atividade({"id": atividade.id})
            if confirmacao:
                self.__atividade_dao.remove(atividade.id)
                self.__tela_atividade.mostra_mensagem("Atividade removida com sucesso!")

    def adicionar_nota_para_aluno(self):
        lista_alunos = [
            {"cpf": aluno.cpf, "nome": aluno.nome} for aluno in self.__controlador_aluno.listar_todos_alunos()
        ]

        if not lista_alunos:
            self.__tela_atividade.mostra_mensagem("Não há alunos disponíveis para atribuir nota.")
            return

        dados_nota = self.__tela_atividade.pega_dados_nota(lista_alunos)
        if not dados_nota:
            return

        atividade = self.__atividade_dao.get(dados_nota["atividade_id"])
        if not atividade:
            self.__tela_atividade.mostra_mensagem("Atividade não encontrada.")
            return

        if dados_nota["nota"] > atividade.nota_maxima:
            self.__tela_atividade.mostra_mensagem("Nota excede a nota máxima da atividade.")
            return

        if atividade.id not in self.__notas_atividade:
            self.__notas_atividade[atividade.id] = {}

        self.__notas_atividade[atividade.id][dados_nota["aluno_cpf"]] = dados_nota["nota"]
        self.__tela_atividade.mostra_mensagem("Nota adicionada com sucesso!")

    def gerar_relatorio_atividade(self):
        atividades = self.__atividade_dao.get_all()

        if not atividades:
            self.__tela_atividade.mostra_mensagem("Nenhuma atividade cadastrada.")
            return

        lista_atividades = [{"id": atividade.id, "nota_maxima": atividade.nota_maxima} for atividade in atividades]
        id_atividade = self.__tela_atividade.seleciona_atividade(lista_atividades)

        if id_atividade:
            atividade = self.__atividade_dao.get(id_atividade)
            if atividade:
                notas = list(self.__notas_atividade.get(id_atividade, {}).values())
                if notas:
                    dados_relatorio = {
                        "nota_maxima": max(notas),
                        "nota_minima": min(notas),
                        "quantidade_alunos": len(notas),
                        "nota_media": sum(notas) / len(notas),
                    }
                else:
                    dados_relatorio = {
                        "nota_maxima": 0,
                        "nota_minima": 0,
                        "quantidade_alunos": 0,
                        "nota_media": 0,
                    }
                self.__tela_atividade.mostrar_relatorio(dados_relatorio)
            else:
                self.__tela_atividade.mostra_mensagem("Atividade não encontrada.")

    def selecionar_questoes_existentes(self, quantidade):
        questoes_disponiveis = self.__controlador_questao.listar_questoes_disponiveis()

        if not questoes_disponiveis:
            self.__tela_atividade.mostra_mensagem("Nenhuma questão disponível.")
            return []

        ids_selecionados = self.__tela_atividade.selecionar_multiplos_itens(questoes_disponiveis)

        if not ids_selecionados or len(ids_selecionados) < quantidade:
            self.__tela_atividade.mostra_mensagem("Número insuficiente de questões selecionadas.")
            return []

        questoes_selecionadas = [
            Questao(
                id=questao["id"],
                enunciado=questao["enunciado"],
                alternativas=questao["alternativas"],
                respostas_corretas=questao["respostas_corretas"]
            )
            for questao in questoes_disponiveis if questao["id"] in ids_selecionados
        ]
        return questoes_selecionadas

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {
            1: self.cadastrar_atividade,
            2: self.editar_atividade,
            3: self.remover_atividade,
            4: self.listar_atividades,
            5: self.adicionar_nota_para_aluno,
            6: self.gerar_relatorio_atividade,
        }

        while True:
            opcao = self.__tela_atividade.mostrar_menu_opcoes()
            if opcao == 0:  # Opção "Voltar"
                self.voltar()
                break
            funcao_escolhida = opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_atividade.mostra_mensagem("Opção inválida.")