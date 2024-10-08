from telaquestao import TelaQuestao

class ControladorQuestao():
    def __init__(self):
        self.__questoes = []
        self.__tela_questao = TelaQuestao()

    def pega_questao_por_id(self, id: int):
        for questao in self.__questoes:
            if(questao.id == id):
                return questao
            return None

    def incluir_questao(self):
        dados_questao = self.__tela_questao.pega_dados_questao()
        q = self.pega_questao_por_id(dados_questao["id"])
        if q is None:
            questao = Livro(dados_questao["id"], dados_questao["enunciado"],dados_questao["alternativas"],dados_questao["resposta_correta"])
            self.__questoes.append(questao)
        else:
            self.__tela_questao.mostra_mensagem("ATENCAO: Questao já existente")

    def lista_questao(self):
        for questao in self.__questoes:
            self.__tela_questao.mostra_questao({"id": questao.id, "enunciado": questao.enunciado})
        
    def excluir_questao(self):
        self.lista_questao()
        id_questao = self.__tela_livro.seleciona_questao()
        questao = self.pega_livro_por_id(id_questao)

        if(questao is not None):
            self.__questoes.remove(questao)
        else:
            self.__tela_livro.mostra_mensagem("ATENCAO: Questao não existente")
    

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_questao, 2: self.excluir_questao}

        continua = True
        while continua:
            lista_opcoes[self.__tela_questao.mostrar_menu_opcoes()]()