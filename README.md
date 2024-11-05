### PROBLEMA
O projeto tem como objetivo desenvolver um **sistema de gerenciamento de cursos para uma universidade online**, utilizando princípios de Programação Orientada a Objetos (POO) em Python. Esse sistema visa organizar de maneira eficiente o processo de criação e administração de cursos, inscrição de alunos, acompanhamento de progresso, emissão de certificados e geração de relatórios de desempenho.

### ESCOPO
A plataforma permitirá o cadastro de novos cursos, incluindo informações detalhadas como nome, descrição, carga horária (cada curso possui uma quantidade X de horas-aula específicas), mensalidade e quantidade mínima e máxima de semestres. Cada curso será composto por diversos módulos, que também poderão ser cadastrados com suas devidas informações. Os professores também poderão ter suas informações gerenciadas, como nome, especialidade, formação, e-mail.
Os alunos poderão se inscrever na plataforma, sendo que seus dados, como nome, e-mail, endereço, serão registrados no sistema. Após o cadastro de um aluno na plataforma, é gerada uma matrícula única e ele poderá optar por qual curso, dentre aqueles disponíveis na plataforma, ele deseja iniciar, levando em consideração a mensalidade, carga horária e a quantidade de semestres do curso. Será possível matricular o aluno nos módulos, bem como registrar as notas finais obtidas em cada módulo cursado, buscar o progresso do aluno no curso através de método específico e do desempenho desse aluno nos módulos cursados durante a formação. Permitindo que professores acompanhem o desempenho de cada aluno. No final do curso o aluno deve receber orientação de um professor para desenvolver o trabalho de final de curso (TCC).
Ao final do curso, o sistema será capaz de emitir certificados para os alunos que concluírem todos os módulos de um curso. Além da possibilidade de obter um certificado, o aluno pode avaliar os módulos, dando  uma nota de 1 a 10, ao final será gerada uma nota de avaliação média do curso.
A plataforma também será capaz de gerar relatórios detalhados sobre tempo médio de conclusão dos cursos, relatório das atividades avaliativas, dos cursos mais populares (aqueles com maior quantidade de alunos inscritos), e dos cursos melhor avaliados. 


### CONSIDERE ALGUMAS REGRAS
Não é permitido o cadastro duplicado de alunos e cursos
Apenas o aluno que concluir todos os módulos de um curso poderá emitir um certificado.
Não será possível cadastrar uma Atividade Avaliativa se não houverem questões cadastradas
Não será possível cadastrar um aluno se não houverem cursos cadastrados
Um aluno poderá realizar apenas um curso por vez, não podendo matricular-se simultaneamente em dois ou mais cursos

### DIVISÃO DE TAREFAS

#### 1) Kalel
* Pessoa: implementação da classe base para representar todos os usuários do sistema.
* Professor: desenvolvimento da classe para gerenciar informações dos professores, incluindo especialização e formação.
* Orientação: implementação da classe para registro de orientação de TCC.
* Módulo: desenvolvimento da classe para gerenciar informações de cada módulo, incluindo pré-requisitos.
* Questao: classe para gerenciar as questões das atividades avaliativas, incluindo alternativas e respostas corretas.
* AtividadeAvaliativa: criação da classe para gerenciar as atividades avaliativas.


#### 2) Igor
* Endereco:  implementação da classe para guardar informações do endereço dos usuários.
* Aluno:  desenvolvimento da classe de representação dos alunos da universidade.
* Certificado: classe para representar os certificados emitidos aos alunos que concluíram os cursos.
* Matricula: classe para gerenciar a matrícula dos alunos nos cursos
* Curso: classe para representar os cursos, com informações como nome, descrição, carga horária e módulos associados.
* Controlador de sistema: controlador principal do sistema

### DIAGRAMA UML 

Link do diagrama UML: https://app.diagrams.net/#G1UzeYze8jbGo7-l1-_ml9oWYumVcZ4Gpr#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

### IMPLEMENTAÇÃO

Link do repositório do GitHub: https://github.com/IgorBandero/cursoead

