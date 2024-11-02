class TelaSistema:
    def menu_opcoes(self):
        print("\n-------- SISTEMA DE CURSOS EAD ---------")
        print("Escolha uma opção:")
        print("1 - Alunos")
        print("2 - Atividades Avaliativas")
        print("3 - Questões")
        print("4 - Professores")
        print("5 - Orientações")
        print("6 - Cursos")
        print("7 - Módulos")  # Nova opção para módulos
        print("0 - Finalizar sistema")
        
        try:
            opcao = int(input("Escolha a opção: "))
            return opcao
        except ValueError:
            print("Opção inválida! Por favor, insira um número.")
            return -1

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)

