from flask import Flask, render_template, request, redirect, url_for
from database import criar_tabela_produtos, consultar, adicionar

app = Flask(__name__)

criar_tabela_produtos()

@app.route('/')
def inicio():
    return 'Pagina Inicial'

@app.route('/sobre')
def sobre():

    sobre = [
        {
            "informacao": "O miriti é o nome dado à fibra leve e flexível extraída do pecíolo (talo da folha) da palmeira buritizeiro (Mauritia flexuosa), nativa das áreas alagadiças da Amazônia e do Cerrado.  Conhecido popularmente como o 'isopor natural da Amazônia', esse material é biodegradável e sustentável, pois sua obtenção não exige o derrubamento da árvore, apenas a poda criteriosa das folhas mais velhas."
        }
    ]

    return render_template('sobre.html', sobre=sobre)

@app.route('/produtos')
def produtos():
    return render_template('produtos.html', produtos=consultar())

@app.route('/produtos/novo', methods=('GET', 'POST'))
def novo_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        estoque = int(request.form['estoque'])
        estoque_minimo = int(request.form['estoque_minimo'])
        adicionar(nome, preco, estoque, estoque_minimo)
        return redirect(url_for('produtos'))
    return render_template('novo_produto.html')

@app.route('/clientes')
def clientes():
    return 'Pagina de Clientes'

if __name__ == "__main__":
    app.run(debug=True)