# 💧 Água Fácil — Estudos com Flask, Jinja e SQLite

Este projeto faz parte dos meus estudos de **Python para desenvolvimento web**, utilizando o framework **Flask**, templates **Jinja**, banco de dados **SQLite** e HTML.

A ideia inicial é construir, aos poucos, uma aplicação para o projeto **Água Fácil**, começando por conceitos simples de Flask e evoluindo para um sistema com produtos, clientes, pedidos, estoque e outras funcionalidades.

> **Objetivo principal:** não apenas construir o sistema, mas entender o que cada parte faz para conseguir recriá-lo futuramente sem depender de IA.

---

# 📚 Conteúdos estudados

Durante este projeto estou estudando:

* Python
* Flask
* Rotas
* HTTP
* GET e POST
* HTML
* Jinja
* Templates
* Herança de templates
* `render_template()`
* `url_for()`
* Formulários HTML
* SQLite
* SQL
* CRUD
* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`
* Parâmetros `?` em SQL
* Prevenção de SQL Injection
* `sqlite3.Row`
* Organização de projetos Flask

---

# 1. 🐍 Criando o projeto

Primeiro criei a pasta do projeto:

```bash
mkdir myproject
cd myproject
```

Depois criei um ambiente virtual Python:

```bash
python3 -m venv .venv
```

O ambiente virtual serve para manter as dependências desse projeto separadas das outras aplicações Python do computador.

---

# 2. 🔎 Verificando o Shell

Usei:

```bash
echo $SHELL
```

Esse comando mostra qual shell estou utilizando.

Como estou utilizando o **Fish**, a ativação do ambiente virtual é diferente do exemplo tradicional do Bash.

Ativei o ambiente com:

```bash
source .venv/bin/activate.fish
```

Depois verifiquei qual Python estava sendo utilizado:

```bash
which python
```

Isso é importante para confirmar que estou usando o Python dentro do ambiente virtual.

---

# 3. 📦 Instalando Flask

Com o ambiente virtual ativado:

```bash
pip install flask
```

O Flask é o framework Python que estou utilizando para criar a aplicação web.

---

# 4. 🚀 Primeiro Flask

Meu primeiro `app.py` foi:

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "ola agua facil"


if __name__ == "__main__":
    app.run(debug=True)
```

Depois de ativar novamente o ambiente virtual:

```bash
source .venv/bin/activate.fish
```

consegui executar:

```bash
python app.py
```

O Flask iniciou um servidor local e mostrou:

```text
http://127.0.0.1:5000
```

Esse endereço representa o servidor rodando localmente no meu próprio computador.

---

# 5. 🛣️ Entendendo as rotas

Depois comecei a criar novas páginas.

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "ola agua facil"


@app.route("/sobre")
def sobre():
    return "sistema miriti"


if __name__ == "__main__":
    app.run(debug=True)
```

Agora existem duas rotas:

```text
/
```

e:

```text
/sobre
```

Portanto:

```text
http://127.0.0.1:5000/
```

retorna:

```text
ola agua facil
```

Enquanto:

```text
http://127.0.0.1:5000/sobre
```

retorna:

```text
sistema miriti
```

---

# 6. ➕ Criando mais rotas

Continuei adicionando páginas:

```python
@app.route("/produtos")
def produtos():
    return "Pagina de Produtos"


@app.route("/clientes")
def clientes():
    return "Pagina de Clientes"
```

A aplicação passou a ter:

```text
/
├── /sobre
├── /produtos
└── /clientes
```

Essa foi minha primeira percepção de que uma aplicação Flask é basicamente composta por **rotas que executam funções Python**.

---

# 7. 🧱 Começando a utilizar HTML

Em vez de retornar apenas texto:

```python
return "Pagina de Produtos"
```

comecei a utilizar templates HTML.

Primeiro importei:

```python
from flask import Flask, render_template
```

> Atenção: o nome correto é `render_template`, no singular.
> `render_templates` não é a função utilizada pelo Flask.

Criei a pasta:

```text
templates/
```

E dentro dela:

```text
templates/
└── produtos.html
```

Meu HTML inicial:

```html
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>Produtos</title>
</head>

<body>

    <h1>Produtos</h1>

    <p>Garrafão 20L</p>
    <p>Água 500ml</p>

</body>

</html>
```

---

# 8. 🔄 `render_template()`

A rota passou a ser:

```python
@app.route("/produtos")
def produtos():
    return render_template("produtos.html")
```

O fluxo agora é:

```text
Navegador
    ↓
GET /produtos
    ↓
Flask
    ↓
função produtos()
    ↓
render_template()
    ↓
templates/produtos.html
    ↓
HTML
    ↓
Navegador
```

---

# 9. 📦 Passando dados do Python para o HTML

Depois fiz um teste colocando os produtos diretamente no Python:

```python
@app.route("/produtos")
def produtos():

    produtos = [
        {
            "nome": "Agua fulanoDeTow 20L",
            "preco": 10
        }
    ]

    return render_template(
        "produtos.html",
        produtos=produtos
    )
```

Aqui estou enviando uma variável chamada:

```python
produtos
```

para o template.

---

# 10. 🧩 Jinja

No HTML posso utilizar Jinja:

```html
{% for produto in produtos %}

<div>

    <h2>{{ produto.nome }}</h2>

    <p>
        {{ produto.preco }}
    </p>

</div>

{% endfor %}
```

Existem duas estruturas importantes:

## `{{ }}`

Usado para mostrar valores.

Exemplo:

```html
{{ produto.nome }}
```

Significa:

> Mostre o valor de `produto.nome`.

---

## `{% %}`

Usado para estruturas de controle do Jinja.

Exemplo:

```html
{% for produto in produtos %}
```

e:

```html
{% endfor %}
```

Isso permite percorrer uma lista.

---

# 11. 📝 Testando Jinja na página Sobre

Também fiz um teste passando informações do Python para `sobre.html`:

```python
@app.route("/sobre")
def sobre():

    sobre = [
        {
            "informacao": "O miriti é o nome dado à fibra leve e flexível extraída do pecíolo (talo da folha) da palmeira buritizeiro (Mauritia flexuosa), nativa das áreas alagadiças da Amazônia e do Cerrado. Conhecido popularmente como o 'isopor natural da Amazônia', esse material é biodegradável e sustentável, pois sua obtenção não exige o derrubamento da árvore, apenas a poda criteriosa das folhas mais velhas."
        }
    ]

    return render_template(
        "sobre.html",
        sobre=sobre
    )
```

Esse exercício me ajudou a entender que o Flask pode pegar dados do Python e entregá-los para o Jinja.

---

# 12. 🗄️ SQLite

Depois comecei a trabalhar com banco de dados.

O Python já possui uma biblioteca própria para SQLite:

```python
import sqlite3
```

Não preciso instalar SQLite com `pip` para utilizar a biblioteca básica do Python.

Meu objetivo passou a ser deixar de armazenar os produtos diretamente no Python:

```python
produtos = [
    ...
]
```

e passar a armazená-los em um banco de dados.

---

# 13. 📁 `database.py`

Criei um arquivo separado para concentrar as operações do banco:

```text
database.py
```

A ideia é separar:

```text
app.py
    ↓
rotas da aplicação


database.py
    ↓
operações com banco
```

---

# 14. 🔌 Conectando ao SQLite

Meu código:

```python
import sqlite3


bancoDeDados = "aguaFacil.db"


def conectar():

    conectando = sqlite3.connect(bancoDeDados)

    conectando.row_factory = sqlite3.Row

    return conectando
```

> Durante meus testes usei nomes diferentes para o arquivo (`aguaFacil.db` / `aguaFacil.sql`). O ideal é manter um único nome e extensão para evitar confusão.

---

# 15. 🧠 `sqlite3.Row`

Uma descoberta importante foi:

```python
conectando.row_factory = sqlite3.Row
```

Isso faz com que os resultados das consultas sejam mais fáceis de trabalhar.

Sem `row_factory`, um resultado poderia parecer:

```python
(1, "Garrafão 20L", 10.0, 43)
```

Com:

```python
sqlite3.Row
```

posso acessar os dados pelo nome da coluna:

```python
produto["nome"]
```

Isso combina muito bem com Jinja.

---

# 16. 🏗️ Criando a tabela de produtos

Criei:

```python
def criar_tabela_produtos():

    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL,
            estoque_minimo INTEGER NOT NULL,
            ativo INTEGER NOT NULL DEFAULT 1
        )
    """)

    conexao.commit()
    conexao.close()
```

A tabela possui:

```text
id
nome
preco
estoque
estoque_minimo
ativo
```

---

# 17. 🔑 Chave primária

Usei:

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
```

O `id` identifica cada produto.

Por exemplo:

```text
1 → Garrafão 20L
2 → Água 500ml
3 → Água 1,5L
```

O `AUTOINCREMENT` permite que o SQLite gere os IDs automaticamente.

---

# 18. ⚠️ Correção importante no código original

Minha primeira versão tinha:

```sql
id nome TEXT PRIMARY KEY
```

Isso estava incorreto.

O correto é separar as colunas:

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
```

---

# 19. 💾 `commit()` e `close()`

Depois de executar uma alteração:

```python
conexao.commit()
```

confirma a alteração no banco.

Depois:

```python
conexao.close()
```

fecha a conexão.

Fluxo:

```text
conectar()
    ↓
executar SQL
    ↓
commit()
    ↓
close()
```

---

# 20. ➕ Adicionando produtos

Criei uma função para inserir produtos:

```python
def adicionar(nome, preco, estoque, estoque_minimo):

    conexao = conectar()

    conexao.execute("""
        INSERT INTO produtos
        (nome, preco, estoque, estoque_minimo)
        VALUES (?, ?, ?, ?)
    """, (
        nome,
        preco,
        estoque,
        estoque_minimo
    ))

    conexao.commit()
    conexao.close()
```

Essa função utiliza:

```sql
INSERT INTO
```

para inserir um novo registro.

---

# 21. ❓ Por que utilizar `?`

Um conceito que achei muito importante foi o uso de:

```sql
VALUES (?, ?, ?, ?)
```

em vez de montar SQL com strings, como:

```python
f"INSERT INTO produtos VALUES ('{nome}', ...)"
```

Os `?` são parâmetros da consulta.

Isso ajuda a evitar **SQL Injection** e é a forma correta de passar valores para esse tipo de consulta.

Portanto:

```python
conexao.execute(
    """
    INSERT INTO produtos
    (nome, preco, estoque, estoque_minimo)
    VALUES (?, ?, ?, ?)
    """,
    (nome, preco, estoque, estoque_minimo)
)
```

é preferível a concatenar valores diretamente no SQL.

---

# 22. 🔎 Consultando produtos

Criei uma segunda função:

```python
def consultar():

    conexao = conectar()

    produtos = conexao.execute("""
        SELECT *
        FROM produtos
        WHERE ativo = 1
        ORDER BY nome
    """).fetchall()

    conexao.close()

    return produtos
```

Essa função utiliza:

```sql
SELECT
```

para consultar os produtos.

---

# 23. Entendendo o SELECT

```sql
SELECT *
FROM produtos
WHERE ativo = 1
ORDER BY nome
```

Significa:

```text
SELECT *
    ↓
selecione os dados

FROM produtos
    ↓
da tabela produtos

WHERE ativo = 1
    ↓
somente produtos ativos

ORDER BY nome
    ↓
ordene pelo nome
```

O:

```python
.fetchall()
```

retorna todos os resultados encontrados.

---

# 24. 🔗 Ligando Flask e banco

No `app.py` passei a importar as funções do banco:

```python
from flask import Flask, render_template

from database import (
    criar_tabela_produtos,
    consultar
)
```

Depois:

```python
app = Flask(__name__)

criar_tabela_produtos()
```

Isso garante que a tabela seja criada quando a aplicação for iniciada.

---

# 25. 📦 Produtos agora vêm do banco

A rota:

```python
@app.route("/produtos")
def produtos():
    return render_template(
        "produtos.html",
        produtos=consultar()
    )
```

Agora funciona assim:

```text
Navegador
    ↓
/produtos
    ↓
Flask
    ↓
consultar()
    ↓
SQLite
    ↓
SELECT
    ↓
produtos
    ↓
Jinja
    ↓
produtos.html
```

Esse foi um dos primeiros momentos em que o projeto deixou de ser apenas uma página estática.

---

# 26. 🧱 `base.html` e herança de templates

Depois comecei a estudar uma funcionalidade muito interessante do Jinja:

```text
{% extends %}
{% block %}
```

Criei:

```text
templates/
├── base.html
├── produtos.html
└── novo_produto.html
```

O `base.html` funciona como um **molde** para as outras páginas.

---

# 27. `base.html`

Minha estrutura:

```html
<!DOCTYPE html>

<html lang="pt-br">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>
        {% block title %}
            Água Fácil
        {% endblock %}
    </title>

    <link
        rel="stylesheet"
        href="{{ url_for('static', filename='css/style.css') }}"
    >

</head>

<body>

    <header>
        <h1>Água Fácil</h1>
    </header>

    <main>

        {% block content %}
        {% endblock %}

    </main>

</body>

</html>
```

---

# 28. 🧠 O que são os Blocks?

Os:

```jinja
{% block title %}
{% endblock %}
```

e:

```jinja
{% block content %}
{% endblock %}
```

definem espaços que podem ser preenchidos pelas páginas que utilizarem esse template.

Por isso considero o `base.html` como um **molde**.

A ideia é:

```text
base.html
│
├── estrutura HTML
├── cabeçalho
├── CSS
├── <main>
│
└── espaço para conteúdo
```

E outras páginas aproveitam essa estrutura.

---

# 29. ♻️ `extends`

No `produtos.html`:

```jinja
{% extends "base.html" %}
```

significa:

> Esta página utiliza `base.html` como modelo.

Depois posso preencher o bloco:

```jinja
{% block title %}
Produtos
{% endblock %}
```

e:

```jinja
{% block content %}

<h2>Produtos</h2>

{% endblock %}
```

---

# 30. Produtos utilizando o `base.html`

O template ficou:

```html
{% extends "base.html" %}

{% block title %}
Produtos
{% endblock %}

{% block content %}

<h2>Produtos</h2>

<a href="/produtos/novo">
    Novo Produto
</a>

{% for produto in produtos %}

<article>

    <h3>
        {{ produto["nome"] }}
    </h3>

    <p>
        R$ {{ "%.2f"|format(produto["preco"]) }}
    </p>

    <p>
        Estoque:
        {{ produto["estoque"] }}
    </p>

</article>

{% endfor %}

{% endblock %}
```

---

# 31. 🔗 Link para cadastro

Usei:

```html
<a href="/produtos/novo">
    Novo Produto
</a>
```

Esse link leva para:

```text
/produtos/novo
```

A intenção é que essa rota apresente o formulário de cadastro.

---

# 32. 📋 Formulário de novo produto

Criei:

```text
templates/novo_produto.html
```

O formulário contém:

```html
<form method="POST">

    <label for="nome">
        Nome
    </label>

    <input
        type="text"
        id="nome"
        name="nome"
        required
    >

    <label for="preco">
        Preço
    </label>

    <input
        type="number"
        id="preco"
        name="preco"
        min="0"
        required
    >

    <label for="estoque">
        Estoque
    </label>

    <input
        type="number"
        id="estoque"
        name="estoque"
        required
    >

    <label for="estoque_minimo">
        Estoque mínimo
    </label>

    <input
        type="number"
        id="estoque_minimo"
        name="estoque_minimo"
        required
    >

    <button type="submit">
        Cadastrar
    </button>

</form>
```

---

# 33. ⚠️ Correção importante no `novo_produto.html`

Durante meus estudos, escrevi algo semelhante a:

```html
{% extends "base.html" %}

{% block content %}
novo produto
{% endblock %}

{% block content %}
...
{% endblock %}
```

Isso possui dois `blocks` com o mesmo nome.

O correto é utilizar **um único `block content`**:

```html
{% extends "base.html" %}

{% block title %}
Cadastro de Novo Produto
{% endblock %}

{% block content %}

<h2>Novo Produto</h2>

<form method="POST">

    ...

</form>

{% endblock %}
```

Além disso, quando utilizamos `extends`, ele deve ficar no início do template, e não dentro de `<body>`.

---

# 34. 🧭 Rota do novo produto

No `app.py`:

```python
@app.route("/produtos/novo")
def novo_produto():
    return render_template("novo_produto.html")
```

Por enquanto essa rota apenas mostra o formulário.

Ainda falta fazer o formulário:

```text
HTML
 ↓
POST
 ↓
Flask
 ↓
request.form
 ↓
adicionar()
 ↓
SQLite
```

Esse será o próximo passo.

---

# 35. 🏗️ Estado atual da aplicação

Atualmente a aplicação possui aproximadamente esta estrutura:

```text
agua-facil/
│
├── .venv/
│
├── app.py
│
├── database.py
│
├── aguaFacil.db
│
├── templates/
│   ├── base.html
│   ├── produtos.html
│   ├── novo_produto.html
│   └── sobre.html
│
└── static/
    └── css/
        └── style.css
```

---

# 36. Fluxo atual

O fluxo dos produtos agora é:

```text
                    USUÁRIO
                       │
                       ▼
                /produtos
                       │
                       ▼
                    Flask
                       │
                       ▼
                  consultar()
                       │
                       ▼
                    SQLite
                       │
                     SELECT
                       │
                       ▼
                   produtos
                       │
                       ▼
                    Jinja
                       │
                       ▼
                produtos.html
                       │
                       ▼
                   navegador
```

---

# 37. O que já aprendi

Até aqui consegui entender os seguintes conceitos:

### Python

```python
import
def
return
list
dict
```

### Flask

```python
Flask()
@app.route()
app.run()
render_template()
```

### Jinja

```jinja
{{ variavel }}

{% for %}
{% endfor %}

{% extends %}
{% block %}
```

### HTML

```html
<form>
<input>
<label>
<button>
<a>
```

### SQLite

```python
sqlite3.connect()
commit()
close()
```

### SQL

```sql
CREATE TABLE
INSERT
SELECT
WHERE
ORDER BY
```

### Segurança

```text
?
```

como parâmetros SQL, evitando a montagem insegura de consultas através de strings.

---

# 38. 🧠 Conceito que preciso estudar mais: GET e POST

Ainda preciso aprofundar o funcionamento de:

```text
GET
POST
```

A ideia inicial é:

```text
GET
↓
pedir/consultar uma página ou informação
```

e:

```text
POST
↓
enviar dados para o servidor
```

No cadastro de produtos, o fluxo deverá ser:

```text
Usuário abre:

/produtos/novo

        ↓

GET

        ↓

Flask mostra o formulário
```

Depois:

```text
Usuário preenche:

Nome
Preço
Estoque
Estoque mínimo

        ↓

POST

        ↓

Flask recebe os dados

        ↓

SQLite

        ↓

INSERT

        ↓

produto salvo
```

---

# 39. 🧠 Conceito que preciso estudar mais: Jinja Blocks

Ainda preciso entender melhor:

```jinja
{% extends "base.html" %}
```

```jinja
{% block title %}
{% endblock %}
```

```jinja
{% block content %}
{% endblock %}
```

Minha compreensão atual é:

```text
base.html
    ↓
molde principal

produtos.html
    ↓
herda o molde

novo_produto.html
    ↓
herda o molde

sobre.html
    ↓
herda o molde
```

Isso evita repetir toda a estrutura HTML em cada página.

---

# 40. 🎯 Próximos passos

A evolução planejada para o projeto é:

```text
[✓] Criar ambiente virtual
[✓] Instalar Flask
[✓] Criar primeira rota
[✓] Criar múltiplas rotas
[✓] Criar templates
[✓] Passar dados Python → Jinja
[✓] Criar banco SQLite
[✓] Criar tabela de produtos
[✓] Consultar produtos
[✓] Utilizar Jinja
[✓] Criar base.html
[✓] Utilizar extends e blocks
[✓] Criar formulário de produto
[ ] Aprender GET e POST profundamente
[ ] Receber formulário com request.form
[ ] Inserir produto pelo formulário
[ ] Redirecionar após cadastro
[ ] Editar produto
[ ] Excluir/desativar produto
[ ] Criar CRUD completo
[ ] Criar clientes
[ ] Criar pedidos
[ ] Criar itens dos pedidos
[ ] Relacionar tabelas
[ ] Controlar estoque
[ ] Criar entregas
[ ] Criar caixa
[ ] Adicionar JavaScript
[ ] Melhorar CSS/mobile
```

---

# 🚰 Objetivo final

A ideia é transformar os estudos em um sistema semelhante a:

```text
                 ÁGUA FÁCIL
                      │
       ┌──────────────┼──────────────┐
       │              │              │
    CLIENTES       PRODUTOS       PEDIDOS
       │              │              │
       │           ESTOQUE           │
       │              │              │
       └──────────────┼──────────────┘
                      │
                   ENTREGAS
                      │
                    CAIXA
```

O objetivo não é apenas fazer uma aplicação que funcione.

Quero entender a relação entre:

```text
HTML
  ↕
Jinja
  ↕
Flask
  ↕
Python
  ↕
SQL
  ↕
SQLite
```

para conseguir desenvolver e manter o projeto de forma independente.

---

# 📌 Anotações importantes

## Ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate.fish
```

## Instalar Flask

```bash
pip install flask
```

## Executar

```bash
python app.py
```

## Servidor local

```text
http://127.0.0.1:5000
```

## Biblioteca SQLite

```python
import sqlite3
```

## Template

```python
render_template("arquivo.html")
```

## Passar dados para Jinja

```python
render_template(
    "produtos.html",
    produtos=produtos
)
```

## Mostrar variável no Jinja

```jinja
{{ produto["nome"] }}
```

## Loop

```jinja
{% for produto in produtos %}

...

{% endfor %}
```

## Herança

```jinja
{% extends "base.html" %}
```

## Blocos

```jinja
{% block content %}

...

{% endblock %}
```

## Consulta SQL parametrizada

```sql
VALUES (?, ?, ?, ?)
```

## Conexão SQLite

```python
conexao = sqlite3.connect("aguaFacil.db")
```

## Confirmar alterações

```python
conexao.commit()
```

## Fechar conexão

```python
conexao.close()
```

---

# 💡 Principal aprendizado até aqui

O projeto começou como:

```text
return "Olá Água Fácil"
```

e está evoluindo para:

```text
                    FLASK
                      │
             ┌────────┴────────┐
             │                 │
          ROTAS             TEMPLATES
             │                 │
          PYTHON              JINJA
             │                 │
             └────────┬────────┘
                      │
                    SQLITE
                      │
                     SQL
```

A próxima grande etapa é fazer o formulário de **Novo Produto realmente funcionar**, utilizando:

```text
<form method="POST">
        ↓
request.form
        ↓
validação
        ↓
adicionar()
        ↓
INSERT
        ↓
SQLite
        ↓
redirect()
        ↓
/produtos
```

Esse será o primeiro CRUD realmente funcional do Água Fácil.
