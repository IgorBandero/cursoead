from views.tela_certificado import TelaCertificado
from views.tela_aluno import TelaAluno
from models.certificado import Certificado
from datetime import datetime as date

from models.curso import Curso
from models.aluno import Aluno
class ControladorCertificado():

    def __init__(self, controlador_sistema, controlador_aluno):
        self.__certificados = []
        self.__tela_certificado = TelaCertificado()
        self.__tela_aluno = TelaAluno()
        self.__controlador_aluno = controlador_aluno
        self.__controlador_sistema = controlador_sistema

        curso1 = Curso("Sistemas de Informação", "Gestão e Tecnologia", 3500, 8, 16, 750.00, [])
        curso2 = Curso("Engenharia de Produção", "Gestão Industrial", 3300, 10, 18, 900.00, [])
        curso3 = Curso("Arquitetura e Urbanismo", "Planejamento do Espaço Construído", 4000, 10, 18, 850.00, [])
        aluno1 = Aluno("Carlos", 11122233344, "(48) 991122333", "carlos@contato.com", "carlos123", "123456", "Rua de Cima", 350, "Pantanal", "Florianópolis", "88040-100", curso1, "24100299", date.today())
        aluno2 = Aluno("Maria", 22233344455, "(48) 992233444", "maria@contato.com", "maria123", "123456", "Rua do Lado", 100, "Trindade", "Florianópolis", "88040-900", curso2, "24100299", date.today())
        aluno3 = Aluno("João", 33344455566, "(48) 993344555", "joao@contato.com", "joao123", "123456", "Rua de Baixo", 1200, "Córrego Grande", "Florianópolis", "88040-500", curso3, "24100299", date.today())

        certificado1 = Certificado(aluno1, curso1, 8.6, date.today())
        certificado2 = Certificado(aluno2, curso2, 7.2, date.today())
        certificado3 = Certificado(aluno3, curso3, 9.3, date.today())
        self.__certificados.append(certificado1)
        self.__certificados.append(certificado2)
        self.__certificados.append(certificado3)

        
    def emitir_certificado(self):
        cpf_aluno = self.__tela_aluno.buscar_aluno_pelo_cpf()
        if (cpf_aluno is not None):
            aluno = self.__controlador_aluno.buscar_aluno_pelo_cpf(cpf_aluno)
            ex_aluno = self.__controlador_aluno.buscar_ex_aluno_pelo_cpf(cpf_aluno)
            if (aluno is not None):
                progresso = aluno.matricula.calcular_progresso()
                if (progresso == 100.00):
                    curso = aluno.matricula.curso
                    nota_final = self.__tela_certificado.emitir_certificado()
                    novo_certificado = Certificado(aluno, curso, nota_final, date.today())
                    self.__certificados.append(novo_certificado)
                    self.__tela_certificado.mostrar_mensagem("\n********** CERTICADO EMITIDO COM SUCESSO! **********")
                else:
                    self.__tela_certificado.mostrar_mensagem("\n********* ALUNO AINDA NÃO CONCLUIU O CURSO *********")
            elif (ex_aluno is not None):
                if (ex_aluno in self.__controlador_aluno._ControladorAluno__ex_alunos):
                    curso = ex_aluno.matricula.curso
                    nota_final = ex_aluno.matricula.calcular_media()
                    novo_certificado = Certificado(ex_aluno, curso, nota_final, date.today())
                    self.__certificados.append(novo_certificado)
                    self.__tela_certificado.mostrar_certificado({"aluno": ex_aluno.nome, "cpf": ex_aluno.cpf, "curso": ex_aluno.matricula.curso.nome, "carga_horaria": ex_aluno.matricula.curso.carga_horaria, "nota_final": nota_final, "data_emissao": novo_certificado.data_emissao})
                    self.__tela_certificado.mostrar_mensagem("\n********** CERTICADO EMITIDO COM SUCESSO! **********")
            else:
                self.__tela_certificado.mostrar_mensagem("\n*********** ERRO AO EMITIR O CERTIFICADO! **********")

    def editar_certificado(self):
        certificado = self.selecionar_certificado()
        if(certificado is not None):
            self.mostrar_certificado(certificado)
            while(True):
                campo, info_atualizada = self.__tela_certificado.editar_certificado()
                if info_atualizada is not None:
                    for item in self.__certificados:
                        if(item == certificado):
                            if campo == 1:
                                item.data_emissao = info_atualizada
                            self.mostrar_certificado(certificado)
                else:
                    self.__tela_certificado.mostrar_mensagem("\n************* ERRO: Edição não concluída *************")
                continuar = self.__tela_certificado.continuar("Deseja editar outro campo? \n1 - SIM \n2 - NÃO (Sair)")
                if not continuar:
                    break

    def excluir_certificado(self):
        certificado = self.selecionar_certificado()
        if(certificado is not None):
            excluir = self.__tela_certificado.excluir_certificado()
            if (excluir):
                self.__certificados.remove(certificado)
                self.__tela_certificado.mostrar_mensagem(f"\nO certificado foi removido dos registros de certificados.")
            else:
                self.__tela_aluno.mostrar_mensagem("\n*************** EXCLUSÃO CANCELADA *****************")

    def listar_certificados(self):
        if(len(self.__certificados) == 0):
            self.__tela_certificado.mostrar_mensagem("\n********** NENHUM CERTIFICADO REGISTRADO! **********")
            return
        print("\n-------------- LISTA DE CERTIFICADOS ---------------\n")
        for indice, certificado in enumerate(self.__certificados):
            self.__tela_certificado.mostrar_opcao_certificado({"indice": indice, "aluno": certificado.aluno.nome, "curso": certificado.curso.nome, "nota_final": certificado.nota_final, "data_emissao": certificado.data_emissao})

    def selecionar_certificado(self):
        while (True):
            self.__tela_certificado.mostrar_mensagem("\n-------------- SELECIONAR CERTIFICADO --------------")
            self.listar_certificados()
            indice_certificado_escolhido = self.__tela_certificado.selecionar_certificado(len(self.__certificados))
            if (indice_certificado_escolhido is not None):
                certificado = self.__certificados[indice_certificado_escolhido]
                if(certificado is not None):
                    return certificado
                else:
                    self.__tela_certificado.mostrar_mensagem("\n******* ATENÇÃO: Certificado não encontrado! *******")
                continuar = self.__tela_certificado.continuar("Deseja tentar novamente? \n1 - SIM \n2 - NÃO (Sair)")
                if not continuar:
                    break

    def mostrar_certificado(self, certificado):
        self.__tela_certificado.mostrar_certificado({"aluno": certificado.aluno.nome, "cpf": certificado.aluno.cpf, "curso": certificado.curso.nome, "carga_horaria": certificado.curso.carga_horaria, "nota_final": certificado.nota_final, "data_emissao": certificado.data_emissao})

    def abrir_tela(self):
        menu_opcoes = {1: self.emitir_certificado, 2: self.editar_certificado, 3: self.excluir_certificado, 4: self.listar_certificados, 0: self.voltar}
        while True:
            menu_opcoes[self.__tela_certificado.mostrar_menu_opcoes()]()

    def voltar(self):
        self.__controlador_sistema.abrir_tela()