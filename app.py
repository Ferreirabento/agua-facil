from flask import Flask, render_template, request, redirect, url_for
from database import criar_tabela_produtos, consultar, adicionar, atualizar, deletar

app = Flask(__name__)

criar_tabela_produtos()

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

@app.route('/produtos/novo', methods=('GET', 'POST'))
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

"""@app.route('/clientes')
def clientes():
    return render_template('clientes.html')"""

if __name__ == "__main__":
    app.run(debug=True)