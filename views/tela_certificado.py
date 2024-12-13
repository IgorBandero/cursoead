from datetime import datetime
import PySimpleGUI as sg
import re
from exceptions.OpcaoInvalidaException import OpcaoInvalidaException
from exceptions.CertificadoExceptions import EdicaoCertificadoException
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

    def editar_certificado(self, certificado):
        layout = [
            [sg.Text("----------------- Editar Certificado -----------------", font=("Helvica", 20), pad=((0, 0), (0, 10)))],
            [sg.Text("Aluno:", size=(17, 1)), sg.Input(default_text=certificado["aluno"], key="aluno")],
            [sg.Text("Curso:", size=(17, 1)), sg.Input(default_text=certificado["curso"], key="curso")],
            [sg.Text("Nota Final:", size=(17, 1)), sg.Input(default_text=certificado["nota_final"], key="nota_final")],
            [sg.Text("Data da Emissão (DD/MM/AAAA):", size=(17, 1)), sg.Input(default_text=certificado["data_emissao"].strftime("%d/%m/%Y"), key="data_emissao")],
            [sg.Button("Confirmar", size=(15, 1), pad=((5, 0), (20, 20))), sg.Button("Cancelar", size=(15, 1), pad=((15, 0), (20, 20)))]
        ]
        self.__window = sg.Window("Editar Certificado").Layout(layout)

        while True:
            button, values = self.open()
            if button == None or button == "Cancelar":
                self.close()
                return None
            elif button == "Confirmar":
                try:
                    if not self.aluno_valido(values["nome"]):
                        raise ValueError("Nome do aluno inválido! \nNome deve ser um texto com mais de 5 caracteres")
                    if not self.curso_valido(values["curso"]):
                        raise ValueError("Nome do curso inválido! \nNome deve ser um texto com mais de 5 caracteres")
                    if not self.nota_valida(values["nota_final"]):
                        raise ValueError("Nota final inválida! \nNota deve ser um número entre 0 e 10")
                    data = self.data_valida(values["data_emissao"])
                    if data is None:
                        raise ValueError("Formato da data de emissão inválida! Use DD/MM/AAAA...\n")
                    else:
                        data_emissao = data

                    certificado_atualizado = {
                        "aluno": values["aluno"],
                        "curso": values["curso"],
                        "nota_final": float(values["nota_final"]),
                        "data_emissao": data_emissao
                    }
                    if certificado_atualizado:
                        self.close()
                        return certificado_atualizado
                    else:
                        self.close()
                        raise EdicaoCertificadoException
                except Exception as e:
                    self.mostrar_mensagem(str(e))

    def aluno_valido(self, aluno):
        return len(aluno) > 5

    def curso_valido(self, curso):
        return len(curso) > 5

    def nota_valida(self, nota):
        if re.fullmatch(r"\d+([.,]\d+)?", nota):
            nota = float(nota.replace(",", "."))
            if 0.00 <= nota <= 10.00:
                return True
        return False

    def data_valida(self, data):
        try:
            data_valida = datetime.strptime(data, "%d/%m/%Y")
            return data_valida
        except ValueError:
            return None


    def excluir_certificado(self, certificado):
        layout = [
            [sg.Text(f"Confirma a exclusão do CERTIFICADO de: {certificado["aluno"]}?", font=("Helvetica", 14))],
            [sg.Button("SIM", size=(10, 1), pad=((5, 0), (10, 10))), sg.Button("NÃO", size=(10, 1), pad=((10, 0), (10, 10)))]
        ]
        self.__window = sg.Window("Confirmar Exclusão").Layout(layout)

        while True:
            button, values = self.open()
            self.close()
            if button == None:
                return False
            elif button == "SIM":
                return True
            elif button == "NÃO":
                return False

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
        print("ENTROU NA TELA")
        nomes_certificados = [certificado["aluno"] for certificado in lista_certificados]
        layout = [
            [sg.Text(mensagem, font=("Helvetica", 14), pad=((0, 0), (10, 10)))],
            [sg.Listbox(nomes_certificados, size=(70, 10), key="titular_certificado_selecionado", enable_events=True)],
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
                    dono_certificado_selecionado = values["titular_certificado_selecionado"]
                    print(dono_certificado_selecionado)
                    if dono_certificado_selecionado:
                        self.close()
                        return dono_certificado_selecionado[0]
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