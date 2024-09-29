from curso import Curso
from aluno import Aluno
from professor import Professor
from administrador import Administrador


class Universidade:
    def __init__(self):
        # Inicialização das listas de cursos, professores, alunos e administradores
        self.__cursos = []
        self.__professores = []
        self.__alunos = []
        self.__administradores = []

    # Métodos para adicionar e remover cursos
    def adicionar_curso(self, curso: Curso):
        if not isinstance(curso, Curso):
            raise TypeError("O curso deve ser um objeto da classe Curso.")
        self.__cursos.append(curso)
    
    def remover_curso(self, curso: Curso):
        if curso in self.__cursos:
            self.__cursos.remove(curso)
        else:
            raise ValueError("O curso não está registrado na universidade.")
    
    def listar_cursos(self):
        return self.__cursos
    
    # Métodos para adicionar e remover professores
    def adicionar_professor(self, professor: Professor):
        if not isinstance(professor, Professor):
            raise TypeError("O professor deve ser um objeto da classe Professor.")
        self.__professores.append(professor)
    
    def remover_professor(self, professor: Professor):
        if professor in self.__professores:
            self.__professores.remove(professor)
        else:
            raise ValueError("O professor não está registrado na universidade.")
    
    def listar_professores(self):
        return self.__professores
    
    # Métodos para adicionar e remover alunos
    def adicionar_aluno(self, aluno: Aluno):
        if not isinstance(aluno, Aluno):
            raise TypeError("O aluno deve ser um objeto da classe Aluno.")
        self.__alunos.append(aluno)
    
    def remover_aluno(self, aluno: Aluno):
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)
        else:
            raise ValueError("O aluno não está registrado na universidade.")
    
    def listar_alunos(self):
        return self.__alunos
    
    # Métodos para adicionar e remover administradores
    def adicionar_administrador(self, administrador: Administrador):
        if not isinstance(administrador, Administrador):
            raise TypeError("O administrador deve ser um objeto da classe Administrador.")
        self.__administradores.append(administrador)
    
    def remover_administrador(self, administrador: Administrador):
        if administrador in self.__administradores:
            self.__administradores.remove(administrador)
        else:
            raise ValueError("O administrador não está registrado na universidade.")
    
    def listar_administradores(self):
        return self.__administradores
    
    def certificados_emitidos(self):

        alunos_com_certificado = []
        
        for aluno in self.__alunos:
            estado_aluno = aluno.estado_aluno
            
            # Verifica se o progresso do aluno é 100% (curso concluído)
            if estado_aluno.calcular_progresso() == 100:
                # Verifica se o aluno já tem um certificado emitido
                if len(estado_aluno.certificados) > 0:
                    alunos_com_certificado.append(aluno)
        
        return alunos_com_certificado

    # Método para calcular o tempo médio de conclusão dos alunos
    def tempo_media_conclusao(self):
        total_tempo = 0
        alunos_concluidos = 0

        for aluno in self.__alunos:
            if aluno.matricula.data_final is not None:  # O curso foi concluído
                duracao = aluno.matricula.data_final - aluno.matricula.data_inicio
                total_tempo += duracao.days  # Soma o tempo de conclusão em dias
                alunos_concluidos += 1

        if alunos_concluidos == 0:
            return 0  # Nenhum aluno concluiu o curso

        # Retorna a média do tempo de conclusão em dias
        return total_tempo / alunos_concluidos
    

    def cursos_mais_popular(self):
        if not self.__cursos:
            return None  # Sem cursos cadastrados

        # Inicializa um dicionário para contar o número de alunos por curso
        popularidade = {curso: 0 for curso in self.__cursos}

        # Conta o número de alunos em cada curso
        for aluno in self.__alunos:
            curso_aluno = aluno.matricula.curso
            if curso_aluno in popularidade:
                popularidade[curso_aluno] += 1

        # Encontra o curso com o maior número de alunos inscritos
        curso_mais_popular = max(popularidade, key=popularidade.get)

        # Retorna o curso mais popular
        return curso_mais_popular