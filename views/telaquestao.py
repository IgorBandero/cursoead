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
        if opcao in {"1", "2", "3", "0"}:
            return int(opcao)
        else:
            print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")
            return None

    def pega_dados_questao(self):
        print("-------- DADOS DA QUESTAO ----------")
        id = self.pegar_id()
        enunciado = self.pegar_enunciado()
        alternativas = self.pegar_alternativas()
        resposta_correta = self.pegar_resposta_correta(alternativas)
        
        # Transforme resposta_correta em uma lista
        respostas_corretas = [resposta_correta]
        
        return {
            "id": id,
            "enunciado": enunciado,
            "alternativas": alternativas,
            "respostas_corretas": respostas_corretas
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

    def mostrar_questao(self, dados_questao):
        print("-------- QUESTAO ----------")
        print("ID DA QUESTAO: ", dados_questao["id"])
        print("ENUNCIADO DA QUESTAO: ", dados_questao["enunciado"])
        print("ALTERNATIVAS DA QUESTAO: ", ", ".join(dados_questao["alternativas"]))
        
        # Converte a lista de respostas corretas em uma string sem colchetes
        resposta_correta_str = ", ".join(dados_questao["respostas_corretas"])
        print("RESPOSTA CORRETA: ", resposta_correta_str)
        print("\n")



    