from views.tela_aluno import TelaAluno
from views.tela_modulo import TelaModulo
from models.aluno import Aluno
from models.matricula import Matricula
from collections import Counter
from datetime import date
from datetime import timedelta
import random

from models.curso import Curso
class ControladorAluno():

    def __init__(self, controlador_sistema, controlador_curso, controlador_modulo):
        self.__alunos = []
        self.__ex_alunos = []
        self.__tela_aluno = TelaAluno()
        self.__tela_modulo = TelaModulo()
        self.__controlador_curso = controlador_curso
        self.__controlador_modulo = controlador_modulo
        self.__controlador_sistema = controlador_sistema

        curso1 = Curso("Sistemas de Informação", "Gestão e Tecnologia", 3500, 8, 16, 750.00, [])
        curso2 = Curso("Engenharia de Produção", "Gestão Industrial", 3300, 10, 18, 900.00, [])
        curso3 = Curso("Arquitetura e Urbanismo", "Planejamento do Espaço Construído", 4000, 10, 18, 850.00, [])
        curso4 = Curso("Filosofia", "Lógica e Epistemologia", 3200, 8, 16, 500.00, [])

        controlador_curso._ControladorCurso__cursos.append(curso1)
        controlador_curso._ControladorCurso__cursos.append(curso2)
        controlador_curso._ControladorCurso__cursos.append(curso3)
        controlador_curso._ControladorCurso__cursos.append(curso4)

        aluno1 = Aluno("Carlos", 11122233344, "(48) 991122333", "carlos@contato.com", "carlos123", "123456", "Rua de Cima", 350, "Pantanal", "Florianópolis", "88040-100", curso1, "24100299", date.today())
        aluno2 = Aluno("Maria", 22233344455, "(48) 992233444", "maria@contato.com", "maria123", "123456", "Rua do Lado", 100, "Trindade", "Florianópolis", "88040-900", curso2, "24100299", date.today())
        aluno3 = Aluno("João", 33344455566, "(48) 993344555", "joao@contato.com", "joao123", "123456", "Rua de Baixo", 1200, "Córrego Grande", "Florianópolis", "88040-500", curso3, "24100299", date.today())
        self.__alunos.append(aluno1)
        self.__alunos.append(aluno2)
        self.__alunos.append(aluno3)

        aluno4 = Aluno("Carlos", 21122233344, "(48) 991122333", "carlos@contato.com", "carlos123", "123456", "Rua de Cima", 350, "Pantanal", "Florianópolis", "88040-100", curso1, "24100299", date.today())
        aluno5 = Aluno("Maria", 32233344455, "(48) 992233444", "maria@contato.com", "maria123", "123456", "Rua do Lado", 100, "Trindade", "Florianópolis", "88040-900", curso1, "24100299", date.today())
        aluno6 = Aluno("João", 53344455566, "(48) 993344555", "joao@contato.com", "joao123", "123456", "Rua de Baixo", 1200, "Córrego Grande", "Florianópolis", "88040-500", curso3, "24100299", date.today())
        self.__alunos.append(aluno4)
        self.__alunos.append(aluno5)
        self.__alunos.append(aluno6)

        aluno7 = Aluno("Carlos", 71122233344, "(48) 991122333", "carlos@contato.com", "carlos123", "123456", "Rua de Cima", 350, "Pantanal", "Florianópolis", "88040-100", curso1, "24100299", date.today())
        aluno8 = Aluno("Maria", 72233344455, "(48) 992233444", "maria@contato.com", "maria123", "123456", "Rua do Lado", 100, "Trindade", "Florianópolis", "88040-900", curso2, "24100299", date.today())
        aluno9 = Aluno("João", 73344455566, "(48) 993344555", "joao@contato.com", "joao123", "123456", "Rua de Baixo", 1200, "Córrego Grande", "Florianópolis", "88040-500", curso2, "24100299", date.today())
        self.__alunos.append(aluno7)
        self.__alunos.append(aluno8)
        self.__alunos.append(aluno9)

    def cadastrar_aluno(self):
        num_cursos_disponiveis = len(self.__controlador_curso._ControladorCurso__cursos)
        if (num_cursos_disponiveis == 0):
            self.__tela_aluno.mostrar_mensagem("\n****** NENHUM CURSO DISPONÍVEL PARA MATRÍCULA! ******")
            return
        aluno = self.__tela_aluno.cadastrar_aluno()
        if (aluno is not None):
            self.__tela_aluno.mostrar_mensagem("Curso: ")
            curso = self.__controlador_curso.selecionar_curso()
            if (curso is not None):
                codigo = self.gerar_codigo_matricula()
                data_inicio = date.today()
                aluno_cadastrado = self.buscar_aluno_pelo_cpf(aluno["cpf"])
                if aluno_cadastrado is None:
                    novo_aluno = Aluno(aluno["nome"], aluno["cpf"], aluno["telefone"], aluno["email"], aluno["usuario"], aluno["senha"], aluno["rua"], aluno["num_residencia"], aluno["bairro"], aluno["cidade"], aluno["cep"], curso, codigo, data_inicio)
                    self.__alunos.append(novo_aluno)
                    print("\nAluno: ", self.__alunos[-1].nome, " cadastrado(a) com sucesso!")
                else:
                    self.__tela_aluno.mostrar_mensagem("\n********* ATENÇÃO: Aluno já cadastrado! *********")
            else:
                self.__tela_aluno.mostrar_mensagem("\n*********** ATENÇÃO: Curso inválido! ************")
        else:
            self.__tela_aluno.mostrar_mensagem("\n************* ERRO NO CADASTRO DE ALUNO ************")

    def editar_aluno(self):
        aluno = self.selecionar_aluno()
        if(aluno is not None):
            self.mostrar_aluno(aluno)
            while(True):
                campo, info_atualizada = self.__tela_aluno.editar_aluno()
                if info_atualizada is not None:
                    for item in self.__alunos:
                        if(item.cpf == aluno.cpf):
                            if campo == 1:
                                item.nome = info_atualizada
                            elif campo == 2:
                                for caso in self.__alunos:
                                    if caso.cpf == info_atualizada:
                                        print("\n*********** ERRO: CPF JÁ CADASTRADO! ***********")
                                        return
                                item.cpf = info_atualizada
                            elif campo == 3:
                                item.telefone = info_atualizada
                            elif campo == 4:
                                item.email = info_atualizada
                            elif campo == 5:
                                for caso in self.__alunos:
                                    if caso.usuario == info_atualizada:
                                        print("\n*********** ERRO: USUÁRIO JÁ CADASTRADO! ***********")
                                        return
                                item.usuario = info_atualizada
                            elif campo == 6:
                                item.rua = info_atualizada
                            elif campo == 7:
                                item.num_residencia = info_atualizada
                            elif campo == 8:
                                item.bairro = info_atualizada
                            elif campo == 9:
                                item.cidade = info_atualizada
                            elif campo == 10:
                                item.cep = info_atualizada
                            elif campo == 11:
                                novo_curso = self.__controlador_curso.selecionar_curso()
                                print("NOVO CURSO: ", novo_curso.nome)
                                if (novo_curso is not None):
                                    item.matricula.curso = novo_curso
                            elif campo == 12:
                                for caso in self.__alunos:
                                    if caso.matricula.codigo == info_atualizada:
                                        print("\n*********** ERRO: MATRICULA JÁ CADASTRADA! ***********")
                                        return
                                item.matricula = Matricula(aluno.matricula.curso, info_atualizada, aluno.matricula.data_inicio)
                            elif campo == 13:
                                while(True):
                                    self.__tela_aluno.mostrar_mensagem("\nInforme a senha atual... ")
                                    senha_atual = input("Digite a senha atual: ")
                                    if senha_atual == aluno.senha:
                                        self.__tela_aluno.mostrar_mensagem("\nInforme a nova senha... ")
                                        nova_senha = self.__tela_aluno.cadastrar_senha()
                                        item.senha = nova_senha
                                    else:
                                        self.__tela_aluno.mostrar_mensagem("\n****************** SENHA INCORRETA! ******************")
                            self.mostrar_aluno(aluno)
                else:
                    self.__tela_aluno.mostrar_mensagem("\n************* ERRO: Edição não concluída *************")
                continuar = self.__tela_aluno.continuar_edicao()
                if not continuar:
                    break

    def excluir_aluno(self):
        aluno = self.selecionar_aluno()
        if(aluno is not None):
            excluir = self.__tela_aluno.excluir_aluno({"nome": aluno.nome, "curso": aluno.matricula.curso.nome})
            if (excluir):
                self.__alunos.remove(aluno)
                self.__tela_aluno.mostrar_mensagem(f"\nAluno: {aluno.nome} foi removido da lista de alunos da universidade.")
            else:
                self.__tela_aluno.mostrar_mensagem("\n*************** EXCLUSÃO CANCELADA ****************")

    def listar_alunos(self):
        if(len(self.__alunos) == 0):
            self.__tela_aluno.mostrar_mensagem("\n****** NENHUM ALUNO CADASTRADO ATÉ O MOMENTO! ******")
            return
        print("\n----------------- LISTA DE ALUNOS ------------------\n")
        for indice, aluno in enumerate(self.__alunos):
            self.__tela_aluno.mostrar_opcao_aluno({"indice": indice, "nome": aluno.nome, "cpf": aluno.cpf, "matricula": aluno.matricula.codigo, "curso": aluno.matricula.curso.nome})

    def buscar_aluno(self):
        aluno = self.selecionar_aluno()
        if aluno is not None:
            self.mostrar_aluno(aluno)

    def mostrar_aluno(self, aluno):
        self.__tela_aluno.mostrar_aluno({"nome": aluno.nome, "cpf": aluno.cpf, "telefone": aluno.telefone, "email": aluno.email, "usuario": aluno.usuario, "rua": aluno.endereco.rua, "num_residencia": aluno.endereco.num_residencia, "bairro": aluno.endereco.bairro, "cidade": aluno.endereco.cidade, "cep": aluno.endereco.cep, "curso": aluno.matricula.curso.nome, "codigo": aluno.matricula.codigo, "data_inicio": aluno.matricula.data_inicio})
        if len(aluno.matricula.modulos_atuais) > 0:
            self.__tela_aluno.mostrar_mensagem("\n------------------ MÓDULOS ATUAIS -----------------")
            for modulo in aluno.matricula.modulos_atuais:
                self.__tela_modulo.mostrar_modulo({"codigo": modulo.codigo, "nome": modulo.nome, "area": modulo.area, "carga_horaria": modulo.carga_horaria})
        if len(aluno.matricula.modulos_finalizados) > 0:
            self.__tela_aluno.mostrar_mensagem("\n--------------- MÓDULOS FINALIZADOS ---------------")
            for modulo in aluno.matricula.modulos_finalizados:
                print(modulo["modulo"].nome)
                self.__tela_modulo.mostrar_modulo_finalizado({"codigo": modulo["modulo"].codigo, "nome": modulo["modulo"].nome, "area": modulo["modulo"].area, "carga_horaria": modulo["modulo"].carga_horaria, "nota": modulo["nota"]})

    def selecionar_aluno(self):
        self.__tela_aluno.mostrar_mensagem("\n----------------- SELECIONAR ALUNO -----------------")
        tipo_consulta = self.__tela_aluno.selecionar_aluno(len(self.__alunos))
        if tipo_consulta == "Buscar pelo cpf":
            aluno = self.selecionar_aluno_pelo_cpf()
            if(aluno is not None):
                return aluno
            else:
                self.__tela_aluno.mostrar_mensagem("\n********* ATENÇÃO: Aluno não encontrado! *********")
        elif tipo_consulta == "Selecionar da lista":
            self.listar_alunos()
            indice_aluno_escolhido = self.__tela_aluno.selecionar_aluno_na_lista(len(self.__alunos))
            if (indice_aluno_escolhido is not None):
                aluno = self.__alunos[indice_aluno_escolhido]
                if(aluno is not None):
                    return aluno
                else:
                    self.__tela_aluno.mostrar_mensagem("\n********* ATENÇÃO: Aluno não encontrado! *********")

    def selecionar_aluno_pelo_cpf(self):
        cpf = self.__tela_aluno.buscar_aluno_pelo_cpf()
        if (cpf is not None):
            aluno = self.buscar_aluno_pelo_cpf(cpf)
            if(aluno is not None):
                return aluno

    def buscar_aluno_pelo_cpf(self, cpf):
        for aluno in self.__alunos:
            if aluno.cpf == cpf:
                return aluno
        return None

    def gerar_codigo_matricula(self):
        data = date.today()
        ano = data.strftime('%Y')
        semestre = "100" if data.month in [1, 2, 3, 4, 5, 6] else "200"
        numero = random.randint(1, 9999)
        numero = str(numero).zfill(4)
        return ano+semestre+numero

    def matricular_aluno_modulos(self):
        aluno = self.selecionar_aluno()
        if aluno is not None:
            self.__tela_aluno.mostrar_mensagem(f"\nALUNO(A): {aluno.nome} | CURSO: {aluno.matricula.curso.nome} | MATRÍCULA: {aluno.matricula.codigo} | CPF: {aluno.cpf}")
            modulos = self.__controlador_modulo.selecionar_modulos()
            if (modulos is not None):
                for item in modulos:
                    if item not in aluno.matricula.modulos_atuais:
                        aluno.matricula.adicionar_modulo_atual(item)

    def lancar_notas_aluno(self):
        aluno = self.selecionar_aluno()
        if aluno is not None:
            self.__tela_aluno.mostrar_mensagem(f"\nALUNO(A): {aluno.nome} | CURSO: {aluno.matricula.curso.nome} | MATRÍCULA: {aluno.matricula.codigo} | CPF: {aluno.cpf}")
            if(len(aluno.matricula.modulos_atuais) == 0):
                self.__tela_aluno.mostrar_mensagem("\n********* ALUNO SEM MÓDULOS MATRICULADOS! **********")
                return
            print("\n----------------- MÓDULOS ATUAIS -------------------\n")
            for indice, modulo in enumerate(aluno.matricula.modulos_atuais):
                self.__tela_modulo.mostrar_opcao_modulo({"indice": indice, "codigo": modulo.codigo, "nome": modulo.nome, "area": modulo.area, "carga_horaria": modulo.carga_horaria})
            indice_modulo = self.__tela_modulo.selecionar_modulo_na_lista(len(aluno.matricula.modulos_atuais))
            if indice_modulo is not None:
                nota = self.__tela_aluno.lancar_nota_modulo()
                if nota is not None:
                    registro_nota = {"modulo": aluno.matricula.modulos_atuais[indice_modulo], "nota": nota}
                    aluno.matricula.modulos_finalizados.append(registro_nota)
                    aluno.matricula.modulos_atuais.remove(aluno.matricula.modulos_atuais[indice_modulo])
                    self.__tela_aluno.mostrar_mensagem("\n************ NOTA LANÇADA COM SUCESSO! *************")

    def finalizar_curso(self):
        aluno = self.selecionar_aluno()
        if aluno is not None:
            self.__tela_aluno.mostrar_mensagem(f"\nALUNO(A): {aluno.nome} | CURSO: {aluno.matricula.curso.nome} | MATRÍCULA: {aluno.matricula.codigo} | CPF: {aluno.cpf}")
            if self.aluno_concluinte(aluno):
                aluno.matricula.data_final = self.__tela_aluno.data_conclusao()
                self.__ex_alunos.append(aluno)
                self.__alunos.remove(aluno)
                self.__tela_aluno.mostrar_mensagem("\n********** CURSO FINALIZADO COM SUCESSO! ***********")
            else:
                self.__tela_aluno.mostrar_mensagem("\n*********** ALUNO NÃO APTO À CONCLUSÃO! ************")

    def aluno_concluinte(self, aluno):
        if len(aluno.matricula.modulos_finalizados) == len(aluno.matricula.curso.modulos):
            lista_modulos = []
            for modulo in aluno.matricula.modulos_finalizados:
                lista_modulos.append(modulo["modulo"])
                print(modulo["modulo"].nome)
            for modulo_obrigatorio in aluno.matricula.curso.modulos:
                if modulo_obrigatorio not in lista_modulos:
                    return False
            return True
        else:
            return False

    def cursos_populares(self):
        cursos = [aluno.matricula.curso for aluno in self.__alunos]
        contador_cursos = Counter(cursos)
        cursos_mais_populares = contador_cursos.most_common()
        print("\n-------------- CURSOS MAIS POPULARES ---------------")
        for curso, frequencia in cursos_mais_populares[0:3]:
            self.__tela_aluno.mostrar_mensagem(f"CURSO: {curso.nome} | ALUNOS: {frequencia}")

    def cursos_melhor_avaliados(self):
        cursos = {aluno.matricula.curso for aluno in self.__alunos}
        avaliacoes = [(curso, curso.avaliacao_media_curso()) for curso in cursos]
        cursos_ordenados = sorted(avaliacoes, key=lambda x: x[1], reverse=True)
        for curso, avaliacao in cursos_ordenados:
            self.__tela_aluno.mostrar_mensagem(f"CURSO: {curso.nome} | AVALIAÇÃO MÉDIA: {avaliacao}")

    def tempo_medio_conclusao(self):
        if (len(self.__ex_alunos) == 0):
            self.__tela_aluno.mostrar_mensagem(f"\n****** NENHUM ALUNO CONCLUINTE ATÉ O MOMENTO! ******")
        else: 
            duracoes = []
            for aluno in self.__ex_alunos:
                data_inicio = aluno.matricula.data_inicio
                data_final = aluno.matricula.data_final
                duracao = (data_final - data_inicio).days
                print("DURAÇÃO: ", duracao)
                duracoes.append(duracao)
            media_duracao = sum(duracoes) / len(duracoes) if duracoes else 0
            media_duracao_timedelta = timedelta(days=media_duracao)
            self.__tela_aluno.mostrar_mensagem(f"\nTEMPO MÉDIO PARA CONCLUSÃO: {media_duracao_timedelta}")

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        menu_opcoes = {1: self.cadastrar_aluno, 2: self.editar_aluno, 3: self.excluir_aluno, 4: self.listar_alunos, 5: self.buscar_aluno, 6: self.matricular_aluno_modulos, 7: self.lancar_notas_aluno, 8: self.finalizar_curso, 9: self.cursos_populares, 10: self.cursos_melhor_avaliados, 11: self.tempo_medio_conclusao, 0: self.voltar}
        while True:
            menu_opcoes[self.__tela_aluno.mostrar_menu_opcoes()]()
