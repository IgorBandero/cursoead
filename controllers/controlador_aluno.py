from views.tela_aluno import TelaAluno
from views.tela_modulo import TelaModulo
from models.aluno import Aluno
from models.matricula import Matricula
from exceptions.CursoExceptions import ListaCursosVaziaException, CursoInvalidoException
from exceptions.AlunoExceptions import AlunoJaRegistradoException, AlunoInvalidoException, CpfAlunoJaRegistradoException, UsuarioAlunoJaRegistradoException, EdicaoAlunoException, ListaAlunosVaziaException, AlunoNaoEncontradoException, AlunoNaoConcluinteException, ListaExAlunosVaziaException
from collections import Counter
from datetime import date
from datetime import timedelta
import random
from daos.aluno_dao import AlunoDAO
class ControladorAluno():

    def __init__(self, controlador_sistema, controlador_curso, controlador_modulo):
        #self.__alunos = []
        self.__ex_alunos = []
        self.__tela_aluno = TelaAluno()
        self.__tela_modulo = TelaModulo()
        self.__controlador_curso = controlador_curso
        self.__controlador_modulo = controlador_modulo
        self.__controlador_sistema = controlador_sistema
        self.__aluno_DAO = AlunoDAO()

    def cadastrar_aluno(self):
        try:
            num_cursos_disponiveis = len(self.__controlador_curso._ControladorCurso__curso_DAO.get_all())
            if (num_cursos_disponiveis == 0):
                raise ListaCursosVaziaException
            aluno = self.__tela_aluno.cadastrar_aluno()
            if (aluno is not None):
                curso = self.__controlador_curso.selecionar_curso("Selecionar o curso do aluno:")
                if (curso is not None):
                    codigo = self.gerar_codigo_matricula()
                    aluno_cadastrado = self.buscar_aluno_pelo_cpf(aluno["cpf"])
                    if aluno_cadastrado is None:
                        novo_aluno = Aluno(aluno["nome"], aluno["cpf"], aluno["telefone"], aluno["email"], aluno["usuario"], aluno["senha"], aluno["rua"], aluno["num_residencia"], aluno["bairro"], aluno["cidade"], aluno["cep"], curso, codigo, aluno["data_inicio"])
                        self.__aluno_DAO.add(novo_aluno)
                        self.__tela_aluno.mostrar_mensagem(f"Aluno(a): {novo_aluno.nome} cadastrado(a) com sucesso!\n")
                    else:
                        raise CpfAlunoJaRegistradoException
                else:
                    raise CursoInvalidoException
            else:
                raise AlunoInvalidoException
        except Exception as e:
            self.__tela_aluno.mostrar_mensagem(str(e))
        self.abrir_tela()

    def editar_aluno(self):
        try:
            if(len(self.__aluno_DAO.get_all()) == 0):
                raise ListaAlunosVaziaException
            aluno = self.selecionar_aluno("Selecione um(a) aluno(a) para editar:")
            if(aluno is not None):
                aluno_atualizado = self.__tela_aluno.editar_aluno({"nome": aluno.nome, "cpf": aluno.cpf, "telefone": aluno.telefone,
                                                    "email": aluno.email, "usuario": aluno.usuario, "senha": aluno.senha,
                                                    "rua": aluno.endereco.rua, "num_residencia": aluno.endereco.num_residencia, "bairro": aluno.endereco.bairro,
                                                    "cidade": aluno.endereco.cidade, "cep": aluno.endereco.cep, "data_inicio": aluno.matricula.data_inicio})
                if aluno_atualizado:
                    if aluno.cpf != aluno_atualizado["cpf"]:
                        try:
                            self.__aluno_DAO.remove(aluno.cpf)
                            if self.buscar_aluno_pelo_cpf(aluno_atualizado["cpf"]) is not None:
                                raise CpfAlunoJaRegistradoException
                            aluno_novo = Aluno(aluno_atualizado["nome"], aluno_atualizado["cpf"], aluno_atualizado["telefone"], aluno_atualizado["email"],
                                                aluno_atualizado["usuario"], aluno_atualizado["senha"], aluno_atualizado["rua"], aluno_atualizado["num_residencia"], 
                                                aluno_atualizado["bairro"], aluno_atualizado["cidade"], aluno_atualizado["cep"], aluno.matricula.curso,
                                                aluno.matricula.codigo, aluno_atualizado["data_inicio"])
                            self.__aluno_DAO.add(aluno_novo)
                        except CpfAlunoJaRegistradoException as e:
                            self.__tela_aluno.mostrar_mensagem(str(e))
                    else:
                        for item in self.__aluno_DAO.get_all():
                            if(item.cpf == aluno_atualizado["cpf"]):
                                item.nome = aluno_atualizado["nome"]
                                item.telefone = aluno_atualizado["telefone"]
                                item.email = aluno_atualizado["email"]
                                item.usuario = aluno_atualizado["usuario"]
                                item.senha = aluno_atualizado["senha"]
                                item.rua = aluno_atualizado["rua"]
                                item.num_residencia = aluno_atualizado["num_residencia"]
                                item.bairro = aluno_atualizado["bairro"]
                                item.cidade = aluno_atualizado["cidade"]
                                item.cep = aluno_atualizado["cep"]
                                item.data_inicio = aluno_atualizado["data_inicio"]
                                self.__aluno_DAO.update(item)
                    self.__tela_aluno.mostrar_mensagem(f"Informações do(a) aluno(a) {aluno.nome} atualizadas com sucesso!\n")
        except Exception as e:
            self.__tela_aluno.mostrar_mensagem(str(e))
        self.abrir_tela()

    def selecionar_aluno(self, mensagem):
        try:
            if(len(self.__aluno_DAO.get_all()) == 0):
                raise ListaAlunosVaziaException
            lista_alunos = []
            for aluno in self.__aluno_DAO.get_all():
                lista_alunos.append({"nome": aluno.nome, "cpf": aluno.cpf})
            cpf_aluno_escolhido = self.__tela_aluno.selecionar_aluno_na_lista(lista_alunos, mensagem)
            if (cpf_aluno_escolhido is not None):
                try:
                    aluno = self.__aluno_DAO.get(cpf_aluno_escolhido)
                    return aluno
                except AlunoNaoEncontradoException:
                    return
        except Exception as e:
            self.abrir_tela()
            self.__tela_aluno.mostrar_mensagem(str(e))



        try:
            while (True):
                self.__tela_aluno.mostrar_mensagem("\n----------------- SELECIONAR ALUNO -----------------")
                tipo_consulta = self.__tela_aluno.selecionar_aluno(len(self.__alunos))
                if tipo_consulta == "Buscar pelo cpf":
                    aluno = self.selecionar_aluno_pelo_cpf()
                    if(aluno is not None):
                        return aluno
                    else:
                        raise AlunoNaoEncontradoException
                elif tipo_consulta == "Selecionar da lista":
                    self.listar_alunos()
                    indice_aluno_escolhido = self.__tela_aluno.selecionar_aluno_na_lista(len(self.__alunos))
                    if (indice_aluno_escolhido is not None):
                        aluno = self.__alunos[indice_aluno_escolhido]
                        if(aluno is not None):
                            return aluno
                        else:
                            raise AlunoNaoEncontradoException
                continuar = self.__tela_aluno.continuar("Deseja tentar novamente? \n1 - SIM \n2 - NÃO (Sair)")
                if not continuar:
                    break
        except Exception as e:
            self.__tela_aluno.mostrar_mensagem(str(e))

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
        try:
            if(len(self.__alunos) == 0):
                raise ListaAlunosVaziaException
            print("\n----------------- LISTA DE ALUNOS ------------------\n")
            for indice, aluno in enumerate(self.__alunos):
                self.__tela_aluno.mostrar_opcao_aluno({"indice": indice, "nome": aluno.nome, "cpf": aluno.cpf, "matricula": aluno.matricula.codigo, "curso": aluno.matricula.curso.nome})
        except Exception as e:
            self.__tela_aluno.mostrar_mensagem(str(e))

    def buscar_aluno(self):
        aluno = self.selecionar_aluno()
        if aluno is not None:
            self.mostrar_aluno(aluno)

    def mostrar_aluno(self, aluno):
        self.__tela_aluno.mostrar_aluno({"nome": aluno.nome, "cpf": aluno.cpf, "telefone": aluno.telefone, "email": aluno.email, "usuario": aluno.usuario, "rua": aluno.endereco.rua, "num_residencia": aluno.endereco.num_residencia, "bairro": aluno.endereco.bairro, "cidade": aluno.endereco.cidade, "cep": aluno.endereco.cep, "data_inicio": aluno.matricula.data_inicio, "data_final": aluno.matricula.data_final, "curso": aluno.matricula.curso.nome, "codigo": aluno.matricula.codigo, "data_inicio": aluno.matricula.data_inicio})
        if len(aluno.matricula.modulos_atuais) > 0:
            self.__tela_aluno.mostrar_mensagem("\n------------------ MÓDULOS ATUAIS -----------------")
            for modulo in aluno.matricula.modulos_atuais:
                self.__tela_modulo.mostrar_modulo({"codigo": modulo.codigo, "nome": modulo.nome, "area": modulo.area, "carga_horaria": modulo.carga_horaria})
        if len(aluno.matricula.modulos_finalizados) > 0:
            self.__tela_aluno.mostrar_mensagem("\n--------------- MÓDULOS FINALIZADOS ---------------")
            for modulo in aluno.matricula.modulos_finalizados:
                print(modulo["modulo"].nome)
                self.__tela_modulo.mostrar_modulo_finalizado({"codigo": modulo["modulo"].codigo, "nome": modulo["modulo"].nome, "area": modulo["modulo"].area, "carga_horaria": modulo["modulo"].carga_horaria, "nota": modulo["nota"]})

    def selecionar_aluno_pelo_cpf(self):
        cpf = self.__tela_aluno.buscar_aluno_pelo_cpf()
        if (cpf is not None):
            aluno = self.buscar_aluno_pelo_cpf(cpf)
            if(aluno is not None):
                return aluno

    def buscar_aluno_pelo_cpf(self, cpf):
        for aluno in self.__aluno_DAO.get_all():
            if aluno.cpf == cpf:
                return aluno
        return None

    def buscar_ex_aluno_pelo_cpf(self, cpf):
        for aluno in self.__ex_alunos:
            if aluno.cpf == cpf:
                return aluno
        return None

    def gerar_codigo_matricula(self):
        while (True):
            data = date.today()
            ano = data.strftime('%Y')
            semestre = "100" if data.month in [1, 2, 3, 4, 5, 6] else "200"
            numero = random.randint(1, 999)
            numero = str(numero).zfill(4)
            num_matricula = ano+semestre+numero
            if (self.matricula_unica(num_matricula)):
                return num_matricula

    def matricula_unica(self, num_matricula):
        for aluno in self.__aluno_DAO.get_all():
            if aluno.matricula.codigo == num_matricula:
                return False
        return True

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
                    if nota >= 7.00:
                        registro_nota = {"modulo": aluno.matricula.modulos_atuais[indice_modulo], "nota": nota}
                        aluno.matricula.modulos_finalizados.append(registro_nota)
                        aluno.matricula.modulos_atuais.remove(aluno.matricula.modulos_atuais[indice_modulo])
                    else:
                        aluno.matricula.modulos_atuais.remove(aluno.matricula.modulos_atuais[indice_modulo])
                    self.__tela_aluno.mostrar_mensagem("\n************ NOTA LANÇADA COM SUCESSO! *************")

    def finalizar_curso(self):
        try:
            aluno = self.selecionar_aluno()
            if aluno is not None:
                self.__tela_aluno.mostrar_mensagem(f"\nALUNO(A): {aluno.nome} | CURSO: {aluno.matricula.curso.nome} | MATRÍCULA: {aluno.matricula.codigo} | CPF: {aluno.cpf}")
                if self.aluno_concluinte(aluno):
                    aluno.matricula.data_final = self.__tela_aluno.cadastrar_data("Data de conclusão (DD/MM/AAAA): ")
                    self.__ex_alunos.append(aluno)
                    self.__alunos.remove(aluno)
                    self.__tela_aluno.mostrar_mensagem("\n********** CURSO FINALIZADO COM SUCESSO! ***********")
                else:
                    raise AlunoNaoConcluinteException
        except Exception as e:
            self.__tela_aluno.mostrar_mensagem(str(e))

    def aluno_concluinte(self, aluno):
        if len(aluno.matricula.modulos_finalizados) == len(aluno.matricula.curso.modulos) and len(aluno.matricula.curso.modulos) > 0:
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
        for curso, frequencia in cursos_mais_populares:
            self.__tela_aluno.mostrar_mensagem(f"CURSO: {curso.nome} | ALUNOS: {frequencia}")

    def tempo_medio_conclusao(self):
        try:
            if (len(self.__ex_alunos) == 0):
                raise ListaExAlunosVaziaException
            else:
                duracoes = []
                for aluno in self.__ex_alunos:
                    data_inicio = aluno.matricula.data_inicio
                    data_final = aluno.matricula.data_final
                    duracao = (data_final - data_inicio).days
                    duracoes.append(duracao)
                media_duracao = sum(duracoes) / len(duracoes) if duracoes else 0
                media_duracao_timedelta = timedelta(days=media_duracao)
                self.__tela_aluno.mostrar_mensagem(f"\nTEMPO MÉDIO PARA CONCLUSÃO: {media_duracao_timedelta.days} DIAS")
        except Exception as e:
            self.__tela_aluno.mostrar_mensagem(str(e))

    def voltar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {
            1: self.cadastrar_aluno,
            2: self.editar_aluno,
            3: self.excluir_aluno,
            4: self.listar_alunos,
            5: self.buscar_aluno,
            6: self.matricular_aluno_modulos,
            7: self.lancar_notas_aluno,
            8: self.finalizar_curso,
            9: self.cursos_populares,
            10: self.tempo_medio_conclusao,
            0: self.voltar
        }
        opcao_escolhida = self.__tela_aluno.menu_opcoes()
        funcao_escolhida = opcoes.get(opcao_escolhida)
        if funcao_escolhida:
            funcao_escolhida()
