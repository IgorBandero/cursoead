class TelaModulo:
    def mostrar_menu_opcoes(self):
        print("\n---------------- MÓDULOS ----------------")
        print("1 - Cadastrar Módulo")
        print("2 - Editar Módulo")
        print("3 - Excluir Módulo")
        print("4 - Listar Módulos")
        print("0 - Voltar")
        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_modulo(self):
        codigo = input("Código do Módulo: ")
        nome = input("Nome do Módulo: ")
        area = input("Área do Módulo: ")
        carga_horaria = int(input("Carga Horária do Módulo: "))
        return {"codigo": codigo, "nome": nome, "area": area, "carga_horaria": carga_horaria}

    def selecionar_modulo(self, num_opcoes):
        if num_opcoes == 0:
            return None
        while True:
            try:
                indice_modulo = int(input("\nInforme o número da opção do módulo que deseja selecionar: "))
                if 1 <= indice_modulo <= num_opcoes:
                    return indice_modulo - 1
                else:
                    print("Opção inválida. Por favor, digite o número da opção de módulo desejado.")
            except ValueError:
                print("Entrada inválida! Insira um número.")

    def listar_modulos(self, modulos):
        if not modulos:
            print("Nenhum módulo cadastrado.")
        else:
            print("\n-------- LISTA DE MÓDULOS --------\n")
            for indice, modulo in enumerate(modulos, start=1):
                print(f"{indice} - CÓDIGO: {modulo.codigo}, NOME: {modulo.nome}, ÁREA: {modulo.area}, CARGA HORÁRIA: {modulo.carga_horaria}")

    def mostrar_mensagem(self, msg):
        print(msg)
