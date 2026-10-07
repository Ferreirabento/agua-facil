from flask import Flask, render_template
from database import criar_tabela_produtos

app = Flask(__name__)

criar_tabela_produtos()

@app.route('/')
def inicio():
    return 'ola agua facil'


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

    produtos = [
        {
            "nome": "Agua fulanoDeTow 20L",
            "preco": 10
        }
    ]

    return render_template('produtos.html', produtos=produtos)

@app.route('/clientes')
def clientes():
    return 'Pagina de Clientes'

if __name__ == "__main__":
    app.run(debug=True)