import sqlite3
from dieta import alimentos

DB = "nutricao.db"

def criar_banco():
    conn = sqlite3.connect(DB)
    with open("schema.sql", "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Tabelas criadas.")

def popular_alimentos():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    for nome, dados in alimentos.items():
        cursor.execute(
            """INSERT OR IGNORE INTO alimento
               (nome, categoria, kcal_100g, proteina_100g, carbo_100g, gordura_100g)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (nome, dados["categoria"], dados["kcal"], dados["prot"], dados["carbo"], dados["gord"])
        )

    conn.commit()
    conn.close()
    print(f"{len(alimentos)} alimentos inseridos (ou já existentes, ignorados).")

if __name__ == "__main__":
    criar_banco()
    popular_alimentos()