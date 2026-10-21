import sqlite3

bancoDeDados = "aguaFacil.sql"

def conectar():
    conectando = sqlite3.connect(bancoDeDados)
    conectando.row_factory = sqlite3.Row
    return conectando

def criar_tabela_produtos():
    conexao = conectar()
    conexao.execute("""CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, preco REAL NOT NULL, estoque INTEGER NOT NULL, estoque_minimo INTEGER NOT NULL, ativo INTEGER NOT NULL DEFAULT 1)""")
    conexao.commit()
    conexao.close()

def criar_tabela_clientes():
    conexao = conectar()
    conexao.execute("""
    CREATE TABLE IF NOT EXIST clientes (
    id_cliente INTERGER PRIMARY KEY AUTOINCREMENT,
    id_produtos INTERGER,
    nomeCliente TEXT NOT NULL,
    telefone TEXT,
    CONSTRAINT fk_proClinte FOREIGN KEY (id_produtos) REFERENCES produtos (id)
    """)
    conexao.commit()
    conexao.close()

def adicionar(nome, preco, estoque, estoque_minimo):
    conexao = conectar()
    conexao.execute("""INSERT INTO produtos (nome, preco, estoque, estoque_minimo) VALUES (?, ?, ?, ?)""", (nome, preco, estoque, estoque_minimo))
    conexao.commit()
    conexao.close()


def consultar():
    conexao = conectar()
    produtos = conexao.execute("""SELECT * FROM produtos WHERE ativo = 1 ORDER BY nome""").fetchall()
    conexao.close()
    return produtos


def atualizar(id, nome, preco, estoque, estoque_minimo):
    conexao = conectar()
    conexao.execute("""UPDATE produtos SET nome = ?, preco = ?, estoque = ?, estoque_minimo = ? WHERE id = ?""", (nome, preco, estoque, estoque_minimo, id))
    conexao.commit()
    conexao.close()


def deletar(id):
    conexao = conectar()
    conexao.execute("""DELETE FROM produtos WHERE id = ?""", (id,))
    conexao.commit()
    conexao.close()


def buscar_produto(id):
    conexao = conectar()
    resultado = conexao.execute("""SELECT * FROM produtos WHERE id = ?""", (id,)).fetchone()
    conexao.close()
    return resultado