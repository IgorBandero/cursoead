class TelaCurso():

    def mostrar_menu_opcoes(self):
        print("\n---------------- CURSOS ----------------")
        print("Escolha a opção:")
        print("1 - Cadastrar Curso")
        print("2 - Editar Curso")
        print("3 - Excluir Curso")
        print("4 - Listar Cursos Disponíveis")
        print("0 - Voltar ")
        opcao = int(input("Escolha a opção: "))
        return opcao

    def cadastrar_curso(self):
        print("\n------------ DADOS DO CURSO ------------")
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        carga_horaria = int(input("Carga horária: "))
        min_semestres = int(input("Mínimo de semestres: "))
        max_semestres = int(input("Máximo de semestres: "))
        mensalidade = float(input("Mensalidade: "))
        
        return {
            "nome": nome, "descricao": descricao, "carga_horaria": carga_horaria, "min_semestres": min_semestres, "max_semestres": max_semestres, "mensalidade": mensalidade
        }
    
    def excluir_curso(self, num_opcoes):
        if (num_opcoes == 0):
            return
        while(True):
            indice_curso = int(input("\nInforme o número da opção do curso que deseja excluir: "))
            if 1 <= indice_curso < num_opcoes+1 :
                return indice_curso - 1
            else:
                print("Opção inválida. Por favor, digite o número da opção de curso desejada.")

    def editar_curso(self):
        print("\n------------ ATUALIZAÇÃO DE DADOS DO CURSO ------------")
        return self.cadastrar_curso()
    
    def selecionar_curso(self, num_opcoes):
        if (num_opcoes == 0):
            return
        while(True):
            indice_curso = int(input("\nInforme o número da opção do curso que deseja selecionar: "))
            if 1 <= indice_curso < num_opcoes+1 :
                return indice_curso - 1
            else:
                print("Opção inválida. Por favor, digite o número da opção de curso desejada.")
    
    def mostrar_curso(self, curso):
        print("\n-----------------------------------------------")
        print("NOME: ", curso["nome"])
        print("DESCRIÇÃO: ", curso["descricao"])
        print("CARGA HORÁRIA: ", curso["carga_horaria"])
        print("MÍNIMO DE SEMESTRES: ", curso["min_semestres"])
        print("MÁXIMO DE SEMESTRES: ", curso["max_semestres"])
        print("MENSALIDADE: ", curso["mensalidade"])
        print("\n")

    def mostrar_opcao_curso(self, curso):
        print(curso["indice"]+1, " - ", curso["nome"])

    def mostrar_mensagem(self, msg):
        print(msg)