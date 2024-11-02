class TelaOrientacao:
    def mostrar_menu_opcoes(self):
        print("-------- MENU ORIENTAÇÃO --------")
        print("1 – Cadastrar Orientação")
        print("2 – Listar Orientações")
        print("3 – Editar Orientação")
        print("4 – Excluir Orientação")
        print("5 – Listar Orientandos de um Professor")
        print("0 – Voltar")
        opcao = input("Escolha uma opção: ")
        return int(opcao)

    def pega_dados_orientacao(self):
        cpf_aluno = input("CPF do Aluno: ")
        cpf_professor = input("CPF do Professor: ")
        return {"cpf_aluno": cpf_aluno, "cpf_professor": cpf_professor}
    
    def pegar_cpf_professor(self):
        while True:
            try:
                cpf_professor = int(input("Informe o CPF do professor: "))
                return cpf_professor
            except ValueError:
                print("CPF deve ser um número inteiro. Tente novamente.")

    def mostrar_orientacao(self, dados_orientacao):
        print(f"Aluno: {dados_orientacao['nome_aluno']} (CPF: {dados_orientacao['cpf_aluno']})")
        print(f"Professor: {dados_orientacao['nome_professor']} (CPF: {dados_orientacao['cpf_professor']})\n")

    def mostra_orientando(self, nome_aluno, cpf_aluno):
        print(f"Nome do Aluno: {nome_aluno}")
        print(f"CPF do Aluno: {cpf_aluno}")

    def mostrar_orientador(self, nome_professor, cpf_professor):
        print(f"Nome do Orientador: {nome_professor}")
        print(f"CPF do Orientador: {cpf_professor}")

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)

    def seleciona_orientacao(self):
        while True:
            try:
                cpf_aluno = int(input("Digite o CPF do aluno para selecionar a orientação: "))
                return cpf_aluno
            except ValueError:
                print("CPF deve ser um número inteiro. Por favor, tente novamente.")