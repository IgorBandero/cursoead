from pessoa import Pessoa
from aluno import Aluno
from professor import Professor
from orientacao import Orientacao
from curso import Curso
from datetime import date

# Tentativa de instanciar um objeto de classe abstrata, deve dar erro
# pessoa1 = Pessoa("Ana", "000.111.222-33", "48 998877111", "ana@contato.com", "ana123", "12345", "Rua de cima", 250, "Trindade", "Florianópolis", "88040-170")

# Criando dois professores
professor1 = Professor(nome="Dr. Silva", cpf="123456789", telefone="99999-9999", email="dr.silva@email.com", usuario="drsilva", senha="1234", formacao="PhD", especialidade="Matemática", rua = "Rua de cima", num_residencia = 250, bairro = "Trindade", cidade = "Florianópolis", cep = "88040-900")
professor2 = Professor(nome="Dra. Santos", cpf="987654321", telefone="88888-8888", email="dra.santos@email.com", usuario="drasantos", senha="5678", formacao="PhD", especialidade="Física", rua = "Rua do lado", num_residencia = 540, bairro = "Pantanal", cidade = "Florianópolis", cep = "88040-500")

# Criando dois cursos
curso1 = Curso("Sistemas de informação", "Tecnologia aplicada em organizações", 3500, 8, 16, 800.00)
print("Curso 1: ", curso1.nome)
curso2 = Curso("Arquitetura e urbanismo", "Planejamento do espaço construido", 4000, 8, 16, 1000.00)
print("Curso 2: ", curso2.nome)

# Criando dois alunos
aluno1 = Aluno("João", "000.111.222-33", "48 991122333", "igor@contato.com", "igor123", "12345", "Rua de Cima", 250, "Pantanal", "Florianópolis", "88040-100", curso1, "24100450", date.today())
print("Aluno 1: ", aluno1.nome)
aluno2 = Aluno("Maria", "111.222.333-44", "48 995566222", "maria@contato.com", "maria123", "12345", "Rua do Lado", 1500, "Trindade", "Florianópolis", "88040-100", curso2, "23100680", date.today())
print("Aluna 2: ", aluno2.nome)

# Criando orientações
orientacao1 = Orientacao(aluno=aluno1, professor=professor1)  # João é orientando de Dr. Silva
orientacao2 = Orientacao(aluno=aluno2, professor=professor1)  # Maria é orientanda de Dr. Silva

# Adicionando orientandos ao professor correto
professor1.adicionar_orientando(orientacao1)
professor1.adicionar_orientando(orientacao2)

# Listando orientandos de cada professor
print(professor1.listar_orientandos())
print(professor2.listar_orientandos())
