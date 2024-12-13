import PySimpleGUI as sg
from exceptions.ModulosExceptions import EdicaoModuloException
from exceptions.OpcaoInvalidaException import OpcaoInvalidaException


class TelaModulo:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')  # Definir tema
        layout = [
            [sg.Text('--------------------- MÓDULOS ---------------------', font=("Helvetica", 25))],
            [sg.Text('Escolha a opção:', font=("Helvetica", 15))],
            [sg.Radio('Cadastrar Módulo', "RD1", key='1')],
            [sg.Radio('Editar Módulo', "RD1", key='2')],
            [sg.Radio('Excluir Módulo', "RD1", key='3')],
            [sg.Radio('Listar Módulos', "RD1", key='4')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Módulos', layout)

    def mostrar_menu_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values.get('1'):
            opcao = 1
        elif values.get('2'):
            opcao = 2
        elif values.get('3'):
            opcao = 3
        elif values.get('4'):
            opcao = 4
        elif values.get('0') or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def pega_dados_modulo(self):
        layout = [
            [sg.Text("Código do Módulo: "), sg.InputText(key="codigo")],
            [sg.Text("Nome do Módulo: "), sg.InputText(key="nome")],
            [sg.Text("Área do Módulo: "), sg.InputText(key="area")],
            [sg.Text("Carga Horária: "), sg.InputText(key="carga_horaria")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("Cadastro de Módulo", layout)

        event, values = self.__window.Read()
        if event in (None, "Cancelar"):
            self.close()
            return None

        try:
            carga_horaria = int(values["carga_horaria"])
            if carga_horaria <= 0:
                raise ValueError("Carga horária deve ser maior que zero.")
            modulo = {
                "codigo": values["codigo"],
                "nome": values["nome"],
                "area": values["area"],
                "carga_horaria": carga_horaria
            }
            self.close()
            return modulo
        except ValueError:
            sg.Popup("Erro: Carga horária inválida. Deve ser um número maior que zero.")
            self.close()
            return None

    def editar_modulo(self, modulo):
        layout = [
            [sg.Text("Editar Módulo", font=("Helvetica", 20))],
            [sg.Text("Código:", size=(20, 1)), sg.Input(default_text=modulo["codigo"], key="codigo")],
            [sg.Text("Nome:", size=(20, 1)), sg.Input(default_text=modulo["nome"], key="nome")],
            [sg.Text("Área:", size=(20, 1)), sg.Input(default_text=modulo["area"], key="area")],
            [sg.Text("Carga Horária:", size=(20, 1)), sg.Input(default_text=modulo["carga_horaria"], key="carga_horaria")],
            [sg.Button("Salvar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("Editar Módulo", layout)

        event, values = self.__window.Read()
        if event in (None, "Cancelar"):
            self.close()
            return None

        try:
            carga_horaria = int(values["carga_horaria"])
            if carga_horaria <= 0:
                raise ValueError("Carga horária deve ser maior que zero.")
            modulo_atualizado = {
                "codigo": values["codigo"],
                "nome": values["nome"],
                "area": values["area"],
                "carga_horaria": carga_horaria
            }
            self.close()
            return modulo_atualizado
        except ValueError:
            sg.Popup("Erro: Carga horária inválida. Deve ser um número maior que zero.")
            self.close()
            return None

    def listar_modulos(self, modulos):
        if not modulos:
            sg.Popup("Nenhum módulo cadastrado.")
            return
        modulo_list = [f"{modulo['codigo']} - {modulo['nome']} ({modulo['area']}, {modulo['carga_horaria']}h)" for modulo in modulos]
        layout = [[sg.Listbox(values=modulo_list, size=(50, len(modulo_list)), key="lista_modulos")], [sg.Button("Voltar")]]
        self.__window = sg.Window("Lista de Módulos", layout)
        self.__window.Read()
        self.close()

    def selecionar_modulo(self, modulos):
        if not modulos:
            sg.Popup("Nenhum módulo disponível.")
            return None

        modulo_list = [f"{modulo['codigo']} - {modulo['nome']}" for modulo in modulos]
        layout = [
            [sg.Text("Selecione um módulo:")],
            [sg.Listbox(values=modulo_list, size=(50, 10), key="modulo_selecionado")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("Selecionar Módulo", layout)
        event, values = self.__window.Read()

        if event in (None, "Cancelar") or not values["modulo_selecionado"]:
            self.close()
            return None

        modulo_selecionado = values["modulo_selecionado"][0].split(" - ")[0]
        self.close()
        return modulo_selecionado

    def close(self):
        if self.__window:
            self.__window.close()

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)
