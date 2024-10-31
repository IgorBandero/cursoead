class TelaProfessor:
    def mostrar_menu_opcoes(self):
        print("-------- MENU PROFESSOR --------")
        print("1 - Cadastrar Professor")
        print("2 - Listar Professores")
        print("3 - Editar Professor")
        print("4 - Remover Professor")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")
        return int(opcao)

    def pega_dados_professor(self):
        print("Cadastro de Professor")
        
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        formacao = input("Formação: ")
        especialidade = input("Especialidade: ")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = input("CEP: ")

        while True:
            try:
                num_residencia = int(input("Número da Residência: "))
                break 
            except ValueError:
                print("Número da Residência deve ser um valor inteiro. Por favor, tente novamente.")

        while True:
            try:
                cpf = int(input("CPF: "))
                break  
            except ValueError:
                print("CPF deve ser um valor inteiro. Por favor, tente novamente.")
        
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
        while True:
            try:
                cpf = int(input("CPF do professor que deseja selecionar: "))
                return cpf
            except ValueError:
                print("CPF deve ser um valor inteiro. Por favor, tente novamente.")

    def mostra_mensagem(self, msg: str):
        print(msg)
