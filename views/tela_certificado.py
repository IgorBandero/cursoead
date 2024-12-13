from datetime import datetime
import PySimpleGUI as sg
from exceptions.OpcaoInvalidaException import OpcaoInvalidaException
class TelaCertificado():

    def __init__(self):
        self.__window = None
        self.mostrar_menu_opcoes()

    def mostrar_menu_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("------------------- Certificados -------------------", font=("Helvica", 25), pad=((0, 0), (10, 15)))],
            [sg.Text("Escolha sua opção: ", font=("Helvica", 14), pad=((5, 0), (0, 10)))],
            [sg.Radio("Emitir Certificado", "RD1", key="1")],
            [sg.Radio("Editar Certificado", "RD1", key="2")],
            [sg.Radio("Excluir Certificado", "RD1", key="3")],
            [sg.Radio("Listar Certificados Emitidos", "RD1", key="4")],
            [sg.Radio("Voltar", "RD1", key="0")],
            [sg.Button("Confirmar", size=(8, 1), pad=((10, 0), (20, 20))), sg.Cancel("Cancelar", size=(8, 1), pad=((15, 0), (20, 20)))]
        ]
        self.__window = sg.Window("Sistema de Certificados").Layout(layout)

    def menu_opcoes(self):
        while(True):
            self.mostrar_menu_opcoes()
            button, values = self.__window.Read()
            opcao = 0
            try:
                if values["0"] or button in (None, "Cancelar"):
                    opcao = 0
                elif values["1"]:
                    opcao = 1
                elif values["2"]:
                    opcao = 2
                elif values["3"]:
                    opcao = 3
                elif values['4']:
                    opcao = 4
                else:
                    raise OpcaoInvalidaException
                self.close()
                return opcao
            except OpcaoInvalidaException as e:
                self.mostrar_mensagem(str(e))
                self.close()

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

    def listar_certificados(self, certificados):
        lista_certificados = [f"{i + 1}. ALUNO: {certificado["aluno"]} / CURSO: {certificado["curso"]} / NOTA FINAL: {certificado["nota_final"]})" for i, certificado in enumerate(certificados)]
        layout = [
            [sg.Text("Lista de Certificados", font=("Helvetica", 14), pad=((0, 0), (10, 10)))],
            [sg.Listbox(values=lista_certificados, size=(70, 10), key="certificado_selecionado", enable_events=False, font=("Helvetica", 10), pad=((5, 0), (5, 0)))],
            [sg.Button("Voltar", size=(10, 1), pad=((5, 0), (15, 15)))]
        ]
        self.__window = sg.Window("Lista Certificados", layout)
        while True:
            button, values = self.open()
            if button in (None, "Voltar"):
                self.close()
                break

    def selecionar_certificado_na_lista(self, lista_certificados, mensagem):
        nomes_certificados = [certificado["nome"] for certificado in lista_certificados]
        layout = [
            [sg.Text(mensagem, font=("Helvetica", 14), pad=((0, 0), (10, 10)))],
            [sg.Listbox(nomes_certificados, size=(70, 10), key="nome_certificado_selecionado", enable_events=True)],
            [sg.Button("Confirmar", size=(8, 1), pad=((5, 0), (15, 15))), sg.Button("Cancelar", size=(8, 1), pad=((15, 0), (15, 15)))]
        ]
        self.__window = sg.Window('Selecionar Certificado').Layout(layout)
        while(True):
            try:
                button, values = self.open()
                if button == None or button == "Cancelar":
                    self.close()
                    return None
                if button == "Confirmar":
                    certificado_selecionado = values["nome_certificado_selecionado"]
                    if certificado_selecionado:
                        self.close()
                        return certificado_selecionado[0]
                    else:
                        raise OpcaoInvalidaException
            except OpcaoInvalidaException as e:
                self.mostrar_mensagem(str(e))

    """def selecionar_certificado(self, num_opcoes):
        if (num_opcoes == 0):
            return
        while(True):
            indice_certificado = int(input("\nInforme o número da opção do certificado que deseja selecionar: "))
            if 1 <= indice_certificado < num_opcoes+1 :
                return indice_certificado - 1
            else:
                print("Opção inválida. Por favor, digite o número da opção de certificado desejada.") """

    def mostrar_opcao_certificado(self, certificado):
        print(certificado["indice"]+1, " - Aluno(a): ", certificado["aluno"], " | Curso: ", certificado["curso"], " | MÉDIA FINAL: ", certificado["nota_final"], " | DATA DE EMISSÃO: ", certificado["data_emissao"].strftime("%d/%m/%Y"))

    def mostrar_certificado(self, certificado):
        layout = [
            [sg.Text("Informações do Certificado", font=("Helvetica", 16), pad=((0, 0), (10, 20)))],
            [sg.Text(f"ALUNO: {certificado['aluno']}", font=("Helvetica", 12))],
            [sg.Text(f"CPF: {certificado['cpf']}", font=("Helvetica", 12))],
            [sg.Text(f"CURSO: {certificado['curso']}", font=("Helvetica", 12))],
            [sg.Text(f"CARGA HORÁRIA: {certificado['carga_horaria']} horas", font=("Helvetica", 12))],
            [sg.Text(f"MÉDIA FINAL: {certificado['nota_final']:.2f}", font=("Helvetica", 12))],
            [sg.Text(f"DATA DE EMISSÃO: {certificado['data_emissao'].strftime('%d/%m/%Y') if certificado['data_emissao'] else 'N/A'}", font=("Helvetica", 12))],
            [sg.Button("Voltar", size=(10, 1), pad=((5, 0), (20, 10)))]
        ]
        self.__window = sg.Window("Detalhes do Certificado", layout, size=(500, 350))
        while True:
            button, values = self.open()
            if button in (None, "Voltar"):
                self.close()
                break
        self.close()

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

    def mostrar_mensagem(self, mensagem: str):
        sg.Popup("Alerta!", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def voltar(self):
        self.__controlador_sistema.abrir_tela()