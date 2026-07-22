import sqlite3

DB = "nutricao.db"

def conectar():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def buscar_usuario():
    conn = conectar()
    usuario = conn.execute("SELECT * FROM usuario LIMIT 1").fetchone()
    conn.close()
    return usuario

def salvar_usuario(dados):
    conn = conectar()
    existente = conn.execute("SELECT id FROM usuario LIMIT 1").fetchone()

    if existente:
        conn.execute("""
            UPDATE usuario SET
                nome = ?, idade = ?, sexo = ?, peso_atual = ?, peso_desejado = ?,
                altura = ?, nivel_atividade = ?, objetivo = ?, tmb = ?, meta_calorica = ?,
                meta_proteina = ?, meta_carbo = ?, meta_gordura = ?
            WHERE id = ?
        """, (
            dados["nome"], dados["idade"], dados["sexo"], dados["peso_atual"],
            dados["peso_desejado"], dados["altura"], dados["nivel_atividade"],
            dados["objetivo"], dados["tmb"], dados["meta_calorica"],
            dados["meta_proteina"], dados["meta_carbo"], dados["meta_gordura"], existente["id"]
        ))
    else:
        conn.execute("""
            INSERT INTO usuario
                (nome, idade, sexo, peso_atual, peso_desejado, altura,
                 nivel_atividade, objetivo, tmb, meta_calorica,
                 meta_proteina, meta_carbo, meta_gordura)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            dados["nome"], dados["idade"], dados["sexo"], dados["peso_atual"],
            dados["peso_desejado"], dados["altura"], dados["nivel_atividade"],
            dados["objetivo"], dados["tmb"], dados["meta_calorica"],
            dados["meta_proteina"], dados["meta_carbo"], dados["meta_gordura"]
        ))

    conn.commit()
    conn.close()
    
def listar_alimentos():
    conn = conectar()
    alimentos = conn.execute("SELECT * FROM alimento ORDER BY categoria, nome").fetchall()
    conn.close()
    return alimentos

def registrar_refeicao(usuario_id, alimento_id, data, nome_refeicao, gramas):
    conn = conectar()
    conn.execute("""
        INSERT INTO registro_refeicao (usuario_id, alimento_id, data, nome_refeicao, gramas)
        VALUES (?, ?, ?, ?, ?)
    """, (usuario_id, alimento_id, data, nome_refeicao, gramas))
    conn.commit()
    conn.close()

def progresso_do_dia(usuario_id, data):
    conn = conectar()
    resultado = conn.execute("""
        SELECT
            SUM(r.gramas * a.kcal_100g / 100) AS total_kcal,
            SUM(r.gramas * a.proteina_100g / 100) AS total_prot,
            SUM(r.gramas * a.carbo_100g / 100) AS total_carbo,
            SUM(r.gramas * a.gordura_100g / 100) AS total_gord
        FROM registro_refeicao r
        JOIN alimento a ON a.id = r.alimento_id
        WHERE r.usuario_id = ? AND r.data = ?
    """, (usuario_id, data)).fetchone()
    conn.close()
    return resultado

def listar_refeicoes_do_dia(usuario_id, data):
    conn = conectar()
    refeicoes = conn.execute("""
        SELECT r.nome_refeicao, a.nome AS alimento, r.gramas,
               (r.gramas * a.kcal_100g / 100) AS kcal
        FROM registro_refeicao r
        JOIN alimento a ON a.id = r.alimento_id
        WHERE r.usuario_id = ? AND r.data = ?
        ORDER BY r.criado_em
    """, (usuario_id, data)).fetchall()
    conn.close()
    return refeicoes

def listar_dias_com_registro(usuario_id):
    conn = conectar()
    dias = conn.execute("""
        SELECT DISTINCT data
        FROM registro_refeicao
        WHERE usuario_id = ?
        ORDER BY data DESC
    """, (usuario_id,)).fetchall()
    conn.close()
    return dias