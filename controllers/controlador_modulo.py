from models.Modulo import Modulo
from views.tela_modulo import TelaModulo

class ControladorModulo:
    def __init__(self, controlador_sistema):
        self.__modulos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_modulo = TelaModulo()

    def cadastrar_modulo(self):
        dados_modulo = self.__tela_modulo.pega_dados_modulo()
        if self.buscar_modulo_por_codigo(dados_modulo["codigo"]) is None:
            novo_modulo = Modulo(dados_modulo["codigo"], dados_modulo["nome"], dados_modulo["area"], dados_modulo["carga_horaria"])
            self.__modulos.append(novo_modulo)
            self.__tela_modulo.mostrar_mensagem("Módulo cadastrado com sucesso!")
        else:
            self.__tela_modulo.mostrar_mensagem("Erro: Módulo com este código já cadastrado.")

    def editar_modulo(self):
        self.listar_modulos()
        indice_modulo = self.__tela_modulo.selecionar_modulo_na_lista(len(self.__modulos))
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
        indice_modulo = self.__tela_modulo.selecionar_modulo_na_lista(len(self.__modulos))
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

    def selecionar_modulos(self):
        lista_modulos = []
        while True:
            self.__tela_modulo.mostrar_mensagem("\n----------------- SELECIONAR MÓDULO ----------------")
            tipo_consulta = self.__tela_modulo.selecionar_modulo(len(self.__modulos))
            if tipo_consulta == "Buscar pelo codigo":
                modulo = self.selecionar_modulo_pelo_codigo()
                if modulo and modulo not in lista_modulos:
                    self.__tela_modulo.mostrar_mensagem(f"\nCÓDIGO: {modulo.codigo} | NOME: {modulo.nome} | ÁREA: {modulo.area} | CARGA HORÁRIA: {modulo.carga_horaria}")
                    lista_modulos.append(modulo)
                else:
                    self.__tela_modulo.mostrar_mensagem("\nMódulo já selecionado ou não encontrado.")
            elif tipo_consulta == "Selecionar da lista":
                self.listar_modulos()
                indice_modulo_escolhido = self.__tela_modulo.selecionar_modulo_na_lista(len(self.__modulos))
                modulo = self.__modulos[indice_modulo_escolhido]
                if modulo and modulo not in lista_modulos:
                    self.__tela_modulo.mostrar_mensagem(f"\nCÓDIGO: {modulo.codigo} | NOME: {modulo.nome} | ÁREA: {modulo.area} | CARGA HORÁRIA: {modulo.carga_horaria}")
                    lista_modulos.append(modulo)
                else:
                    self.__tela_modulo.mostrar_mensagem("\nMódulo já selecionado ou não encontrado.")
            if not self.__tela_modulo.continuar_registro_modulos():
                break
        return lista_modulos

    def selecionar_modulo_pelo_codigo(self):
        codigo = self.__tela_modulo.buscar_modulo_pelo_codigo()
        return self.buscar_modulo_por_codigo(codigo)

    def avaliar_modulos(self):
        modulos = self.selecionar_modulos()
        if modulos is not None:
            for modulo in modulos:
                nota = self.__tela_modulo.avaliar_modulos({"modulo": modulo.nome})
                if nota is not None:
                    modulo.adicionar_avaliacao(nota)

    def abrir_tela(self):
        opcoes = {
            1: self.cadastrar_modulo,
            2: self.editar_modulo,
            3: self.excluir_modulo,
            4: self.listar_modulos,
            5: self.avaliar_modulos,
            0: self.voltar
        }
        while True:
            opcao = self.__tela_modulo.mostrar_menu_opcoes()
            funcao_escolhida = opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_modulo.mostrar_mensagem("Opção inválida.")

    def voltar(self):
        self.__controlador_sistema.abrir_tela()
