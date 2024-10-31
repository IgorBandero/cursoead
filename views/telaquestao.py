class TelaQuestao:
    def mostrar_menu_opcoes(self):
        print("-------- QUESTOES ----------")
        print("Escolha a opção")
        print("1. Adicionar Questao")
        print("2. Excluir Questao")
        print("3. Listar Questões")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")
        return int(opcao)

    def pega_dados_questao(self):
        print("-------- DADOS QUESTAO ----------")
        id = int(input("Id: "))
        enunciado = input("Enunciado: ")
        alternativas = input("Alternativas (separadas por vírgula): ").split(", ")
        resposta_correta = [input("Resposta Correta (exatamente como aparece nas alternativas): ")]
        return {
            "id": id,
            "enunciado": enunciado,
            "alternativas": alternativas,
            "resposta_correta": resposta_correta
        }

    def mostra_mensagem(self, msg):
        print(msg)

    def seleciona_questao(self):
        id = int(input("Código da Questao que deseja selecionar: "))  # Converte o ID para inteiro
        return id

    
    def mostra_questao(self, dados_questao):
        print("-------- QUESTAO ----------")
        print("ID DA QUESTAO: ", dados_questao["id"])
        print("ENUNCIADO DA QUESTAO: ", dados_questao["enunciado"])
        print("ALTERNATIVAS DA QUESTAO: ", ", ".join(dados_questao["alternativas"]))
        print("RESPOSTA CORRETA: ", ", ".join(dados_questao["resposta_correta"]))
        print("\n")



    