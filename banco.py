import sqlite3

conn = sqlite3.connect("finaceiro.db")
cursor = conn.cursor()


def criar_tabela():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            tipo TEXT NOT NULL,
            data TEXT NOT NULL
        )
    """)
    conn.commit()


def fechar():
    conn.close()