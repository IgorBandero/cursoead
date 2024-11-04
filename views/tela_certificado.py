from datetime import datetime
class TelaCertificado():

    def mostrar_menu_opcoes(self):
        while(True):
            print("\n------------------- CERTIFICADOS -------------------")
            print("Escolha a opção:")
            print("----------------------------------------------------")
            print("1 - Emitir Certificado")
            print("2 - Editar Certificado")
            print("3 - Excluir Certificado")
            print("4 - Listar Certificados Emitidos")
            print("0 - Voltar ")
            print("----------------------------------------------------")
            opcao = input("Escolha a opção: ")
            if opcao in ["1", "2", "3", "4", "0"]:
                return int(opcao)
            else:
                print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")

    def editar_certificado(self):
        print("\n--------------- ATRIBUTOS PARA EDITAR --------------")
        print("1 - DATA EMISSÃO")
        print("----------------------------------------------------")
        while(True):
            opcao = input("\nEscolha uma opção: ")
            if (opcao == "1"):
                print("\nInforme a nova data de emissão...")
                data_emissao = self.cadastrar_data("Data de emissão (DD/MM/AAAA): ")
                return [int(opcao), data_emissao]
            else:
                print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")

    def excluir_certificado(self):
        while(True):
            print(f"\nConfirma a exclusão do certificado? \n1 – SIM \n2 – NÃO (Cancelar)")
            excluir = input("\nEscolha a opção: ")
            if (excluir == "1"):
                return True
            elif (excluir == "2"):
                return False
            else:
                print("\n******** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... ********")

    def selecionar_certificado(self, num_opcoes):
        if (num_opcoes == 0):
            return
        while(True):
            indice_certificado = int(input("\nInforme o número da opção do certificado que deseja selecionar: "))
            if 1 <= indice_certificado < num_opcoes+1 :
                return indice_certificado - 1
            else:
                print("Opção inválida. Por favor, digite o número da opção de certificado desejada.")

    def mostrar_opcao_certificado(self, certificado):
        print(certificado["indice"]+1, " - Aluno(a): ", certificado["aluno"], " | Curso: ", certificado["curso"], " | MÉDIA FINAL: ", certificado["nota_final"], " | DATA DE EMISSÃO: ", certificado["data_emissao"].strftime("%d/%m/%Y"))

    def mostrar_certificado(self, certificado):
        print("\n----------------------------------------------------")
        print("ALUNO: ", certificado["aluno"])
        print("CPF: ", certificado["cpf"])
        print("CURSO: ", certificado["curso"])
        print("CARGA HORÁRIA: ", certificado["carga_horaria"])
        print("MÉDIA FINAL: ", certificado["nota_final"])
        if (certificado["data_emissao"] is not None):
            print("DATA DE EMISSÃO: ", certificado["data_emissao"].strftime("%d/%m/%Y"))
        print("\n")

    def mostrar_mensagem(self, msg):
        print(msg)

    def continuar(self, mensagem):
        while(True):
            print("\n----------------------------------------------------")
            print(mensagem)
            opcao = input("\nEscolha a opção: ")
            if (opcao == "1"):
                return True
            elif (opcao == "2"):
                return False
            else:
                print("\n******** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... ********")

    def cadastrar_data(self, mensagem):
        while(True):
            data = input(mensagem)
            try:
                data_valida = datetime.strptime(data, "%d/%m/%Y")
                return data_valida
            except ValueError:
                print("\nFormato de data inválido! Use DD/MM/AAAA...")