from datetime import date
class TelaAluno():

    def mostrar_menu_opcoes(self):
        print("\n---------------- ALUNOS ----------------")
        print("Escolha a opção:")
        print("1 - Cadastrar Aluno")
        print("2 - Excluir Aluno")
        print("3 - Listar Alunos")
        print("0 - Voltar ")
        opcao = int(input("Escolha a opção: "))
        return opcao

    def cadastrar_aluno(self):
        print("\n------------ DADOS DO ALUNO ------------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        usuario = input("Usuario: ")
        senha = input("Senha: ")
        rua = input("Rua: ")
        num_residencia = int(input("Número: "))
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = input("CEP: ")
        
        return {
            "nome": nome, "cpf": cpf, "telefone": telefone, "email": email, "usuario": usuario,
            "senha": senha, "rua": rua, "num_residencia": num_residencia, "bairro": bairro,
            "cidade": cidade, "cep": cep
        }
    
    def excluir_aluno(self, num_opcoes):
        if (num_opcoes == 0):
            return
        while(True):
            indice_aluno = int(input("\nInforme o número da opção do aluno que deseja excluir: "))
            if 1 <= indice_aluno < num_opcoes+1 :
                return indice_aluno - 1
            else:
                print("Opção inválida. Por favor, digite o número da opção de aluno desejada.")

    def selecionar_aluno(self, num_opcoes):
        if (num_opcoes == 0):
            return
        while(True):
            indice_aluno = int(input("\nInforme o número da opção do aluno que deseja selecionar: "))
            if 1 <= indice_aluno < num_opcoes+1 :
                return indice_aluno - 1
            else:
                print("Opção inválida. Por favor, digite o número da opção de aluno desejada.")

    def mostrar_opcao_aluno(self, aluno):
        print(aluno["indice"]+1, " - Nome: ", aluno["nome"], " | Matrícula: ", aluno["matricula"], " | Curso: ", aluno["curso"])

    def mostrar_aluno(self, aluno):
        print("\n-----------------------------------------------")
        print("NOME: ", aluno["nome"])
        print("CPF: ", aluno["cpf"])
        print("TELEFONE: ", aluno["telefone"])
        print("EMAIL: ", aluno["email"])
        print("USUÁRIO: ", aluno["usuario"])
        print("RUA: ", aluno["rua"])
        print("NÚMERO: ", aluno["num_residencia"])
        print("BAIRRO: ", aluno["bairro"])
        print("CIDADE: ", aluno["cidade"])
        print("CEP: ", aluno["cep"])
        print("CURSO: ", aluno["curso"])
        print("MATRÍCULA: ", aluno["matricula"])
        print("\n")

    def mostrar_mensagem(self, msg):
        print(msg)