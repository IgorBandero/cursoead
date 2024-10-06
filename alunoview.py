class AlunoView:

    def mostrar_menu_opcoes(self):
        print("1. Incluir Aluno")
        print("2. Atualizar Estado do Aluno")
        print("3. Atualizar Orientador")
        print("4. Registrar Módulo Atual")
        print("5. Remover Módulo Atual")
        print("6. Registrar Módulo Finalizado")
        print("7. Remover Módulo Finalizado")
        print("8. Registrar Certificado")
        print("9. Exibir Detalhes do Aluno")
        print("10. Exibir Módulos Atuais")
        print("11. Exibir Módulos Finalizados")
        print("12. Exibir Certificados")
        print("13. Exibir Progresso do Aluno")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        return int(opcao)

    def mostrar_detalhes_do_aluno(self, aluno):
        print(f"Detalhes do Aluno:")
        print(f"Nome: {aluno.nome}")
        print(f"CPF: {aluno.cpf}")
        print(f"Curso: {aluno.matricula.curso.nome}")
        print(f"Progresso: {aluno.estado_aluno.progresso}%")
        print("-----------------------------")

    def mostrar_mensagem(self, mensagem: str):
        print(f"Mensagem: {mensagem}")

    def escolher_orientador(self, orientadores):
        """
        Permite ao usuário escolher um orientador existente de uma lista fornecida.
        """
        print("Escolha um dos orientadores disponíveis:")
        for i, orientador in enumerate(orientadores):
            print(f"{i + 1}. {orientador.nome}")

        escolha = int(input("Digite o número do orientador escolhido: ")) - 1
        return orientadores[escolha] if 0 <= escolha < len(orientadores) else None

    def escolher_modulo(self, modulos):
        """
        Permite ao usuário escolher um módulo existente de uma lista fornecida.
        """
        print("Escolha um dos módulos disponíveis:")
        for i, modulo in enumerate(modulos):
            print(f"{i + 1}. {modulo.nome}")

        escolha = int(input("Digite o número do módulo escolhido: ")) - 1
        return modulos[escolha] if 0 <= escolha < len(modulos) else None

    def escolher_certificado(self, certificados):
        """
        Permite ao usuário escolher um certificado existente de uma lista fornecida.
        """
        print("Escolha um dos certificados disponíveis:")
        for i, certificado in enumerate(certificados):
            print(f"{i + 1}. {certificado.nome}")

        escolha = int(input("Digite o número do certificado escolhido: ")) - 1
        return certificados[escolha] if 0 <= escolha < len(certificados) else None

    def mostrar_detalhes_do_aluno(self, aluno: Aluno):
        print(f"Detalhes do Aluno:")
        print(f"Nome: {aluno.nome}")
        print(f"CPF: {aluno.cpf}")
        print(f"Telefone: {aluno.telefone}")
        print(f"Email: {aluno.email}")
        print(f"Curso: {aluno.matricula.curso.nome}")
        print(f"Estado atual: {aluno.estado_aluno}")
        print(f"Progresso: {aluno.estado_aluno.progresso}%")

    def mostrar_mensagem(self, mensagem: str):
        print(f"Mensagem: {mensagem}")