from models.orientacao import Orientacao
from views.tela_orientacao import TelaOrientacao
from models.aluno import Aluno
from models.professor import Professor
class ControladorOrientacao:
    def __init__(self, controlador_sistema):
        self.__orientacoes = []
        self.__tela_orientacao = TelaOrientacao()
        self.__controlador_sistema = controlador_sistema

    def buscar_orientacao_por_aluno(self, cpf_aluno):
        for orientacao in self.__orientacoes:
            if orientacao.aluno.cpf == cpf_aluno:
                return orientacao
        return None

    def cadastrar_orientacao(self):
        dados_orientacao = self.__tela_orientacao.pega_dados_orientacao()
        
        try:
            cpf_aluno = int(dados_orientacao["cpf_aluno"])
            cpf_professor = int(dados_orientacao["cpf_professor"])
        except ValueError:
            self.__tela_orientacao.mostra_mensagem("Erro: CPF do aluno e do professor devem ser números inteiros.")
            return

        # Verifica se aluno e professor existem
        aluno = self.__controlador_sistema.controlador_alunos.buscar_aluno_pelo_cpf(cpf_aluno)
        professor = self.__controlador_sistema.controlador_professores.buscar_professor_por_cpf(cpf_professor)
        
        if isinstance(aluno, Aluno) and isinstance(professor, Professor):
            # Verifica se já existe uma orientação para esse aluno com esse professor
            for orientacao in self.__orientacoes:
                if orientacao.aluno.cpf == cpf_aluno and orientacao.professor.cpf == cpf_professor:
                    self.__tela_orientacao.mostra_mensagem("Erro: Orientação já cadastrada para este aluno e professor.")
                    return
            
            # Cadastra nova orientação
            orientacao = Orientacao(aluno, professor)
            self.__orientacoes.append(orientacao)
            self.__tela_orientacao.mostra_mensagem("Orientação cadastrada com sucesso!")
        else:
            self.__tela_orientacao.mostra_mensagem("Erro: Aluno ou Professor não encontrados.")


    def listar_orientacoes(self):
        if not self.__orientacoes:
            self.__tela_orientacao.mostra_mensagem("Nenhuma orientação cadastrada.")
        else:
            for orientacao in self.__orientacoes:
                self.__tela_orientacao.mostrar_orientacao({
                    "nome_aluno": orientacao.aluno.nome,
                    "cpf_aluno": orientacao.aluno.cpf,
                    "nome_professor": orientacao.professor.nome,
                    "cpf_professor": orientacao.professor.cpf
                })

    def editar_orientacao(self):
        cpf_aluno = self.__tela_orientacao.pegar_cpf_aluno()
        orientacao = self.buscar_orientacao_por_cpf_aluno(cpf_aluno)

        if orientacao:
            while True:
                print("\nEscolha o que deseja editar para a orientação:")
                print("1 - Alterar Orientador")
                print("2 - Alterar Orientando (Aluno)")
                print("0 - Voltar")

                opcao = int(input("Escolha uma opção: "))

                if opcao == 1:
                    # Alterar orientador
                    cpf_novo_professor = self.__tela_orientacao.pegar_cpf_professor()
                    novo_professor = self.__controlador_sistema.controlador_professor.buscar_professor_por_cpf(cpf_novo_professor)
                    if novo_professor:
                        orientacao.professor = novo_professor
                        self.__tela_orientacao.mostra_mensagem("Orientador alterado com sucesso!")
                    else:
                        self.__tela_orientacao.mostra_mensagem("Erro: Professor não encontrado.")

                elif opcao == 2:
                    # Alterar orientando (aluno)
                    cpf_novo_aluno = self.__tela_orientacao.pegar_cpf_aluno()
                    novo_aluno = self.__controlador_sistema.controlador_alunos.buscar_aluno_pelo_cpf(cpf_novo_aluno)
                    if novo_aluno:
                        orientacao.aluno = novo_aluno
                        self.__tela_orientacao.mostra_mensagem("Orientando (Aluno) alterado com sucesso!")
                    else:
                        self.__tela_orientacao.mostra_mensagem("Erro: Aluno não encontrado.")

                elif opcao == 0:
                    # Voltar
                    break
                else:
                    self.__tela_orientacao.mostra_mensagem("Opção inválida. Tente novamente.")
        else:
            self.__tela_orientacao.mostra_mensagem("Erro: Orientação não encontrada para este aluno.")


    def excluir_orientacao(self):
        cpf_aluno = self.__tela_orientacao.seleciona_orientacao()
        orientacao = self.buscar_orientacao_por_aluno(cpf_aluno)
        
        if orientacao:
            self.__orientacoes.remove(orientacao)
            self.__tela_orientacao.mostra_mensagem("Orientação excluída com sucesso!")
        else:
            self.__tela_orientacao.mostra_mensagem("Orientação não encontrada.")

    def listar_orientandos_do_professor(self):
        cpf_professor = self.__tela_orientacao.pegar_cpf_professor()
        orientacoes_do_professor = [o for o in self.__orientacoes if o.professor.cpf == cpf_professor]
        
        if orientacoes_do_professor:
            self.__tela_orientacao.mostra_mensagem(f"Orientandos do Professor (CPF {cpf_professor}):")
            for orientacao in orientacoes_do_professor:
                self.__tela_orientacao.mostra_orientando(orientacao.aluno.nome, orientacao.aluno.cpf)
        else:
            self.__tela_orientacao.mostra_mensagem("Nenhum orientando encontrado para este professor.")

    def buscar_orientador_do_aluno(self):
        # Solicita o CPF do aluno na interface de usuário
        cpf_aluno = self.__tela_orientacao.pegar_cpf_aluno()  # Método para capturar o CPF do aluno
        if cpf_aluno:
            # Busca o orientador com o CPF fornecido
            orientador = self.buscar_orientador_do_aluno(cpf_aluno)
            if orientador:
                # Mostra o orientador encontrado
                self.__tela_orientacao.mostrar_orientador(orientador)
            else:
                self.__tela_orientacao.mostra_mensagem("Orientador não encontrado para o aluno.")
        else:
            self.__tela_orientacao.mostra_mensagem("CPF inválido.")


    def mostrar_orientador_do_aluno(self, cpf_aluno):
        orientador = self.buscar_orientador_do_aluno(cpf_aluno)
        if orientador:
            self.__tela_orientacao.mostrar_orientador(orientador.nome, orientador.cpf)
        else:
            self.__tela_orientacao.mostra_mensagem("Orientação não encontrada para este aluno.")

    def buscar_orientacao_por_cpf_aluno(self, cpf_aluno):
        for orientacao in self.__orientacoes:
            if orientacao.aluno.cpf == cpf_aluno:
                return orientacao
        return None

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

    def abre_tela(self):
        opcoes = {
            1: self.cadastrar_orientacao,
            2: self.listar_orientacoes,
            3: self.editar_orientacao,
            4: self.excluir_orientacao,
            5: self.listar_orientandos_do_professor,
            6: self.buscar_orientador_do_aluno
        }

        while True:
            opcao = self.__tela_orientacao.mostrar_menu_opcoes()
            funcao_escolhida = opcoes.get(opcao)
            
            if funcao_escolhida:
                funcao_escolhida()
            elif opcao == 0:
                self.voltar()
                break
            else:
                self.__tela_orientacao.mostra_mensagem("Opção inválida. Tente novamente.")

