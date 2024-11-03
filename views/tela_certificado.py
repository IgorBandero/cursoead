class TelaCertificado():

    def mostrar_menu_opcoes(self):
        print("\n---------------- CERTIFICADOS ----------------")
        print("Escolha a opção:")
        print("1 - Emitir Certificado")
        print("2 - Editar Certificado")
        print("3 - Excluir Certificado")
        print("4 - Listar Certificados Emitidos")
        print("0 - Voltar ")
        opcao = int(input("Escolha a opção: "))
        return opcao

    def emitir_certificado(self):
        pass

    def excluir_certificado(self, num_opcoes):
        if (num_opcoes == 0):
            return
        while(True):
            indice_certificado = int(input("\nInforme o número da opção do certificado que deseja excluir: "))
            if 1 <= indice_certificado < num_opcoes+1 :
                return indice_certificado - 1
            else:
                print("Opção inválida. Por favor, digite o número da opção de certificado desejada.")

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
        print(certificado["indice"]+1, " - Aluno: ", certificado["aluno"], " | Curso: ", certificado["curso"])

    def mostrar_certificado(self, certificado):
        print("\n-----------------------------------------------")
        print("ALUNO: ", certificado["aluno"])
        print("CPF: ", certificado["cpf"])
        print("CURSO: ", certificado["curso"])
        print("CARGA HORÁRIA: ", certificado["carga_horaria"])
        print("MÉDIA FINAL: ", certificado["nota_final"])
        print("DATA DE EMISSÃO: ", certificado["data_emissao"])
        print("\n")

    def mostrar_mensagem(self, msg):
        print(msg)