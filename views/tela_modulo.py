class TelaModulo:
    def mostrar_menu_opcoes(self):
        while True:
            print("\n---------------------- MÓDULOS ---------------------")
            print("Escolha a opção:")
            print("----------------------------------------------------")
            print("1 - Cadastrar Módulo")
            print("2 - Editar Módulo")
            print("3 - Excluir Módulo")
            print("4 - Listar Módulos")
            print("0 - Voltar")
            print("----------------------------------------------------")
            opcao = input("Escolha a opção: ")
            if opcao in ["1", "2", "3", "4", "0"]:
                return int(opcao)
            else:
                print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")

    def pega_dados_modulo(self):
        while True:
            codigo = input("Código do Módulo: ")
            if len(codigo) >= 3:
                break
            else:
                print("O código deve ter pelo menos 3 caracteres.")

        while True:
            nome = input("Nome do Módulo: ")
            if len(nome) >= 5:
                break
            else:
                print("O nome deve ter pelo menos 5 caracteres.")

        area = input("Área do Módulo: ")

        while True:
            try:
                carga_horaria = int(input("Carga Horária do Módulo: "))
                if carga_horaria > 0:
                    break
                else:
                    print("A carga horária deve ser maior que zero.")
            except ValueError:
                print("Carga horária inválida. Deve ser um número inteiro.")

        return {"codigo": codigo, "nome": nome, "area": area, "carga_horaria": carga_horaria}

    def selecionar_modulo(self, num_opcoes):
        if num_opcoes == 0:
            print("\n************ NENHUM MÓDULO CADASTRADO ***********")
            return None
        while True:
            opcao = input("\nComo deseja selecionar o módulo? \n1 - Procurar módulo pelo CÓDIGO \n2 - Selecionar da lista de módulos \n\nEscolha uma opção: ")
            if opcao in ["1", "2"]:
                return "Buscar pelo codigo" if opcao == "1" else "Selecionar da lista"
            else:
                print("\n****** OPÇÃO INVÁLIDA, TENTE NOVAMENTE... *******")

    def listar_modulos(self, modulos):
        if not modulos:
            print("Nenhum módulo cadastrado.")
        else:
            print("\n-------- LISTA DE MÓDULOS --------\n")
            for indice, modulo in enumerate(modulos, start=1):
                print(f"{indice} - CÓDIGO: {modulo.codigo}, NOME: {modulo.nome}, ÁREA: {modulo.area}, CARGA HORÁRIA: {modulo.carga_horaria}")

    def mostrar_mensagem(self, msg):
        print(msg)

    def buscar_modulo_pelo_codigo(self):
        while True:
            codigo = input("\nInforme o código do módulo que deseja selecionar: ")
            if len(codigo) >= 3:
                return codigo
            else:
                print("Código inválido! Tente novamente.")

    def selecionar_modulo_na_lista(self, num_opcoes):
        while True:
            indice_modulo = input("Informe o número da opção do módulo que deseja selecionar: ")
            if indice_modulo.isdigit():
                indice_modulo = int(indice_modulo) - 1
                if 0 <= indice_modulo < num_opcoes:
                    return indice_modulo
                else:
                    print("Opção inválida. Por favor, selecione uma opção válida.")
            else:
                print("Opção inválida. Por favor, insira um número.")

    def continuar_registro_modulos(self):
        while True:
            print("\nDeseja adicionar outro módulo? \n1 - SIM \n2 - NÃO (Finalizar)")
            opcao = input("Escolha a opção: ")
            if opcao == "1":
                return True
            elif opcao == "2":
                return False
            else:
                print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")

    def mostrar_modulo(self, modulo):
        print(f"CÓDIGO: {modulo['codigo']} | NOME: {modulo['nome']} | ÁREA: {modulo['area']} | CARGA HORÁRIA: {modulo['carga_horaria']}")
