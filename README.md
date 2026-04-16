VOCÊ NO CONTROLE
 
 🧠 Do Zero ao Primeiro Sistema em Python

Tudo começou quando eu, ainda iniciante em Python, decidi criar meu primeiro projeto no terminal: um mini sistema de controle nutricional.

A ideia inicial era simples, quase básica, mas suficiente para me desafiar a aplicar tudo o que eu vinha aprendendo no estudo da linguagem.

🗺️ Planejamento e construção da ideia

Antes de escrever qualquer linha de código, comecei pelo mais importante: o planejamento.

Estruturei o fluxo do sistema, imaginando como ele funcionaria na prática:

abrir o menu principal
acessar ficha do usuário
registrar refeições
acompanhar a dieta
visualizar progresso

Esse processo de “desenhar o sistema” foi essencial para transformar uma ideia solta em algo estruturado.

🎨 Interface e visão do sistema

Mesmo sendo um projeto de terminal, eu quis pensar na experiência do usuário.

Estudando um pouco sobre design de interfaces, cheguei até o Figma e fiz um esboço simples de como seria a estrutura do sistema, como se fosse uma interface visual, mesmo que ele rodasse apenas no terminal.

Isso me ajudou a pensar melhor na organização dos menus e na lógica de navegação.

💻 Construção do backend (em Python puro)

Com a base planejada, comecei a implementação utilizando os conhecimentos que já tinha:

lógica de programação
entrada e saída de dados
estruturas condicionais (if/else/elif)
laços de repetição (while e for)
funções (def)
listas e dicionários

Durante esse processo, percebi na prática como o código começa a fazer sentido quando quebramos problemas grandes em pequenas funções.

💾 Persistência de dados com JSON

Um dos primeiros desafios foi entender como salvar informações para não perder tudo ao fechar o programa.

Foi aí que comecei a estudar e aplicar o uso de arquivos JSON, com ajuda de conteúdos e referências como canais de programação no YouTube (ex: Otávio Miranda e Hashtag Programação).

Com isso, consegui salvar dados como:

ficha do usuário
refeições do dia
progresso da dieta
📅 Automação e lógica de tempo

Um dos recursos mais interessantes do projeto foi a implementação do reset diário da dieta.

Para isso, utilizei o módulo datetime do Python, permitindo que o sistema identificasse a mudança de dia e reiniciasse os dados automaticamente.

🍽️ Cálculo nutricional e base científica

Na parte de cálculo, utilizei a fórmula de Harris-Benedict para estimar o TMB (Taxa Metabólica Basal), além de fatores de atividade para estimar gasto calórico total.

Também trabalhei com estimativas de déficit e superávit calórico para definir metas de dieta.

📊 Base de alimentos

Criei um dicionário com diversos alimentos e seus valores nutricionais (aproximadamente 70 itens), baseado em tabelas nutricionais públicas como a TACO (Tabela Brasileira de Composição de Alimentos).

⚙️ Evolução durante o desenvolvimento

Durante o desenvolvimento, aprendi também conceitos importantes como:

uso de with open para manipulação de arquivos
criação de funções auxiliares para inputs (perguntar_int, perguntar_float)
organização de código para evitar repetição
🧩 Aprendizado mais importante

No início, eu tinha receio de começar projetos maiores.

Mas ao longo do desenvolvimento, percebi que programação não é sobre “sair codando”, e sim sobre planejamento, divisão de problemas e construção por etapas.

Foi aí que o projeto começou a tomar forma de verdade.

🚀 Experiência pessoal

Esse projeto marcou minha evolução inicial com Python.

Mesmo sabendo que ainda existem melhorias a serem feitas, estou muito satisfeito com esse passo na minha jornada.

Além disso, aproveitei para aplicar também conhecimentos de Git e GitHub, realizando o versionamento e upload do projeto via terminal.

📌 Tecnologias utilizadas
Python
JSON
datetime
Git & GitHub
🎯 Objetivo do projeto

Criar um sistema funcional de controle nutricional no terminal, aplicando lógica de programação, estruturação de dados e persistência local, como forma de aprendizado prático em Python.

<img width="600" height="645" alt="image" src="https://github.com/user-attachments/assets/ca8157f8-decc-462f-bea1-43bc0e35c1ed" /> 
Arquivo criado no Figma utilzado como base


