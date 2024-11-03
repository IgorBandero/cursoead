from models.Modulo import Modulo
from views.tela_modulo import TelaModulo

class ControladorModulo:
    def __init__(self, controlador_sistema):
        self.__modulos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_modulo = TelaModulo()

        modulo1 = Modulo("INE5610", "Introdução à Informática", "Informática", 100)
        modulo2 = Modulo("INE5620", "Organização de Computadores", "Informática", 100)
        modulo3 = Modulo("INE5630", "Circuitos Digitais", "Informática", 100)
        modulo4 = Modulo("EGC5010", "Teoria Geral de Sistemas", "Gestão do Conhecimento", 100)
        modulo5 = Modulo("EGC5020", "Marketing Pessoal e Empreendedorismo", "Gestão do Conhecimento", 100)
        modulo6 = Modulo("EGC5030", "Administração I", "Gestão do Conhecimento", 100)
        self.__modulos.append(modulo1)
        self.__modulos.append(modulo2)
        self.__modulos.append(modulo3)
        self.__modulos.append(modulo4)
        self.__modulos.append(modulo5)
        self.__modulos.append(modulo6)
        
    def cadastrar_modulo(self):
        dados_modulo = self.__tela_modulo.pega_dados_modulo()
        modulo_existente = self.buscar_modulo_por_codigo(dados_modulo["codigo"])

        if modulo_existente is None:
            novo_modulo = Modulo(dados_modulo["codigo"], dados_modulo["nome"], dados_modulo["area"], dados_modulo["carga_horaria"])
            self.__modulos.append(novo_modulo)
            self.__tela_modulo.mostrar_mensagem("Módulo cadastrado com sucesso!")
        else:
            self.__tela_modulo.mostrar_mensagem("Erro: Módulo com este código já cadastrado.")

    def editar_modulo(self):
        self.listar_modulos()
        indice_modulo = self.__tela_modulo.selecionar_modulo(len(self.__modulos))
        if indice_modulo is not None:
            modulo = self.__modulos[indice_modulo]
            dados_modulo = self.__tela_modulo.pega_dados_modulo()
            
            modulo.codigo = dados_modulo["codigo"]
            modulo.nome = dados_modulo["nome"]
            modulo.area = dados_modulo["area"]
            modulo.carga_horaria = dados_modulo["carga_horaria"]

            self.__tela_modulo.mostrar_mensagem("Módulo editado com sucesso!")
        else:
            self.__tela_modulo.mostrar_mensagem("Erro: Módulo não encontrado.")

    def excluir_modulo(self):
        self.listar_modulos()
        indice_modulo = self.__tela_modulo.selecionar_modulo(len(self.__modulos))
        if indice_modulo is not None:
            modulo = self.__modulos.pop(indice_modulo)
            self.__tela_modulo.mostrar_mensagem(f"Módulo {modulo.nome} excluído com sucesso!")
        else:
            self.__tela_modulo.mostrar_mensagem("Erro: Módulo não encontrado.")

    def listar_modulos(self):
        if not self.__modulos:
            self.__tela_modulo.mostrar_mensagem("Nenhum módulo cadastrado.")
        else:
            self.__tela_modulo.listar_modulos(self.__modulos)

    def buscar_modulo_por_codigo(self, codigo):
        for modulo in self.__modulos:
            if modulo.codigo == codigo:
                return modulo
        return None

    def abrir_tela(self):
        opcoes = {
            1: self.cadastrar_modulo,
            2: self.editar_modulo,
            3: self.excluir_modulo,
            4: self.listar_modulos
        }

        while True:
            opcao = self.__tela_modulo.mostrar_menu_opcoes()
            funcao_escolhida = opcoes.get(opcao)

            if funcao_escolhida:
                funcao_escolhida()
            elif opcao == 0:
                break
            else:
                self.__tela_modulo.mostrar_mensagem("Opção inválida. Tente novamente.")

    def selecionar_modulos(self):
        exit = False
        lista_modulos = []
        while(not exit):
            print("\nSelecione o módulo:")
            self.listar_modulos()
            indice_modulo_escolhido = self.__tela_modulo.selecionar_modulo(len(self.__modulos))
            if (indice_modulo_escolhido is not None):
                modulo = self.__modulos[indice_modulo_escolhido]
                if(modulo is not None):
                    lista_modulos.append(modulo)
                else:
                    self.__tela_modulo.mostrar_mensagem("********* ATENÇÃO: Módulo não encontrado! *********")
            opcao = int(input("\nCadastrar outro módulo? \n1 - Sim \n2 - Não"))
            if opcao == 2:
                exit = True
        return lista_modulos

