import PySimpleGUI as sg
from exceptions.OpcaoInvalidaException import OpcaoInvalidaException
class TelaSistema:

    def __init__(self):
        self.__window = None
        self.mostrar_menu_opcoes()

    def mostrar_menu_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("-------------- Sistema de Cursos EAD ---------------", font=("Helvica",25), pad=((0, 0), (10, 15)))],
            [sg.Text("Escolha sua opção:", font=("Helvica",15), pad=((0, 0), (0, 10)))],
            [sg.Radio("Alunos","RD1", key="1")],
            [sg.Radio("Atividades Avaliativas","RD1", key="2")],
            [sg.Radio("Questões","RD1", key="3")],
            [sg.Radio("Professores","RD1", key="4")],
            [sg.Radio("Orientações", "RD1", key="5")],
            [sg.Radio("Cursos", "RD1", key="6")],
            [sg.Radio("Módulos", "RD1", key="7")],
            [sg.Radio("Certificados", "RD1", key="8")],
            [sg.Radio("Finalizar Sistema", "RD1", key="0")],
            [sg.Button("Confirmar", pad=((15, 0), (20, 20))), sg.Cancel("Cancelar", pad=((15, 0), (20, 20)))],
        ]
        self.__window = sg.Window("Sistema de Cursos EAD").Layout(layout)

    def menu_opcoes(self):
        while(True):
            self.mostrar_menu_opcoes()
            button, values = self.__window.Read()
            opcao = 0
            try:
                if values["1"]:
                    opcao = 1
                elif values["2"]:
                    opcao = 2
                elif values["3"]:
                    opcao = 3
                elif values["4"]:
                    opcao = 4
                elif values["5"]:
                    opcao = 5
                elif values["6"]:
                    opcao = 6
                elif values["7"]:
                    opcao = 7
                elif values["8"]:
                    opcao = 8
                elif values["0"] or button in (None, "Cancelar"):
                    opcao = 0
                else:
                    raise OpcaoInvalidaException
                self.close()
                return opcao
            except OpcaoInvalidaException as e:
                self.mostra_mensagem(str(e))
                self.close()

    def mostra_mensagem(self, mensagem: str):
        sg.Popup("Alerta!", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()