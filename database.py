import sqlite3

bancoDeDados = "aguaFacil.sql"

def conectar():
    conectando = sqlite3.connect(bancoDeDados)
    conectando.row_factory = sqlite3.Row
    return conectando

def criar_tabela():
    conexao = conectar()
    conexao.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
        id nome TEXT PRIMARY KEY,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL,
        estoque_minimo INTEGER NOT NULL,
        ativo INTEGER NOT NULL DEFAULT 1
        )""")

    conexao.commit()
    conexao.close()


