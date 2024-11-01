class TelaOrientacao:
    def mostrar_menu_opcoes(self):
        print("-------- MENU ORIENTAÇÃO --------")
        print("1 - Cadastrar Orientação")
        print("2 - Listar Orientações")
        print("3 - Editar Orientação")
        print("4 - Excluir Orientação")
        print("5 - Listar Orientandos de um Professor")
        print("6 - Buscar Orientador de um Aluno")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")
        return int(opcao)

    def pega_dados_orientacao(self):
        cpf_aluno = input("CPF do Aluno: ")
        cpf_professor = input("CPF do Professor: ")
        return {"cpf_aluno": cpf_aluno, "cpf_professor": cpf_professor}

    def seleciona_orientacao(self):
        cpf_aluno = input("CPF do Aluno para selecionar a orientação: ")
        return cpf_aluno

    def mostra_orientacao(self, dados_orientacao):
        print(f"Aluno: {dados_orientacao['nome_aluno']} (CPF: {dados_orientacao['cpf_aluno']})")
        print(f"Professor: {dados_orientacao['nome_professor']} (CPF: {dados_orientacao['cpf_professor']})\n")

    def mostra_mensagem(self, msg):
        print(msg)
