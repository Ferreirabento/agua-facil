import sqlite3

bancoDeDados = "aguaFacil.sql"

def conectar():
    conectando = sqlite3.connect(bancoDeDados)
    conectando.row_factory = sqlite3.Row
    return conectando

def criar_tabela_produtos():
    conexao = conectar()
    conexao.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL,
        estoque_minimo INTEGER NOT NULL,
        ativo INTEGER NOT NULL DEFAULT 1
        )""")

    conexao.commit()
    conexao.close()

def adicionar(nome, preco, estoque, estoque_minimo):
    conexao = conectar()
    conexao.execute("""
    INSERT INTO produtos (nome, preco, estoque, estoque_minimo)
    VALUES (?, ?, ?, ?)
    """, (nome, preco, estoque, estoque_minimo))
    conexao.commit()
    conexao.close()


def consultar():
    conexao = conectar()
    produtos = conexao.execute("""
    SELECT * FROM produtos
    WHERE ativo = 1
    ORDER BY nome
    """).fetchall()
    conexao.close()
    return produtos