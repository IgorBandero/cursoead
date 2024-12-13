import PySimpleGUI as sg

class TelaQuestao:
    def __init__(self):
        self.__window = None

    def open(self):
        return self.__window.read()

    def close(self):
        if self.__window:
            self.__window.close()

    def mostrar_menu_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("---------------------- QUESTÕES ----------------------", font=("Helvetica", 25), pad=((0, 0), (10, 15)))],
            [sg.Text("Escolha a opção:", font=("Helvetica", 14), pad=((5, 0), (0, 10)))],
            [sg.Radio("Adicionar Questão", "RD1", key="1")],
            [sg.Radio("Editar Questão", "RD1", key="2")],
            [sg.Radio("Excluir Questão", "RD1", key="3")],
            [sg.Radio("Listar Questões", "RD1", key="4")],
            [sg.Radio("Voltar", "RD1", key="0")],
            [sg.Button("Confirmar", size=(8, 1), pad=((10, 0), (20, 20))),
             sg.Cancel("Cancelar", size=(8, 1), pad=((15, 0), (20, 20)))]
        ]
        self.__window = sg.Window("Sistema de Questões").Layout(layout)

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
            elif values.get("0"):
                opcao = 0
            else:
                self.mostra_mensagem("Opção inválida.")
                continue  # Mostra mensagem e exibe novamente o menu

            self.close()
            return opcao



    def pega_dados_questao(self, dados_questao=None):
        """
        Exibe um formulário para cadastro ou edição de uma questão.
        :param dados_questao: Dicionário contendo os dados atuais da questão (se edição).
        :return: Dicionário com os dados atualizados ou None se a edição for cancelada.
        """
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Editar Questão" if dados_questao else "Cadastro de Questão", font=("Helvetica", 20))],
            [sg.Text("ID:", size=(15, 1)),
             sg.InputText(dados_questao["id"] if dados_questao else "", key="id", disabled=bool(dados_questao))],
            [sg.Text("Enunciado:", size=(15, 1)),
             sg.InputText(dados_questao["enunciado"] if dados_questao else "", key="enunciado")],
            [sg.Text("Alternativas (separadas por vírgula):", size=(15, 1)),
             sg.InputText(", ".join(dados_questao["alternativas"]) if dados_questao else "", key="alternativas")],
            [sg.Text("Resposta Correta:", size=(15, 1)),
             sg.InputText(", ".join(dados_questao["respostas_corretas"]) if dados_questao else "",
                          key="resposta_correta")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("Questão").Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, "Cancelar"):
                self.close()
                return None
            if button == "Confirmar":
                try:
                    alternativas = values["alternativas"].split(", ")
                    if len(alternativas) < 2:
                        raise ValueError("Forneça pelo menos duas alternativas.")
                    if values["resposta_correta"] not in alternativas:
                        raise ValueError("A resposta correta deve estar entre as alternativas.")
                    self.close()
                    return {
                        "id": int(values["id"]),
                        "enunciado": values["enunciado"],
                        "alternativas": alternativas,
                        "respostas_corretas": [values["resposta_correta"]]
                    }
                except ValueError as e:
                    self.mostra_mensagem(str(e))

    def listar_questoes(self, questoes):
        if not questoes:
            self.mostra_mensagem("Nenhuma questão cadastrada.")
            return
        questao_list = [
            f"ID: {questao['id']} | Enunciado: {questao['enunciado']} | Alternativas: {', '.join(questao['alternativas'])} | Resposta Correta: {', '.join(questao['respostas_corretas'])}"
            for questao in questoes
        ]
        layout = [
            [sg.Text("Lista de Questões", font=("Helvetica", 20))],
            [sg.Listbox(values=questao_list, size=(80, 15), key="lista")],
            [sg.Button("Voltar")]
        ]
        self.__window = sg.Window("Lista de Questões").Layout(layout)
        self.open()
        self.close()

    def excluir_questao(self, questao):
        """
        Exibe uma janela para confirmar a exclusão de uma questão.
        :param questao: Dicionário contendo os dados da questão a ser excluída.
        :return: True se a exclusão for confirmada, False caso contrário.
        """
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text(f"Confirma a exclusão da questão ID: {questao['id']}?", font=("Helvetica", 14))],
            [sg.Text(f"Enunciado: {questao['enunciado']}", font=("Helvetica", 12))],
            [sg.Button("Sim"), sg.Button("Não")]
        ]
        self.__window = sg.Window("Excluir Questão").Layout(layout)

        while True:
            button, _ = self.open()
            if button == "Sim":
                self.close()
                return True
            elif button in (None, "Não"):
                self.close()
                return False

    def seleciona_questao(self, questoes):
        """
        Permite ao usuário selecionar uma questão a partir de uma lista exibida.
        :param questoes: Lista de dicionários contendo as questões cadastradas (com ID e enunciado).
        :return: ID da questão selecionada ou None se cancelado.
        """
        if not questoes:
            self.mostra_mensagem("Nenhuma questão cadastrada.")
            return None

        sg.ChangeLookAndFeel('DarkTeal4')
        lista_exibicao = [
            f"ID: {questao['id']} | Enunciado: {questao['enunciado']}" for questao in questoes
        ]
        layout = [
            [sg.Text("Selecione uma Questão", font=("Helvetica", 20))],
            [sg.Listbox(values=lista_exibicao, size=(60, 15), key="questao_selecionada", enable_events=False)],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("Selecionar Questão").Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, "Cancelar"):
                self.close()
                return None
            if button == "Confirmar":
                try:
                    if not values["questao_selecionada"]:
                        raise ValueError("Nenhuma questão selecionada!")
                    questao_selecionada = values["questao_selecionada"][0]
                    id_questao = int(questao_selecionada.split("ID: ")[1].split(" |")[0])
                    self.close()
                    return id_questao
                except Exception as e:
                    self.mostra_mensagem(str(e))


    def mostra_mensagem(self, mensagem: str):
        sg.Popup("Alerta!", mensagem)

    def close(self):
        if self.__window:
            self.__window.Close()









