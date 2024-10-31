from models.questao import Questao
from models.atividadeavaliativa import AtividadeAvaliativa 
from views.TelaAtividadeAvaliativa import TelaAtividadeAvaliativa
from controllers.controlador_questao import ControladorQuestao

class ControladorAtividadeAvaliativa:
    def __init__(self, controlador_questao):
        self.__atividades = []
        self.__tela_atividade = TelaAtividadeAvaliativa()
        self.__controlador_questao = controlador_questao  # Referência ao controlador de questões
        self.__id_atual = 1  # Inicializa o ID único para as atividades

    def gerar_id(self):
        """Gera um ID único para cada nova atividade e incrementa o contador."""
        id_gerado = self.__id_atual
        self.__id_atual += 1
        return id_gerado

    def adicionar_atividade(self):
        dados_atividade = self.__tela_atividade.pega_dados_atividade()
        nota_maxima = dados_atividade["nota_maxima"]
        quantidade_questoes = dados_atividade["quantidade_questoes"]
        
        # Passe a quantidade de questões desejada para o método de seleção
        questoes = self.selecionar_questoes_existentes(quantidade_questoes)

        if questoes:
            # Gera um ID para a nova atividade e cria o objeto `AtividadeAvaliativa`
            id_atividade = self.gerar_id()
            atividade = AtividadeAvaliativa(id_atividade, questoes, nota_maxima)
            self.__atividades.append(atividade)
            self.__tela_atividade.mostra_mensagem("Atividade Avaliativa adicionada com sucesso!")
        else:
            self.__tela_atividade.mostra_mensagem("Nenhuma questão foi adicionada à atividade.")

    def selecionar_questoes_existentes(self, quantidade):
        questoes_selecionadas = []

        # Lista as questões existentes para o usuário
        questoes_existentes = self.__controlador_questao.listar_questoes_disponiveis()

        if questoes_existentes:
            while len(questoes_selecionadas) < quantidade:
                try:
                    id_questao = int(input("Informe o ID da questão para adicionar à atividade (0 para finalizar): "))
                    if id_questao == 0:
                        break  # Permite ao usuário finalizar antes de atingir a quantidade desejada
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
                            "respostas_corretas": questao.respostas_corretas
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
            3: self.listar_atividades
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
                self.__tela_atividade.mostra_mensagem("Opção inválida. Tente novamente.")


