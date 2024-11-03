class TelaMatricula():

    def mostrar_menu_opcoes(self):
        while(True):
            print("\n-------------------- MATRÍCULA ---------------------")
            print("Escolha a opção:")
            print("----------------------------------------------------")
            print("1 - Matricular aluno em módulos")
            print("2 - Lançar notas de aluno")
            print("3 - Finalizar curso de aluno")
            print("4 - Relatório de cursos mais populares")
            print("5 - Relatório de cursos melhor avaliados")
            print("6 - Relatório de tempo médio de conclusção de curso")
            print("0 - Voltar ")
            print("----------------------------------------------------")
            opcao = input("Escolha a opção: ")
            if (opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4" or opcao == "5" or opcao == "5" or opcao == "0"):
                return int(opcao)
            else:
                print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")

    def mostrar_mensagem(self, msg):
        print(msg)