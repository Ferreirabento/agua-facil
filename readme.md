# 💧 Água Fácil — Sistema Miriti

Projeto desenvolvido como parte dos meus estudos de **Python, Flask, desenvolvimento Web e Backend**.

A ideia inicial do projeto é criar um sistema para uma empresa de revenda de água, começando com uma aplicação Web simples e evoluindo gradualmente para páginas dinâmicas, organização de produtos, clientes e outras funcionalidades.

> 🚧 **Status:** Em desenvolvimento
> 📚 **Objetivo atual:** Estudo de Flask, rotas, templates HTML, Jinja2 e integração entre Python e HTML.

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **Flask**
* **HTML5**
* **Jinja2**
* **Ambiente virtual (`venv`)**
* **Linux / CachyOS**
* **Git e GitHub**

---

# 📁 Estrutura inicial do projeto

O projeto começou com a criação de uma pasta para a aplicação:

```bash
mkdir myproject
cd myproject
```

Depois foi criado um ambiente virtual Python:

```bash
python3 -m venv .venv
```

O ambiente virtual permite instalar as dependências do projeto de forma isolada, evitando misturar os pacotes dessa aplicação com os pacotes Python do sistema.

---

# 🐍 Ambiente virtual no Fish Shell

Como estou utilizando o **Fish Shell**, primeiro verifiquei qual shell estava sendo utilizado:

```bash
echo $SHELL
```

Depois ativei o ambiente virtual com:

```bash
source .venv/bin/activate.fish
```

Para conferir qual interpretador Python estava sendo utilizado:

```bash
which python
```

A ideia é que o resultado aponte para o Python localizado dentro do ambiente virtual `.venv`.

Por fim, instalei o Flask:

```bash
pip install flask
```

---

# 🚀 Primeiro Flask

Criei o arquivo:

```text
app.py
```

E comecei com uma aplicação extremamente simples:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "ola agua facil"

if __name__ == "__main__":
    app.run(debug=True)
```

## O que esse código faz?

### Importação do Flask

```python
from flask import Flask
```

Importa a classe `Flask`, que será utilizada para criar a aplicação Web.

### Criando a aplicação

```python
app = Flask(__name__)
```

Aqui é criada a aplicação Flask.

O `__name__` ajuda o Flask a identificar onde a aplicação está localizada.

### Criando uma rota

```python
@app.route("/")
def inicio():
    return "ola agua facil"
```

A função `inicio()` será executada quando o usuário acessar a rota:

```text
/
```

Ou seja, a página inicial.

### Executando o programa

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Isso faz com que o servidor Flask seja iniciado quando o arquivo `app.py` for executado diretamente.

O parâmetro:

```python
debug=True
```

ativa o modo de desenvolvimento do Flask, permitindo, entre outras coisas, que alterações no código sejam detectadas automaticamente durante o desenvolvimento.

---

# ▶️ Executando a aplicação

Depois de ativar novamente o ambiente virtual:

```bash
source .venv/bin/activate.fish
```

executei:

```bash
python app.py
```

O Flask iniciou um servidor local e disponibilizou a aplicação em:

```text
http://127.0.0.1:5000
```

O endereço `127.0.0.1` representa o próprio computador, enquanto a porta `5000` é a porta utilizada pelo servidor Flask nesse projeto.

---

# 🌐 Criando novas páginas

Depois do primeiro teste, comecei a criar novas rotas.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'ola agua facil'

@app.route('/sobre')
def sobre():
    return 'sistema miriti'

if __name__ == "__main__":
    app.run(debug=True)
```

Agora a aplicação possui duas páginas:

| Rota     | Função                 |
| -------- | ---------------------- |
| `/`      | Página inicial         |
| `/sobre` | Página sobre o sistema |

Por exemplo:

```text
http://127.0.0.1:5000/
```

e:

```text
http://127.0.0.1:5000/sobre
```

---

# 📦 Criando Produtos e Clientes

Continuei adicionando rotas para representar partes do futuro sistema:

```python
@app.route('/produtos')
def produtos():
    return 'Pagina de Produtos'

@app.route('/clientes')
def clientes():
    return 'Pagina de Clientes'
```

A aplicação passou a ter:

```text
/
├── Página inicial
│
├── /sobre
│   └── Informações sobre o sistema
│
├── /produtos
│   └── Página de produtos
│
└── /clientes
    └── Página de clientes
```

Nesse momento, as páginas ainda retornavam apenas textos diretamente pelo Python.

---

# 🖥️ Separando Python e HTML

O próximo passo foi deixar de escrever todo o conteúdo da página diretamente dentro do Python.

Para isso, criei a pasta:

```text
templates/
```

E dentro dela:

```text
templates/
└── produtos.html
```

O Flask procura automaticamente os arquivos HTML dentro da pasta `templates`.

---

# 📄 Primeiro HTML

O arquivo `produtos.html` ficou inicialmente assim:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Produtos</title>
</head>

<body>

    <h1>Produtos</h1>

    <p>Garrafão 20L</p>
    <p>Água 500ml</p>

</body>
</html>
```

Agora o Flask pode entregar uma página HTML completa em vez de simplesmente retornar um texto.

---

# 🔗 Renderizando HTML com Flask

Para renderizar um arquivo HTML, utilizei:

```python
from flask import Flask, render_template
```

E a rota:

```python
@app.route('/produtos')
def produtos():
    return render_template('produtos.html')
```

> ⚠️ **Importante:** o nome correto da função é `render_template()`, e não `render_templates()`.

O Flask então procura:

```text
templates/produtos.html
```

e envia esse HTML para o navegador.

---

# 🔄 Enviando dados do Python para o HTML

Depois de conseguir renderizar uma página HTML, o próximo passo foi tornar a página dinâmica.

Criei uma lista de produtos no Python:

```python
@app.route('/produtos')
def produtos():

    produtos = [
        {
            "nome": "Agua fulanoDeTow 20L",
            "preco": 10
        }
    ]

    return render_template('produtos.html', produtos=produtos)
```

Aqui existe uma parte importante:

```python
produtos=produtos
```

O primeiro `produtos` é o nome que será utilizado dentro do HTML.

O segundo `produtos` é a variável criada no Python.

Assim, os dados podem ser enviados para o template.

---

# 🧩 Jinja2

O Flask utiliza o **Jinja2** como mecanismo de templates.

Com ele, podemos utilizar Python de maneira controlada dentro do HTML.

Por exemplo:

```html
{% for produto in produtos %}
```

indica que o template deve percorrer os produtos recebidos pelo Flask.

Para acessar os dados:

```html
{{ produto.nome }}
```

e:

```html
{{ produto.preco }}
```

---

# 📋 Exibindo os produtos

O template `produtos.html` ficou:

```html
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Produtos</title>
</head>

<body>

    <h1>Produtos</h1>

    {% for produto in produtos %}

    <div>
        <h2>{{ produto.nome }}</h2>

        <p>
            {{ produto.preco }}
        </p>
    </div>

    {% endfor %}

</body>

</html>
```

O resultado é que o HTML não precisa conhecer antecipadamente quais produtos existem.

O Python fornece os dados e o Jinja2 monta a página.

---

# 🔁 Fluxo da aplicação

O funcionamento pode ser entendido desta maneira:

```text
Navegador
    │
    │ GET /produtos
    ▼
Flask
    │
    │ executa a função produtos()
    ▼
Python
    │
    │ cria lista de produtos
    ▼
Jinja2
    │
    │ insere os dados no HTML
    ▼
templates/produtos.html
    │
    ▼
Navegador
```

Isso representa um dos conceitos que estou estudando no desenvolvimento Backend:

**dados → processamento → apresentação**

---

# 📖 Testando a página "Sobre"

Também utilizei o mesmo conceito na página `/sobre`.

A rota passou a enviar informações para um template:

```python
@app.route('/sobre')
def sobre():

    sobre = [
        {
            "informacao": "O miriti é o nome dado à fibra leve e flexível extraída do pecíolo (talo da folha) da palmeira buritizeiro (Mauritia flexuosa), nativa das áreas alagadiças da Amazônia e do Cerrado. Conhecido popularmente como o 'isopor natural da Amazônia', esse material é biodegradável e sustentável, pois sua obtenção não exige o derrubamento da árvore, apenas a poda criteriosa das folhas mais velhas."
        }
    ]

    return render_template('sobre.html', sobre=sobre)
```

O HTML pode então utilizar a variável enviada pelo Python.

Por exemplo:

```html
{% for informacao in sobre %}

<p>
    {{ informacao.informacao }}
</p>

{% endfor %}
```

---

# 📁 Estrutura atual

Neste estágio, a estrutura do projeto pode ser organizada desta forma:

```text
myproject/
│
├── .venv/
│   └── Ambiente virtual Python
│
├── templates/
│   ├── produtos.html
│   └── sobre.html
│
├── app.py
│
└── README.md
```

A pasta `.venv` é o ambiente virtual e **não deve ser enviada para o GitHub**.

Por isso, posteriormente será necessário criar um:

```text
.gitignore
```

com algo como:

```gitignore
.venv/
__pycache__/
*.pyc
```

---

# 🧠 O que aprendi até aqui

Durante essa primeira etapa do projeto, pratiquei:

* criação de ambiente virtual Python;
* utilização do `venv`;
* ativação de ambiente virtual no Fish Shell;
* instalação de bibliotecas com `pip`;
* criação de uma aplicação Flask;
* criação de rotas;
* execução de servidor local;
* utilização de `127.0.0.1`;
* utilização de portas;
* criação de páginas HTML;
* utilização da pasta `templates`;
* utilização do `render_template()`;
* passagem de dados do Python para o HTML;
* utilização de listas e dicionários;
* utilização de Jinja2;
* estruturas `{% for %}`;
* utilização de `{{ variavel }}` dentro do HTML;
* separação inicial entre Backend e apresentação.

---

# 🚧 Próximos passos

A aplicação ainda está em uma fase inicial. A ideia é evoluir o projeto gradualmente.

Possíveis próximos passos:

* [ ] Criar um layout base com HTML/CSS
* [ ] Criar `base.html`
* [ ] Utilizar `extends` e `block` do Jinja2
* [ ] Criar uma página de cadastro de produtos
* [ ] Criar cadastro de clientes
* [ ] Adicionar quantidade/estoque dos produtos
* [ ] Criar sistema de pedidos
* [ ] Criar banco de dados
* [ ] Utilizar SQLite inicialmente
* [ ] Aprender SQLAlchemy
* [ ] Criar operações CRUD
* [ ] Separar melhor as responsabilidades do projeto
* [ ] Adicionar CSS
* [ ] Criar uma API
* [ ] Trabalhar com autenticação
* [ ] Fazer deploy da aplicação

---

# 🎯 Objetivo do projeto

O objetivo do **Água Fácil / Sistema Miriti** não é apenas criar uma aplicação funcional, mas utilizar o projeto como laboratório para aprender desenvolvimento Backend.

A aplicação será construída gradualmente, começando pelo básico:

```text
Python
   ↓
Flask
   ↓
Rotas
   ↓
HTML
   ↓
Jinja2
   ↓
Dados
   ↓
Banco de dados
   ↓
CRUD
   ↓
API
   ↓
Aplicação completa
```

Dessa forma, cada nova funcionalidade representa uma etapa de aprendizado em **Python, Backend, bancos de dados e desenvolvimento Web**.

---

## 👨‍💻 Projeto de estudo

Projeto desenvolvido por **João Bento** como parte dos estudos em **Análise e Desenvolvimento de Sistemas**, com foco em Python, Backend, dados e desenvolvimento de aplicações Web.
