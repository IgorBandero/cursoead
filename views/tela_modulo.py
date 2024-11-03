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
        if (num_opcoes == 0):
            print("\n************ NENHUM MÓDULO CADASTRADO ***********")
            return
        while(True):
            opcao = input("\nComo deseja selecionar o módulo? \n1 - Procurar módulo pelo CÓDIGO \n2 - Selecionar da lista de módulos \n\nEscolha uma opção: ")
            if (opcao == "1" or opcao == "2"):
                break
            else:
                print("\n****** OPÇÃO INVÁLIDA, TENTE NOVAMENTE... *******")
        if (opcao == "1"):
            return "Buscar pelo codigo"
        if (opcao == "2"):
            return "Selecionar da lista"

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
        while(True):
            codigo = input("\nInforme o código do módulo que deseja selecionar: ")
            if codigo is not None:
                return codigo
            else:
                print("\n******* CÓDIGO INVÁLIDO! TENTE NOVAMENTE... ********")

    def selecionar_modulo_na_lista(self, num_opcoes):
        while(True):
            indice_modulo = input("\nInforme o número da opção do módulo que deseja selecionar: ")
            if indice_modulo.isdigit():
                if 1 <= int(indice_modulo) < num_opcoes+1:
                    return int(indice_modulo) - 1
                else:
                    print("Opção inválida. Por favor, digite o número da opção de módulo desejada.")
            else:
                print("Opção inválida. Por favor, digite o número da opção de módulo desejada.")

    def continuar_registro_modulos(self):
        while(True):
            print("\n----------------------------------------------------")
            print("Deseja adicionar outro módulo? \n1 - SIM \n2 - NÃO (Finalizar)")
            opcao = input("\nEscolha a opção: ")
            if (opcao == "1"):
                return True
            elif (opcao == "2"):
                return False
            else:
                print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")