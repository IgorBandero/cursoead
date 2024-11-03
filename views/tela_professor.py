class TelaProfessor:
    def mostrar_menu_opcoes(self):
        print("-------- MENU PROFESSOR --------")
        print("Escolha a opção:")
        print("--------------------------------")
        print("1 - Cadastrar Professor")
        print("2 - Listar Professores")
        print("3 - Editar Professor")
        print("4 - Remover Professor")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")
        return int(opcao)

    def pega_dados_professor(self):
        print("Cadastro de Professor")
        
        nome = self.cadastrar_nome()
        cpf = self.cadastrar_cpf()
        telefone = self.cadastrar_telefone()
        email = self.cadastrar_email()
        usuario = self.cadastrar_usuario()
        senha = self.cadastrar_senha()
        formacao = input("Formação: ")
        especialidade = input("Especialidade: ")
        rua = self.cadastrar_rua()
        num_residencia = self.cadastrar_num_residencia()
        bairro = self.cadastrar_bairro()
        cidade = self.cadastrar_cidade()
        cep = self.cadastrar_cep()
        
        return {
            "nome": nome,
            "cpf": cpf,
            "telefone": telefone,
            "email": email,
            "usuario": usuario,
            "senha": senha,
            "formacao": formacao,
            "especialidade": especialidade,
            "rua": rua,
            "num_residencia": num_residencia,
            "bairro": bairro,
            "cidade": cidade,
            "cep": cep
        }

    def mostra_professor(self, dados_professor):
        print(f"CPF: {dados_professor['cpf']}")
        print(f"\nNome: {dados_professor['nome']}")
        print(f"Especialidade: {dados_professor['especialidade']}")
        print(f"Formação: {dados_professor['formacao']}\n")

    def seleciona_professor(self):
        return self.cadastrar_cpf()

    def mostra_mensagem(self, msg: str):
        print(msg)

    def cadastrar_nome(self):
        while True:
            nome = input("Nome: ")
            if len(nome) >= 3 and all(char.isalpha() or char.isspace() for char in nome):
                return nome
            print("\n******* NOME DEVE TER PELO MENOS 3 CARACTERES E APENAS LETRAS OU ESPAÇOS *******")

    def cadastrar_cpf(self):
        while True:
            cpf = input("CPF: ")
            if cpf.isdigit() and len(cpf) == 11:
                return int(cpf)
            print("\n******* CPF INVÁLIDO! DEVE TER 11 DÍGITOS NUMÉRICOS *******")

    def cadastrar_telefone(self):
        while True:
            telefone = input("Telefone: ")
            if telefone.isdigit() and len(telefone) >= 8:
                return telefone
            print("\n******* TELEFONE INVÁLIDO! DEVE TER PELO MENOS 8 DÍGITOS *******")

    def cadastrar_email(self):
        while True:
            email = input("Email: ")
            if "@" in email and "." in email and len(email) >= 5:
                return email
            print("\n******* EMAIL INVÁLIDO! INSIRA UM EMAIL VÁLIDO COM '@' E '.' *******")

    def cadastrar_usuario(self):
        while True:
            usuario = input("Usuário: ")
            if len(usuario) >= 8:
                return usuario
            print("\n******* USUÁRIO INVÁLIDO! DEVE TER PELO MENOS 8 CARACTERES *******")

    def cadastrar_senha(self):
        while True:
            senha = input("Senha: ")
            if len(senha) >= 8 and any(char.isalpha() for char in senha) and any(char.isdigit() for char in senha):
                return senha
            print("\n******* SENHA INVÁLIDA! DEVE TER PELO MENOS 8 CARACTERES, CONTENDO LETRAS E NÚMEROS *******")

    def cadastrar_rua(self):
        while True:
            rua = input("Rua: ")
            if len(rua) >= 5:
                return rua
            print("\n******* RUA INVÁLIDA! DEVE TER PELO MENOS 5 CARACTERES *******")

    def cadastrar_num_residencia(self):
        while True:
            num_residencia = input("Número da Residência: ")
            if num_residencia.isdigit():
                return int(num_residencia)
            print("\n******* NÚMERO DA RESIDÊNCIA INVÁLIDO! INSIRA SOMENTE NÚMEROS *******")

    def cadastrar_bairro(self):
        while True:
            bairro = input("Bairro: ")
            if len(bairro) >= 5 and all(char.isalpha() or char.isspace() for char in bairro):
                return bairro
            print("\n******* BAIRRO INVÁLIDO! DEVE TER PELO MENOS 5 CARACTERES E APENAS LETRAS OU ESPAÇOS *******")

    def cadastrar_cidade(self):
        while True:
            cidade = input("Cidade: ")
            if len(cidade) >= 5 and all(char.isalpha() or char.isspace() for char in cidade):
                return cidade
            print("\n******* CIDADE INVÁLIDA! DEVE TER PELO MENOS 5 CARACTERES E APENAS LETRAS OU ESPAÇOS *******")

    def cadastrar_cep(self):
        while True:
            cep = input("CEP: ")
            if cep.isdigit() and len(cep) >= 8:
                return cep
            print("\n******* CEP INVÁLIDO! DEVE TER PELO MENOS 8 DÍGITOS *******")

