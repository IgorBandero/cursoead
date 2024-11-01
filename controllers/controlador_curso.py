from views.tela_curso import TelaCurso
from models.curso import Curso

class ControladorCurso():

    def __init__(self, controlador_sistema):
        self.__cursos = []
        self.__tela_curso = TelaCurso()
        self.__controlador_sistema = controlador_sistema
        
    def cadastrar_curso(self):
        curso = self.__tela_curso.cadastrar_curso()
        curso_cadastrado = self.buscar_curso_pelo_nome(curso["nome"])
        if curso_cadastrado is None:
            novoCurso = Curso(curso["nome"], curso["descricao"], curso["carga_horaria"], curso["min_semestres"], curso["max_semestres"], curso["mensalidade"])
            self.__cursos.append(novoCurso)
            self.__tela_curso.mostrar_mensagem(f"\nCurso: {self.__cursos[-1].nome} cadastrado com sucesso!")
        else:
            self.__tela_curso.mostrar_mensagem("********* ATENÇÃO: Curso já cadastrado! *********")

    def excluir_curso(self):
        curso = self.selecionar_curso()
        if(curso is not None):
                self.__cursos.remove(curso)
                self.__tela_curso.mostrar_mensagem(f"\nCurso: {curso.nome} foi removido da lista de cursos da universidade.")

    def editar_curso(self):
        curso = self.selecionar_curso()
        if(curso is not None):
            for item in self.__cursos:
                if(item.nome == curso.nome):
                    curso_atualizado = self.__tela_curso.editar_curso()
                    item.nome = curso_atualizado["nome"]
                    item.descricao = curso_atualizado["descricao"]
                    item.carga_horaria = curso_atualizado["carga_horaria"]
                    item.min_semestres = curso_atualizado["min_semestres"]
                    item.min_semestres = curso_atualizado["min_semestres"]
                    item.mensalidade = curso_atualizado["mensalidade"]

    def selecionar_curso(self):
        print("\nSelecione o curso:")
        self.listar_cursos()
        indice_curso_escolhido = self.__tela_curso.selecionar_curso(len(self.__cursos))
        if (indice_curso_escolhido is not None):
            curso = self.__cursos[indice_curso_escolhido]
            if(curso is not None):
                return curso
            else:
                self.__tela_curso.mostrar_mensagem("********* ATENÇÃO: Curso não encontrado! *********")

    def listar_cursos(self):
        print("\n")
        if(len(self.__cursos) == 0):
            self.__tela_curso.mostrar_mensagem("******* NENHUM CURSO CADASTRADO ATÉ O MOMENTO! *******")
        for indice, curso in enumerate(self.__cursos):
            self.__tela_curso.mostrar_opcao_curso({"indice": indice, "nome": curso.nome})


    def buscar_curso_pelo_nome(self, nome: str):
        for curso in self.__cursos:
            if(curso.nome == nome):
                return curso
        return None

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        menu_opcoes = {1: self.cadastrar_curso, 2: self.editar_curso, 3: self.excluir_curso, 4: self.listar_cursos, 0: self.voltar}

        while True:
            menu_opcoes[self.__tela_curso.mostrar_menu_opcoes()]()