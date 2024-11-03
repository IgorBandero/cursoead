from views.tela_certificado import TelaCertificado
from models.certificado import Certificado
from datetime import date

class ControladorCertificado():

    def __init__(self, controlador_sistema, controlador_aluno):
        self.__certificados = []
        self.__tela_certificado = TelaCertificado()
        self.__controlador_aluno = controlador_aluno
        self.__controlador_sistema = controlador_sistema
        
    def emitir_certificado(self):
        aluno = self.__controlador_aluno.selecionar_aluno_pelo_cpf()
        if (aluno is not None):
            progresso = aluno.matricula.calcular_progresso()
            if (progresso == 100.00):
                curso = aluno.matricula.curso
                nota_final = self.__tela_certificado.cadastrar_certificado()
                novoCertificado = Certificado(aluno, curso, nota_final, date.today())
                self.__certificados.append(novoCertificado)
            else:
                raise ValueError # Erro de aluno não concluiu o curso

    def abrir_tela(self):
        menu_opcoes = {1: self.emitir_certificado, 0: self.voltar}
        while True:
            menu_opcoes[self.__tela_certificado.mostrar_menu_opcoes()]()

    def voltar(self):
        self.__controlador_sistema.abrir_tela()