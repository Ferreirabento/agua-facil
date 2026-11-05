import sqlite3

bancoDeDados = "aguaFacil.sql"

def conectar():
    conectando = sqlite3.connect(bancoDeDados)
    conectando.row_factory = sqlite3.Row
    conectando.execute("PRAGMA foreign_key = ON")
    return conectando

def criar_tabela_produtos():
    conexao = conectar()
    conexao.execute("""CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, preco REAL NOT NULL, estoque INTEGER NOT NULL, estoque_minimo INTEGER NOT NULL, ativo INTEGER NOT NULL DEFAULT 1)""")
    conexao.commit()
    conexao.close()

def criar_tabela_clientes():
    conexao = conectar()
    conexao.execute("""CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, telefone TEXT, ativo INTEGER NOT NULL DEFAULT 1)""")
    conexao.commit()
    conexao.close()

def criar_tabelas_pedidos():
    conecxao = conectar()
    conectar.execute("""CREATE TABLE pedidos (id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_id INTEGER NOT NULL, data_pedido TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'Pendente', ativo INTEGER NOT NULL DEFAULT 1, FOREIGN KEY (cliente_id) REFERENCES clientes(id));""")
    conecxao.commit()
    conecxao.close()

def criar_tabela_iten_pedido():
    conexao = conectar()
    conexao.execute("""CREATE TABLE itens_pedido (id INTEGER PRIMARY KEY AUTOINCREMENT, pedido_id INTEGER NOT NULL, produto_id INTEGER NOT NULL, quantidade INTEGER NOT NULL, preco_unitario REAL NOT NULL, FOREIGN KEY (pedido_id) REFERENCES pedidos(id), FOREIGN KEY (produto_id) REFERENCES produtos(id));""")
    conexao.commit()
    conexao.close()

def adicionar_clientes(nome, telefone):
    conexao = conectar()
    conexao.execute("""INSERT INTO clientes (nome, telefone) VALUES (?, ?)""", (nome, telefone))
    conexao.commit()
    conexao.close()

def consultar_clientes():
    conexao = conectar()
    clientes = conexao.execute("""SELECT * FROM clientes WHERE ativo = 1 ORDER BY nome""").fetchall()
    conexao.close()
    return clientes

def atualizar_clientes(id, nome, telefone):
    conecxao = conectar()
    conecxao.execute("""UPDATE clientes SET nome = ?, telefone = ? WHERE id = ?""", (nome, telefone, id))
    conecxao.commit()
    conecxao.close()

def buscar_cliente(id):
    concxao = conectar()
    cliente = concxao.execute("""SELECT * FROM clientes WHERE id = ?""", (id,)).fetchone()
    concxao.close()
    return cliente

def deletar_cliente(id):
    conexao = conectar()
    conexao.execute("""DELETE FROM clientes WHERE id = ?""", (id,))
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