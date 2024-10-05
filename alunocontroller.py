class AlunoController:

    def __init__(self, model: Aluno, view: AlunoView):
        self.model = model
        self.view = view

    def exibir_detalhes_do_aluno(self):
        self.view.mostrar_detalhes_do_aluno(self.model)

    def atualizar_estado_do_aluno(self, novo_estado: EstadoAluno):
        if not isinstance(novo_estado, EstadoAluno):
            raise TypeError("Estado deve ser uma instância de EstadoAluno.")
        self.model.estado_aluno = novo_estado
        self.view.mostrar_mensagem("Estado do aluno atualizado com sucesso.")

    def atualizar_orientador(self, orientador: Professor):
        if not isinstance(orientador, Professor):
            raise TypeError("Orientador deve ser um objeto do tipo Professor.")
        self.model.orientador = orientador
        self.view.mostrar_mensagem("Orientador do aluno atualizado com sucesso.")

    def registrar_modulo_atual_para_aluno(self, modulo: Modulo):
        self.model.estado_aluno.adicionar_modulo_atual(modulo)
        self.view.mostrar_mensagem(f"Módulo '{modulo.nome}' adicionado aos módulos atuais.")

    def remover_modulo_atual_para_aluno(self, modulo: Modulo):
        self.model.estado_aluno.remover_modulo_atual(modulo
        self.view.mostrar_mensagem(f"Módulo '{modulo.nome}' removido dos módulos atuais.")

    def registrar_modulo_finalizado_para_aluno(self, modulo: Modulo):
        self.model.estado_aluno.adicionar_modulo_finalizado(modulo)
        self.view.mostrar_mensagem(f"Módulo '{modulo.nome}' adicionado aos módulos finalizados.")

    def remover_modulo_finalizado_para_aluno(self, modulo: Modulo):
        self.model.estado_aluno.remover_modulo_finalizado(modulo)
        self.view.mostrar_mensagem(f"Módulo '{modulo.nome}' removido dos módulos finalizados.")

    def registrar_certificado_para_aluno(self, certificado: Certificado):
        self.model.estado_aluno.adicionar_certificado(certificado)
        self.view.mostrar_mensagem(f"Certificado '{certificado.nome}' adicionado ao aluno.")

    def exibir_modulos_atuais(self):
        modulos_atuais = self.model.estado_aluno.modulos_atuais
        if modulos_atuais:
            self.view.mostrar_mensagem("Módulos atuais do aluno:")
            for modulo in modulos_atuais:
                print(f" - {modulo.nome}")
        else:
            self.view.mostrar_mensagem("O aluno não está cursando módulos no momento.")

    def exibir_modulos_finalizados(self):
        modulos_finalizados = self.model.estado_aluno.modulos_finalizados
        if modulos_finalizados:
            self.view.mostrar_mensagem("Módulos finalizados do aluno:")
            for modulo in modulos_finalizados:
                print(f" - {modulo.nome}")
        else:
            self.view.mostrar_mensagem("O aluno não concluiu módulos até o momento.")

    def exibir_certificados(self):
        certificados = self.model.estado_aluno.certificados
        if certificados:
            self.view.mostrar_mensagem("Certificados do aluno:")
            for certificado in certificados:
                print(f" - {certificado.nome}")
        else:
            self.view.mostrar_mensagem("O aluno não possui certificados no momento.")

    def exibir_progresso(self):
        progresso = self.model.estado_aluno.progresso
        self.view.mostrar_mensagem(f"O progresso atual do aluno é de {progresso:.2f}%.")
