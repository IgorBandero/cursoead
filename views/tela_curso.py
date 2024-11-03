import re
class TelaCurso():

    def mostrar_menu_opcoes(self):
        while(True):
            print("\n---------------------- CURSOS ----------------------")
            print("Escolha a opção:")
            print("----------------------------------------------------")
            print("1 - Cadastrar Curso")
            print("2 - Editar Curso")
            print("3 - Excluir Curso")
            print("4 - Listar Cursos Disponíveis")
            print("5 - Mostrar Curso")
            print("0 - Voltar ")
            print("----------------------------------------------------")
            opcao = input("Escolha a opção: ")
            if (opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4" or  opcao == "5" or opcao == "0"):
                return int(opcao)
            else:
                print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")

    def cadastrar_curso(self):
        print("\n------------------ DADOS DO CURSO -------------------")
        nome = self.cadastrar_nome()
        descricao = self.cadastrar_descricao()
        carga_horaria = self.cadastrar_carga_horaria()
        min_semestres = self.cadastrar_min_semestres()
        max_semestres = self.cadastrar_max_semestres()
        mensalidade = float(input("Mensalidade: "))
        return {
            "nome": nome, "descricao": descricao, "carga_horaria": carga_horaria, "min_semestres": min_semestres, "max_semestres": max_semestres, "mensalidade": mensalidade
        }
    
    def excluir_curso(self, curso):
        while(True):
            print(f"\nConfirma a exclusão do CURSO: {curso['nome']}? \n1 – SIM \n2 – NÃO (Cancelar)")
            excluir = input("\nEscolha a opção: ")
            if (excluir == "1"):
                return True
            elif (excluir == "2"):
                return False
            else:
                print("\n******** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... ********")

    def editar_curso(self):
        print("\n--------------- ATRIBUTOS PARA EDITAR --------------")
        print("1 - NOME")
        print("2 - DESCRIÇÃO")
        print("3 - CARGA HORÁRIA")
        print("4 - MÍNIMO DE SEMESTRES")
        print("5 - MÁXIMO DE SEMESTRES")
        print("6 - MENSALIDADE")
        print("----------------------------------------------------")
        while(True):
            opcao = input("\nEscolha uma opção: ")
            if (opcao == "1"):
                print("\nInforme o novo NOME...")
                nome = self.cadastrar_nome()
                return [int(opcao), nome]
            if (opcao == "2"):
                print("\nInforme a nova DESCRIÇÃO...")
                descricao = self.cadastrar_descricao()
                return [int(opcao), descricao]
            if (opcao == "3"):
                print("\nInforme a nova CARGA HORÁRIA...")
                carga = self.cadastrar_carga_horaria()
                return [int(opcao), carga]
            if (opcao == "4"):
                print("\nInforme o novo MÍNIMO DE SEMESTRES...")
                min_semestres = self.cadastrar_min_semestres()
                return [int(opcao), min_semestres]
            if (opcao == "5"):
                print("\nInforme o novo MÁXIMO DE SEMESTRES...")
                max_semestres = self.cadastrar_max_semestres()
                return [int(opcao), max_semestres]
            if (opcao == "6"):
                print("\nInforme a nova MENSALIDADE...")
                mensalidade = self.cadastrar_mensalidade()
                return [int(opcao), mensalidade]
            else:
                print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")
    
    def selecionar_curso(self, num_opcoes):
        if (num_opcoes == 0):
            print("\n************** NENHUM CURSO CADASTRADO *************")
            return
        while(True):
            opcao = input("\nComo deseja selecionar o curso? \n1 - Procurar curso pelo NOME \n2 - Selecionar da lista de cursos \n\nEscolha uma opção: ")
            if (opcao == "1" or opcao == "2"):
                break
            else:
                print("\n******** OPÇÃO INVÁLIDA, TENTE NOVAMENTE... ********")
        if (opcao == "1"):
            return "Buscar pelo nome"
        if (opcao == "2"):
            return "Selecionar da lista"
    
    def selecionar_curso_na_lista(self, num_opcoes):
        while(True):
            indice_curso = input("\nInforme o número da opção do curso que deseja selecionar: ")
            if indice_curso.isdigit():
                if 1 <= int(indice_curso) < num_opcoes+1:
                    return int(indice_curso) - 1
                else:
                    print("Opção inválida. Por favor, digite o número da opção de curso desejada.")
            else:
                print("Opção inválida. Por favor, digite o número da opção de curso desejada.")

    def buscar_curso_pelo_nome(self):
        while(True):
            nome = input("\nInforme o nome do curso que deseja selecionar: ")
            if len(nome) >= 5:
                return nome
            else:
                print("\n******** NOME INVÁLIDO! TENTE NOVAMENTE... ********")

    def mostrar_curso(self, curso):
        print("\n----------------------------------------------------")
        print("NOME: ", curso["nome"])
        print("DESCRIÇÃO: ", curso["descricao"])
        print("CARGA HORÁRIA: ", curso["carga_horaria"])
        print("MÍNIMO DE SEMESTRES: ", curso["min_semestres"])
        print("MÁXIMO DE SEMESTRES: ", curso["max_semestres"])
        print("MENSALIDADE: ", curso["mensalidade"])

    def continuar_edicao(self):
        while(True):
            print("\n----------------------------------------------------")
            print("Deseja editar outro campo? \n1 - SIM \n2 - NÃO (Sair)")
            opcao = input("\nEscolha a opção: ")
            if (opcao == "1"):
                return True
            elif (opcao == "2"):
                return False
            else:
                print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")

    def mostrar_opcao_curso(self, curso):
        print(curso["indice"]+1, " - ", curso["nome"])

    def mostrar_mensagem(self, msg):
        print(msg)

    def cadastrar_nome(self):
        while(True):
            nome = input("Nome: ")
            if len(nome) >= 5:
                break
            else:
                if len(nome) < 5:
                    print("\n******* NOME DEVE TER PELO MENOS 5 CARACTERES ******")
                opcao = input("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar cadastro) \n\nEscolha uma opção: ")
                if (opcao == "2"):
                    return
                print("\n")
        return nome
    
    def cadastrar_descricao(self):
        while(True):
            descricao = input("Descrição: ")
            if len(descricao) >= 10:
                break
            else:
                if len(descricao) < 10:
                    print("\n**** DESCRIÇÃO DEVE TER PELO MENOS 5 CARACTERES ***")
                opcao = input("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar cadastro) \n\nEscolha uma opção: ")
                if (opcao == "2"):
                    return
                print("\n")
        return descricao
    
    def cadastrar_carga_horaria(self):
        while(True):
            carga_horaria = input("Carga Horária: ")
            if carga_horaria.isdigit():
                if int(carga_horaria) >= 1:
                    break
            else:
                if not carga_horaria.isdigit():
                    print("\n********** CARGA HORÁRIA DEVE SER UM NÚMERO ********")
                elif int(carga_horaria) < 1:
                    print("\n******* CARGA HORÁRIA DEVE SER MAIOR QUE ZERO ******")
                opcao = input("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar cadastro) \n\nEscolha uma opção: ")
                if (opcao == "2"):
                    return
                print("\n")
        return int(carga_horaria)
    
    def cadastrar_min_semestres(self):
        while(True):
            min_semestres = input("Mínimo de Semestres: ")
            if min_semestres.isdigit():
                if int(min_semestres) >= 1:
                    break
            else:
                if not min_semestres.isdigit():
                    print("\n******* MÍNIMO DE SEMESTRES DEVE SER UM NÚMERO *****")
                elif int(min_semestres) < 1:
                    print("\n**** MÍNIMO DE SEMESTRES DEVE SER MAIOR QUE ZERO ***")
                opcao = input("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar cadastro) \n\nEscolha uma opção: ")
                if (opcao == "2"):
                    return
                print("\n")
        return int(min_semestres)
    
    def cadastrar_max_semestres(self):
        while(True):
            max_semestres = input("Máximo de Semestres: ")
            if max_semestres.isdigit():
                if int(max_semestres) >= 1:
                    break
            else:
                if not max_semestres.isdigit():
                    print("\n******* MÁXIMO DE SEMESTRES DEVE SER UM NÚMERO *****")
                elif int(max_semestres) < 1:
                    print("\n**** MÁXIMO DE SEMESTRES DEVE SER MAIOR QUE ZERO ***")
                opcao = input("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar cadastro) \n\nEscolha uma opção: ")
                if (opcao == "2"):
                    return
                print("\n")
        return int(max_semestres)
    
    def cadastrar_mensalidade(self):
        while(True):
            mensalidade = input("Mensalidade: ")
            if bool(re.fullmatch(r"\d+([.,]\d+)?", mensalidade)):
                if float(mensalidade) >= 0:
                    break
            else:
                if not bool(re.fullmatch(r"\d+([.,]\d+)?", mensalidade)):
                    print("\n*********** MENSALIDADE DEVE SER UM NÚMERO *********")
                elif float(mensalidade) < 0:
                    print("\n******** MENSALIDADE DEVE SER MAIOR QUE ZERO *******")
                opcao = input("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar cadastro) \n\nEscolha uma opção: ")
                if (opcao == "2"):
                    return
                print("\n")
        return float(mensalidade)