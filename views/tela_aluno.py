from datetime import datetime
from exceptions.OpcaoInvalidaException import OpcaoInvalidaException
from exceptions.CpfInvalidoException import CpfInvalidoException
import re
import PySimpleGUI as sg
class TelaAluno():

    def mostrar_menu_opcoes(self):
        while(True):
            try:
                print("\n---------------------- ALUNOS ----------------------")
                print("Escolha a opção:")
                print("----------------------------------------------------")
                print("1 -  Cadastrar Aluno")
                print("2 -  Editar Aluno")
                print("3 -  Excluir Aluno")
                print("4 -  Listar Alunos")
                print("5 -  Mostrar Aluno")
                print("6 -  Matricular aluno em módulos")
                print("7 -  Lançar notas de aluno")
                print("8 -  Finalizar curso de aluno")
                print("9 -  Relatório de cursos mais populares")
                print("10 - Relatório de tempo médio de conclusão")
                print("0 -  Voltar ")
                print("----------------------------------------------------")
                opcao = input("Escolha a opção: ")
                if (opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4" or opcao == "5" or opcao == "6" or opcao == "7" or opcao == "8" or opcao == "9" or opcao == "10" or opcao == "0"):
                    return int(opcao)
                else:
                    raise OpcaoInvalidaException
            except Exception as e:
                self.mostrar_mensagem(str(e))

    def cadastrar_aluno(self):
        print("\n------------------ DADOS DO ALUNO ------------------")
        nome = self.cadastrar_nome()
        cpf = self.cadastrar_cpf()
        telefone = self.cadastrar_telefone()
        email = self.cadastrar_email()
        usuario = self.cadastrar_usuario()
        senha = self.cadastrar_senha()
        rua = self.cadastrar_rua()
        num_residencia = self.cadastrar_num_residencia()
        bairro = self.cadastrar_bairro()
        cidade = self.cadastrar_cidade()
        cep = self.cadastrar_cep()
        data_inicio = self.cadastrar_data("Data de início (DD/MM/AAAA): ")
        return {
            "nome": nome, "cpf": cpf, "telefone": telefone, "email": email, "usuario": usuario,
            "senha": senha, "rua": rua, "num_residencia": num_residencia, "bairro": bairro,
            "cidade": cidade, "cep": cep, "data_inicio": data_inicio
        }

    def editar_aluno(self):
        print("\n--------------- ATRIBUTOS PARA EDITAR --------------")
        print("1 - NOME")
        print("2 - CPF")
        print("3 - TELEFONE")
        print("4 - EMAIL")
        print("5 - USUÁRIO")
        print("6 - RUA")
        print("7 - NÚMERO DE RESIDÊNCIA")
        print("8 - BAIRRO")
        print("9 - CIDADE")
        print("10 - CEP")
        print("11 - CURSO")
        print("12 - MATRÍCULA")
        print("13 - SENHA")
        print("----------------------------------------------------")
        while(True):
            try:
                opcao = input("\nEscolha uma opção: ")
                if (opcao == "1"):
                    print("\nInforme o novo NOME...")
                    nome = self.cadastrar_nome()
                    return [int(opcao), nome]
                if (opcao == "2"):
                    print("\nInforme o novo CPF...")
                    cpf = self.cadastrar_cpf()
                    return [int(opcao), cpf]
                if (opcao == "3"):
                    print("\nInforme o novo TELEFONE...")
                    telefone = self.cadastrar_telefone()
                    return [int(opcao), telefone]
                if (opcao == "4"):
                    print("\nInforme o novo EMAIL...")
                    email = self.cadastrar_email()
                    return [int(opcao), email]
                if (opcao == "5"):
                    print("\nInforme o novo USUÁRIO...")
                    usuario = self.cadastrar_usuario()
                    return [int(opcao), usuario]
                if (opcao == "6"):
                    print("\nInforme a nova RUA...")
                    rua = self.cadastrar_rua()
                    return [int(opcao), rua]
                if (opcao == "7"):
                    print("\nInforme o novo NÚMERO DE RESIDÊNCIA...")
                    num_residencia = self.cadastrar_num_residencia()
                    return [int(opcao), num_residencia]
                if (opcao == "8"):
                    print("\nInforme o novo BAIRRO...")
                    bairro = self.cadastrar_bairro()
                    return [int(opcao), bairro]
                if (opcao == "9"):
                    print("\nInforme a nova CIDADE...")
                    cidade = self.cadastrar_cidade()
                    return [int(opcao), cidade]
                if (opcao == "10"):
                    print("\nInforme o novo CEP...")
                    cep = self.cadastrar_cep()
                    return [int(opcao), cep]
                if (opcao == "11"):
                    print("\nInforme o novo curso...")
                    return [int(opcao), ""]
                if (opcao == "12"):
                    print("\nInforme o novo CÓDIGO DE MATRÍCULA...")
                    codigo = self.cadastrar_codigo()
                    return [int(opcao), codigo]
                if (opcao == "13"):
                    return [int(opcao), ""]
                else:
                    raise OpcaoInvalidaException
            except Exception as e:
                self.mostrar_mensagem(str(e))


    def excluir_aluno(self, aluno):
        while(True):
            try:
                print(f"\nConfirma a exclusão do(a) ALUNO(A): {aluno['nome']} do CURSO: {aluno['curso']} da lista de alunos da universidade? \n1 – SIM \n2 – NÃO (Cancelar)")
                excluir = input("\nEscolha a opção: ")
                if (excluir == "1"):
                    return True
                elif (excluir == "2"):
                    return False
                else:
                    raise OpcaoInvalidaException
            except Exception as e:
                self.mostrar_mensagem(str(e))

    def mostrar_opcao_aluno(self, aluno):
        print(aluno["indice"]+1, " - NOME: ", aluno["nome"], " | CPF: ", aluno["cpf"], " | MATRÍCULA: ", aluno["matricula"], " | CURSO: ", aluno["curso"])

    def selecionar_aluno(self, num_opcoes):
        if (num_opcoes == 0):
            print("\n************** NENHUM ALUNO CADASTRADO *************")
            return
        while(True):
            try:
                opcao = input("\nComo deseja selecionar o aluno? \n1 - Procurar aluno pelo CPF \n2 - Selecionar da lista de alunos \n\nEscolha uma opção: ")
                if (opcao == "1" or opcao == "2"):
                    break
                else:
                    raise OpcaoInvalidaException
            except Exception as e:
                self.mostrar_mensagem(str(e))
        if (opcao == "1"):
            return "Buscar pelo cpf"
        if (opcao == "2"):
            return "Selecionar da lista"

    def selecionar_aluno_na_lista(self, num_opcoes):
        while(True):
            try:
                indice_aluno = input("\nInforme o número da opção do aluno que deseja selecionar: ")
                if indice_aluno.isdigit():
                    if 1 <= int(indice_aluno) < num_opcoes+1:
                        return int(indice_aluno) - 1
                    else:
                        raise OpcaoInvalidaException
                else:
                    raise OpcaoInvalidaException
            except Exception as e:
                self.mostrar_mensagem(str(e))

    def buscar_aluno_pelo_cpf(self):
        while(True):
            try:
                cpf = input("\nInforme o número do CPF do aluno que deseja selecionar: ")
                if cpf.isdigit() and len(cpf) == 11:
                    return int(cpf)
                else:
                    raise CpfInvalidoException
            except Exception as e:
                self.mostrar_mensagem(str(e))

    def mostrar_aluno(self, aluno):
        print("\n---------------------- ALUNO(A) --------------------")
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
        if (aluno["data_inicio"] is not None):
            print("DATA INÍCIO: ", aluno["data_inicio"].strftime("%d/%m/%Y"))
        if (aluno["data_final"] is not None):
            print("DATA FINAL: ", aluno["data_final"].strftime("%d/%m/%Y"))
        print("CURSO: ", aluno["curso"])
        print("MATRÍCULA: ", aluno["codigo"])

    def mostrar_mensagem(self, msg):
        print(msg)

    def cadastrar_nome(self):
        while(True):
            nome = input("Nome: ")
            if len(nome) >= 3 and all(char.isalpha() or char.isspace() for char in nome):
                break
            else:
                if len(nome) < 3:
                    print("\n******* NOME DEVE TER PELO MENOS 3 CARACTERES ******")
                else:
                    print("\n****** NOME DEVE TER APENAS LETRAS OU ESPAÇOS ******")
                opcao = self.continuar("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar)")
                if (not opcao):
                    return
                print("\n")
        return nome

    def cadastrar_cpf(self):
        while (True):
            cpf = input("CPF: ")
            if len(cpf) >= 11 and cpf.isdigit():
                cpf = int(cpf)
                break
            else:
                if len(cpf) < 11:
                    print("\n******** CPF DEVE TER PELO MENOS 11 DÍGITOS ********")
                else:
                    print("\n************ CPF DEVE TER SOMENTE NÚMEROS **********")
                opcao = self.continuar("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar)")
                if (not opcao):
                    return
                print("\n")
        return cpf

    def cadastrar_telefone(self):
        while(True):
            telefone = input("Telefone: ")
            if len(telefone) >= 8  and telefone.isdigit():
                break
            else:
                if len(telefone) < 8:
                    print("\n****** TELEFONE DEVE TER PELO MENOS 8 DÍGITOS ******")
                else:
                    print("\n********* TELEFONE DEVE TER SOMENTE NÚMEROS ********")
                opcao = self.continuar("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar)")
                if (not opcao):
                    return
                print("\n")
        return telefone
    
    def cadastrar_email(self):
        while(True):
            email = input("E-mail: ")
            if len(email) >= 5 and "@" in email and "." in email:
                break
            else:
                if len(email) < 5:
                    print("\n****** EMAIL DEVE TER PELO MENOS 5 CARACTERES ******")
                else:
                    print("\n******** EMAIL INVÁLIDO! TENTE NOVAMENTE... ********")
                opcao = self.continuar("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar)")
                if (not opcao):
                    return
                print("\n")
        return email
    
    def cadastrar_usuario(self):
        while(True):
            usuario = input("Usuario: ")
            if len(usuario) >= 8:
                break
            else:
                print("\n***** USUÁRIO DEVE TER PELO MENOS 8 CARACTERES ****")
                opcao = self.continuar("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar)")
                if (not opcao):
                    return
                print("\n")
        return usuario
    
    def cadastrar_senha(self):
        while(True):
            senha = input("Senha: ")
            if len(senha) >= 8 and (bool(re.search(r"[a-zA-Z]", senha)) and bool(re.search(r"[0-9]", senha))) :
                break
            else:
                if len(senha) < 8:
                    print("\n***** SENHA DEVE TER PELO MENOS 8 CARACTERES ******")
                else:
                    print("\n********* SENHA DEVE TER NÚMEROS E LETRAS *********")
                opcao = self.continuar("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar)")
                if (not opcao):
                    return
                print("\n")
        return senha
    
    def cadastrar_rua(self):
        while(True):
            rua = input("Rua: ")
            if len(rua) >= 5 and bool(re.search(r"[a-zA-Z]", rua)):
                break
            else:
                if len(rua) < 5:
                    print("\n****** RUA DEVE TER PELO MENOS 5 CARACTERES *******")
                else:
                    print("\n********* RUA INVÁLIDA! TENTE NOVAMENTE... ********")
                opcao = self.continuar("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar)")
                if (not opcao):
                    return
                print("\n")
        return rua
    
    def cadastrar_num_residencia(self):
        while(True):
            num_residencia = input("Número: ")
            if len(num_residencia) >= 1 and num_residencia.isdigit():
                num_residencia = int(num_residencia)
                break
            else:
                if len(num_residencia) < 1:
                    print("\n******* NÚMERO DEVE TER PELO MENOS 1 DÍGITO *******")
                else:
                    print("\n********* NÚMERO DEVE TER SOMENTE NÚMEROS *********")
                opcao = self.continuar("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar)")
                if (not opcao):
                    return
                print("\n")
        return num_residencia
    
    def cadastrar_bairro(self):
        while(True):
            bairro = input("Bairro: ")
            if len(bairro) >= 5 and all(char.isalpha() or char.isspace() for char in bairro):
                break
            else:
                if len(bairro) < 5:
                    print("\n***** BAIRRO DEVE TER PELO MENOS 5 CARACTERES *****")
                else:
                    print("\n******* BAIRRO INVÁLIDO! TENTE NOVAMENTE... *******")
                opcao = self.continuar("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar)")
                if (not opcao):
                    return
                print("\n")
        return bairro
    
    def cadastrar_cidade(self):
        while(True):
            cidade = input("Cidade: ")
            if len(cidade) >= 5 and all(char.isalpha() or char.isspace() for char in cidade):
                break
            else:
                if len(cidade) < 5:
                    print("\n***** CIDADE DEVE TER PELO MENOS 5 CARACTERES *****")
                else:
                    print("\n******* CIDADE INVÁLIDA! TENTE NOVAMENTE... *******")
                opcao = self.continuar("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar)")
                if (not opcao):
                    return
                print("\n")
        return cidade
    
    def cadastrar_codigo(self):
        while (True):
            codigo = input("CÓDIGO DE MATRÍCULA: ")
            if len(codigo) == 11 and codigo.isdigit():
                break
            else:
                if len(codigo) < 11 or len(codigo) > 11:
                    print("\n****** CÓDIGO DE MATRÍCULA DEVE TER 11 DÍGITOS *****")
                else:
                    print("\n********** CÓDIGO DEVE TER SOMENTE NÚMEROS *********")
                opcao = self.continuar("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar)")
                if (not opcao):
                    return
                print("\n")
        return codigo

    def cadastrar_cep(self):
        while(True):
            cep = input("CEP: ")
            if len(cep) >= 8 and cep.isdigit():
                break
            else:
                if len(cep) < 8:
                    print("\n******** CEP DEVE TER PELO MENOS 8 DÍGITOS *********")
                else:
                    print("\n*********** CEP DEVE TER SOMENTE NÚMEROS ***********")
                opcao = self.continuar("\nTENTAR NOVAMENTE? \n1 - SIM \n2 - NÃO (Cancelar)")
                if (not opcao):
                    return
                print("\n")
        return cep
    
    def lancar_nota_modulo(self):
        while(True):
            nota = input("\nInforme a nota do aluno no módulo: ")
            if bool(re.fullmatch(r"\d+([.,]\d+)?", nota)):
                if 0.00 <= float(nota) <= 10.00:
                    return float(nota)
                else:
                    print("\n********* NOTA DEVE SER UM NÚMERO DE 0 A 10 ********")
            else:
                print("\nNOTA INVÁLIDA! Por favor, tente novamente...")

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