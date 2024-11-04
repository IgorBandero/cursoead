class AlunoNaoConcluinteException(Exception):
    def __init__(self):
        super().__init__("\n\n********* ALUNO AINDA NÃO CONCLUIU O CURSO *********")

class EmissaoCertificadoException(Exception):
    def __init__(self):
        super().__init__("\n\n*********** ERRO NA EMISSÃO DO CERTIFICAO! ***********")

class EdicaoCertificadoException(Exception):
    def __init__(self):
        super().__init__("\n\n*********** ERRO NA EDIÇÃO DO CERTIFICADO! ***********")

class ListaCertificadosVaziaException(Exception):
    def __init__(self):
        super().__init__("\n\n****** NENHUM CERTIFICADO CADASTRADO ATÉ O MOMENTO! *****")
