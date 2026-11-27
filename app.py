from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from database import (criar_tabela_produtos, adicionar_produtos, consultar_produtos, atualizar_produtos, deletar_produtos, buscar_produto,
criar_tabela_clientes, adicionar_clientes, consultar_clientes, atualizar_clientes, buscar_cliente, deletar_cliente,
criar_tabelas_pedidos, consultar_pedidos,
criar_tabela_iten_pedido)
from pedido_service import registrar_pedido

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

    linhas = [{'produto_id': '', 'quantidade': ''}]
    cliente_selecionado = ''

    if request.method == 'POST':
        cliente_selecionado = request.form.get('cliente_id', '')
        produto_ids = request.form.getlist('produto_id')
        quantidades = request.form.getlist('quantidade')

        if len(produto_ids) != len(quantidades):
            erro = "Os produtos e as quantidades enviados não correspondem."
            return render_template(
                'novo_pedido.html',
                clientes=listar_cliente,
                produtos=listar_produtos,
                linhas=linhas,
                cliente_selecionado=cliente_selecionado,
                erro=erro
            ), 400

        linhas = [
            {'produto_id': produto_id, 'quantidade': quantidade}
            for produto_id, quantidade in zip(produto_ids, quantidades)
        ]

        acao = request.form.get('acao')

        if acao == 'adicionar_item':
            linhas.append({'produto_id': '', 'quantidade': ''})

        elif acao == 'cadastrar':
            itens = []
            erro = None

            for linha in linhas:
                produto_id = linha['produto_id'].strip()
                quantidade = linha['quantidade'].strip()

                if not produto_id and not quantidade:
                    continue

                if not produto_id or not quantidade:
                    erro = "Preencha o produto e a quantidade de cada item."
                    break

                itens.append({
                    'produto_id': produto_id,
                    'quantidade': quantidade
                })

            if erro is None:
                try:
                    cliente_id = int(cliente_selecionado)
                    registrar_pedido(cliente_id, itens)
                    return redirect(url_for('pedidos'))
                except ValueError as erro_validacao:
                    erro = str(erro_validacao)
                except (TypeError, OverflowError):
                    erro = "Selecione um cliente válido."

            return render_template(
                'novo_pedido.html',
                clientes=listar_cliente,
                produtos=listar_produtos,
                linhas=linhas,
                cliente_selecionado=cliente_selecionado,
                erro=erro
            ), 400

    return render_template(
        'novo_pedido.html',
        clientes=listar_cliente,
        produtos=listar_produtos,
        linhas=linhas,
        cliente_selecionado=cliente_selecionado
    )


if __name__ == "__main__":
    app.run(debug=True)