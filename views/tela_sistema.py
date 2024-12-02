import PySimpleGUI as sg
class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def menu_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['8']:
            opcao = 8
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    """def menu_opcoes(self):
        print("\n-------------- SISTEMA DE CURSOS EAD ---------------")
        print("Escolha uma opção:")
        print("----------------------------------------------------")
        print("1 - Alunos")
        print("2 - Atividades Avaliativas")
        print("3 - Questões")
        print("4 - Professores")
        print("5 - Orientações")
        print("6 - Cursos")
        print("7 - Módulos")  # Nova opção para módulos
        print("8 - Certificados")
        print("0 - Finalizar sistema")
        print("----------------------------------------------------")

        try:
            opcao = int(input("Escolha a opção: "))
            return opcao
        except ValueError:
            print("Opção inválida! Por favor, insira um número.")
            return -1 """

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)

    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------------- SISTEMA DE CURSOS EAD ---------------', font=("Helvica",25))],
            [sg.Text('Escolha sua opção:', font=("Helvica",15))],
            [sg.Radio('Alunos',"RD1", key='1')],
            [sg.Radio('Atividades Avaliativas',"RD1", key='2')],
            [sg.Radio('Questões',"RD1", key='3')],
            [sg.Radio('Professores',"RD1", key='4')],
            [sg.Radio('Orientações', "RD1", key='5')],
            [sg.Radio('Cursos', "RD1", key='6')],
            [sg.Radio('Modulo', "RD1", key='7')],
            [sg.Radio('Certificados', "RD1", key='8')],
            [sg.Radio('Finalizar sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Cursos EAD').Layout(layout)