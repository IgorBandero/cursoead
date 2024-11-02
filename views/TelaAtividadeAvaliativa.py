class TelaAtividadeAvaliativa:
    def mostrar_menu_opcoes(self):
        print("-------- MENU ATIVIDADES AVALIATIVAS --------")
        print("1. Adicionar Atividade Avaliativa")
        print("2. Remover Atividade Avaliativa")
        print("3. Listar Atividades Avaliativas")
        print("4. Adicionar Nota a Aluno")
        print("5. Gerar Relatório de Desempenho")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")
        return int(opcao)

    def pega_dados_atividade(self):
        nota_maxima = float(input("Nota Máxima da Atividade: "))
        quantidade_questoes = int(input("Quantas questões deseja adicionar à atividade? "))
        return {"nota_maxima": nota_maxima, "quantidade_questoes": quantidade_questoes}
    
    def pega_dados_nota(self):
        atividade_id = int(input("ID da Atividade: "))
        aluno_cpf = int(input("CPF do Aluno: "))
        try:
            nota = float(input("Nota do Aluno: "))
            return {"atividade_id": atividade_id, "aluno_cpf": aluno_cpf, "nota": nota}
        except ValueError:
            print("Nota inválida. Deve ser um número.")
            return None
    
    def mostrar_relatorio(self, dados_relatorio):
        print("\n--- Relatório de Desempenho da Atividade ---")
        print(f"Nota Máxima: {dados_relatorio['nota_maxima']}")
        print(f"Nota Mínima: {dados_relatorio['nota_minima']}")
        print(f"Quantidade de Alunos: {dados_relatorio['quantidade_alunos']}")
        print(f"Nota Média: {dados_relatorio['nota_media']:.2f}")
        print("\n")

    def mostra_atividade(self, dados_atividade):
        print("-------- ATIVIDADE AVALIATIVA ----------")
        print("ID:", dados_atividade["id"]) 
        print("Nota Máxima:", dados_atividade["nota_maxima"])
        print("Questões:")
        for questao in dados_atividade["questoes"]:
            print("  Enunciado:", questao["enunciado"])
            print("  Alternativas:", ", ".join(questao["alternativas"]))
            print("  Resposta Correta:", ", ".join(questao["respostas_corretas"]))
            print(' ')
        print("\n")

    def mostra_mensagem(self, msg):
        print(msg)

    def seleciona_atividade(self):
        return int(input("ID da atividade que deseja selecionar: "))



