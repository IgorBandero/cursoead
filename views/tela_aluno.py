from datetime import datetime
from exceptions.OpcaoInvalidaException import OpcaoInvalidaException
from exceptions.CpfInvalidoException import CpfInvalidoException
from exceptions.AlunoExceptions import EdicaoAlunoException
import re
import PySimpleGUI as sg


class TelaAluno():

    def __init__(self):
        self.__window = None
        self.mostrar_menu_opcoes()

    def mostrar_menu_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("----------------------- Alunos -----------------------", font=("Helvica", 25),
            pad=((0, 0), (10, 15)))],
            [sg.Text("Escolha sua opção: ", font=("Helvica", 14), pad=((5, 0), (0, 10)))],
            [sg.Radio("Cadastrar Aluno", "RD1", key="1")],
            [sg.Radio("Editar Aluno", "RD1", key="2")],
            [sg.Radio("Excluir Aluno", "RD1", key="3")],
            [sg.Radio("Listar Alunos", "RD1", key="4")],
            [sg.Radio("Mostrar Aluno", "RD1", key="5")],
            [sg.Radio("Matricular aluno em módulos", "RD1", key="6")],
            [sg.Radio("Lançar notas de aluno", "RD1", key="7")],
            [sg.Radio("Finalizar curso de aluno", "RD1", key="8")],
            [sg.Radio("Relatório de cursos mais populares", "RD1", key="9")],
            [sg.Radio("Relatório de tempo médio de conclusão", "RD1", key="10")],
            [sg.Radio("Voltar", "RD1", key="0")],
            [sg.Button("Confirmar", size=(8, 1), pad=((10, 0), (20, 20))),
            sg.Cancel("Cancelar", size=(8, 1), pad=((15, 0), (20, 20)))]
        ]
        self.__window = sg.Window("Sistema de Alunos").Layout(layout)

    def menu_opcoes(self):
        while (True):
            self.mostrar_menu_opcoes()
            button, values = self.open()
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
                elif values["7"]:
                    opcao = 7
                elif values["8"]:
                    opcao = 8
                elif values["9"]:
                    opcao = 9
                elif values["10"]:
                    opcao = 10
                elif values["0"] or button in (None, "Cancelar"):
                    opcao = 0
                else:
                    raise OpcaoInvalidaException
                self.close()
                return opcao
            except OpcaoInvalidaException as e:
                self.mostrar_mensagem(str(e))
                self.close()

    def cadastrar_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("---------------- Dados do Aluno ----------------", font=("Helvica", 20), pad=((0, 0), (0, 10)))],
            [sg.Text("Nome: ", size=(20, 1)), sg.InputText("", key="nome", size=(45, 1))],
            [sg.Text("CPF: ", size=(20, 1)), sg.InputText("", key="cpf", size=(45, 1))],
            [sg.Text("Telefone: ", size=(20, 1)), sg.InputText("", key="telefone", size=(45, 1))],
            [sg.Text("E-mail: ", size=(20, 1)), sg.InputText("", key="email", size=(45, 1))],
            [sg.Text("Usuário: ", size=(20, 1)), sg.InputText("", key="usuario", size=(45, 1))],
            [sg.Text("Senha: ", size=(20, 1)), sg.InputText("", key="senha", size=(45, 1))],
            [sg.Text("Rua: ", size=(20, 1)), sg.InputText("", key="rua", size=(45, 1))],
            [sg.Text("Número de Residência: ", size=(20, 1)), sg.InputText("", key="num_residencia", size=(45, 1))],
            [sg.Text("Bairro: ", size=(20, 1)), sg.InputText("", key="bairro", size=(45, 1))],
            [sg.Text("Cidade: ", size=(20, 1)), sg.InputText("", key="cidade", size=(45, 1))],
            [sg.Text("CEP: ", size=(20, 1)), sg.InputText("", key="cep", size=(45, 1))],
            [sg.Text("Data Início (DD/MM/AAAA): ", size=(20, 1)), sg.InputText("", key="data_inicio", size=(45, 1))],
            [sg.Button("Confirmar", size=(8, 1), pad=((5, 0), (20, 20))), sg.Cancel("Cancelar", size=(8, 1), pad=((15, 0), (20, 20)))]
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
                        raise ValueError("Nome inválido! \nNome deve ser um texto com mais de 2 caracteres\n")
                    cpf = values["cpf"]
                    if not self.cpf_valido(cpf):
                        raise ValueError("CPF inválido! \nCPF deve ser um número com 11 dígitos\n")
                    telefone = values["telefone"]
                    if not self.telefone_valido(telefone):
                        raise ValueError("Telefone inválido! \nTelefone deve ser um número com 8 ou mais dígitos\n")
                    email = values["email"]
                    if not self.email_valido(email):
                        raise ValueError("E-mail inválido! \nTente novamente...\n")
                    usuario = values["usuario"]
                    if not self.usuario_valido(usuario):
                        raise ValueError("Usuário inválido! \nUsuário deve ter pelo menos 8 caracteres\n")
                    senha = values["senha"]
                    if not self.senha_valida(senha):
                        raise ValueError("Senha inválida! \nSenha deve ter pelo menos 8 caracteres\n")
                    rua = values["rua"]
                    if not self.rua_valida(rua):
                        raise ValueError("Rua inválida! \nRua deve ter mais de 5 caracteres\n")
                    num_residencia = values["num_residencia"]
                    if not self.num_residencia_valido(num_residencia):
                        raise ValueError("Número de residência inválido! \nNúmero deve ter pelo menos 1 dígito\n")
                    bairro = values["bairro"]
                    if not self.bairro_valido(bairro):
                        raise ValueError("Bairro inválido! \nBairro deve ter mais de 5 caracteres\n")
                    cidade = values["cidade"]
                    if not self.cidade_valida(cidade):
                        raise ValueError("Cidade inválida! \nCidade deve ter mais de 5 caracteres\n")
                    cep = values["cep"]
                    if not self.cep_valido(cep):
                        raise ValueError("CEP inválido! \nCEP deve ser um número com 8 dígitos\n")
                    data_inicio = values["data_inicio"]
                    data = self.data_valida(data_inicio)
                    if data is None:
                        raise ValueError("Formato da data de início inválida! Use DD/MM/AAAA...\n")
                    else:
                        data_inicio = data
                    self.close()
                    return {
                        "nome": nome, "cpf": int(cpf), "telefone": telefone, "email": email, "usuario": usuario,
                        "senha": senha, "rua": rua, "num_residencia": int(num_residencia), "bairro": bairro,
                        "cidade": cidade, "cep": cep, "data_inicio": data_inicio
                    }
            except Exception as e:
                self.mostrar_mensagem(str(e))

    def editar_aluno(self, aluno):
        layout = [
            [sg.Text("-------------------- Editar Aluno --------------------", font=("Helvica", 20),
            pad=((0, 0), (0, 10)))],
            [sg.Text("Nome: ", size=(20, 1)), sg.InputText(default_text=aluno["nome"], key="nome", size=(50, 1))],
            [sg.Text("CPF: ", size=(20, 1)), sg.InputText(default_text=aluno["cpf"], key="cpf", size=(50, 1))],
            [sg.Text("Telefone: ", size=(20, 1)),
            sg.InputText(default_text=aluno["telefone"], key="telefone", size=(50, 1))],
            [sg.Text("E-mail: ", size=(20, 1)), sg.InputText(default_text=aluno["email"], key="email", size=(50, 1))],
            [sg.Text("Usuário: ", size=(20, 1)),
            sg.InputText(default_text=aluno["usuario"], key="usuario", size=(50, 1))],
            [sg.Text("Senha: ", size=(20, 1)), sg.InputText(default_text=aluno["senha"], key="senha", size=(50, 1))],
            [sg.Text("Rua: ", size=(20, 1)), sg.InputText(default_text=aluno["rua"], key="rua", size=(50, 1))],
            [sg.Text("Número de Residência: ", size=(20, 1)),
            sg.InputText(default_text=aluno["num_residencia"], key="num_residencia", size=(50, 1))],
            [sg.Text("Bairro: ", size=(20, 1)), sg.InputText(default_text=aluno["bairro"], key="bairro", size=(50, 1))],
            [sg.Text("Cidade: ", size=(20, 1)), sg.InputText(default_text=aluno["cidade"], key="cidade", size=(50, 1))],
            [sg.Text("CEP: ", size=(20, 1)), sg.InputText(default_text=aluno["cep"], key="cep", size=(50, 1))],
            [sg.Text("Data Início (DD/MM/AAAA): ", size=(20, 1)),
            sg.InputText(default_text=aluno["data_inicio"].strftime("%d/%m/%Y"), key="data_inicio", size=(50, 1))],
            [sg.Button("Confirmar", size=(8, 1), pad=((5, 0), (20, 20))),
            sg.Cancel("Cancelar", size=(8, 1), pad=((15, 0), (20, 20)))]
        ]
        self.__window = sg.Window("Editar Aluno").Layout(layout)

        while True:
            button, values = self.open()
            if button == None or button == "Cancelar":
                self.close()
                return None
            elif button == "Confirmar":
                try:
                    if not self.nome_valido(values["nome"]):
                        raise ValueError("Nome inválido! \nNome deve ser um texto com mais de 2 caracteres\n")
                    if not self.cpf_valido(values["cpf"]):
                        raise ValueError("CPF inválido! \nCPF deve ser um número com 11 dígitos\n")
                    if not self.telefone_valido(values["telefone"]):
                        raise ValueError("Telefone inválido! \nTelefone deve ser um número com 8 ou mais dígitos\n")
                    if not self.email_valido(values["email"]):
                        raise ValueError("E-mail inválido! \nTente novamente...\n")
                    if not self.usuario_valido(values["usuario"]):
                        raise ValueError("Usuário inválido! \nUsuário deve ter pelo menos 8 caracteres\n")
                    if not self.senha_valida(values["senha"]):
                        raise ValueError("Senha inválida! \nSenha deve ter pelo menos 8 caracteres\n")
                    if not self.rua_valida(values["rua"]):
                        raise ValueError("Rua inválida! \nRua deve ter mais de 5 caracteres\n")
                    if not self.num_residencia_valido(values["num_residencia"]):
                        raise ValueError("Número de residência inválido! \nNúmero deve ter pelo menos 1 dígito\n")
                    if not self.bairro_valido(values["bairro"]):
                        raise ValueError("Bairro inválido! \nBairro deve ter mais de 5 caracteres\n")
                    if not self.cidade_valida(values["cidade"]):
                        raise ValueError("Cidade inválida! \nCidade deve ter mais de 5 caracteres\n")
                    if not self.cep_valido(values["cep"]):
                        raise ValueError("CEP inválido! \nCEP deve ser um número com 8 dígitos\n")
                    data = self.data_valida(values["data_inicio"])
                    if data is None:
                        raise ValueError("Formato da data de início inválida! Use DD/MM/AAAA...\n")
                    else:
                        data_inicio = data

                    aluno_atualizado = {
                        "nome": values["nome"],
                        "cpf": int(values["cpf"]),
                        "telefone": values["telefone"],
                        "email": values["email"],
                        "usuario": values["usuario"],
                        "senha": values["senha"],
                        "rua": values["rua"],
                        "num_residencia": int(values["num_residencia"]),
                        "bairro": values["bairro"],
                        "cidade": values["cidade"],
                        "cep": values["cep"],
                        "data_inicio": data_inicio
                    }

                    if aluno_atualizado:
                        self.close()
                        return aluno_atualizado
                    else:
                        self.close()
                        raise EdicaoAlunoException
                except Exception as e:
                    self.mostrar_mensagem(str(e))

    def excluir_aluno(self, aluno):
        layout = [
            [sg.Text(f"Confirma a exclusão do ALUNO(A): {aluno["nome"]}?", font=("Helvetica", 14))],
            [sg.Button("SIM", size=(10, 1), pad=((5, 0), (10, 10))), sg.Button("NÃO", size=(10, 1), pad=((10, 0), (10, 10)))]
        ]
        self.__window = sg.Window("Confirmar Exclusão").Layout(layout)

        while True:
            button, values = self.open()
            self.close()
            if button == None:
                return False
            elif button == "SIM":
                return True
            elif button == "NÃO":
                return False

    def listar_alunos(self, alunos):
        lista_alunos = [f"{i + 1}. {aluno["nome"]} (CPF: {aluno["cpf"]} / Curso: {aluno["curso"]})" for i, aluno in enumerate(alunos)]
        layout = [
            [sg.Text("Lista de Alunos", font=("Helvetica", 14), pad=((0, 0), (10, 10)))],
            [sg.Listbox(values=lista_alunos, size=(70, 10), enable_events=False, font=("Helvetica", 10), pad=((5, 0), (5, 0)))],
            [sg.Button("Voltar", size=(10, 1), pad=((5, 0), (15, 15)))]
        ]
        self.__window = sg.Window("Lista Alunos", layout)
        while True:
            button, values = self.open()
            if button in (None, "Voltar"):
                self.close()
                break

    def mostrar_opcao_aluno(self, aluno):
        print(aluno["indice"] + 1, " - NOME: ", aluno["nome"], " | CPF: ", aluno["cpf"], " | MATRÍCULA: ",
            aluno["matricula"], " | CURSO: ", aluno["curso"])

    def selecionar_aluno(self, num_opcoes):
        if (num_opcoes == 0):
            print("\n************** NENHUM ALUNO CADASTRADO *************")
            return
        while (True):
            try:
                opcao = input(
                    "\nComo deseja selecionar o aluno? \n1 - Procurar aluno pelo CPF \n2 - Selecionar da lista de alunos \n\nEscolha uma opção: ")
                if (opcao == "1" or opcao == "2"):
                    break
                else:
                    raise OpcaoInvalidaException
            except Exception as e:
                self.mostrar_mensagem(str(e))
        if (opcao == "1"):
            return "Buscar pelo cpf"
        if (opcao == "2"):
            return "Selecionar da lista"

    def selecionar_aluno_na_lista(self, lista_alunos, mensagem):
        nomes_alunos = [aluno["nome"] for aluno in lista_alunos]
        layout = [
            [sg.Text(mensagem, font=("Helvetica", 14), pad=((0, 0), (10, 10)))],
            [sg.Listbox(nomes_alunos, size=(70, 10), key="nome_aluno_selecionado", enable_events=True)],
            [sg.Button("Confirmar", size=(8, 1), pad=((5, 0), (15, 15))), sg.Button("Cancelar", size=(8, 1), pad=((15, 0), (15, 15)))]
        ]
        self.__window = sg.Window('Selecionar Aluno').Layout(layout)
        while(True):
            try:
                button, values = self.open()
                if button == None or button == "Cancelar":
                    self.close()
                    return None
                if button == "Confirmar":
                    aluno_selecionado = values["nome_aluno_selecionado"]
                    for aluno in lista_alunos:
                        if aluno["nome"] == aluno_selecionado[0]:
                            cpf_aluno_selecionado = aluno["cpf"]
                    if cpf_aluno_selecionado:
                        self.close()
                        return cpf_aluno_selecionado
                    else:
                        raise OpcaoInvalidaException
            except OpcaoInvalidaException as e:
                self.mostrar_mensagem(str(e))

    def buscar_aluno_pelo_cpf(self):
        while (True):
            try:
                cpf = input("\nInforme o número do CPF do aluno que deseja selecionar: ")
                if cpf.isdigit() and len(cpf) == 11:
                    return int(cpf)
                else:
                    raise CpfInvalidoException
            except Exception as e:
                self.mostrar_mensagem(str(e))

    def mostrar_aluno(self, aluno):
        listar_modulos_atuais = [f"{i + 1}. {modulo["codigo"]} - {modulo["nome"]}" for i, modulo in enumerate(aluno["modulos_atuais"])]
        listar_modulos_finalizados = [f"{i + 1}. {modulo["codigo"]} - {modulo["nome"]}" for i, modulo in enumerate(aluno["modulos_finalizados"])]

        layout_scroll = [
            [sg.Text("Informações do Aluno(a)", font=("Helvetica", 16), pad=((0, 0), (10, 20)))],
            [sg.Text("NOME:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5))), sg.Text(aluno["nome"], font=("Helvetica", 10))],
            [sg.Text("CPF:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5))), sg.Text(aluno["cpf"], font=("Helvetica", 10))],
            [sg.Text("TELEFONE:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5))), sg.Text(aluno["telefone"], font=("Helvetica", 10))],
            [sg.Text("EMAIL:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5))), sg.Text(aluno["email"], font=("Helvetica", 10))],
            [sg.Text("USUÁRIO:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5))), sg.Text(aluno["usuario"], font=("Helvetica", 10))],
            [sg.Text("ENDEREÇO:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5))), sg.Text(f"{aluno["rua"]}, {aluno["num_residencia"]}", font=("Helvetica", 10))],
            [sg.Text("BAIRRO:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5))), sg.Text(aluno["bairro"], font=("Helvetica", 10))],
            [sg.Text("CIDADE:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5))), sg.Text(aluno["cidade"], font=("Helvetica", 10))],
            [sg.Text("CEP:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5))), sg.Text(aluno["cep"], font=("Helvetica", 10))],
            [sg.Text("DATA INÍCIO:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5))), sg.Text(aluno["data_inicio"], font=("Helvetica", 10))],
            [sg.Text("CURSO:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5))), sg.Text(aluno["curso"], font=("Helvetica", 10))],
            [sg.Text("MATRÍCULA:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5))), sg.Text(aluno["codigo"], font=("Helvetica", 10))],
            [sg.Text("MÓDULOS MATRICULADOS:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5)))],
            [sg.Listbox(values=listar_modulos_atuais, size=(80, 5), enable_events=False, font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5)))],
            [sg.Text("MÓDULOS FINALIZADOS:", font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5)))],
            [sg.Listbox(values=listar_modulos_finalizados, size=(80, 5), enable_events=False, font=("Helvetica", 10, "bold"), pad=((5, 5), (5, 5)))],
            [sg.Button("Voltar", size=(10, 1), pad=((5, 0), (20, 10)))]
        ]

        scrollable_column = sg.Column(layout_scroll, size=(600, 500), scrollable=True, vertical_scroll_only=True)
        layout = [[scrollable_column]]

        self.__window = sg.Window("Detalhes do Aluno", layout)

        while True:
            button, values = self.open()
            if button in (None, "Voltar"):
                self.__window.close()
                break

    def nome_valido(self, nome):
        return len(nome) > 2 and all(char.isalpha() or char.isspace() for char in nome)

    def cpf_valido(self, cpf):
        return len(cpf) == 11 and cpf.isdigit()

    def telefone_valido(self, telefone):
        return len(telefone) >= 8 and telefone.isdigit()

    def email_valido(self, email):
        return len(email) > 5 and "@" in email and "." in email

    def usuario_valido(self, usuario):
        return len(usuario) > 7

    def senha_valida(self, senha):
        return len(senha) > 7

    def rua_valida(self, rua):
        return len(rua) > 5

    def num_residencia_valido(self, num_residencia):
        return len(num_residencia) > 0 and num_residencia.isdigit()

    def bairro_valido(self, bairro):
        return len(bairro) > 5 and all(char.isalpha() or char.isspace() for char in bairro)

    def cidade_valida(self, cidade):
        return len(cidade) > 5 and all(char.isalpha() or char.isspace() for char in cidade)

    def cep_valido(self, cep):
        return len(cep) == 8 and cep.isdigit()

    def data_valida(self, data):
        try:
            data_valida = datetime.strptime(data, "%d/%m/%Y")
            return data_valida
        except ValueError:
            return None

    def cadastrar_codigo(self):
        while (True):
            codigo = input("CÓDIGO DE MATRÍCULA: ")
            if len(codigo) == 11 and codigo.isdigit():
                break
            else:
                if len(codigo) < 11 or len(codigo) > 11:
                    print("\n****** CÓDIGO DE MATRÍCULA DEVE TER 11 DÍGITOS *****")
                else:
                    print("\n********** CÓDIGO DEVE TER SOMENTE NÚMEROS *********")
                opcao = self.continuar("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar)")
                if (not opcao):
                    return
                print("\n")
        return codigo

    def lancar_nota_modulo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Informe a nota do aluno no módulo:", font=("Helvetica", 14))],
            [sg.Input(key="nota", size=(10, 1), font=("Helvetica", 12))],
            [sg.Button("Confirmar", size=(8, 1), pad=((5, 0), (20, 20))), sg.Button("Cancelar", size=(8, 1), pad=((5, 0), (20, 20)))]
        ]

        self.__window = sg.Window("Sistema de Alunos").Layout(layout)

        while True:
            try:
                button, values = self.open()
                if button in (None, "Cancelar"):
                    self.close()
                    return None

                if button == "Confirmar":
                    nota = values["nota"]
                    if re.fullmatch(r"\d+([.,]\d+)?", nota):
                        nota = float(nota.replace(",", "."))
                        if 0.00 <= nota <= 10.00:
                            self.close()
                            return nota
                        else:
                            raise ValueError("Nota inválida! Insira um número válido entre 0 e 10")
                    else:
                        raise ValueError("Nota inválida! Por favor, tente novamente...")
            except Exception as e:
                self.mostrar_mensagem(str(e))

    def continuar(self, mensagem):
        while (True):
            print("\n----------------------------------------------------")
            print(mensagem)
            opcao = input("\nEscolha a opção: ")
            if (opcao == "1"):
                return True
            elif (opcao == "2"):
                return False
            else:
                print("\n******** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... ********")

    def mostrar_mensagem(self, mensagem: str):
        sg.Popup("Alerta!", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def voltar(self):
        self.__controlador_sistema.abrir_tela()