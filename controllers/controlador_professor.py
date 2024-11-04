from models.professor import Professor
from views.tela_professor import TelaProfessor
from exceptions.ListaProfessoresVaziaException import ListaProfessoresVaziaException
from exceptions.ProfessorNaoEncontradoException import ProfessorNaoEncontradoException
from exceptions.ProfessorJaRegistradoException import ProfessorJaRegistradoException


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
            raise ProfessorJaRegistradoException

    def listar_professores(self):
        if not self.__professores:
            raise ListaProfessoresVaziaException
        else:
            for professor in self.__professores:
                dados_professor = {
                    "nome": professor.nome,
                    "cpf": professor.cpf,
                    "especialidade": professor.especialidade,
                    "formacao": professor.formacao,
                    "telefone": professor.telefone,
                    "email": professor.email,
                    "usuario": professor.usuario,
                    "rua": professor.endereco.rua,
                    "num_residencia": professor.endereco.num_residencia,
                    "bairro": professor.endereco.bairro,
                    "cidade": professor.endereco.cidade,
                    "cep": professor.endereco.cep
                }
                self.__tela_professor.mostrar_professor(dados_professor)

    def buscar_professor_por_cpf(self, cpf: int):
        for professor in self.__professores:
            if professor.cpf == cpf:  
                return professor
        return None
    
    def selecionar_professor(self):
        cpf = self.__tela_professor.seleciona_professor()
        professor = self.buscar_professor_por_cpf(cpf)
        if professor:
            return professor
        else:
            raise ProfessorNaoEncontradoException

    def editar_professor(self):
        professor = self.selecionar_professor()
        if professor:
            self.__tela_professor.mostrar_professor({
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
            while True:
                campo, info_atualizada = self.__tela_professor.editar_professor()
                if info_atualizada is not None:
                    if campo == 1:
                        professor.nome = info_atualizada
                    elif campo == 2:
                        professor.cpf = info_atualizada
                    elif campo == 3:
                        professor.telefone = info_atualizada
                    elif campo == 4:
                        professor.email = info_atualizada
                    elif campo == 5:
                        professor.usuario = info_atualizada
                    elif campo == 6:
                        professor.senha = info_atualizada
                    elif campo == 7:
                        professor.formacao = info_atualizada
                    elif campo == 8:
                        professor.especialidade = info_atualizada
                    elif campo == 9:
                        professor.endereco.rua = info_atualizada
                    elif campo == 10:
                        professor.endereco.num_residencia = info_atualizada
                    elif campo == 11:
                        professor.endereco.bairro = info_atualizada
                    elif campo == 12:
                        professor.endereco.cidade = info_atualizada
                    elif campo == 13:
                        professor.endereco.cep = info_atualizada
                continuar = self.__tela_professor.continuar_edicao()
                if not continuar:
                    break

    def remover_professor(self):
        cpf = self.__tela_professor.seleciona_professor()
        professor = self.buscar_professor_por_cpf(cpf)
        if professor:
            self.__professores.remove(professor)
            self.__tela_professor.mostra_mensagem("Professor removido com sucesso!")
        else:
            raise ProfessorNaoEncontradoException

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

