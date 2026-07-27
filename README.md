# Você no Controle

Sistema web de controle nutricional: cálculo de meta calórica e de macronutrientes, registro de refeições, acompanhamento diário de progresso e histórico por data.

Este projeto nasceu como uma aplicação de terminal (Python puro + JSON) e foi migrado para uma aplicação web completa em Flask + SQLite, aplicando modelagem de dados relacional, separação de camadas e boas práticas de desenvolvimento web.

## Stack

- **Backend:** Python + Flask
- **Banco de dados:** SQLite
- **Front-end:** HTML + CSS + JavaScript puro (sem frameworks)

## Funcionalidades

- Cadastro de ficha do usuário (idade, peso, altura, nível de atividade, objetivo)
- Cálculo de TMB via fórmula de Harris-Benedict, ajustado por nível de atividade
- Cálculo de meta calórica diária (déficit para cut, superávit para bulk, ou manutenção)
- Cálculo de metas de macronutrientes (proteína, carboidrato, gordura) por kg de peso corporal, com valores baseados em literatura de nutrição esportiva (ISSN Position Stand 2017, Helms et al. 2014, Schoenfeld & Aragon 2018)
- Base de 75 alimentos (referência TACO) com valores nutricionais por 100g
- Registro de refeições do dia, com cálculo automático de calorias e macros consumidos
- Tela de progresso diário: comparação visual entre consumido e meta, por caloria e por macronutriente, com aviso quando um macro está desbalanceado
- Histórico de dias anteriores, com resumo visual de consumo por dia
- Tratamento de erro em formulários (validação server-side, sem quebra da aplicação em entrada inválida)
- Páginas de erro customizadas (404/500)

## Decisões técnicas

**Por que SQLite, e não outro banco:** o projeto é single-user, sem necessidade de servidor de banco separado — SQLite elimina fricção de configuração de ambiente sem sacrificar modelagem relacional real (três tabelas normalizadas, chaves estrangeiras, integridade referencial ativa via `PRAGMA foreign_keys`).

**Reset diário sem lógica de "reset":** a versão original em terminal precisava de uma rotina explícita para detectar mudança de dia e zerar os dados. Na versão web, isso deixou de ser necessário: cada refeição registrada carrega sua própria data, então o histórico nunca é sobrescrito — o "dia atual" é apenas um filtro de consulta, não um estado que precisa ser resetado.

**Cálculo de macros feito via JOIN, não pré-calculado:** os valores de calorias/proteína/carboidrato/gordura de cada refeição não são armazenados prontos no banco — são calculados no momento da consulta, multiplicando a quantidade registrada pelos valores nutricionais do alimento (via `JOIN` entre `registro_refeicao` e `alimento`). Isso evita duplicação de dado e mantém uma única fonte de verdade para os valores nutricionais.

**Separação de camadas:** `app.py` cuida exclusivamente de rotas (entrada de requisição, orquestração, resposta); `database.py` cuida exclusivamente de acesso a dados. Nenhuma rota executa SQL diretamente.

**Sem login/múltiplos usuários:** decisão consciente de escopo — o sistema foi desenhado para uso pessoal único, evitando complexidade de autenticação sem propósito real no estágio atual do projeto.

## Como rodar localmente

```bash
git clone https://github.com/vitorrodrigues-dev/voc-_no_controle.git
cd voc-_no_controle

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt

python seed.py                # cria o banco e popula a base de alimentos
python app.py                  # inicia o servidor
```

Acesse `http://127.0.0.1:5000` no navegador.

## Estrutura do projeto

voc-_no_controle/
├── app.py # rotas Flask
├── database.py # acesso a dados (SQLite)
├── schema.sql # definição das tabelas
├── seed.py # popula o banco com a base de alimentos
├── templates/ # HTML (Jinja2, herança via base.html)
├── static/
│ ├── css/style.css
│ └── js/script.js
└── legado/ # versão original em terminal (pré-migração)

## Sobre a pasta `legado/`

Contém a implementação original do projeto: um sistema de terminal em Python puro, com persistência em JSON, que deu origem à versão web atual. Mantida no repositório como registro da evolução do projeto, não como parte funcional da aplicação atual.