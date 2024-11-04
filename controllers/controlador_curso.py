from views.tela_curso import TelaCurso
from views.tela_modulo import TelaModulo
from models.curso import Curso
class ControladorCurso():

    def __init__(self, controlador_sistema, controlador_modulo):
        self.__cursos = []
        self.__tela_curso = TelaCurso()
        self.__tela_modulo = TelaModulo()
        self.__controlador_modulo = controlador_modulo
        self.__controlador_sistema = controlador_sistema

    def cadastrar_curso(self):
        num_modulos_disponiveis = len(self.__controlador_modulo._ControladorModulo__modulos)
        if (num_modulos_disponiveis == 0):
            self.__tela_curso.mostrar_mensagem("\n****** NENHUM MÓDULO DISPONÍVEL PARA CURSOS! ******")
            return
        curso = self.__tela_curso.cadastrar_curso()
        if (curso is not None):
            self.__tela_curso.mostrar_mensagem("Módulos: ")
            modulos = self.__controlador_modulo.selecionar_modulos()
            if (modulos is not None):
                curso_cadastrado = self.buscar_curso_pelo_nome(curso["nome"])
                if curso_cadastrado is None:
                    novo_curso = Curso(curso["nome"], curso["descricao"], curso["carga_horaria"], curso["min_semestres"], curso["max_semestres"], curso["mensalidade"], modulos)
                    self.__cursos.append(novo_curso)
                    self.__tela_curso.mostrar_mensagem(f"\nCurso: {self.__cursos[-1].nome} cadastrado com sucesso!")
                else:
                    self.__tela_curso.mostrar_mensagem("********* ATENÇÃO: Curso já cadastrado! *********")
            else:
                self.__tela_curso.mostrar_mensagem("\n*********** ATENÇÃO: Curso inválido! **********")
        else:
            self.__tela_curso.mostrar_mensagem("\n************* ERRO NO CADASTRO DE CURSO ************")

    def editar_curso(self):
        curso = self.selecionar_curso()
        if(curso is not None):
            self.mostrar_curso(curso)
            while(True):
                campo, info_atualizada = self.__tela_curso.editar_curso()
                if info_atualizada is not None:
                    for item in self.__cursos:
                        if(item.nome == curso.nome):
                            if campo == 1:
                                for caso in self.__cursos:
                                    if caso.nome == info_atualizada:
                                        print("\n*********** ERRO: NOME JÁ CADASTRADO! **********")
                                        return
                                item.nome = info_atualizada
                            elif campo == 2:
                                item.descricao = info_atualizada
                            elif campo == 3:
                                item.carga_horaria = info_atualizada
                            elif campo == 4:
                                item.min_semestres = info_atualizada
                            elif campo == 5:
                                item.max_semestres = info_atualizada
                            elif campo == 6:
                                item.mensalidade = info_atualizada
                            self.mostrar_curso(curso)
                else:
                    self.__tela_curso.mostrar_mensagem("\n************* ERRO: Edição não concluída *************")
                continuar = self.__tela_curso.continuar("Deseja editar outro campo? \n1 - SIM \n2 - NÃO (Sair)")
                if not continuar:
                    break

    def excluir_curso(self):
        curso = self.selecionar_curso()
        if(curso is not None):
            excluir = self.__tela_curso.excluir_curso({"nome": curso.nome})
            if (excluir):
                self.__cursos.remove(curso)
                self.__tela_curso.mostrar_mensagem(f"\nCurso: {curso.nome} foi removido da lista de cursos da universidade.")
            else:
                self.__tela_curso.mostrar_mensagem("\n*************** EXCLUSÃO CANCELADA ****************")

    def selecionar_curso(self):
        while (True):
            self.__tela_curso.mostrar_mensagem("\n----------------- SELECIONAR CURSO -----------------")
            tipo_consulta = self.__tela_curso.selecionar_curso(len(self.__cursos))
            if tipo_consulta == "Buscar pelo nome":
                curso = self.selecionar_curso_pelo_nome()
                if(curso is not None):
                    return curso
                else:
                    self.__tela_curso.mostrar_mensagem("\n********** ATENÇÃO: Curso não encontrado! **********")
            elif tipo_consulta == "Selecionar da lista":
                self.listar_cursos()
                indice_curso_escolhido = self.__tela_curso.selecionar_curso_na_lista(len(self.__cursos))
                if (indice_curso_escolhido is not None):
                    curso = self.__cursos[indice_curso_escolhido]
                    if(curso is not None):
                        return curso
                    else:
                        self.__tela_curso.mostrar_mensagem("\n********* ATENÇÃO: Curso não encontrado! *********")
            continuar = self.__tela_curso.continuar("Deseja tentar novamente? \n1 - SIM \n2 - NÃO (Sair)")
            if not continuar:
                break

    def selecionar_curso_pelo_nome(self):
        nome = self.__tela_curso.buscar_curso_pelo_nome()
        if (nome is not None):
            curso = self.buscar_curso_pelo_nome(nome)
            if(curso is not None):
                return curso

    def buscar_curso_pelo_nome(self, nome):
        for curso in self.__cursos:
            if curso.nome.upper() == nome.upper():
                return curso
        return None

    def listar_cursos(self):
        if(len(self.__cursos) == 0):
            self.__tela_curso.mostrar_mensagem("\n****** NENHUM CURSO CADASTRADO ATÉ O MOMENTO! ******")
            return
        print("\n----------------- LISTA DE CURSOS ------------------\n")
        for indice, curso in enumerate(self.__cursos):
            self.__tela_curso.mostrar_opcao_curso({"indice": indice, "nome": curso.nome})

    def buscar_curso(self):
        curso = self.selecionar_curso()
        if curso is not None:
            self.mostrar_curso(curso)

    def mostrar_curso(self, curso):
        self.__tela_curso.mostrar_curso({"nome": curso.nome, "descricao": curso.descricao, "carga_horaria": curso.carga_horaria, "min_semestres": curso.min_semestres, "max_semestres": curso.max_semestres, "mensalidade": curso.mensalidade})
        if len(curso.modulos) > 0:
            self.__tela_curso.mostrar_mensagem("\n--------------- MÓDULOS OBRIGATÓRIOS --------------")
            for modulo in curso.modulos:
                self.__tela_modulo.mostrar_modulo({"codigo": modulo.codigo, "nome": modulo.nome, "area": modulo.area, "carga_horaria": modulo.carga_horaria})

    def cursos_melhor_avaliados(self):
        avaliacoes = [(curso, curso.avaliacao_media_curso()) for curso in self.__cursos]
        cursos_ordenados = sorted(avaliacoes, key=lambda x: x[1], reverse=True)
        for curso, avaliacao in cursos_ordenados:
            self.__tela_curso.mostrar_mensagem(f"CURSO: {curso.nome} | AVALIAÇÃO MÉDIA: {avaliacao}")

    def abrir_tela(self):
        menu_opcoes = {1: self.cadastrar_curso, 2: self.editar_curso, 3: self.excluir_curso, 4: self.listar_cursos, 5: self.buscar_curso, 6: self.cursos_melhor_avaliados, 0: self.voltar}

        while True:
            menu_opcoes[self.__tela_curso.mostrar_menu_opcoes()]()

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

