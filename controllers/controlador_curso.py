from views.tela_curso import TelaCurso
from views.tela_modulo import TelaModulo
from models.curso import Curso
from exceptions.ModulosExceptions import ListaModulosVaziaException
from exceptions.CursoExceptions import ListaCursosVaziaException, CursoJaRegistradoException, CursoInvalidoException, NomeCursoJaRegistradoException, CursoNaoEncontradoException, EdicaoCursoException
from daos.curso_dao import CursoDAO
class ControladorCurso():

    def __init__(self, controlador_sistema, controlador_modulo):
        self.__tela_curso = TelaCurso()
        self.__tela_modulo = TelaModulo()
        self.__controlador_modulo = controlador_modulo
        self.__controlador_sistema = controlador_sistema
        self.__curso_DAO = CursoDAO()

    def cadastrar_curso(self):
        try:
            num_modulos_disponiveis = len(self.__controlador_modulo._ControladorModulo__modulos)
            if (num_modulos_disponiveis == 0):
                raise ListaModulosVaziaException
            curso = self.__tela_curso.cadastrar_curso()
            if (curso is not None):
                modulos = self.__controlador_modulo.selecionar_modulos()
                if (modulos is not None):
                    curso_cadastrado = self.buscar_curso_pelo_nome(curso["nome"])
                    if curso_cadastrado is None:
                        novo_curso = Curso(curso["nome"], curso["descricao"], curso["carga_horaria"], curso["min_semestres"], curso["max_semestres"], curso["mensalidade"], modulos)
                        self.__curso_DAO.add(novo_curso)
                        self.__tela_curso.mostrar_mensagem(f"Curso: {novo_curso.nome} cadastrado com sucesso!\n")
                    else:
                        raise CursoJaRegistradoException
                else:
                    raise CursoInvalidoException
            else:
                raise CursoInvalidoException
        except Exception as e:
            self.__tela_curso.mostrar_mensagem(str(e))
        self.abrir_tela()

    def editar_curso(self):
        try:
            if(len(self.__curso_DAO.get_all()) == 0):
                raise ListaCursosVaziaException
            curso = self.selecionar_curso("Selecione um curso para editar:")
            if(curso is not None):
                curso_atualizado = self.__tela_curso.editar_curso({"nome": curso.nome, "descricao": curso.descricao, "carga_horaria": curso.carga_horaria,
                                                    "min_semestres": curso.min_semestres, "max_semestres": curso.max_semestres, "mensalidade": curso.mensalidade})
                if curso_atualizado:
                    if curso.nome != curso_atualizado["nome"]:
                        self.__curso_DAO.remove(curso.nome)
                        curso_novo = Curso(curso_atualizado["nome"], curso_atualizado["descricao"], curso_atualizado["carga_horaria"],
                                        curso_atualizado["min_semestres"], curso_atualizado["max_semestres"], curso_atualizado["mensalidade"],
                                        curso.modulos)
                        self.__curso_DAO.add(curso_novo)
                    else:
                        for item in self.__curso_DAO.get_all():
                            if(item.nome == curso.nome):
                                item.nome = curso_atualizado["nome"]
                                item.descricao = curso_atualizado["descricao"]
                                item.carga_horaria = curso_atualizado["carga_horaria"]
                                item.min_semestres = curso_atualizado["min_semestres"]
                                item.max_semestres = curso_atualizado["max_semestres"]
                                item.mensalidade = curso_atualizado["mensalidade"]
                                self.__curso_DAO.update(item)
                    self.__tela_curso.mostrar_mensagem(f"Curso {curso.nome} atualizado com sucesso!\n")
        except Exception as e:
            self.__tela_curso.mostrar_mensagem(str(e))
        self.abrir_tela()

    def excluir_curso(self):
        try:
            if(len(self.__curso_DAO.get_all()) == 0):
                    raise ListaCursosVaziaException
            curso = self.selecionar_curso("Selecione um curso para excluir:")
            if(curso is not None):
                excluir = self.__tela_curso.excluir_curso({"nome": curso.nome})
                if (excluir):
                    self.__curso_DAO.remove(curso.nome)
                    self.__tela_curso.mostrar_mensagem(f"Curso: {curso.nome} foi removido da lista de cursos da universidade\n")
                else:
                    self.__tela_curso.mostrar_mensagem("EXCLUSÃO CANCELADA!\n")
        except Exception as e:
            self.__tela_curso.mostrar_mensagem(str(e))
        self.abrir_tela()

    def selecionar_curso(self, mensagem):
        try:
            if(len(self.__curso_DAO.get_all()) == 0):
                raise ListaCursosVaziaException
            lista_cursos = []
            for curso in self.__curso_DAO.get_all():
                lista_cursos.append({"nome": curso.nome})
            nome_curso_escolhido = self.__tela_curso.selecionar_curso_na_lista(lista_cursos, mensagem)
            if (nome_curso_escolhido is not None):
                try:
                    curso = self.__curso_DAO.get(nome_curso_escolhido)
                    return curso
                except CursoNaoEncontradoException:
                    return
        except Exception as e:
            self.abrir_tela()
            self.__tela_curso.mostrar_mensagem(str(e))

    def listar_cursos(self):
        try:
            if(len(self.__curso_DAO.get_all()) == 0):
                raise ListaCursosVaziaException
            lista_cursos = []
            for curso in self.__curso_DAO.get_all():
                lista_cursos.append({"nome": curso.nome, "carga_horaria": curso.carga_horaria, "mensalidade": curso.mensalidade})
            curso = self.__tela_curso.listar_cursos(lista_cursos)
            self.abrir_tela()
        except Exception as e:
            self.abrir_tela()
            self.__tela_curso.mostrar_mensagem(str(e))

    def buscar_curso_pelo_nome(self, nome):
        for curso in self.__curso_DAO.get_all():
            if curso.nome.upper() == nome.upper():
                return curso
        return None

    def buscar_curso(self):
        try:
            curso = self.selecionar_curso("Selecione um curso para ver os detalhes:")
            if curso is not None:
                self.mostrar_curso(curso)
            else:
                raise CursoNaoEncontradoException
        except Exception as e:
            self.__tela_curso.mostrar_mensagem(str(e))
        self.abrir_tela()

    def mostrar_curso(self, curso):
        self.__tela_curso.mostrar_curso({"nome": curso.nome, "descricao": curso.descricao, "carga_horaria": curso.carga_horaria, "min_semestres": curso.min_semestres, "max_semestres": curso.max_semestres, "mensalidade": curso.mensalidade})
        if len(curso.modulos) > 0:
            self.__tela_curso.mostrar_mensagem("\n--------------- MÓDULOS OBRIGATÓRIOS --------------")
            for modulo in curso.modulos:
                self.__tela_modulo.mostrar_modulo({"codigo": modulo.codigo, "nome": modulo.nome, "area": modulo.area, "carga_horaria": modulo.carga_horaria})

    def cursos_melhor_avaliados(self):
        avaliacoes = [(curso, curso.avaliacao_media_curso()) for curso in self.__curso_DAO.get_all()]
        cursos_ordenados = sorted(avaliacoes, key=lambda x: x[1], reverse=True)
        lista_avaliacoes = []
        for curso, avaliacao in cursos_ordenados:
            lista_avaliacoes.append({"nome": curso.nome, "avaliacao": avaliacao})
        self.__tela_curso.mostrar_avaliacoes(lista_avaliacoes)
        self.abrir_tela()

    def abrir_tela(self):
        opcoes = {
            1: self.cadastrar_curso,
            2: self.editar_curso,
            3: self.excluir_curso,
            4: self.listar_cursos,
            5: self.buscar_curso,
            6: self.cursos_melhor_avaliados,
            0: self.voltar
        }
        opcao_escolhida = self.__tela_curso.menu_opcoes()
        funcao_escolhida = opcoes.get(opcao_escolhida)
        if funcao_escolhida:
            funcao_escolhida()

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

