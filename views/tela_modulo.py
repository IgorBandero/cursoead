import PySimpleGUI as sg

class TelaModulo:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')  # Definir tema
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
        button, values = self.__window.Read()  # Correção aqui: chamada de Read() no lugar certo
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
        self.close()  # Aqui chamando o close de forma correta.
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

    def selecionar_modulo(self, num_opcoes):
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

    def selecionar_modulo_na_lista(self, num_opcoes):
        layout = [[sg.Text("Selecione o número do módulo:")]]
        layout += [[sg.Button(f"Opção {i+1}") for i in range(num_opcoes)]]
        self.__window = sg.Window("Seleção de Módulo", layout)
        event, values = self.__window.Read()

        if event and event.startswith("Opção"):
            return int(event.split()[1]) - 1
        self.close()
        return None

    def mostrar_modulo(self, modulo):
        sg.Popup(f"CÓDIGO: {modulo.codigo} | NOME: {modulo.nome} | ÁREA: {modulo.area} | CARGA HORÁRIA: {modulo.carga_horaria}")

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)

    def close(self):
        if self.__window:
            self.__window.close()

