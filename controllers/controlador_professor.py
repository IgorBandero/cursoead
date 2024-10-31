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
            while True:
                print("\nEscolha o campo que deseja editar:")
                print("1 - Nome")
                print("2 - Telefone")
                print("3 - Email")
                print("4 - Usuário")
                print("5 - Senha")
                print("6 - Formação")
                print("7 - Especialidade")
                print("8 - Rua")
                print("9 - Número da Residência")
                print("10 - Bairro")
                print("11 - Cidade")
                print("12 - CEP")
                print("0 - Finalizar Edição")

                opcao = int(input("Escolha uma opção: "))

                if opcao == 1:
                    professor.nome = input("Novo nome: ")
                elif opcao == 2:
                    professor.telefone = input("Novo telefone: ")
                elif opcao == 3:
                    professor.email = input("Novo email: ")
                elif opcao == 4:
                    professor.usuario = input("Novo usuário: ")
                elif opcao == 5:
                    professor.senha = input("Nova senha: ")
                elif opcao == 6:
                    professor.formacao = input("Nova formação: ")
                elif opcao == 7:
                    professor.especialidade = input("Nova especialidade: ")
                elif opcao == 8:
                    professor.rua = input("Nova rua: ")
                elif opcao == 9:
                    while True:
                        try:
                            professor.num_residencia = int(input("Novo número da residência: "))
                            break
                        except ValueError:
                            print("Número da residência deve ser um valor inteiro. Tente novamente.")
                elif opcao == 10:
                    professor.bairro = input("Novo bairro: ")
                elif opcao == 11:
                    professor.cidade = input("Nova cidade: ")
                elif opcao == 12:
                    professor.cep = input("Novo CEP: ")
                elif opcao == 0:
                    self.__tela_professor.mostra_mensagem("Edição finalizada.")
                    break
                else:
                    self.__tela_professor.mostra_mensagem("Opção inválida. Tente novamente.")
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

