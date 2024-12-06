from views.tela_certificado import TelaCertificado
from views.tela_aluno import TelaAluno
from models.certificado import Certificado
from exceptions.CertificadoExceptions import AlunoNaoConcluinteException, EmissaoCertificadoException, EdicaoCertificadoException, ListaCertificadosVaziaException
from datetime import datetime as date
class ControladorCertificado():

    def __init__(self, controlador_sistema, controlador_aluno):
        self.__certificados = []
        self.__tela_certificado = TelaCertificado()
        self.__tela_aluno = TelaAluno()
        self.__controlador_aluno = controlador_aluno
        self.__controlador_sistema = controlador_sistema
        
    def emitir_certificado(self):
        try:
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
                        raise AlunoNaoConcluinteException
                elif (ex_aluno is not None):
                    if (ex_aluno in self.__controlador_aluno._ControladorAluno__ex_alunos):
                        curso = ex_aluno.matricula.curso
                        nota_final = ex_aluno.matricula.calcular_media()
                        novo_certificado = Certificado(ex_aluno, curso, nota_final, date.today())
                        self.__certificados.append(novo_certificado)
                        self.__tela_certificado.mostrar_certificado({"aluno": ex_aluno.nome, "cpf": ex_aluno.cpf, "curso": ex_aluno.matricula.curso.nome, "carga_horaria": ex_aluno.matricula.curso.carga_horaria, "nota_final": nota_final, "data_emissao": novo_certificado.data_emissao})
                        self.__tela_certificado.mostrar_mensagem("\n********** CERTICADO EMITIDO COM SUCESSO! **********")
                else:
                    raise EmissaoCertificadoException
        except Exception as e:
            self.__tela_certificado.mostrar_mensagem(str(e))

    def editar_certificado(self):
        try:
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
                        raise EdicaoCertificadoException
                    continuar = self.__tela_certificado.continuar("Deseja editar outro campo? \n1 - SIM \n2 - NÃO (Sair)")
                    if not continuar:
                        break
        except Exception as e:
            self.__tela_certificado.mostrar_mensagem(str(e))

    def excluir_certificado(self):
        certificado = self.selecionar_certificado()
        if(certificado is not None):
            excluir = self.__tela_certificado.excluir_certificado()
            if (excluir):
                self.__certificados.remove(certificado)
                self.__tela_certificado.mostrar_mensagem(f"\nO certificado foi removido dos registros de certificados.")
            else:
                self.__tela_certificado.mostrar_mensagem("\n*************** EXCLUSÃO CANCELADA *****************")

    def listar_certificados(self):
        try:
            if(len(self.__certificados) == 0):
                raise ListaCertificadosVaziaException
            print("\n-------------- LISTA DE CERTIFICADOS ---------------\n")
            for indice, certificado in enumerate(self.__certificados):
                self.__tela_certificado.mostrar_opcao_certificado({"indice": indice, "aluno": certificado.aluno.nome, "curso": certificado.curso.nome, "nota_final": certificado.nota_final, "data_emissao": certificado.data_emissao})
        except Exception as e:
            self.__tela_certificado.mostrar_mensagem(str(e))

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