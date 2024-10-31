class TelaAtividadeAvaliativa:
    def mostrar_menu_opcoes(self):
        print("-------- ATIVIDADES AVALIATIVAS ----------")
        print("1. Adicionar Atividade Avaliativa")
        print("2. Remover Atividade Avaliativa")
        print("3. Listar Atividades Avaliativas")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")
        return int(opcao)

    def pega_dados_atividade(self):
        nota_maxima = float(input("Nota Máxima da Atividade: "))
        quantidade_questoes = int(input("Quantas questões deseja adicionar à atividade? "))
        return {"nota_maxima": nota_maxima, "quantidade_questoes": quantidade_questoes}

    def mostra_atividade(self, dados_atividade):
        print("-------- ATIVIDADE AVALIATIVA ----------")
        print("ID:", dados_atividade["id"]) 
        print("Nota Máxima:", dados_atividade["nota_maxima"])
        print("Questões:")
        for questao in dados_atividade["questoes"]:
            print("  Enunciado:", questao["enunciado"])
            print("  Alternativas:", ", ".join(questao["alternativas"]))
            print("  Resposta Correta:", ", ".join(questao["respostas_corretas"]))
        print("\n")

    def mostra_mensagem(self, msg):
        print(msg)

    def seleciona_atividade(self):
        return int(input("ID da atividade que deseja selecionar: "))



