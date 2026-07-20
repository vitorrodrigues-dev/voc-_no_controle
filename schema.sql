CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    sexo TEXT NOT NULL CHECK(sexo IN ('M','F')),
    peso_atual REAL NOT NULL,
    peso_desejado REAL NOT NULL,
    altura REAL NOT NULL,
    nivel_atividade INTEGER NOT NULL CHECK(nivel_atividade BETWEEN 1 AND 4),
    objetivo INTEGER NOT NULL CHECK(objetivo IN (1,2,3)),
    tmb REAL,
    meta_calorica REAL,
    criado_em TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE alimento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    categoria TEXT NOT NULL,
    kcal_100g REAL NOT NULL,
    proteina_100g REAL NOT NULL,
    carbo_100g REAL NOT NULL,
    gordura_100g REAL NOT NULL
);

CREATE TABLE registro_refeicao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL REFERENCES usuario(id),
    alimento_id INTEGER NOT NULL REFERENCES alimento(id),
    data TEXT NOT NULL,
    nome_refeicao TEXT NOT NULL,
    gramas REAL NOT NULL,
    criado_em TEXT DEFAULT CURRENT_TIMESTAMP
);
