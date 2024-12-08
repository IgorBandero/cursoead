from exceptions.CursoExceptions import ListaCursosVaziaException, EdicaoCursoException
from exceptions.OpcaoInvalidaException import OpcaoInvalidaException
import re
import PySimpleGUI as sg
class TelaCurso():

    def __init__(self):
        self.__window = None
        self.mostrar_menu_opcoes()

    def mostrar_menu_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("---------------------- Cursos ----------------------", font=("Helvica", 25), pad=((0, 0), (10, 15)))],
            [sg.Text("Escolha sua opção: ", font=("Helvica", 14), pad=((0, 0), (0, 10)))],
            [sg.Radio("Cadastrar Curso", "RD1", key="1")],
            [sg.Radio("Editar Curso", "RD1", key="2")],
            [sg.Radio("Excluir Curso", "RD1", key="3")],
            [sg.Radio("Listar Cursos Disponíveis", "RD1", key="4")],
            [sg.Radio("Mostrar Curso", "RD1", key="5")],
            [sg.Radio("Relatório de cursos melhor avaliados", "RD1", key="6")],
            [sg.Radio("Voltar", "RD1", key="0")],
            [sg.Button("Confirmar", pad=((15, 0), (20, 20))), sg.Cancel("Cancelar", pad=((15, 0), (20, 20)))]
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
                elif values['4']:
                    opcao = 4
                elif values["5"]:
                    opcao = 5
                elif values["6"]:
                    opcao = 6
                elif values["0"] or button in (None, "Cancelar"):
                    opcao = 0
                else:
                    raise OpcaoInvalidaException
                self.close()
                return opcao
            except OpcaoInvalidaException as e:
                self.mostrar_mensagem(str(e))
                self.close()

    def cadastrar_curso(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("------------------ Dados do Curso -------------------", font=("Helvica", 25), pad=((0, 0), (0, 10)))],
            [sg.Text("Nome: "), sg.InputText("", key="nome", size=(50, 1))],
            [sg.Text("Descrição: "), sg.InputText("", key="descricao", size=(50, 1))],
            [sg.Text("Carga Horária: "), sg.InputText("", key="carga_horaria", size=(50, 1))],
            [sg.Text("Mínimo de semestres: "), sg.InputText("", key="min_semestres", size=(50, 1))],
            [sg.Text("Máximo de semestres: "), sg.InputText("", key="max_semestres", size=(50, 1))],
            [sg.Text("Mensalidade: "), sg.InputText("", key="mensalidade", size=(50, 1))],
            [sg.Button("Confirmar", pad=((5, 0), (20, 20))), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("Sistema de livros").Layout(layout)

        while(True):
            try:
                button, values = self.open()
                if button == None or button == "Cancelar":
                    self.close()
                    return None
                elif button == "Confirmar":
                    nome = values["nome"]
                    if not self.nome_valido(nome):
                        raise ValueError("Nome do curso inválido! \nNome deve ser um texto com mais de 5 caracteres")
                    descricao = values["descricao"]
                    if not self.descricao_valida(descricao):
                        raise ValueError("Descrição do curso inválida! \nDescrição deve ser um texto com mais de 10 caracteres")
                    carga_horaria = values["carga_horaria"]
                    if not self.carga_semestres_valido(carga_horaria):
                        raise ValueError("Carga horária do curso inválida! \nCarga horária deve ser um número maior que zero")
                    min_semestres = values["min_semestres"]
                    if not self.carga_semestres_valido(min_semestres):
                        raise ValueError("Mínimo de semestres inválido! \nMínimo de semestres deve ser um número maior que zero")
                    max_semestres = values["max_semestres"]
                    if not self.carga_semestres_valido(max_semestres):
                        raise ValueError("Máximo de semestres inválido! \nMáximo de semestres deve ser um número maior que zero")
                    mensalidade = values["mensalidade"]
                    if not self.mensalidade_valida(mensalidade):
                        raise ValueError("Mensalidade inválida! \nMensalidade deve ser um número não negativo")
                    self.close()
                    return {"nome": nome, "descricao": descricao, "carga_horaria": int(carga_horaria),
                            "min_semestres": int(min_semestres), "max_semestres": int(max_semestres), "mensalidade": float(mensalidade)}
            except Exception as e:
                self.mostrar_mensagem(str(e))

    def editar_curso(self, curso):
        layout = [
            [sg.Text("Editar Curso:", font=("Helvetica", 14), pad=((0, 0), (0, 10)))],
            [sg.Text("Nome:", size=(17, 1)), sg.Input(default_text=curso["nome"], key="nome")],
            [sg.Text("Descrição:", size=(17, 1)), sg.Input(default_text=curso["descricao"], key="descricao")],
            [sg.Text("Carga Horária (h):", size=(17, 1)), sg.Input(default_text=str(curso["carga_horaria"]), key="carga_horaria")],
            [sg.Text("Mínimo de Semestres:", size=(17, 1)), sg.Input(default_text=str(curso["min_semestres"]), key="min_semestres")],
            [sg.Text("Máximo de Semestres:", size=(17, 1)), sg.Input(default_text=str(curso["max_semestres"]), key="max_semestres")],
            [sg.Text("Mensalidade (R$):", size=(17, 1)), sg.Input(default_text=f"{curso['mensalidade']:.2f}", key="mensalidade")],
            [sg.Button("Confirmar", size=(10, 1), pad=((5, 0), (20, 20))), sg.Button("Cancelar", size=(10, 1), pad=((15, 0), (20, 20)))]
        ]
        self.__window = sg.Window("Editar Curso").Layout(layout)

        while True:
            button, values = self.__window.read()
            if button == None or button == "Cancelar":
                self.close()
                return None
            elif button == "Confirmar":
                try:
                    curso_atualizado = {
                        "nome": values["nome"],
                        "descricao": values["descricao"],
                        "carga_horaria": int(values["carga_horaria"]),
                        "min_semestres": int(values["min_semestres"]),
                        "max_semestres": int(values["max_semestres"]),
                        "mensalidade": float(values["mensalidade"])
                    }
                    if curso_atualizado:
                        self.close()
                        return curso_atualizado
                    else:
                        self.close()
                        raise EdicaoCursoException
                except Exception as e:
                    self.mostrar_mensagem(str(e))

    def selecionar_curso_na_lista(self, lista_cursos):
        nomes_cursos = [curso["nome"] for curso in lista_cursos]
        layout = [
            [sg.Text("Selecione um curso para editar:", font=("Helvetica", 14))],
            [sg.Listbox(nomes_cursos, size=(70, 10), key="nome_curso_selecionado", enable_events=True)],
            [sg.Button("Confirmar", size=(10, 1), pad=((5, 0), (10, 10))), sg.Button("Cancelar", size=(10, 1), pad=((10, 0), (10, 10)))]
        ]
        self.__window = sg.Window('Selecionar Curso').Layout(layout)
        while(True):
            try:
                button, values = self.open()
                if button == None or button == "Cancelar":
                    self.close()
                    return None
                if button == "Confirmar":
                    curso_selecionado = values["nome_curso_selecionado"]
                    if curso_selecionado:
                        self.close()
                        return curso_selecionado[0]
                    else:
                        raise OpcaoInvalidaException
            except OpcaoInvalidaException as e:
                self.mostrar_mensagem(str(e))

    def excluir_curso(self, curso):
        layout = [
            [sg.Text(f"Confirma a exclusão do CURSO: {curso["nome"]}?", font=("Helvetica", 14))],
            [sg.Button("SIM", size=(10, 1), pad=((5, 0), (10, 10))), sg.Button("NÃO", size=(10, 1), pad=((10, 0), (10, 10)))]
        ]
        janela = sg.Window("Confirmar Exclusão", layout, modal=True)

        while True:
            button, values = janela.read()
            if button == sg.WINDOW_CLOSED:
                janela.close()
                return False
            elif button == "SIM":
                janela.close()
                return True
            elif button == "NÃO":
                janela.close()
                return False
    
    def selecionar_curso(self, num_opcoes):
        if (num_opcoes == 0):
            raise ListaCursosVaziaException
        while(True):
            opcao = input("\nComo deseja selecionar o curso? \n1 - Procurar curso pelo NOME \n2 - Selecionar da lista de cursos \n\nEscolha uma opção: ")
            if (opcao == "1" or opcao == "2"):
                break
            else:
                print("\n******** OPÇÃO INVÁLIDA, TENTE NOVAMENTE... ********")
        if (opcao == "1"):
            return "Buscar pelo nome"
        if (opcao == "2"):
            return "Selecionar da lista"

    def nome_valido(self, nome):
        return len(nome) >= 5 

    def descricao_valida(self, descricao):
        return len(descricao) >= 10

    def carga_semestres_valido(self, variavel):
        if variavel.isdigit():
            return len(variavel) >= 1 and int(variavel) > 0
        return False

    def mensalidade_valida(self, mensalidade):
        if bool(re.fullmatch(r"\d+([.,]\d+)?", mensalidade)):
            return float(mensalidade) >= 0
        return False

    def buscar_curso_pelo_nome(self):
        while(True):
            nome = input("\nInforme o nome do curso que deseja selecionar: ")
            if len(nome) >= 5:
                return nome
            else:
                print("\n******** NOME INVÁLIDO! TENTE NOVAMENTE... ********")

    def mostrar_curso(self, curso):
        print("\n----------------------------------------------------")
        print("NOME: ", curso["nome"])
        print("DESCRIÇÃO: ", curso["descricao"])
        print("CARGA HORÁRIA: ", curso["carga_horaria"])
        print("MÍNIMO DE SEMESTRES: ", curso["min_semestres"])
        print("MÁXIMO DE SEMESTRES: ", curso["max_semestres"])
        print("MENSALIDADE: ", curso["mensalidade"])

    def continuar(self, mensagem):
        while(True):
            print("\n----------------------------------------------------")
            print(mensagem)
            opcao = input("\nEscolha a opção: ")
            if (opcao == "1"):
                return True
            elif (opcao == "2"):
                return False
            else:
                print("\n******** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... ********")

    def mostrar_opcao_curso(self, curso):
        print(curso["indice"]+1, " - ", curso["nome"])

    def mostrar_mensagem(self, mensagem: str):
        sg.Popup("Alerta!", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def voltar(self):
        self.__controlador_sistema.abrir_tela()