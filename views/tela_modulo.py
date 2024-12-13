import PySimpleGUI as sg
from exceptions.ModulosExceptions import EdicaoModuloException
from exceptions.OpcaoInvalidaException import OpcaoInvalidaException

class TelaModulo:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--------------------- MÓDULOS ---------------------', font=("Helvica", 25))],
            [sg.Text('Escolha a opção:', font=("Helvica", 15))],
            [sg.Radio('Cadastrar Módulo', "RD1", key='1')],
            [sg.Radio('Editar Módulo', "RD1", key='2')],
            [sg.Radio('Excluir Módulo', "RD1", key='3')],
            [sg.Radio('Listar Módulos', "RD1", key='4')],
            [sg.Radio('Avaliar Módulos', "RD1", key='5')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Módulos', layout)

    def mostrar_menu_opcoes(self):
        self.init_components()
        button, values = self.__window.Read() 
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['5']:
            opcao = 5
        elif values['0'] or button in (None, 'Cancelar'):
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

        if event == "Confirmar":
            try:
                carga_horaria = int(values["carga_horaria"])
                if carga_horaria <= 0:
                    sg.Popup("Carga horária deve ser maior que zero.")
                    return None
                return {"codigo": values["codigo"], "nome": values["nome"], "area": values["area"], "carga_horaria": carga_horaria}
            except ValueError:
                sg.Popup("Carga horária deve ser um número válido.")
                return None
        self.close()
        return None

    def editar_modulo(self, modulo):
        layout = [
            [sg.Text("----------------- Editar Módulo -----------------", font=("Helvica", 20), pad=((0, 0), (0, 10)))],
            [sg.Text("Código:", size=(17, 1)), sg.Input(default_text=modulo["codigo"], key="codigo")],
            [sg.Text("Nome:", size=(17, 1)), sg.Input(default_text=modulo["nome"], key="nome")],
            [sg.Text("Área:", size=(17, 1)), sg.Input(default_text=modulo["area"], key="area")],
            [sg.Text("Carga Horária (h):", size=(17, 1)), sg.Input(default_text=str(modulo["carga_horaria"]), key="carga_horaria")],
            [sg.Button("Confirmar", size=(15, 1), pad=((5, 0), (20, 20))), sg.Button("Cancelar", size=(15, 1), pad=((15, 0), (20, 20)))]
        ]
        self.__window = sg.Window("Editar Módulo").Layout(layout)

        while True:
            button, values = self.open()
            if button == None or button == "Cancelar":
                self.close()
                return None
            elif button == "Confirmar":
                try:
                    if not self.codigo_valido(values["codigo"]):
                        raise ValueError("Código do módulo inválido! \nCódigo deve ser um texto com mais de 3 caracteres")
                    if not self.nome_valido(values["nome"]):
                        raise ValueError("Nome do módulo inválido! \nNome deve ser um texto com mais de 5 caracteres")
                    if not self.area_valida(values["area"]):
                        raise ValueError("Área do módulo inválida! \nÁrea deve ser um texto com mais de 5 caracteres")
                    if not self.carga_horaria_valida(values["carga_horaria"]):
                        raise ValueError("Carga horária do curso inválida! \nCarga horária deve ser um número maior que zero")
                    modulo_atualizado = {
                        "codigo": values["codigo"],
                        "nome": values["nome"],
                        "area": values["area"],
                        "carga_horaria": int(values["carga_horaria"])
                    }
                    if modulo_atualizado:
                        self.close()
                        return modulo_atualizado
                    else:
                        self.close()
                        raise EdicaoModuloException
                except Exception as e:
                    self.mostrar_mensagem(str(e))

    def codigo_valido(self, codigo):
        return len(codigo) > 3

    def nome_valido(self, nome):
        return len(nome) > 5

    def area_valida(self, area):
        return len(area) > 5

    def carga_horaria_valida(self, carga_horaria):
        if carga_horaria.isdigit():
            return int(carga_horaria) > 0
        return False

    def listar_modulos(self, modulos):
        if not modulos:
            sg.Popup("Nenhum módulo cadastrado.")
        else:
            modulo_list = [
                f"{indice + 1} - CÓDIGO: {modulo.codigo}, NOME: {modulo.nome}, ÁREA: {modulo.area}, CARGA HORÁRIA: {modulo.carga_horaria}"
                for indice, modulo in enumerate(modulos)
            ]
            layout = [[sg.Text("\n".join(modulo_list))], [sg.Button("Voltar")]]
            self.__window = sg.Window("Lista de Módulos", layout)
            self.__window.Read()
            self.close()

    def selecionar_modulo(self, modulos, mensagem):

        if num_opcoes == 0:
            sg.Popup("Nenhum módulo cadastrado.")
            return None

        layout = [
            [sg.Text("Como deseja selecionar o módulo?")],
            [sg.Button("Buscar pelo Código"), sg.Button("Selecionar da Lista")]
        ]
        self.__window = sg.Window("Seleção de Módulo", layout)
        event, values = self.__window.Read()

        if event == "Buscar pelo Código":
            return self.buscar_modulo_pelo_codigo()
        elif event == "Selecionar da Lista":
            return self.selecionar_modulo_na_lista(num_opcoes)
        self.close()

    def buscar_modulo_pelo_codigo(self):
        layout = [[sg.Text("Informe o código do módulo que deseja selecionar: "), sg.InputText(key="codigo")],
                [sg.Button("Confirmar"), sg.Cancel("Cancelar")]]
        self.__window = sg.Window("Buscar Módulo", layout)
        event, values = self.__window.Read()
        if event == "Confirmar" and len(values["codigo"]) >= 3:
            self.close()
            return values["codigo"]
        else:
            sg.Popup("Código inválido!")
            self.close()
            return None

    def selecionar_modulo_na_lista(self, lista_modulos, mensagem):
        modulos = [f"{modulo["codigo"]} - {modulo["nome"]}" for modulo in lista_modulos]
        layout = [
            [sg.Text(mensagem, font=("Helvetica", 14), pad=((0, 0), (10, 10)))],
            [sg.Listbox(modulos, size=(70, 10), key="modulo_selecionado", enable_events=True)],
            [sg.Button("Confirmar", size=(8, 1), pad=((5, 0), (15, 15))), sg.Button("Cancelar", size=(8, 1), pad=((15, 0), (15, 15)))]
        ]
        self.__window = sg.Window("Selecionar Módulo").Layout(layout)
        while(True):
            try:
                button, values = self.open()
                if button == None or button == "Cancelar":
                    self.close()
                    return None
                if button == "Confirmar":
                    modulo_selecionado = values["modulo_selecionado"]
                    codigo_modulo = modulo_selecionado[0].split(" - ")[0]
                    if modulo_selecionado:
                        self.close()
                        return codigo_modulo
                    else:
                        raise OpcaoInvalidaException
            except OpcaoInvalidaException as e:
                self.mostrar_mensagem(str(e))

    def continuar_registro_modulos(self):
        layout = [
            [sg.Text("Deseja adicionar outro módulo?")],
            [sg.Button("SIM"), sg.Button("NÃO (Finalizar)")]
        ]
        self.__window = sg.Window("Adicionar Novo Módulo", layout)
        event, values = self.__window.Read()

        if event == "SIM":
            self.close()
            return True
        elif event == "NÃO (Finalizar)":
            self.close()
            return False
        else:
            self.close()
            return False

    def close(self):
        if self.__window:
            self.__window.close()

    def mostrar_modulo(self, modulo):
        sg.Popup(f"CÓDIGO: {modulo.codigo} | NOME: {modulo.nome} | ÁREA: {modulo.area} | CARGA HORÁRIA: {modulo.carga_horaria}")

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)

    def close(self):
        if self.__window:
            self.__window.close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
