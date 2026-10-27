from flask import Flask, render_template, request, redirect, url_for
from database import criar_tabela_produtos, criar_tabela_clientes, consultar, consultar_clientes, adicionar, adicionar_clientes, atualizar, atualizar_clientes, deletar, buscar_produto, buscar_cliente

app = Flask(__name__)

criar_tabela_produtos()
criar_tabela_clientes()

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

    return render_template('sobre.html', sobre=sobre)

@app.route('/produtos')
def produtos():
    return render_template('produtos.html', produtos=consultar())

@app.route('/produtos/novo', methods=['GET', 'POST'])
def novo_produto():
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        if not nome:
            return "Nome é orbigatorio", 400
        try:
            preco = float(request.form['preco'])
        except ValueError:
            return "Necessario valor valido", 400
        try:
            estoque = int(request.form['estoque'])
        except ValueError:
            return "Necessario valor valido", 400
        try:
            estoque_minimo = int(request.form['estoque_minimo'])
        except ValueError:
            return "Necessario valor valido", 400
        adicionar(nome, preco, estoque, estoque_minimo)
        return redirect(url_for('inicio'))
    return render_template('novo_produto.html')

@app.route('/produtos/<int:id>/editar', methods=['GET', 'POST'])
def editar_produto(id):
    produto = buscar_produto(id)
    if produto is None:
        return "Produto não encontrado", 404
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        preco = float(request.form['preco'])
        estoque = int(request.form['estoque'])
        estoque_minimo = int(request.form['estoque_minimo'])
        atualizar(id, nome, preco, estoque, estoque_minimo)
        return redirect(url_for('produtos'))
    return render_template('editar_produtos.html', produto=produto)

@app.route('/produtos/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_produto(id):
    produto = buscar_produto(id)
    if produto is None:
        return "produto não encontrado", 404
    if request.method == 'POST':    
        deletar(id)
        return redirect(url_for('produtos'))
    return render_template('produtos.html', produtos=consultar())

@app.route('/clientes')
def clientes():
    return render_template('clientes.html', clientes=consultar_clientes())

@app.route('/clientes/novo', methods=['GET', 'POST'])
def novo_cliente():
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        if not nome:
            return "Nome do cliente é obrigatorio", 400
        try:
            telefone = str(request.form['telefone']).strip()
        except ValueError:
            return "Necessario valor valido", 400
        adicionar_clientes(nome, telefone)
        return redirect(url_for('inicio'))
    return render_template('novo_cliente.html')


@app.route('/clientes/<int:id>/editar', methods=['GET', 'POST'])
def editar_clientes(id):
    cliente = buscar_cliente(id)
    if cliente is None:
        return "Cliente não encontrado", 404
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        telefone = request.form['telefone'].strip()
        atualizar_clientes(id, nome, telefone)
        return redirect(url_for('clientes'))
    return render_template('editar_clientes.html', cliente=cliente)



if __name__ == "__main__":
    app.run(debug=True)