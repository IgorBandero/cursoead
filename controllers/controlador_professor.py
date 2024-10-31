from models.professor import Professor
from views.tela_professor import TelaProfessor

class ControladorProfessor:
    def __init__(self, controlador_sistema):
        self.__professores = []
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema

    def cadastrar_professor(self):
        dados_professor = self.__tela_professor.pega_dados_professor()
        if not self.buscar_professor_por_cpf(dados_professor["cpf"]):
            professor = Professor(**dados_professor)
            self.__professores.append(professor)
            self.__tela_professor.mostra_mensagem("Professor cadastrado com sucesso!")
        else:
            self.__tela_professor.mostra_mensagem("Professor já cadastrado com este CPF.")

    def listar_professores(self):
        if not self.__professores:
            self.__tela_professor.mostra_mensagem("Nenhum professor cadastrado.")
        else:
            for professor in self.__professores:
                dados_professor = {
                    "nome": professor.nome,
                    "cpf": professor.cpf,
                    "especialidade": professor.especialidade,
                    "formacao": professor.formacao
                }
                self.__tela_professor.mostra_professor(dados_professor)

    def buscar_professor_por_cpf(self, cpf: int):
        for professor in self.__professores:
            if professor.cpf == cpf:  
                return professor
        return None

    def editar_professor(self):
        cpf = self.__tela_professor.seleciona_professor()
        professor = self.buscar_professor_por_cpf(cpf)
        if professor:
            novos_dados = self.__tela_professor.pega_dados_professor()
            professor.nome = novos_dados["nome"]
            professor.telefone = novos_dados["telefone"]
            professor.email = novos_dados["email"]
            professor.usuario = novos_dados["usuario"]
            professor.senha = novos_dados["senha"]
            professor.formacao = novos_dados["formacao"]
            professor.especialidade = novos_dados["especialidade"]
            professor.rua = novos_dados["rua"]
            professor.num_residencia = novos_dados["num_residencia"]
            professor.bairro = novos_dados["bairro"]
            professor.cidade = novos_dados["cidade"]
            professor.cep = novos_dados["cep"]
            self.__tela_professor.mostra_mensagem("Professor editado com sucesso!")
        else:
            self.__tela_professor.mostra_mensagem("Professor não encontrado.")

    def remover_professor(self):
        cpf = self.__tela_professor.seleciona_professor()
        professor = self.buscar_professor_por_cpf(cpf)
        if professor:
            self.__professores.remove(professor)
            self.__tela_professor.mostra_mensagem("Professor removido com sucesso!")
        else:
            self.__tela_professor.mostra_mensagem("Professor não encontrado.")

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {
            1: self.cadastrar_professor,
            2: self.listar_professores,
            3: self.editar_professor,
            4: self.remover_professor
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

