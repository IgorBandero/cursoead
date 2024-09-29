from pessoa import Pessoa
from aluno import Aluno
from professor import Professor
from orientacao import Orientacao


# Criando dois professores
professor1 = Professor(nome="Dr. Silva", cpf=123456789, telefone="99999-9999", email="dr.silva@email.com", usuario="drsilva", senha="1234", formacao="PhD", especialidade="Matemática")
professor2 = Professor(nome="Dra. Santos", cpf=987654321, telefone="88888-8888", email="dra.santos@email.com", usuario="drasantos", senha="5678", formacao="PhD", especialidade="Física")

# Criando alunos
aluno1 = Aluno(nome="João")
aluno2 = Aluno(nome="Maria")
aluno3 = Aluno(nome="Pedro")

# Criando orientações
orientacao1 = Orientacao(aluno=aluno1, professor=professor1)  # João é orientando de Dr. Silva
orientacao2 = Orientacao(aluno=aluno2, professor=professor1)  # Maria é orientanda de Dr. Silva
orientacao3 = Orientacao(aluno=aluno3, professor=professor2)  # Pedro é orientando de Dra. Santos

# Adicionando orientandos ao professor correto
professor1.adicionar_orientando(orientacao1)
professor1.adicionar_orientando(orientacao2)
professor2.adicionar_orientando(orientacao3)

# Listando orientandos de cada professor
print(professor1.listar_orientandos())
print(professor2.listar_orientandos())
