import PySimpleGUI as sg


class TelaOrientacao:
    def __init__(self):
        self.__window = None

    def mostrar_menu_opcoes(self):
        layout = [
            [sg.Text("-------- MENU ORIENTAÇÃO --------", font=("Helvetica", 20))],
            [sg.Radio("Cadastrar Orientação", "RD1", key="1")],
            [sg.Radio("Listar Orientações", "RD1", key="2")],
            [sg.Radio("Editar Orientação", "RD1", key="3")],
            [sg.Radio("Excluir Orientação", "RD1", key="4")],
            [sg.Radio("Listar Orientandos de um Professor", "RD1", key="5")],
            [sg.Radio("Voltar", "RD1", key="0")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]
        self.__window = sg.Window("Menu Orientação", layout)

        button, values = self.__window.read()
        opcao = 0
        if button in (None, "Cancelar"):
            opcao = 0
        else:
            for key in values:
                if values[key]:
                    opcao = int(key)
                    break
        self.close()
        return opcao

    def pega_dados_orientacao(self):
        layout = [
            [sg.Text("Digite os dados da Orientação", font=("Helvetica", 20))],
            [sg.Text("CPF do Aluno:", size=(20, 1)), sg.InputText(key="cpf_aluno")],
            [sg.Text("CPF do Professor:", size=(20, 1)), sg.InputText(key="cpf_professor")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]
        self.__window = sg.Window("Cadastrar Orientação", layout)

        button, values = self.__window.read()
        if button in (None, "Cancelar"):
            self.close()
            return None
        self.close()
        return {"cpf_aluno": values["cpf_aluno"], "cpf_professor": values["cpf_professor"]}

    def mostrar_orientacao(self, orientacao):
        sg.Popup(
            f"Aluno: {orientacao['nome_aluno']} (CPF: {orientacao['cpf_aluno']})\n"
            f"Professor: {orientacao['nome_professor']} (CPF: {orientacao['cpf_professor']})"
        )

    def listar_orientacoes(self, orientacoes):
        if not orientacoes:
            sg.Popup("Nenhuma orientação cadastrada.")
        else:
            orientacoes_list = [
                f"Aluno: {o['nome_aluno']} (CPF: {o['cpf_aluno']}) | "
                f"Professor: {o['nome_professor']} (CPF: {o['cpf_professor']})"
                for o in orientacoes
            ]
            layout = [
                [sg.Text("Orientações Cadastradas", font=("Helvetica", 20))],
                [sg.Listbox(values=orientacoes_list, size=(60, 15), key="orientacoes")],
                [sg.Button("Voltar")],
            ]
            self.__window = sg.Window("Lista de Orientações", layout)
            self.__window.read()
            self.close()

    def selecionar_orientacao(self, mensagem="Digite o CPF do aluno:"):
        layout = [
            [sg.Text(mensagem, font=("Helvetica", 15))],
            [sg.InputText(key="cpf_aluno")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]
        self.__window = sg.Window("Selecionar Orientação", layout)

        button, values = self.__window.read()
        if button in (None, "Cancelar"):
            self.close()
            return None
        self.close()
        return values["cpf_aluno"]

    def mostrar_mensagem(self, mensagem):
        sg.Popup(mensagem)

    def selecionar_aluno(self, lista_alunos):
        """Permite selecionar um aluno de uma lista."""
        alunos_formatados = [f"CPF: {aluno['cpf']} | Nome: {aluno['nome']}" for aluno in lista_alunos]
        layout = [
            [sg.Text("Selecione um Aluno", font=("Helvetica", 20))],
            [sg.Listbox(values=alunos_formatados, size=(50, 10), key="aluno_selecionado")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Selecionar Aluno", layout)

        while True:
            event, values = self.__window.read()
            if event in (None, "Cancelar"):
                self.close()
                return None
            if event == "Confirmar":
                try:
                    aluno_selecionado = values["aluno_selecionado"][0]
                    cpf_aluno = aluno_selecionado.split("CPF: ")[1].split(" |")[0].strip()
                    self.close()
                    return cpf_aluno
                except IndexError:
                    sg.popup("Selecione um aluno!")
        self.close()

    def selecionar_professor(self, lista_professores):
        """Permite selecionar um professor de uma lista."""
        professores_formatados = [f"CPF: {professor['cpf']} | Nome: {professor['nome']}" for professor in
                                  lista_professores]
        layout = [
            [sg.Text("Selecione um Professor", font=("Helvetica", 20))],
            [sg.Listbox(values=professores_formatados, size=(50, 10), key="professor_selecionado")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Selecionar Professor", layout)

        while True:
            event, values = self.__window.read()
            if event in (None, "Cancelar"):
                self.close()
                return None
            if event == "Confirmar":
                try:
                    professor_selecionado = values["professor_selecionado"][0]
                    cpf_professor = professor_selecionado.split("CPF: ")[1].split(" |")[0].strip()
                    self.close()
                    return cpf_professor
                except IndexError:
                    sg.popup("Selecione um professor!")
        self.close()

    def close(self):
        if self.__window:
            self.__window.close()