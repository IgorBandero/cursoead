from models.questao import Questao
from models.atividadeavaliativa import AtividadeAvaliativa
from views.TelaAtividadeAvaliativa import TelaAtividadeAvaliativa
from controllers.controlador_questao import ControladorQuestao

class ControladorAtividadeAvaliativa:
    def __init__(self, controlador_questao, controlador_aluno):
        self.__atividades = []
        self.__tela_atividade = TelaAtividadeAvaliativa()
        self.__controlador_questao = controlador_questao
        self.__controlador_aluno = controlador_aluno  # Atribui o controlador de alunos
        self.__id_atual = 1
        self.__notas_atividade = {}  # Inicializa o dicionário para armazenar as notas

    def gerar_id(self):
        """Gera um ID único para cada nova atividade e incrementa o contador."""
        id_gerado = self.__id_atual
        self.__id_atual += 1
        return id_gerado

    def adicionar_atividade(self):
        dados_atividade = self.__tela_atividade.pega_dados_atividade()
        nota_maxima = dados_atividade["nota_maxima"]
        quantidade_questoes = dados_atividade["quantidade_questoes"]

        questoes = self.selecionar_questoes_existentes(quantidade_questoes)

        if questoes:
            id_atividade = self.gerar_id()
            atividade = AtividadeAvaliativa(id_atividade, questoes, nota_maxima)
            self.__atividades.append(atividade)
            self.__tela_atividade.mostra_mensagem("Atividade Avaliativa adicionada com sucesso!")
        else:
            self.__tela_atividade.mostra_mensagem("Nenhuma questão foi adicionada à atividade.")

    def adicionar_nota_para_aluno(self):
        dados_nota = self.__tela_atividade.pega_dados_nota()
        if not dados_nota:
            return

        atividade = self.buscar_atividade_por_id(dados_nota["atividade_id"])
        aluno = self.__controlador_aluno.buscar_aluno_pelo_cpf(dados_nota["aluno_cpf"])

        if atividade and aluno:
            if dados_nota["nota"] <= atividade.nota_maxima:
                if atividade.id not in self.__notas_atividade:
                    self.__notas_atividade[atividade.id] = {}

                self.__notas_atividade[atividade.id][aluno.cpf] = dados_nota["nota"]
                self.__tela_atividade.mostra_mensagem("Nota adicionada com sucesso!")
            else:
                self.__tela_atividade.mostra_mensagem("Nota excede a nota máxima da atividade.")
        else:
            self.__tela_atividade.mostra_mensagem("Atividade ou Aluno não encontrados.")
    
    def gerar_relatorio_atividade(self):
        id_atividade = self.__tela_atividade.seleciona_atividade()
        atividade = self.buscar_atividade_por_id(id_atividade)
        
        if atividade:
            notas = list(self.__notas_atividade.get(id_atividade, {}).values())
            if notas:
                dados_relatorio = {
                    "nota_maxima": max(notas),
                    "nota_minima": min(notas),
                    "quantidade_alunos": len(notas),
                    "nota_media": sum(notas) / len(notas)
                }
            else:
                dados_relatorio = {
                    "nota_maxima": 0,
                    "nota_minima": 0,
                    "quantidade_alunos": 0,
                    "nota_media": 0
                }
            self.__tela_atividade.mostrar_relatorio(dados_relatorio)
        else:
            self.__tela_atividade.mostra_mensagem("Atividade não encontrada.")

    def buscar_atividade_por_id(self, atividade_id):
        for atividade in self.__atividades:
            if atividade.id == atividade_id:
                return atividade
        return None

    def selecionar_questoes_existentes(self, quantidade):
        questoes_selecionadas = []

        # Obter as questões do controlador de questões
        questoes_existentes = self.__controlador_questao.listar_questoes_disponiveis()

        if questoes_existentes:
            while len(questoes_selecionadas) < quantidade:
                try:
                    id_questao = int(input("Informe o ID da questão para adicionar à atividade (0 para finalizar): "))
                    if id_questao == 0:
                        break  
                    questao_selecionada = self.__controlador_questao.pega_questao_por_id(id_questao)
                    if questao_selecionada:
                        questoes_selecionadas.append(questao_selecionada)
                        print(f"Questão {id_questao} adicionada.")
                    else:
                        print("Questão não encontrada.")
                except ValueError:
                    print("ID inválido. Tente novamente.")
        else:
            self.__tela_atividade.mostra_mensagem("Nenhuma questão disponível para seleção.")
        
        return questoes_selecionadas

    def listar_atividades(self):
        if not self.__atividades:
            self.__tela_atividade.mostra_mensagem("Nenhuma atividade avaliativa cadastrada.")
        else:
            for atividade in self.__atividades:
                dados_atividade = {
                    "id": atividade.id,  
                    "nota_maxima": atividade.nota_maxima,
                    "questoes": [
                        {
                            "enunciado": questao.enunciado,
                            "alternativas": questao.alternativas,
                            "respostas_corretas": questao.respostas_corretas  # Exibe como lista completa
                        }
                        for questao in atividade.questoes
                    ]
                }
                self.__tela_atividade.mostra_atividade(dados_atividade)

    def remover_atividade(self):
        self.listar_atividades()
        id_atividade = self.__tela_atividade.seleciona_atividade()
        
        atividade_para_remover = next((a for a in self.__atividades if a.id == id_atividade), None)
        
        if atividade_para_remover:
            self.__atividades.remove(atividade_para_remover)
            self.__tela_atividade.mostra_mensagem("Atividade Avaliativa removida com sucesso!")
        else:
            self.__tela_atividade.mostra_mensagem("ID de atividade inválido.")

    def mostrar_menu(self):
        lista_opcoes = {
            1: self.adicionar_atividade,
            2: self.remover_atividade,
            3: self.listar_atividades,
            4: self.adicionar_nota_para_aluno,
            5: self.gerar_relatorio_atividade
        }
        
        while True:
            opcao = self.__tela_atividade.mostrar_menu_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            
            if funcao_escolhida:
                funcao_escolhida()
            elif opcao == 0:
                self.__tela_atividade.mostra_mensagem("Voltando...")
                break
            else:
                self.__tela_atividade.mostra_mensagem("Opção inválida.")
