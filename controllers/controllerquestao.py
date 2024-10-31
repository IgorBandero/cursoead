from views.telaquestao import TelaQuestao
from models.questao import Questao

class ControladorQuestao:
    def __init__(self):
        self.__questoes = []
        self.__tela_questao = TelaQuestao()

    def pega_questao_por_id(self, id: int):
        for questao in self.__questoes:
            if questao.id == id:
                return questao
        return None

    def incluir_questao(self):
        dados_questao = self.__tela_questao.pega_dados_questao()
        q = self.pega_questao_por_id(dados_questao["id"])
        
        if q is None:
            questao = Questao(dados_questao["id"], dados_questao["enunciado"],
                              dados_questao["alternativas"], dados_questao["resposta_correta"])
            self.__questoes.append(questao)
            self.__tela_questao.mostra_mensagem("Questão adicionada com sucesso!")
        else:
            self.__tela_questao.mostra_mensagem("ATENÇÃO: Questão já existente")

    def lista_questao(self):
        for questao in self.__questoes:
            self.__tela_questao.mostra_questao({
                "id": questao.id,
                "enunciado": questao.enunciado,
                "alternativas": questao.alternativas,
                "resposta_correta": questao.respostas_corretas
            })

    def excluir_questao(self):
        self.lista_questao()
        id_questao = self.__tela_questao.seleciona_questao()
        questao = self.pega_questao_por_id(id_questao)

        if questao is not None:
            self.__questoes.remove(questao)
            self.__tela_questao.mostra_mensagem("Questão excluída com sucesso.")
        else:
            self.__tela_questao.mostra_mensagem("ATENÇÃO: Questão não existente")

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_questao, 2: self.excluir_questao, 3: self.lista_questao}
        
        while True:
            opcao = self.__tela_questao.mostrar_menu_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            
            if funcao_escolhida:
                funcao_escolhida()
            elif opcao == 0:
                self.__tela_questao.mostra_mensagem("Voltando...")
                break
            else:
                self.__tela_questao.mostra_mensagem("Opção inválida. Tente novamente.")