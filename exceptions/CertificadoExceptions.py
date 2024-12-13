class AlunoNaoConcluinteException(Exception):
    def __init__(self):
        super().__init__("ALUNO AINDA NÃO CONCLUIU O CURSO\n")

class EmissaoCertificadoException(Exception):
    def __init__(self):
        super().__init__("ERRO NA EMISSÃO DO CERTIFICAO!\n")

class EdicaoCertificadoException(Exception):
    def __init__(self):
        super().__init__("ERRO NA EDIÇÃO DO CERTIFICADO!\n")

class ListaCertificadosVaziaException(Exception):
    def __init__(self):
        super().__init__("NENHUM CERTIFICADO CADASTRADO ATÉ O MOMENTO!\n")

class CertificadoNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("CERTIFICADO NÃO ENCONTRADO!\n")

class EdicaoCertificadoException(Exception):
    def __init__(self):
        super().__init__("ERRO NA EDIÇÃO DO CERTIFICADO!\n")