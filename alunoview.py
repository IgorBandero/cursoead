class AlunoView:

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
