import sqlite3

conn = sqlite3.connect("nutricao.db")

conn.execute("ALTER TABLE usuario ADD COLUMN meta_proteina REAL")
conn.execute("ALTER TABLE usuario ADD COLUMN meta_carbo REAL")
conn.execute("ALTER TABLE usuario ADD COLUMN meta_gordura REAL")

conn.commit()
conn.close()

print("Colunas adicionadas com sucesso.")