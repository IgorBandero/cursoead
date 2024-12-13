from views.telaquestao import TelaQuestao
from models.questao import Questao
from daos.questao_dao import QuestaoDAO  # Importa o DAO

class ControladorQuestao:
    def __init__(self, controlador_sistema):
        self.__questao_DAO = QuestaoDAO()  # Inicializa o DAO
        self.__tela_questao = TelaQuestao()
        self.__controlador_sistema = controlador_sistema

    def pega_questao_por_id(self, id):
        for questao in self.__questao_DAO.get_all():
            if questao.id == id:
                return questao
        return None

    def incluir_questao(self):
        dados_questao = self.__tela_questao.pega_dados_questao()
        if dados_questao:
            questao_existente = self.pega_questao_por_id(dados_questao["id"])
            if questao_existente is None:
                questao = Questao(**dados_questao)
                self.__questao_DAO.add(questao)  # Salva no DAO
                self.__tela_questao.mostra_mensagem("Questão adicionada com sucesso!")
            else:
                self.__tela_questao.mostra_mensagem("ID já existe!")

    def listar_questoes_disponiveis(self):
        # Retorna uma lista de dicionários representando as questões disponíveis
        return [
            {
                "id": questao.id,
                "enunciado": questao.enunciado,
                "alternativas": questao.alternativas,
                "respostas_corretas": questao.respostas_corretas
            }
            for questao in self.__questao_DAO.get_all()
        ]

    def get_lista_questoes(self):
        """
        Retorna a lista de objetos Questao armazenados no DAO.
        """
        return self.__questao_DAO.get_all()

    def editar_questao(self):
        questoes_disponiveis = [
            {
                "id": questao.id,
                "enunciado": questao.enunciado
            } for questao in self.__questao_DAO.get_all()
        ]
        id_questao = self.__tela_questao.seleciona_questao(questoes_disponiveis)
        questao = self.pega_questao_por_id(id_questao)

        if questao:
            dados_atualizados = self.__tela_questao.pega_dados_questao({
                "id": questao.id,
                "enunciado": questao.enunciado,
                "alternativas": questao.alternativas,
                "respostas_corretas": questao.respostas_corretas
            })
            if dados_atualizados:
                questao.enunciado = dados_atualizados["enunciado"]
                questao.alternativas = dados_atualizados["alternativas"]
                questao.respostas_corretas = dados_atualizados["respostas_corretas"]
                self.__questao_DAO.update(questao)  # Atualiza no DAO
                self.__tela_questao.mostra_mensagem("Questão editada com sucesso!")
            else:
                self.__tela_questao.mostra_mensagem("Edição cancelada pelo usuário.")
        else:
            self.__tela_questao.mostra_mensagem("Questão não encontrada.")

    def excluir_questao(self):
        questoes_disponiveis = [
            {
                "id": questao.id,
                "enunciado": questao.enunciado
            } for questao in self.__questao_DAO.get_all()
        ]
        id_questao = self.__tela_questao.seleciona_questao(questoes_disponiveis)
        questao = self.pega_questao_por_id(id_questao)

        if questao:
            confirmacao = self.__tela_questao.excluir_questao({
                "id": questao.id,
                "enunciado": questao.enunciado
            })
            if confirmacao:
                self.__questao_DAO.remove(questao.id)  # Remove no DAO
                self.__tela_questao.mostra_mensagem("Questão excluída com sucesso!")
            else:
                self.__tela_questao.mostra_mensagem("Exclusão cancelada pelo usuário.")
        else:
            self.__tela_questao.mostra_mensagem("Questão não encontrada.")

    def abre_tela(self):
        opcoes = {
            1: self.incluir_questao,
            2: self.editar_questao,
            3: self.excluir_questao,
            4: self.listar_questoes_disponiveis
        }

        while True:
            opcao = self.__tela_questao.mostrar_menu_opcoes()
            if opcao == 0:  # Opção "Voltar"
                self.voltar()
                break
            funcao_escolhida = opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_questao.mostra_mensagem("Opção inválida.")

    def voltar(self):
        self.__controlador_sistema.abrir_tela()