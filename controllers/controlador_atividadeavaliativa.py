from models.questao import Questao
from models.atividadeavaliativa import AtividadeAvaliativa
from views.TelaAtividadeAvaliativa import TelaAtividadeAvaliativa
from controllers.controlador_questao import ControladorQuestao

class ControladorAtividadeAvaliativa:
    def __init__(self, controlador_questao, controlador_aluno, controlador_sistema):
        self.__atividades = []
        self.__tela_atividade = TelaAtividadeAvaliativa()
        self.__controlador_questao = controlador_questao
        self.__controlador_aluno = controlador_aluno  # Atribui o controlador de alunos
        self.__controlador_sistema = controlador_sistema  # Atribui o controlador do sistema
        self.__id_atual = 1
        self.__notas_atividade = {}

    def gerar_id(self):
        """Gera um ID único para cada atividade."""
        id_gerado = self.__id_atual
        self.__id_atual += 1
        return id_gerado

    def cadastrar_atividade(self):
        dados_atividade = self.__tela_atividade.pega_dados_atividade()

        if dados_atividade:
            quantidade_questoes = dados_atividade.get("quantidade_questoes", 0)

            if quantidade_questoes <= 0:
                self.__tela_atividade.mostra_mensagem("Quantidade de questões inválida.")
                return

            # Selecionar as questões para a atividade
            questoes_selecionadas = self.selecionar_questoes_existentes(quantidade_questoes)

            if not questoes_selecionadas:
                self.__tela_atividade.mostra_mensagem("Atividade não pode ser criada sem questões.")
                return

            # Criar a nova atividade
            atividade = AtividadeAvaliativa(
                id=self.gerar_id(),
                questoes=questoes_selecionadas,
                nota_maxima=dados_atividade["nota_maxima"]
            )
            self.__atividades.append(atividade)
            self.__tela_atividade.mostra_mensagem("Atividade cadastrada com sucesso!")

    def listar_atividades(self):
        try:
            if not self.__atividades:
                raise ListaAtividadesVaziaException
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
                for atividade in self.__atividades
            ]
            self.__tela_atividade.listar_atividades(lista_dados_atividades)
        except ListaAtividadesVaziaException as e:
            self.__tela_atividade.mostra_mensagem(str(e))

    def selecionar_atividade(self):
        try:
            atividades = [{"id": a.id, "nota_maxima": a.nota_maxima} for a in self.__atividades]
            if not atividades:
                raise ListaAtividadesVaziaException
            id_atividade = self.__tela_atividade.seleciona_atividade(atividades)
            atividade = next((a for a in self.__atividades if a.id == id_atividade), None)
            if atividade:
                return atividade
            else:
                raise ValueError("Atividade não encontrada.")
        except ListaAtividadesVaziaException as e:
            self.__tela_atividade.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_atividade.mostra_mensagem(str(e))
        return None

    def editar_atividade(self):
        atividade = self.selecionar_atividade()
        if atividade:
            dados_atividade = {
                "nota_maxima": atividade.nota_maxima,
                "questoes": [
                    {
                        "id": q.id,
                        "enunciado": q.enunciado,
                        "alternativas": q.alternativas,
                        "respostas_corretas": q.respostas_corretas
                    }
                    for q in atividade.questoes
                ]
            }

            dados_atualizados = self.__tela_atividade.editar_atividade(dados_atividade)

            if dados_atualizados:
                atividade.nota_maxima = dados_atualizados["nota_maxima"]

                # Atualizar questões selecionadas
                questoes_atualizadas = [
                    Questao(
                        id=questao["id"],
                        enunciado=questao["enunciado"],
                        alternativas=questao["alternativas"],
                        respostas_corretas=questao["respostas_corretas"]
                    )
                    for questao in dados_atualizados["questoes"]
                ]
                atividade.questoes = questoes_atualizadas

                self.__tela_atividade.mostra_mensagem("Atividade atualizada com sucesso!")

    def buscar_atividade_por_id(self, id_atividade):
        for atividade in self.__atividades:
            if atividade.id == id_atividade:
                return atividade
        return None

    def remover_atividade(self):
        atividade = self.selecionar_atividade()
        if atividade:
            confirmacao = self.__tela_atividade.excluir_atividade({"id": atividade.id})
            if confirmacao:
                self.__atividades.remove(atividade)
                self.__tela_atividade.mostra_mensagem("Atividade removida com sucesso!")

    def adicionar_nota_para_aluno(self):
        # Obter a lista de alunos disponíveis
        lista_alunos = [
            {"cpf": aluno.cpf, "nome": aluno.nome} for aluno in self.__controlador_aluno.listar_todos_alunos()
        ]

        if not lista_alunos:
            self.__tela_atividade.mostra_mensagem("Não há alunos disponíveis para atribuir nota.")
            return

        # Obter os dados da nota
        dados_nota = self.__tela_atividade.pega_dados_nota(lista_alunos)
        if not dados_nota:
            return

        # Busca a atividade pelo ID
        atividade = self.buscar_atividade_por_id(dados_nota["atividade_id"])
        if not atividade:
            self.__tela_atividade.mostra_mensagem(f"Atividade com ID {dados_nota['atividade_id']} não encontrada.")
            return

        # Verifica se a nota é válida
        if dados_nota["nota"] > atividade.nota_maxima:
            self.__tela_atividade.mostra_mensagem("Nota excede a nota máxima da atividade.")
            return

        # Adiciona a nota para o aluno na atividade
        if atividade.id not in self.__notas_atividade:
            self.__notas_atividade[atividade.id] = {}

        self.__notas_atividade[atividade.id][dados_nota["aluno_cpf"]] = dados_nota["nota"]
        self.__tela_atividade.mostra_mensagem("Nota adicionada com sucesso!")

    def gerar_relatorio_atividade(self):
        # Obter a lista de atividades disponíveis
        lista_atividades = [
            {"id": atividade.id, "nota_maxima": atividade.nota_maxima}
            for atividade in self.__atividades
        ]

        if not lista_atividades:
            self.__tela_atividade.mostra_mensagem("Não há atividades cadastradas para gerar relatório.")
            return

        # Selecionar a atividade para gerar o relatório
        id_atividade = self.__tela_atividade.seleciona_atividade(lista_atividades)
        if not id_atividade:
            return

        # Buscar a atividade pelo ID selecionado
        atividade = self.buscar_atividade_por_id(id_atividade)

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
        # Obter as questões disponíveis como dicionários
        questoes_disponiveis = self.__controlador_questao.listar_questoes_disponiveis()

        if not questoes_disponiveis:
            self.__tela_atividade.mostra_mensagem("Nenhuma questão disponível.")
            return []

        # Permitir a seleção de múltiplas questões
        ids_selecionados = self.__tela_atividade.selecionar_multiplos_itens(questoes_disponiveis)

        if not ids_selecionados or len(ids_selecionados) < quantidade:
            self.__tela_atividade.mostra_mensagem("Número insuficiente de questões selecionadas.")
            return []

        # Converter IDs selecionados para objetos Questao
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
        """
        Exibe o menu principal de atividades avaliativas e gerencia as opções selecionadas.
        """
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