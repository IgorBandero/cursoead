import PySimpleGUI as sg

class TelaAtividadeAvaliativa:
    def __init__(self):
        self.__window = None

    def mostrar_menu_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("------ Atividades Avaliativas ------", font=("Helvetica", 25))],
            [sg.Radio("Cadastrar Atividade", "RD1", key="1")],
            [sg.Radio("Editar Atividade", "RD1", key="2")],
            [sg.Radio("Remover Atividade", "RD1", key="3")],
            [sg.Radio("Listar Atividades", "RD1", key="4")],
            [sg.Radio("Atribuir Nota ao Aluno", "RD1", key="5")],
            [sg.Radio("Gerar Relatório", "RD1", key="6")],
            [sg.Radio("Voltar", "RD1", key="0")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("Sistema de Atividades Avaliativas").Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, "Cancelar"):
                opcao = 0
            elif values.get("1"):
                opcao = 1
            elif values.get("2"):
                opcao = 2
            elif values.get("3"):
                opcao = 3
            elif values.get("4"):
                opcao = 4
            elif values.get("5"):
                opcao = 5
            elif values.get("6"):
                opcao = 6
            elif values.get("0"):
                opcao = 0
            else:
                self.mostra_mensagem("Opção inválida.")
                continue

            self.close()
            return opcao

    def pega_dados_atividade(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("--------- Dados da Atividade Avaliativa ---------", font=("Helvetica", 20),
                     pad=((0, 0), (0, 10)))],
            [sg.Text("Nota Máxima:", size=(20, 1)), sg.InputText("", key="nota_maxima")],
            [sg.Text("Quantidade de Questões:", size=(20, 1)), sg.InputText("", key="quantidade_questoes")],
            [sg.Button("Confirmar", size=(10, 1)), sg.Cancel("Cancelar", size=(10, 1))]
        ]
        self.__window = sg.Window("Cadastro de Atividade Avaliativa").Layout(layout)

        while True:
            button, values = self.__window.read()
            if button in (None, "Cancelar"):
                self.close()
                return None
            try:
                nota_maxima = float(values["nota_maxima"])
                quantidade_questoes = int(values["quantidade_questoes"])
                if nota_maxima <= 0 or quantidade_questoes <= 0:
                    raise ValueError("Os valores devem ser positivos.")
                self.close()
                return {"nota_maxima": nota_maxima, "quantidade_questoes": quantidade_questoes}
            except ValueError as e:
                self.mostra_mensagem(f"Erro nos dados fornecidos: {e}")

    def listar_atividades(self, lista_dados_atividades):
        lista_exibicao = [
            f"ID: {a['id']} | Nota Máxima: {a['nota_maxima']}" for a in lista_dados_atividades
        ]
        layout = [
            [sg.Text("Atividades Cadastradas", font=("Helvetica", 20))],
            [sg.Listbox(values=lista_exibicao, size=(80, 15), key="atividades", font=("Helvetica", 12))],
            [sg.Button("Voltar")]
        ]
        self.__window = sg.Window("Lista de Atividades").Layout(layout)

        while True:
            button, _ = self.open()
            if button in (None, "Voltar"):
                self.close()
                break

    def seleciona_atividade(self, lista_atividades):
        lista_exibicao = [f"ID: {a['id']} | Nota Máxima: {a['nota_maxima']}" for a in lista_atividades]
        layout = [
            [sg.Text("Selecione uma Atividade", font=("Helvetica", 20))],
            [sg.Listbox(values=lista_exibicao, size=(80, 15), key="atividade_selecionada", font=("Helvetica", 12))],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("Selecionar Atividade").Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, "Cancelar"):
                self.close()
                return None
            if button == "Confirmar":
                try:
                    if not values["atividade_selecionada"]:
                        raise ValueError("Nenhuma atividade selecionada!")
                    id_atividade = int(values["atividade_selecionada"][0].split("ID: ")[1].split("|")[0].strip())
                    self.close()
                    return id_atividade
                except Exception as e:
                    self.mostra_mensagem(str(e))

    def editar_atividade(self, dados_atividade):
        """
        Permite editar uma atividade, incluindo a edição de suas questões.
        :param dados_atividade: Dicionário contendo os dados atuais da atividade.
        :return: Dicionário com os dados atualizados ou None se cancelado.
        """
        sg.ChangeLookAndFeel('DarkTeal4')
        questoes_formatadas = [
            f"ID: {q['id']} | Enunciado: {q['enunciado']}" for q in dados_atividade["questoes"]
        ]

        layout = [
            [sg.Text("Editar Atividade Avaliativa", font=("Helvetica", 20))],
            [sg.Text("Nota Máxima:", size=(20, 1)), sg.InputText(dados_atividade["nota_maxima"], key="nota_maxima")],
            [sg.Text("Questões Atuais:", font=("Helvetica", 14))],
            [sg.Listbox(values=questoes_formatadas, size=(60, 10), key="questoes",
                        select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)],
            [sg.Button("Salvar"), sg.Cancel("Cancelar")]
        ]

        self.__window = sg.Window("Editar Atividade").Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, "Cancelar"):
                self.close()
                return None
            if button == "Salvar":
                try:
                    nota_maxima = float(values["nota_maxima"])
                    self.close()
                    return {
                        "nota_maxima": nota_maxima,
                        "questoes": dados_atividade["questoes"]  # Retorna as mesmas questões
                    }
                except ValueError as e:
                    self.mostra_mensagem(f"Erro nos dados fornecidos: {e}")

    def excluir_atividade(self, dados_atividade):
        layout = [
            [sg.Text(f"Confirma a exclusão da atividade ID: {dados_atividade['id']}?", font=("Helvetica", 14))],
            [sg.Button("Sim"), sg.Button("Não")]
        ]
        self.__window = sg.Window("Excluir Atividade").Layout(layout)

        while True:
            button, _ = self.open()
            if button == "Sim":
                self.close()
                return True
            elif button in (None, "Não"):
                self.close()
                return False

    def selecionar_multiplos_itens(self, questoes_disponiveis):
        """
        Permite selecionar múltiplas questões de uma lista.
        :param questoes_disponiveis: Lista de dicionários com informações das questões.
        :return: Lista de IDs das questões selecionadas.
        """
        questoes_formatadas = [
            f"ID: {q['id']} | Enunciado: {q['enunciado']}" for q in questoes_disponiveis
        ]
        layout = [
            [sg.Text("Selecione as Questões", font=("Helvetica", 20))],
            [sg.Listbox(values=questoes_formatadas, size=(60, 15), key="questoes",
                        select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]

        self.__window = sg.Window("Selecionar Questões").Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, "Cancelar"):
                self.close()
                return []
            if button == "Confirmar":
                try:
                    if not values["questoes"]:
                        raise ValueError("Nenhuma questão selecionada!")
                    ids_selecionados = [
                        int(item.split("ID: ")[1].split(" |")[0]) for item in values["questoes"]
                    ]
                    self.close()
                    return ids_selecionados
                except Exception as e:
                    self.mostra_mensagem(str(e))

    def pega_dados_nota(self):
        """
        Coleta os dados necessários para adicionar uma nota a uma atividade.
        """
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Adicionar Nota para Aluno", font=("Helvetica", 20))],
            [sg.Text("ID da Atividade:", size=(20, 1)), sg.InputText("", key="atividade_id")],
            [sg.Text("CPF do Aluno:", size=(20, 1)), sg.InputText("", key="aluno_cpf")],
            [sg.Text("Nota:", size=(20, 1)), sg.InputText("", key="nota")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("Adicionar Nota").Layout(layout)

        while True:
            button, values = self.__window.read()
            if button in (None, "Cancelar"):
                self.close()
                return None
            if button == "Confirmar":
                try:
                    atividade_id = int(values["atividade_id"])
                    aluno_cpf = values["aluno_cpf"]
                    nota = float(values["nota"])
                    if nota < 0:
                        raise ValueError("A nota deve ser um número positivo.")
                    self.close()
                    return {"atividade_id": atividade_id, "aluno_cpf": aluno_cpf, "nota": nota}
                except ValueError as e:
                    self.mostra_mensagem(f"Erro nos dados fornecidos: {e}")

    def mostra_mensagem(self, mensagem: str):
        sg.Popup("Alerta!", mensagem)

    def open(self):
        button, values = self.__window.read()
        return button, values

    def close(self):
        self.__window.close()