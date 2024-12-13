import PySimpleGUI as sg

class TelaProfessor:
    def __init__(self):
        self.__window = None

    def mostrar_menu_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("---------------------- PROFESSORES ----------------------", font=("Helvetica", 25),
                     pad=((0, 0), (10, 15)))],
            [sg.Text("Escolha a opção:", font=("Helvetica", 14), pad=((5, 0), (0, 10)))],
            [sg.Radio("Cadastrar Professor", "RD1", key="1")],
            [sg.Radio("Editar Professor", "RD1", key="2")],
            [sg.Radio("Excluir Professor", "RD1", key="3")],
            [sg.Radio("Listar Professores", "RD1", key="4")],
            [sg.Radio("Voltar", "RD1", key="0")],
            [sg.Button("Confirmar", size=(8, 1), pad=((10, 0), (20, 20))),
             sg.Cancel("Cancelar", size=(8, 1), pad=((15, 0), (20, 20)))]
        ]
        self.__window = sg.Window("Sistema de Professores").Layout(layout)

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
                continue

            self.close()
            return opcao

    def pega_dados_professor(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Cadastro de Professor", font=("Helvetica", 20), pad=((0, 0), (0, 10)))],
            [sg.Text("Nome:", size=(15, 1)), sg.InputText("", key="nome")],
            [sg.Text("CPF:", size=(15, 1)), sg.InputText("", key="cpf")],
            [sg.Text("Telefone:", size=(15, 1)), sg.InputText("", key="telefone")],
            [sg.Text("Email:", size=(15, 1)), sg.InputText("", key="email")],
            [sg.Text("Usuário:", size=(15, 1)), sg.InputText("", key="usuario")],
            [sg.Text("Senha:", size=(15, 1)), sg.InputText("", key="senha", password_char="*")],
            [sg.Text("Formação:", size=(15, 1)), sg.InputText("", key="formacao")],
            [sg.Text("Especialidade:", size=(15, 1)), sg.InputText("", key="especialidade")],
            [sg.Text("Rua:", size=(15, 1)), sg.InputText("", key="rua")],
            [sg.Text("Número Residência:", size=(15, 1)), sg.InputText("", key="num_residencia")],
            [sg.Text("Bairro:", size=(15, 1)), sg.InputText("", key="bairro")],
            [sg.Text("Cidade:", size=(15, 1)), sg.InputText("", key="cidade")],
            [sg.Text("CEP:", size=(15, 1)), sg.InputText("", key="cep")],
            [sg.Button("Confirmar", size=(8, 1), pad=((5, 0), (20, 20))),
             sg.Cancel("Cancelar", size=(8, 1), pad=((15, 0), (20, 20)))]
        ]
        self.__window = sg.Window("Dados do Professor").Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, "Cancelar"):
                self.close()
                return None
            try:
                # Conversões e validações
                values["cpf"] = self.validar_e_converter_cpf(values["cpf"])
                values["telefone"] = self.validar_telefone(values["telefone"])
                values["num_residencia"] = self.validar_numero_residencia(values["num_residencia"])
                values["cep"] = self.validar_cep(values["cep"])

                # Valida campos textuais
                self.validar_texto(values["nome"], "Nome", 3)
                self.validar_email(values["email"])
                self.validar_texto(values["usuario"], "Usuário", 8)
                self.validar_senha(values["senha"])
                self.validar_texto(values["formacao"], "Formação", 3)
                self.validar_texto(values["especialidade"], "Especialidade", 3)
                self.validar_texto(values["rua"], "Rua", 5)
                self.validar_texto(values["bairro"], "Bairro", 5)
                self.validar_texto(values["cidade"], "Cidade", 5)

                self.close()
                return values
            except ValueError as e:
                self.mostra_mensagem(f"Erro: {str(e)}")

    def validar_e_converter_cpf(self, cpf):
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF inválido! Deve conter exatamente 11 dígitos numéricos.")
        return int(cpf)

    def validar_telefone(self, telefone):
        if not telefone.isdigit() or len(telefone) < 8:
            raise ValueError("Telefone inválido! Deve conter pelo menos 8 dígitos numéricos.")
        return telefone

    def validar_numero_residencia(self, num_residencia):
        if not num_residencia.isdigit():
            raise ValueError("Número da residência inválido! Deve ser um valor numérico.")
        return int(num_residencia)

    def validar_cep(self, cep):
        if not cep.isdigit() or len(cep) < 8:
            raise ValueError("CEP inválido! Deve conter pelo menos 8 dígitos numéricos.")
        return cep

    def validar_texto(self, texto, campo, tamanho_minimo):
        if len(texto) < tamanho_minimo:
            raise ValueError(f"{campo} inválido! Deve ter pelo menos {tamanho_minimo} caracteres.")
        return texto

    def validar_email(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("Email inválido! Deve conter '@' e '.' em formato válido.")
        return email

    def validar_senha(self, senha):
        if len(senha) < 8 or not any(char.isalpha() for char in senha) or not any(char.isdigit() for char in senha):
            raise ValueError("Senha inválida! Deve ter pelo menos 8 caracteres, incluindo letras e números.")
        return senha

    def valida_campos_professor(self, values):
        if len(values["nome"]) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres.")
        if not values["cpf"].isdigit() or len(values["cpf"]) != 11:
            raise ValueError("CPF deve ter 11 dígitos numéricos.")
        if not values["telefone"].isdigit() or len(values["telefone"]) < 8:
            raise ValueError("Telefone deve ter pelo menos 8 dígitos.")
        if "@" not in values["email"] or "." not in values["email"]:
            raise ValueError("Email inválido.")
        if len(values["usuario"]) < 8:
            raise ValueError("Usuário deve ter pelo menos 8 caracteres.")
        if len(values["senha"]) < 8 or not any(char.isdigit() for char in values["senha"]):
            raise ValueError("Senha deve ter pelo menos 8 caracteres e incluir números.")
        if len(values["formacao"]) < 3:
            raise ValueError("Formação deve ter pelo menos 3 caracteres.")
        if len(values["especialidade"]) < 3:
            raise ValueError("Especialidade deve ter pelo menos 3 caracteres.")
        if len(values["rua"]) < 5:
            raise ValueError("Rua deve ter pelo menos 5 caracteres.")
        if not values["num_residencia"].isdigit():
            raise ValueError("Número da residência deve ser um número.")
        if len(values["bairro"]) < 5:
            raise ValueError("Bairro deve ter pelo menos 5 caracteres.")
        if len(values["cidade"]) < 5:
            raise ValueError("Cidade deve ter pelo menos 5 caracteres.")
        if not values["cep"].isdigit() or len(values["cep"]) < 8:
            raise ValueError("CEP deve ter pelo menos 8 dígitos numéricos.")

    def mostrar_professor(self, dados_professor):
        layout = [
            [sg.Text("Informações do Professor", font=("Helvetica", 20), pad=((0, 0), (0, 10)))],
            [sg.Text(f"NOME: {dados_professor['nome']}", font=("Helvetica", 14))],
            [sg.Text(f"CPF: {dados_professor['cpf']}", font=("Helvetica", 14))],
            [sg.Text(f"TELEFONE: {dados_professor['telefone']}", font=("Helvetica", 14))],
            [sg.Text(f"EMAIL: {dados_professor['email']}", font=("Helvetica", 14))],
            [sg.Text(f"USUÁRIO: {dados_professor['usuario']}", font=("Helvetica", 14))],
            [sg.Text(f"FORMAÇÃO: {dados_professor['formacao']}", font=("Helvetica", 14))],
            [sg.Text(f"ESPECIALIDADE: {dados_professor['especialidade']}", font=("Helvetica", 14))],
            [sg.Text(f"RUA: {dados_professor['rua']}", font=("Helvetica", 14))],
            [sg.Text(f"NÚMERO: {dados_professor['num_residencia']}", font=("Helvetica", 14))],
            [sg.Text(f"BAIRRO: {dados_professor['bairro']}", font=("Helvetica", 14))],
            [sg.Text(f"CIDADE: {dados_professor['cidade']}", font=("Helvetica", 14))],
            [sg.Text(f"CEP: {dados_professor['cep']}", font=("Helvetica", 14))],
            [sg.Button("Voltar", size=(10, 1), pad=((5, 0), (20, 20)))]
        ]
        self.__window = sg.Window("Detalhes do Professor").Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, "Voltar"):
                self.close()
                break

    def listar_professores(self, lista_dados_professores):
        """
        Exibe uma lista de professores em uma janela, cada professor é mostrado com seus dados básicos.
        :param lista_dados_professores: Lista de dicionários contendo dados dos professores.
        """
        sg.ChangeLookAndFeel('DarkTeal4')
        lista_exibicao = [
            f"{prof['nome']} | CPF: {prof['cpf']} | Especialidade: {prof['especialidade']} | Formação: {prof['formacao']}"
            for prof in lista_dados_professores
        ]
        layout = [
            [sg.Text("Lista de Professores", font=("Helvetica", 20), pad=((0, 0), (10, 15)))],
            [sg.Listbox(values=lista_exibicao, size=(80, 15), key="professores", enable_events=False,
                        font=("Helvetica", 12))],
            [sg.Button("Voltar", size=(10, 1), pad=((5, 0), (15, 15)))]
        ]
        self.__window = sg.Window("Professores Cadastrados").Layout(layout)

        while True:
            button, _ = self.open()
            if button in (None, "Voltar"):
                self.close()
                break

    def seleciona_professor(self, lista_professores):
        """
        Permite que o usuário selecione um professor a partir de uma lista de professores exibida.
        :param lista_professores: Lista de dicionários contendo informações dos professores (nome e CPF).
        :return: CPF do professor selecionado.
        """
        sg.ChangeLookAndFeel('DarkTeal4')
        lista_exibicao = [
            f"{prof['nome']} | CPF: {prof['cpf']}" for prof in lista_professores
        ]
        layout = [
            [sg.Text("Selecione um Professor", font=("Helvetica", 20), pad=((0, 0), (10, 15)))],
            [sg.Listbox(values=lista_exibicao, size=(80, 15), key="professor_selecionado", enable_events=True,
                        font=("Helvetica", 12))],
            [sg.Button("Confirmar", size=(10, 1), pad=((5, 0), (15, 15))),
             sg.Button("Cancelar", size=(10, 1), pad=((15, 0), (15, 15)))]
        ]
        self.__window = sg.Window("Selecionar Professor").Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, "Cancelar"):
                self.close()
                return None
            if button == "Confirmar":
                try:
                    if not values["professor_selecionado"]:
                        raise ValueError("Nenhum professor selecionado!")
                    # Extrai o CPF do professor selecionado
                    professor_selecionado = values["professor_selecionado"][0]
                    cpf = int(professor_selecionado.split("| CPF: ")[1].strip())
                    self.close()
                    return cpf
                except Exception as e:
                    self.mostra_mensagem(str(e))

    def editar_professor(self, dados_professor):
        """
        Exibe um formulário para editar os dados de um professor.
        :param dados_professor: Dicionário contendo os dados atuais do professor.
        :return: Dicionário com os dados atualizados ou None se a edição for cancelada.
        """
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Editar Dados do Professor", font=("Helvetica", 20), pad=((0, 0), (0, 10)))],
            [sg.Text("Nome:", size=(15, 1)), sg.InputText(dados_professor["nome"], key="nome")],
            [sg.Text("CPF:", size=(15, 1)), sg.InputText(dados_professor["cpf"], key="cpf", disabled=True)],
            # CPF não deve ser editado
            [sg.Text("Telefone:", size=(15, 1)), sg.InputText(dados_professor["telefone"], key="telefone")],
            [sg.Text("Email:", size=(15, 1)), sg.InputText(dados_professor["email"], key="email")],
            [sg.Text("Usuário:", size=(15, 1)), sg.InputText(dados_professor["usuario"], key="usuario")],
            [sg.Text("Senha:", size=(15, 1)), sg.InputText("", key="senha", password_char="*")],
            # Limpa o campo senha para nova entrada
            [sg.Text("Formação:", size=(15, 1)), sg.InputText(dados_professor["formacao"], key="formacao")],
            [sg.Text("Especialidade:", size=(15, 1)),
             sg.InputText(dados_professor["especialidade"], key="especialidade")],
            [sg.Text("Rua:", size=(15, 1)), sg.InputText(dados_professor["rua"], key="rua")],
            [sg.Text("Número Residência:", size=(15, 1)),
             sg.InputText(dados_professor["num_residencia"], key="num_residencia")],
            [sg.Text("Bairro:", size=(15, 1)), sg.InputText(dados_professor["bairro"], key="bairro")],
            [sg.Text("Cidade:", size=(15, 1)), sg.InputText(dados_professor["cidade"], key="cidade")],
            [sg.Text("CEP:", size=(15, 1)), sg.InputText(dados_professor["cep"], key="cep")],
            [sg.Button("Salvar", size=(10, 1), pad=((5, 0), (20, 20))),
             sg.Button("Cancelar", size=(10, 1), pad=((15, 0), (20, 20)))]
        ]
        self.__window = sg.Window("Editar Professor").Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, "Cancelar"):
                self.close()
                return None
            if button == "Salvar":
                try:
                    # Validações podem ser aplicadas aqui
                    values["cpf"] = int(dados_professor["cpf"])  # Mantém o CPF inalterado
                    self.close()
                    return values
                except ValueError as e:
                    self.mostra_mensagem(f"Erro: {str(e)}")

    def excluir_professor(self, dados_professor):
        """
        Exibe uma janela para confirmar a exclusão de um professor.
        :param dados_professor: Dicionário contendo os dados do professor a ser excluído (nome e CPF).
        :return: True se a exclusão for confirmada, False caso contrário.
        """
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text(f"Confirma a exclusão do professor: {dados_professor['nome']} (CPF: {dados_professor['cpf']})?",
                     font=("Helvetica", 14), pad=((0, 0), (10, 15)))],
            [sg.Button("Sim", size=(10, 1), pad=((5, 10), (10, 10))),
             sg.Button("Não", size=(10, 1), pad=((10, 0), (10, 10)))]
        ]
        self.__window = sg.Window("Excluir Professor").Layout(layout)

        while True:
            button, _ = self.open()
            if button == "Sim":
                self.close()
                return True
            elif button in (None, "Não"):
                self.close()
                return False

    def mostra_mensagem(self, mensagem: str):
        sg.Popup("Alerta!", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()