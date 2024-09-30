### PROBLEMA
O projeto tem como objetivo desenvolver um **sistema de gerenciamento de cursos para uma universidade online**, utilizando princípios de Programação Orientada a Objetos (POO) em Python. Esse sistema visa organizar de maneira eficiente o processo de criação e administração de cursos, inscrição de alunos, acompanhamento de progresso, emissão de certificados e geração de relatórios de desempenho.

### ESCOPO
A plataforma permitirá que os administradores cadastrem novos cursos, incluindo informações detalhadas como nome, descrição, duração (cada curso possui uma quantidade X de horas-aula específicas/ todas as aulas são gravadas), mensalidade, tempo máximo para conclusão. Cada curso será composto por diversos módulos, que também poderão ser cadastrados com informações como título, descrição, professor e duração. Os professores estarão associados aos módulos e poderão ter suas informações gerenciadas, como nome, especialidade, formação, e-mail.
Os alunos poderão se inscrever na plataforma, sendo que seus dados, como nome, e-mail, endereço, data de inscrição serão registrados no sistema. Após o cadastro de um aluno na plataforma, é gerada uma matrícula única e ele poderá optar por qual curso, dentre aqueles disponíveis na plataforma, ele deseja iniciar, levando em consideração a mensalidade, carga horária e o tempo máximo de conclusão. Ao matricular-se no curso escolhido, o aluno terá um tempo específico determinado para assistir todas as aulas, cada módulo possui o seu próprio tempo. Durante o progresso do aluno em um curso específico, a sua evolução (% de conclusão) será monitorada e seu estado registrado, bem como o desempenho desse aluno nas atividades realizadas durante a formação. Permitindo que tanto professores quanto administradores acompanhem o desempenho de cada aluno nos módulos. No final do curso o aluno deve receber orientação de um professor para desenvolver o trabalho de final de curso (TCC).
Ao final do curso, o sistema será capaz de emitir certificados digitais para os alunos que concluírem todos os módulos, além de possuir pelo menos um aproveitamento de 70% na média de acertos nas questões das atividades avaliativas. Cada certificado conterá um código único para verificação de autenticidade e poderá ser acessado online. Além da possibilidade de obter um certificado, o aluno pode avaliar os módulos, optando por uma avaliação de 1 a 5 estrelas, ao final será gerada uma nota média do curso.
A plataforma também será capaz de gerar relatórios detalhados sobre o andamento dos cursos para cada aluno(quantas aulas já foram assistidas), desempenho dos alunos, cursos mais populares (aqueles com maior quantidade de alunos inscritos) e melhor avaliados, quantidade de certificados emitidos e tempo médio de conclusão dos alunos nos cursos.

### CONSIDERE ALGUMAS REGRAS
Apenas o aluno que concluir todos os módulos de um curso e obtiver um aproveitamento de pelo menos 70% nos exercícios, poderá emitir um certificado.
Apenas pessoas com certificado de conclusão do ensino médio podem se matricular na plataforma
Um aluno poderá realizar apenas um curso por vez, não podendo matricular-se simultaneamente em dois ou mais cursos
A matrícula nos módulos devem considerar os pré-requisitos  do módulo.
Cada curso terá um prazo limite para ser concluído. Se o aluno não concluir o curso dentro desse prazo, ele perderá o acesso ao conteúdo e não poderá emitir o certificado.

### DIVISÃO DE TAREFAS

#### 1) Kalel
* Pessoa: implementação da classe base para representar todos os usuários do sistema.
* Professor: desenvolvimento da classe para gerenciar informações dos professores, incluindo especialização e formação.
* Administrador: criação da classe para gerenciar as funcionalidades exclusivas dos administradores na plataforma.
* Orientacao: implementação da classe para registro de orientação de TCC.
* Modulo: desenvolvimento da classe para gerenciar informações de cada módulo, incluindo pré-requisitos.
* Aula: implementação da estrutura de aulas dentro dos módulos, incluindo links para vídeos e textos.
* AtividadeAvaliativa: criação da classe para gerenciar as atividades avaliativas.
Universidade: desenvolvimento da classe que centraliza informações sobre a instituição de ensino.

#### 2) Igor
* Endereco:  implementação da classe para guardar informações do endereço dos usuários.
* Aluno:  desenvolvimento da classe de representação dos alunos da universidade.
* Certificado: classe para representar os certificados emitidos aos alunos que concluíram os cursos.
* EstadoAluno: classe para gerenciar o estado de progresso do aluno em relação ao curso.
* Matricula: classe para gerenciar a matrícula dos alunos nos cursos
* Curso: classe para representar os cursos, com informações como nome, descrição, carga horária e módulos associados.
* Questao: classe para gerenciar as questões das atividades avaliativas, incluindo alternativas e respostas corretas.

### DIAGRAMA UML 

Link do diagrama UML: https://app.diagrams.net/#G1F1Lb_8QGXCCdrmlmxBgRK-T-xfQcClvQ

### IMPLEMENTAÇÃO

Link do repositório do GitHub: https://github.com/IgorBandero/cursoead

