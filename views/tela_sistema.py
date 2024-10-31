class TelaSistema:

    def menu_opcoes(self):
        print("\n-------- SISTEMA DE CURSOS EAD ---------")
        print("Escolha sua opcao:")
        print("1 - Alunos")
        print("2 - Atividades Avaliativas")
        print("3 - Questões")
        print("0 - Finalizar sistema")
        
        try:
            opcao = int(input("Escolha a opcao: "))
            return opcao
        except ValueError:
            print("Opção inválida! Por favor, insira um número.")
            return -1
