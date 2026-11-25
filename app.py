from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from database import (criar_tabela_produtos, adicionar_produtos, consultar_produtos, atualizar_produtos, deletar_produtos, buscar_produto,
criar_tabela_clientes, adicionar_clientes, consultar_clientes, atualizar_clientes, buscar_cliente, deletar_cliente,
criar_tabelas_pedidos, consultar_pedidos, adicionar_pedidos, 
criar_tabela_iten_pedido, adicionar_itens_pedidos)

app = Flask(__name__)

criar_tabela_produtos()
criar_tabela_clientes()
criar_tabelas_pedidos()
criar_tabela_iten_pedido()

@app.template_filter('data_br')
def data_br(valor):
    data = datetime.fromisoformat(valor)
    return data.strftime('%d-%m-%y')

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

    return render_template('sobre.html', sobre=sobre)

@app.route('/produtos')
def produtos():
    return render_template('produtos.html', produtos=consultar_produtos())

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
        adicionar_produtos(nome, preco, estoque, estoque_minimo)
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
        atualizar_produtos(id, nome, preco, estoque, estoque_minimo)
        return redirect(url_for('produtos'))
    return render_template('editar_produtos.html', produto=produto)

@app.route('/produtos/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_produto(id):
    produto = buscar_produto(id)
    if produto is None:
        return "produto não encontrado", 404
    if request.method == 'POST':    
        deletar_produtos(id)
        return redirect(url_for('produtos'))
    return render_template('produtos.html', produtos=consultar_produtos)

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

@app.route('/clientes/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_cliente(id):
    cliente = buscar_cliente(id)
    if cliente is None:
        return "Cliente não encontrado", 404
    if request.method == 'POST':
        deletar_cliente(id)
        return redirect(url_for('clientes'))
    return render_template('clientes.html', clinte=consultar_clientes())

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html', pedidos=consultar_pedidos())

@app.route('/pedidos/novo', methods=['GET', 'POST'])
def novo_pedido():

    listar_cliente = consultar_clientes()
    listar_produtos = consultar_produtos()

    # Primeira linha vazia
    linhas = [
        {
            'produto_id': '',
            'quantidade': ''
        }
    ]

    if request.method == 'POST':

        # Recupera todos os produtos e quantidades enviados
        produto_ids = request.form.getlist('produto_id')
        quantidades = request.form.getlist('quantidade')

        # Organiza os dados em uma lista de dicionários
        linhas = []

        for produto_id, quantidade in zip(produto_ids, quantidades):
            linhas.append({
                'produto_id': produto_id,
                'quantidade': quantidade
            })

        # Verifica qual botão foi pressionado
        acao = request.form.get('acao')

        if acao == 'adicionar_item':

            # Acrescenta uma nova linha vazia
            linhas.append({
                'produto_id': '',
                'quantidade': ''
            })

        elif acao == 'cadastrar':
            return "O cadastro definitivo será implementado na próxima etapa."

    return render_template(
        'novo_pedido.html',
        clientes=listar_cliente,
        produtos=listar_produtos,
        linhas=linhas
    )


if __name__ == "__main__":
    app.run(debug=True)