class TelaQuestao:
    def mostrar_menu_opcoes(self):
        print("-------- QUESTOES ----------")
        print("Escolha a opção:")
        print("----------------------------")
        print("1. Adicionar Questao")
        print("2. Excluir Questao")
        print("3. Listar Questões")
        print("0. Voltar")
        print("----------------------------")
        opcao = input("Escolha a opção: ")
        if (opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4" or  opcao == "5" or opcao == "0"):
            return int(opcao)
        else:
            print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")

    def pega_dados_questao(self):
        print("-------- DADOS DA QUESTÃO ----------")
        id = self.pegar_id()
        enunciado = self.pegar_enunciado()
        alternativas = self.pegar_alternativas()
        resposta_correta = self.pegar_resposta_correta(alternativas)
        
        return {
            "id": id,
            "enunciado": enunciado,
            "alternativas": alternativas,
            "resposta_correta": resposta_correta
        }

    def pegar_id(self):
        while True:
            try:
                id = int(input("ID da Questão: "))
                return id
            except ValueError:
                print("ID inválido! Insira um número inteiro.")

    def pegar_enunciado(self):
        while True:
            enunciado = input("Enunciado: ")
            if len(enunciado) >= 5:
                return enunciado
            else:
                print("Enunciado deve ter pelo menos 5 caracteres.")

    def pegar_alternativas(self):
        while True:
            alternativas = input("Alternativas (separadas por vírgula): ").split(", ")
            if len(alternativas) >= 2:
                return alternativas
            else:
                print("É necessário fornecer pelo menos duas alternativas.")

    def pegar_resposta_correta(self, alternativas):
        while True:
            resposta_correta = input("Resposta Correta (exatamente como aparece nas alternativas): ")
            if resposta_correta in alternativas:
                return resposta_correta
            else:
                print("Resposta correta inválida! Deve corresponder a uma das alternativas fornecidas.")

    def mostra_mensagem(self, msg):
        print(msg)

    def seleciona_questao(self):
        while True:
            try:
                id = int(input("Código da Questão que deseja selecionar: "))
                return id
            except ValueError:
                print("Código inválido! Insira um número inteiro.")

    def mostra_questao(self, dados_questao):
        print("-------- QUESTÃO ----------")
        print("ID DA QUESTÃO: ", dados_questao["id"])
        print("ENUNCIADO DA QUESTÃO: ", dados_questao["enunciado"])
        print("ALTERNATIVAS DA QUESTÃO: ", ", ".join(dados_questao["alternativas"]))
        print("RESPOSTA CORRETA: ", dados_questao["resposta_correta"])
        print("\n")



    