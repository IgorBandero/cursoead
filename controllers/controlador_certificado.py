from views.tela_certificado import TelaCertificado
from views.tela_aluno import TelaAluno
from models.certificado import Certificado
from exceptions.CertificadoExceptions import AlunoNaoConcluinteException, EmissaoCertificadoException, EdicaoCertificadoException, ListaCertificadosVaziaException, CertificadoNaoEncontradoException
from exceptions.AlunoExceptions import AlunoNaoEncontradoException
from datetime import datetime as date
from daos.certificados_dao import CertificadoDAO
class ControladorCertificado():

    def __init__(self, controlador_sistema, controlador_aluno):
        self.__tela_certificado = TelaCertificado()
        self.__tela_aluno = TelaAluno()
        self.__controlador_aluno = controlador_aluno
        self.__controlador_sistema = controlador_sistema
        self.__certificado_DAO = CertificadoDAO()
        
    def emitir_certificado(self):
        try:
            cpf_aluno = self.__tela_aluno.buscar_aluno_pelo_cpf()
            if (cpf_aluno is not None):
                aluno = self.__controlador_aluno.buscar_aluno_pelo_cpf(cpf_aluno)
                ex_aluno = self.__controlador_aluno.buscar_ex_aluno_pelo_cpf(cpf_aluno)
                if (aluno is not None):
                    progresso = aluno.matricula.calcular_progresso()
                    print("PROGRESSO: ", progresso)
                    if (progresso == 100.00):
                        curso = aluno.matricula.curso
                        nota_final = self.__tela_certificado.emitir_certificado()
                        novo_certificado = Certificado(aluno, curso, nota_final, date.today())
                        self.__certificado_DAO.add(novo_certificado)
                        self.__tela_certificado.mostrar_mensagem("CERTICADO EMITIDO COM SUCESSO!\n")
                        self.__tela_certificado.mostrar_certificado({"aluno": aluno.nome, "cpf": aluno.cpf, "curso": aluno.matricula.curso.nome, "carga_horaria": aluno.matricula.curso.carga_horaria, "nota_final": nota_final, "data_emissao": novo_certificado.data_emissao})
                    else:
                        raise AlunoNaoConcluinteException
                elif (ex_aluno is not None):
                    if (ex_aluno in self.__controlador_aluno._ControladorAluno__ex_aluno_DAO.get_all()):
                        curso = ex_aluno.matricula.curso
                        nota_final = ex_aluno.matricula.calcular_media()
                        novo_certificado = Certificado(ex_aluno, curso, nota_final, date.today())
                        self.__certificado_DAO.add(novo_certificado)
                        self.__tela_certificado.mostrar_mensagem("CERTICADO EMITIDO COM SUCESSO!\n")
                        self.__tela_certificado.mostrar_certificado({"aluno": ex_aluno.nome, "cpf": ex_aluno.cpf, "curso": ex_aluno.matricula.curso.nome, "carga_horaria": ex_aluno.matricula.curso.carga_horaria, "nota_final": nota_final, "data_emissao": novo_certificado.data_emissao})
                        
                else:
                    raise EmissaoCertificadoException
            else:
                raise AlunoNaoEncontradoException
        except Exception as e:
            self.__tela_certificado.mostrar_mensagem(str(e))
        self.abrir_tela()

    def editar_certificado(self):
        try:
            if(len(self.__certificado_DAO.get_all()) == 0):
                raise ListaCertificadosVaziaException
            certificado = self.selecionar_certificado("Selecione o(a) titular do certificado para editar:")
            if(certificado is not None):
                certificado_atualizado = self.__tela_certificado.editar_certificado({"aluno": certificado.aluno.nome, "curso": certificado.curso.nome,
                                                    "data_emissao": certificado.data_emissao, "nota_final": certificado.nota_final})
                if certificado_atualizado:
                    if certificado.aluno.nome != certificado_atualizado["aluno"]:
                        self.__certificado_DAO.remove(certificado.aluno.nome)
                        certificado_novo = Certificado(certificado_atualizado["aluno"], certificado_atualizado["curso"],
                                                    certificado_atualizado["nota_final"], certificado_atualizado["data_emissao"])
                        self.__certificado_DAO.add(certificado_novo)
                    else:
                        for item in self.__certificado_DAO.get_all():
                            if(item.aluno.nome == certificado.aluno.nome):
                                item.aluno = certificado_atualizado["aluno"]
                                item.curso = certificado_atualizado["curso"]
                                item.nota_final = certificado_atualizado["nota_final"]
                                item.data_emissao = certificado_atualizado["data_emissao"]
                                self.__certificado_DAO.update(item)
                    self.__tela_certificado.mostrar_mensagem(f"Certificado atualizado com sucesso!\n")
        except Exception as e:
            self.__tela_certificado.mostrar_mensagem(str(e))
        self.abrir_tela()

    def excluir_certificado(self):
        try:
            if(len(self.__certificado_DAO.get_all()) == 0):
                    raise ListaCertificadosVaziaException
            certificado = self.selecionar_certificado("Selecione um certificado para excluir:")
            if(certificado is not None):
                excluir = self.__tela_certificado.excluir_certificado({"aluno": certificado.aluno.nome})
                if (excluir):
                    self.__certificado_DAO.remove(certificado.aluno.nome)
                    self.__tela_certificado.mostrar_mensagem(f"Certificado removido da lista de certificados\n")
                else:
                    self.__tela_certificado.mostrar_mensagem("EXCLUSÃO CANCELADA!\n")
        except Exception as e:
            self.__tela_certificado.mostrar_mensagem(str(e))
        self.abrir_tela()

    def listar_certificados(self):
        try:
            if(len(self.__certificado_DAO.get_all()) == 0):
                raise ListaCertificadosVaziaException
            lista_certificados = []
            for certificado in self.__certificado_DAO.get_all():
                lista_certificados.append({"aluno": certificado.aluno.nome, "curso": certificado.curso.nome, "nota_final": certificado.nota_final, "data_emissao": certificado.data_emissao})
            certificado = self.__tela_certificado.listar_certificados(lista_certificados)
            self.abrir_tela()
        except Exception as e:
            self.abrir_tela()
            self.__tela_certificado.mostrar_mensagem(str(e))

    def selecionar_certificado(self, mensagem):
        try:
            if(len(self.__certificado_DAO.get_all()) == 0):
                raise ListaCertificadosVaziaException
            lista_certificados = []
            for certificado in self.__certificado_DAO.get_all():
                lista_certificados.append({"aluno": certificado.aluno.nome, "curso": certificado.curso.nome, "matricula": certificado.aluno.matricula.codigo})
            titular_certificado_escolhido = self.__tela_certificado.selecionar_certificado_na_lista(lista_certificados, mensagem)
            if (titular_certificado_escolhido is not None):
                try:
                    curso = self.__certificado_DAO.get(titular_certificado_escolhido)
                    return curso
                except CertificadoNaoEncontradoException:
                    return
        except Exception as e:
            self.abrir_tela()
            self.__tela_certificado.mostrar_mensagem(str(e))

    def mostrar_certificado(self, certificado):
        self.__tela_certificado.mostrar_certificado({"aluno": certificado.aluno.nome, "cpf": certificado.aluno.cpf, "curso": certificado.curso.nome, "carga_horaria": certificado.curso.carga_horaria, "nota_final": certificado.nota_final, "data_emissao": certificado.data_emissao})

    def abrir_tela(self):
        opcoes = {
            1: self.emitir_certificado,
            2: self.editar_certificado,
            3: self.excluir_certificado,
            4: self.listar_certificados,
            0: self.voltar
        }
        opcao_escolhida = self.__tela_certificado.menu_opcoes()
        funcao_escolhida = opcoes.get(opcao_escolhida)
        if funcao_escolhida:
            funcao_escolhida()

    def voltar(self):
        self.__controlador_sistema.abrir_tela()