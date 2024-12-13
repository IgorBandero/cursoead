from models.Modulo import Modulo
from views.tela_modulo import TelaModulo
from exceptions.ModulosExceptions import CodigoModuloJaRegistradoException, ListaModulosVaziaException, EdicaoModuloException, ModuloNaoEncontradoException, ModuloInvalidoException, ModuloJaCadastradoNoCurso
from daos.modulo_dao import ModuloDAO

class ControladorModulo:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_modulo = TelaModulo()
        self.__modulo_DAO = ModuloDAO()

    def cadastrar_modulo(self):
        try:
            dados_modulo = self.__tela_modulo.pega_dados_modulo()
            if dados_modulo:
                if self.buscar_modulo_por_codigo(dados_modulo["codigo"]) is None:
                    novo_modulo = Modulo(dados_modulo["codigo"], dados_modulo["nome"], dados_modulo["area"], dados_modulo["carga_horaria"])
                    self.__modulo_DAO.add(novo_modulo)
                    self.__tela_modulo.mostrar_mensagem("Módulo cadastrado com sucesso!")
                else:
                    raise CodigoModuloJaRegistradoException
            else:
                raise ModuloInvalidoException
        except Exception as e:
            self.__tela_modulo.mostrar_mensagem(str(e))

    def editar_modulo(self):
        try:
            if(len(self.__modulo_DAO.get_all()) == 0):
                raise ListaModulosVaziaException
            modulo = self.selecionar_modulo("Selecione um módulo para editar:")
            if modulo is not None:
                modulo_atualizado = self.__tela_modulo.editar_modulo({"codigo": modulo.codigo, "nome": modulo.nome, "area": modulo.area, "carga_horaria": modulo.carga_horaria})
                if modulo_atualizado:
                    if modulo.codigo != modulo_atualizado["codigo"]:
                        try:
                            if self.buscar_modulo_por_codigo(modulo_atualizado["codigo"]) is not None:
                                raise CodigoModuloJaRegistradoException
                            self.__modulo_DAO.remove(modulo.codigo)
                            modulo_novo = Modulo(modulo_atualizado["codigo"], modulo_atualizado["nome"], modulo_atualizado["area"], modulo_atualizado["carga_horaria"])
                            self.__modulo_DAO.add(modulo_novo)
                        except CodigoModuloJaRegistradoException as e:
                            self.__tela_modulo.mostrar_mensagem(str(e))
                    else:
                        for item in self.__modulo_DAO.get_all():
                            if(item.codigo == modulo_atualizado["codigo"]):
                                item.nome = modulo_atualizado["nome"]
                                item.area = modulo_atualizado["area"]
                                item.carga_horaria = modulo_atualizado["carga_horaria"]
                                self.__modulo_DAO.update(item)
                    self.__tela_modulo.mostrar_mensagem(f"Módulo {modulo.nome} atualizado com sucesso!\n")
            else:
                raise EdicaoModuloException
        except Exception as e:
            self.__tela_modulo.mostrar_mensagem(str(e))
        self.abrir_tela()

    def excluir_modulo(self):
        try:
            if(len(self.__modulo_DAO.get_all()) == 0):
                    raise ListaModulosVaziaException
            modulo = self.selecionar_modulo("Selecione um módulo para excluir:")
            if(modulo is not None):
                excluir = self.__tela_modulo.excluir_modulo({"nome": modulo.nome})
                if (excluir):
                    self.__modulo_DAO.remove(modulo.codigo)
                    self.__tela_modulo.mostrar_mensagem(f"Módulo: {modulo.nome} foi removido da lista de módulos\n")
                else:
                    self.__tela_modulo.mostrar_mensagem("EXCLUSÃO CANCELADA!\n")
        except Exception as e:
            self.__tela_modulo.mostrar_mensagem(str(e))
        self.abrir_tela()

        self.listar_modulos()
        indice_modulo = self.__tela_modulo.selecionar_modulo_na_lista(len(self.__modulos))
        if indice_modulo is not None:
            modulo = self.__modulos.pop(indice_modulo)
            self.__tela_modulo.mostrar_mensagem(f"Módulo {modulo.nome} excluído com sucesso!")
        else:
            self.__tela_modulo.mostrar_mensagem("Erro: Módulo não encontrado.")

    def listar_modulos(self):
        try:
            if(len(self.__modulo_DAO.get_all()) == 0):
                raise ListaModulosVaziaException
            lista_modulos = []
            for modulo in self.__modulo_DAO.get_all():
                lista_modulos.append({"codigo": modulo.codigo, "nome": modulo.nome, "carga_horaria": modulo.carga_horaria})
            modulo = self.__tela_modulo.listar_modulos(lista_modulos)
            self.abrir_tela()
        except Exception as e:
            self.abrir_tela()
            self.__tela_modulo.mostrar_mensagem(str(e))

    def buscar_modulo_por_codigo(self, codigo):
        for modulo in self.__modulo_DAO.get_all():
            if modulo.codigo == codigo:
                return modulo
        return None

    def selecionar_modulos(self, mensagem):
        if(len(self.__modulo_DAO.get_all()) == 0):
            raise ListaModulosVaziaException
        lista_modulos_disponiveis = []
        lista_modulos_escolhidos = []
        for modulo in self.__modulo_DAO.get_all():
                lista_modulos_disponiveis.append({"codigo": modulo.codigo, "nome": modulo.nome, "carga_horaria": modulo.carga_horaria})
        while True:
            try:
                codigo_modulo = self.__tela_modulo.selecionar_modulo_na_lista(lista_modulos_disponiveis, mensagem)
                modulo = self.buscar_modulo_por_codigo(codigo_modulo)
                if modulo is not None:
                    if modulo not in lista_modulos_escolhidos:
                        lista_modulos_escolhidos.append(modulo)
                    else:
                        raise ModuloJaCadastradoNoCurso
                else:
                    raise ModuloNaoEncontradoException
                continuar = self.__tela_modulo.continuar_registro_modulos()
                if not continuar:
                    return lista_modulos_escolhidos
            except Exception as e:
                self.__tela_modulo.mostrar_mensagem(str(e))

            """if tipo_consulta == "Buscar pelo codigo":
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
        return lista_modulos """

    def selecionar_modulo_pelo_codigo(self):
        codigo = self.__tela_modulo.buscar_modulo_pelo_codigo()
        return self.buscar_modulo_por_codigo(codigo)

    def selecionar_modulo(self, mensagem):
        try:
            if(len(self.__modulo_DAO.get_all()) == 0):
                raise ListaModulosVaziaException
            lista_modulos = []
            for modulo in self.__modulo_DAO.get_all():
                lista_modulos.append({"codigo": modulo.codigo, "nome": modulo.nome})
            codigo_modulo_escolhido = self.__tela_modulo.selecionar_modulo_na_lista(lista_modulos, mensagem)
            if (codigo_modulo_escolhido is not None):
                try:
                    modulo = self.__modulo_DAO.get(codigo_modulo_escolhido)
                    return modulo
                except ModuloNaoEncontradoException:
                    return
        except Exception as e:
            self.abrir_tela()
            self.__tela_modulo.mostrar_mensagem(str(e))

    def avaliar_modulos(self):
        modulo = self.selecionar_modulo("Selecione o módulo para avaliar:")
        if modulo is not None:
            nota = self.__tela_modulo.avaliar_modulos({"nome": modulo.nome})
            if nota is not None:
                for item in self.__modulo_DAO.get_all():
                    if(item.codigo == modulo.codigo):
                        item.adicionar_avaliacao(nota)
                        self.__modulo_DAO.update(item)
                self.__tela_modulo.mostrar_mensagem(f"Módulo {modulo.nome} avaliado com sucesso!\n")

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
