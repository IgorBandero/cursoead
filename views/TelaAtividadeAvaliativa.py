class TelaAtividadeAvaliativa:
    def mostrar_menu_opcoes(self):
        print("-------- MENU ATIVIDADES AVALIATIVAS --------")
        print("1. Adicionar Atividade Avaliativa")
        print("2. Remover Atividade Avaliativa")
        print("3. Listar Atividades Avaliativas")
        print("4. Adicionar Nota a Aluno")
        print("5. Gerar Relatório de Desempenho")
        print("0. Voltar")
        
        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4, 5]:
                    return opcao
                else:
                    print("\n***** OPÇÃO INVÁLIDA! TENTE NOVAMENTE... *****")
            except ValueError:
                print("\n***** OPÇÃO INVÁLIDA! DIGITE UM NÚMERO INTEIRO *****")

    def pega_dados_atividade(self):
        while True:
            try:
                nota_maxima = float(input("Nota Máxima da Atividade: "))
                if nota_maxima > 0:
                    break
                else:
                    print("Nota máxima deve ser um valor positivo.")
            except ValueError:
                print("Nota máxima inválida. Deve ser um número.")
        
        while True:
            try:
                quantidade_questoes = int(input("Quantas questões deseja adicionar à atividade? "))
                if quantidade_questoes > 0:
                    break
                else:
                    print("A quantidade de questões deve ser um número positivo.")
            except ValueError:
                print("Quantidade de questões inválida. Deve ser um número inteiro.")
        
        return {"nota_maxima": nota_maxima, "quantidade_questoes": quantidade_questoes}
    
    def pega_dados_nota(self):
        while True:
            try:
                atividade_id = int(input("ID da Atividade: "))
                break
            except ValueError:
                print("ID da atividade inválido. Deve ser um número inteiro.")
        
        while True:
            try:
                aluno_cpf = int(input("CPF do Aluno: "))
                if len(str(aluno_cpf)) == 11:
                    break
                else:
                    print("CPF deve conter 11 dígitos.")
            except ValueError:
                print("CPF inválido. Deve ser um número.")
        
        while True:
            try:
                nota = float(input("Nota do Aluno: "))
                return {"atividade_id": atividade_id, "aluno_cpf": aluno_cpf, "nota": nota}
            except ValueError:
                print("Nota inválida. Deve ser um número.")
    
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
            print("  Resposta Correta:", ", ".join(questao["respostas_corretas"]))  # Exibe como string completa
            print(' ')
        print("\n")

    def mostra_mensagem(self, msg):
        print(msg)

    def seleciona_atividade(self):
        while True:
            try:
                id_atividade = int(input("ID da atividade que deseja selecionar: "))
                return id_atividade
            except ValueError:
                print("ID inválido. Deve ser um número inteiro.")




