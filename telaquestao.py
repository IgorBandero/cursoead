class TelaQuestao():

    def mostrar_menu_opcoes(self):
        print("-------- QUESTOES ----------")
        print("Escolha a opcao")
        print("1. Adicionar Questao")
        print("2. Excluir Questao")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")
        return int(opcao)

    def pega_dados_questao(self):
        print("-------- DADOS QUESTAO ----------")
        id = input("Id: ")
        enunciado = input("Enunciado: ")
        alternativas = input("Alternativas: ")
        resposta_correta = input("Resposta Correta: ")

    def mostra_mensagem(self, msg):
        print(msg)

    def seleciona_questao(self):
        id = input("Código da Questao que deseja selecionar: ")
        return id
    
    def mostra_questao(self, dados_questao ):
        print("ID DA QUESTAO: ", dados_questao["id"])
        print("ENUNCIADO DA QUESTAO: ", dados_questao["enunciado"])
        print("ALTERNATIVAS DA QUESTAO: ", dados_questao["alternativas"])
        print("RESPOSTA CORRETA: ", dados_questao["resposta_correta"])
        print("\n")

    