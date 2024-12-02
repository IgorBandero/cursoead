import PySimpleGUI as sg

class TelaQuestao:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')  # Definir tema
        layout = [
            [sg.Text('-------- QUESTOES ----------', font=("Helvetica", 25))],
            [sg.Text('Escolha a opção:', font=("Helvetica", 15))],
            [sg.Radio('Adicionar Questão', "RD1", key='1')],
            [sg.Radio('Excluir Questão', "RD1", key='2')],
            [sg.Radio('Listar Questões', "RD1", key='3')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Questões', layout)

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
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()  # Fechando a janela após a escolha
        return opcao

    def pega_dados_questao(self):
        layout = [
            [sg.Text("ID da Questão: "), sg.InputText(key="id")],
            [sg.Text("Enunciado: "), sg.InputText(key="enunciado")],
            [sg.Text("Alternativas (separadas por vírgula): "), sg.InputText(key="alternativas")],
            [sg.Text("Resposta Correta: "), sg.InputText(key="resposta_correta")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("Cadastro de Questão", layout)

        event, values = self.__window.Read()

        if event in (None, "Cancelar"):
            self.close()
            return None

        if event == "Confirmar":
            try:
                alternativas = values["alternativas"].split(", ")
                if len(alternativas) < 2:
                    sg.Popup("É necessário fornecer pelo menos duas alternativas.")
                    return None
                if values["resposta_correta"] not in alternativas:
                    sg.Popup("A resposta correta deve corresponder a uma das alternativas fornecidas.")
                    return None

                return {
                    "id": int(values["id"]),
                    "enunciado": values["enunciado"],
                    "alternativas": alternativas,
                    "respostas_corretas": [values["resposta_correta"]]
                }
            except ValueError:
                sg.Popup("ID inválido! Insira um número inteiro para o ID.")
                return None
        self.close()
        return None

    def listar_questoes(self, questoes):
        if not questoes:
            sg.Popup("Nenhuma questão cadastrada.")
        else:
            questao_list = [
                f"{indice + 1} - ID: {questao['id']}, Enunciado: {questao['enunciado']}, Alternativas: {', '.join(questao['alternativas'])}, Resposta Correta: {', '.join(questao['respostas_corretas'])}"
                for indice, questao in enumerate(questoes)
            ]
            layout = [[sg.Text("\n".join(questao_list))], [sg.Button("Voltar")]]
            self.__window = sg.Window("Lista de Questões", layout)
            self.__window.Read()
            self.close()

    def seleciona_questao(self):
        layout = [[sg.Text("Informe o código da questão: "), sg.InputText(key="codigo")],
                  [sg.Button("Confirmar"), sg.Cancel("Cancelar")]]
        self.__window = sg.Window("Seleção de Questão", layout)
        event, values = self.__window.Read()

        if event == "Confirmar":
            try:
                return int(values["codigo"])
            except ValueError:
                sg.Popup("Código inválido! Insira um número inteiro.")
        self.close()
        return None

    def mostrar_questao(self, dados_questao):
        sg.Popup(f"ID: {dados_questao['id']} | Enunciado: {dados_questao['enunciado']} | Alternativas: {', '.join(dados_questao['alternativas'])} | Resposta Correta: {', '.join(dados_questao['respostas_corretas'])}")

    def mostra_mensagem(self, msg):
        sg.Popup(msg)

    def close(self):
        if self.__window:
            self.__window.close()








