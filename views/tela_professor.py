class TelaProfessor:
    def mostrar_menu_opcoes(self):
        print("\n---------------------- PROFESSORES ----------------------")
        print("Escolha a opção:")
        print("---------------------------------------------------------")
        print("1 - Cadastrar Professor")
        print("2 - Editar Professor")
        print("3 - Excluir Professor")
        print("4 - Listar Professores")
        print("0 - Voltar")
        print("---------------------------------------------------------")
        opcao = input("Escolha a opção: ")
        if (opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4" or  opcao == "5" or opcao == "0"):
            return int(opcao)
        else:
            print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")
    
    def continuar_edicao(self):
        while True:
            print("\n----------------------------------------------------")
            print("Deseja editar outro campo? \n1 - SIM \n2 - NÃO (Sair)")
            opcao = input("\nEscolha a opção: ")
            if opcao == "1":
                return True
            elif opcao == "2":
                return False
            else:
                print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")

    def mostrar_professor(self, dados_professor):
        print("\n---------------------- PROFESSOR(A) --------------------")
        print(f"NOME: {dados_professor['nome']}")
        print(f"CPF: {dados_professor['cpf']}")
        print(f"TELEFONE: {dados_professor['telefone']}")
        print(f"EMAIL: {dados_professor['email']}")
        print(f"USUÁRIO: {dados_professor['usuario']}")
        print(f"FORMAÇÃO: {dados_professor['formacao']}")
        print(f"ESPECIALIDADE: {dados_professor['especialidade']}")
        print(f"RUA: {dados_professor['rua']}")
        print(f"NÚMERO: {dados_professor['num_residencia']}")
        print(f"BAIRRO: {dados_professor['bairro']}")
        print(f"CIDADE: {dados_professor['cidade']}")
        print(f"CEP: {dados_professor['cep']}")
        print("---------------------------------------------------------\n")
    
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

    def editar_professor(self):
        print("\n--------------- ATRIBUTOS PARA EDITAR --------------")
        print("1 - NOME")
        print("2 - CPF")
        print("3 - TELEFONE")
        print("4 - EMAIL")
        print("5 - USUÁRIO")
        print("6 - SENHA")
        print("7 - FORMAÇÃO")
        print("8 - ESPECIALIDADE")
        print("9 - RUA")
        print("10 - NÚMERO DE RESIDÊNCIA")
        print("11 - BAIRRO")
        print("12 - CIDADE")
        print("13 - CEP")
        print("----------------------------------------------------")
        
        while True:
            opcao = input("\nEscolha uma opção para editar ou 0 para sair: ")
            if opcao == "0":
                return None, None
            elif opcao == "1":
                return int(opcao), self.cadastrar_nome()
            elif opcao == "2":
                return int(opcao), self.cadastrar_cpf()
            elif opcao == "3":
                return int(opcao), self.cadastrar_telefone()
            elif opcao == "4":
                return int(opcao), self.cadastrar_email()
            elif opcao == "5":
                return int(opcao), self.cadastrar_usuario()
            elif opcao == "6":
                return int(opcao), self.cadastrar_senha()
            elif opcao == "7":
                return int(opcao), input("Nova Formação: ")
            elif opcao == "8":
                return int(opcao), input("Nova Especialidade: ")
            elif opcao == "9":
                return int(opcao), self.cadastrar_rua()
            elif opcao == "10":
                return int(opcao), self.cadastrar_num_residencia()
            elif opcao == "11":
                return int(opcao), self.cadastrar_bairro()
            elif opcao == "12":
                return int(opcao), self.cadastrar_cidade()
            elif opcao == "13":
                return int(opcao), self.cadastrar_cep()
            else:
                print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")

    def excluir_professor(self, dados_professor):
        while True:
            print(f"\nConfirma a exclusão do(a) PROFESSOR(A): {dados_professor['nome']} (CPF: {dados_professor['cpf']})? \n1 - SIM \n2 - NÃO (Cancelar)")
            opcao = input("\nEscolha a opção: ")
            if opcao == "1":
                return True
            elif opcao == "2":
                return False
            else:
                print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")

    def mostra_mensagem(self, msg: str):
        print(msg)
    
    def seleciona_professor(self):
        return self.cadastrar_cpf()

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


