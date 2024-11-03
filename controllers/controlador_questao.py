from views.telaquestao import TelaQuestao
from models.questao import Questao

class ControladorQuestao:
    def __init__(self, controlador_sistema):
        self.__questoes = []
        self.__tela_questao = TelaQuestao()
        self.__controlador_sistema = controlador_sistema

    def pega_questao_por_id(self, id: int):
        """Busca uma questão pelo ID."""
        for questao in self.__questoes:
            if questao.id == id:
                return questao
        return None

    def incluir_questao(self):
        """Inclui uma nova questão no sistema."""
        dados_questao = self.__tela_questao.pega_dados_questao()
        questao_existente = self.pega_questao_por_id(dados_questao["id"])
        
        if questao_existente is None:
            questao = Questao(
                dados_questao["id"], 
                dados_questao["enunciado"],
                dados_questao["alternativas"], 
                dados_questao["respostas_corretas"]
            )
            self.__questoes.append(questao)
            self.__tela_questao.mostra_mensagem("Questão adicionada com sucesso!")
        else:
            self.__tela_questao.mostra_mensagem("ATENÇÃO: Questão com este ID já existente.")

    def listar_questoes_disponiveis(self):
        """Lista e retorna as questões disponíveis."""
        if not self.__questoes:
            self.__tela_questao.mostra_mensagem("Nenhuma questão cadastrada.")
        else:
            for questao in self.__questoes:
                self.__tela_questao.mostrar_questao({
                    "id": questao.id,
                    "enunciado": questao.enunciado,
                    "alternativas": questao.alternativas,
                    "respostas_corretas": questao.respostas_corretas
                })
        return self.__questoes


    def excluir_questao(self):
        """Exclui uma questão do sistema."""
        self.listar_questoes_disponiveis()
        id_questao = self.__tela_questao.seleciona_questao()
        questao = self.pega_questao_por_id(id_questao)

        if questao:
            self.__questoes.remove(questao)
            self.__tela_questao.mostra_mensagem("Questão excluída com sucesso.")
        else:
            self.__tela_questao.mostra_mensagem("ATENÇÃO: Questão não existente.")

    def abre_tela(self):
        """Abre o menu de opções do controlador de questões."""
        lista_opcoes = {
            1: self.incluir_questao,
            2: self.excluir_questao,
            3: self.listar_questoes_disponiveis
        }
        
        while True:
            opcao = self.__tela_questao.mostrar_menu_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            
            if funcao_escolhida:
                funcao_escolhida()
            elif opcao == 0:
                self.__tela_questao.mostra_mensagem("Voltando...")
                break
            else:
                self.__tela_questao.mostra_mensagem("Opção inválida.")

