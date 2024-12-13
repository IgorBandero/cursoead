from models.professor import Professor
from views.tela_professor import TelaProfessor
from exceptions.ListaProfessoresVaziaException import ListaProfessoresVaziaException
from exceptions.ProfessorNaoEncontradoException import ProfessorNaoEncontradoException
from exceptions.ProfessorJaRegistradoException import ProfessorJaRegistradoException
from daos.professor_dao import ProfessorDAO  # DAO importado

class ControladorProfessor:
    def __init__(self, controlador_sistema):
        self.__professor_dao = ProfessorDAO()  # Usando o DAO para persistência
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema

    def cadastrar_professor(self):
        try:
            dados_professor = self.__tela_professor.pega_dados_professor()
            if dados_professor:
                if not self.buscar_professor_por_cpf(dados_professor["cpf"]):
                    professor = Professor(**dados_professor)
                    self.__professor_dao.add(professor)  # Persistindo com o DAO
                    self.__tela_professor.mostra_mensagem("Professor cadastrado com sucesso!")
                else:
                    raise ProfessorJaRegistradoException
        except ProfessorJaRegistradoException as e:
            self.__tela_professor.mostra_mensagem(str(e))

    def listar_professores(self):
        try:
            professores = self.__professor_dao.get_all()  # Recupera todos do DAO
            if not professores:
                raise ListaProfessoresVaziaException
            lista_dados_professores = [
                {
                    "nome": professor.nome,
                    "cpf": professor.cpf,
                    "telefone": professor.telefone,
                    "email": professor.email,
                    "usuario": professor.usuario,
                    "formacao": professor.formacao,
                    "especialidade": professor.especialidade,
                    "rua": professor.endereco.rua,
                    "num_residencia": professor.endereco.num_residencia,
                    "bairro": professor.endereco.bairro,
                    "cidade": professor.endereco.cidade,
                    "cep": professor.endereco.cep
                }
                for professor in professores
            ]
            self.__tela_professor.listar_professores(lista_dados_professores)
        except ListaProfessoresVaziaException as e:
            self.__tela_professor.mostra_mensagem(str(e))

    def buscar_professor_por_cpf(self, cpf: int):
        return self.__professor_dao.get(cpf)  # Busca no DAO

    def selecionar_professor(self):
        try:
            professores = [{"nome": prof.nome, "cpf": prof.cpf} for prof in self.__professor_dao.get_all()]
            if not professores:
                raise ListaProfessoresVaziaException
            cpf = self.__tela_professor.seleciona_professor(professores)
            professor = self.buscar_professor_por_cpf(cpf)
            if professor:
                return professor
            else:
                raise ProfessorNaoEncontradoException
        except ListaProfessoresVaziaException as e:
            self.__tela_professor.mostra_mensagem(str(e))
        except ProfessorNaoEncontradoException as e:
            self.__tela_professor.mostra_mensagem(str(e))
        return None

    def editar_professor(self):
        professor = self.selecionar_professor()
        if professor:
            dados_atualizados = self.__tela_professor.editar_professor({
                "nome": professor.nome,
                "cpf": professor.cpf,
                "telefone": professor.telefone,
                "email": professor.email,
                "usuario": professor.usuario,
                "formacao": professor.formacao,
                "especialidade": professor.especialidade,
                "rua": professor.endereco.rua,
                "num_residencia": professor.endereco.num_residencia,
                "bairro": professor.endereco.bairro,
                "cidade": professor.endereco.cidade,
                "cep": professor.endereco.cep
            })
            if dados_atualizados:
                professor.nome = dados_atualizados["nome"]
                professor.telefone = dados_atualizados["telefone"]
                professor.email = dados_atualizados["email"]
                professor.usuario = dados_atualizados["usuario"]
                professor.senha = dados_atualizados["senha"] if dados_atualizados["senha"] else professor.senha
                professor.formacao = dados_atualizados["formacao"]
                professor.especialidade = dados_atualizados["especialidade"]
                professor.endereco.rua = dados_atualizados["rua"]
                professor.endereco.num_residencia = int(dados_atualizados["num_residencia"])
                professor.endereco.bairro = dados_atualizados["bairro"]
                professor.endereco.cidade = dados_atualizados["cidade"]
                professor.endereco.cep = dados_atualizados["cep"]
                self.__professor_dao.update(professor)  # Atualiza no DAO
                self.__tela_professor.mostra_mensagem("Dados do professor atualizados com sucesso!")

    def remover_professor(self):
        professor = self.selecionar_professor()
        if professor:
            confirmacao = self.__tela_professor.excluir_professor({"nome": professor.nome, "cpf": professor.cpf})
            if confirmacao:
                self.__professor_dao.remove(professor.cpf)  # Remove no DAO
                self.__tela_professor.mostra_mensagem("Professor removido com sucesso!")

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {
            1: self.cadastrar_professor,
            2: self.editar_professor,
            3: self.remover_professor,
            4: self.listar_professores
        }

        while True:
            opcao = self.__tela_professor.mostrar_menu_opcoes()
            if opcao == 0:
                self.voltar()
                break
            funcao_escolhida = opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_professor.mostra_mensagem("Opção inválida.")

    def listar_todos_professores(self):
        return self.__professor_dao.get_all()  # Retorna todos do DAO