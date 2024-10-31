from datetime import date

class TelaAluno():

    def mostrar_menu_opcoes(self):
        print("\n---------------- ALUNOS ----------------")
        print("Escolha a opção:")
        print("1 - Cadastrar Aluno")
        print("0 - Voltar ")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def cadastrar_aluno(self):

        print("\n---------------- DADOS DO ALUNO ------------------")
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
        # Mostrar lista de cursos?
        curso = input("Curso: ")
        codigo = input("Código da matrícula: ")
        data_inicio = date.today()

        
        return {
            "nome": nome, "cpf": cpf, "telefone": telefone, "email": email, "usuario": usuario,
            "senha": senha, "rua": rua, "num_residencia": num_residencia, "bairro": bairro,
            "cidade": cidade, "cep": cep, "curso": curso, "codigo": codigo, "data_inicio": data_inicio
        }
    
    def mostrar_mensagem(self, msg):
        print(msg)