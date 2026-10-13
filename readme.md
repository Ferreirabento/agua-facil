**# 💧 Água Fácil — Estudos com Flask, Jinja e SQLite**



Este projeto faz parte dos meus estudos de **\*\*Python para desenvolvimento web\*\***, utilizando o framework **\*\*Flask\*\***, templates **\*\*Jinja\*\***, banco de dados **\*\*SQLite\*\*** e HTML.



A ideia inicial é construir, aos poucos, uma aplicação para o projeto **\*\*Água Fácil\*\***, começando por conceitos simples de Flask e evoluindo para um sistema com produtos, clientes, pedidos, estoque e outras funcionalidades.



\> **\*\*Objetivo principal:\*\*** não apenas construir o sistema, mas entender o que cada parte faz para conseguir recriá-lo futuramente sem depender de IA.



**---**



**# 📚 Conteúdos estudados**



Durante este projeto estou estudando:



\* Python

\* Flask

\* Rotas

\* HTTP

\* GET e POST

\* HTML

\* Jinja

\* Templates

\* Herança de templates

\* \`render_template()\`

\* \`url_for()\`

\* Formulários HTML

\* SQLite

\* SQL

\* CRUD

\* \`SELECT\`

\* \`INSERT\`

\* \`UPDATE\`

\* \`DELETE\`

\* Parâmetros \`?\` em SQL

\* Prevenção de SQL Injection

\* \`sqlite3.Row\`

\* Organização de projetos Flask



**---**



**# 1. 🐍 Criando o projeto**



Primeiro criei a pasta do projeto:



\`\`\`bash

mkdir myproject

cd myproject

\`\`\`



Depois criei um ambiente virtual Python:



\`\`\`bash

python3 -m venv .venv

\`\`\`



O ambiente virtual serve para manter as dependências desse projeto separadas das outras aplicações Python do computador.



**---**



**# 2. 🔎 Verificando o Shell**



Usei:



\`\`\`bash

echo $SHELL

\`\`\`



Esse comando mostra qual shell estou utilizando.



Como estou utilizando o **\*\*Fish\*\***, a ativação do ambiente virtual é diferente do exemplo tradicional do Bash.



Ativei o ambiente com:



\`\`\`bash

source .venv/bin/activate.fish

\`\`\`



Depois verifiquei qual Python estava sendo utilizado:



\`\`\`bash

which python

\`\`\`



Isso é importante para confirmar que estou usando o Python dentro do ambiente virtual.



**---**



**# 3. 📦 Instalando Flask**



Com o ambiente virtual ativado:



\`\`\`bash

pip install flask

\`\`\`



O Flask é o framework Python que estou utilizando para criar a aplicação web.



**---**



**# 4. 🚀 Primeiro Flask**



Meu primeiro \`app.py\` foi:



\`\`\`python

from flask import Flask



app = Flask(\_\_name\_\_)





@app.route("/")

def inicio():

&#x20;   return "ola agua facil"





if \_\_name\_\_ == "\_\_main\_\_":

&#x20;   app.run(debug=True)

\`\`\`



Depois de ativar novamente o ambiente virtual:



\`\`\`bash

source .venv/bin/activate.fish

\`\`\`



consegui executar:



\`\`\`bash

python app.py

\`\`\`



O Flask iniciou um servidor local e mostrou:



\`\`\`text

http\://127.0.0.1:5000

\`\`\`



Esse endereço representa o servidor rodando localmente no meu próprio computador.



**---**



**# 5. 🛣️ Entendendo as rotas**



Depois comecei a criar novas páginas.



\`\`\`python

from flask import Flask



app = Flask(\_\_name\_\_)





@app.route("/")

def inicio():

&#x20;   return "ola agua facil"





@app.route("/sobre")

def sobre():

&#x20;   return "sistema miriti"





if \_\_name\_\_ == "\_\_main\_\_":

&#x20;   app.run(debug=True)

\`\`\`



Agora existem duas rotas:



\`\`\`text

/

\`\`\`



e:



\`\`\`text

/sobre

\`\`\`



Portanto:



\`\`\`text

http\://127.0.0.1:5000/

\`\`\`



retorna:



\`\`\`text

ola agua facil

\`\`\`



Enquanto:



\`\`\`text

http\://127.0.0.1:5000/sobre

\`\`\`



retorna:



\`\`\`text

sistema miriti

\`\`\`



**---**



**# 6. ➕ Criando mais rotas**



Continuei adicionando páginas:



\`\`\`python

@app.route("/produtos")

def produtos():

&#x20;   return "Pagina de Produtos"





@app.route("/clientes")

def clientes():

&#x20;   return "Pagina de Clientes"

\`\`\`



A aplicação passou a ter:



\`\`\`text

/

├── /sobre

├── /produtos

└── /clientes

\`\`\`



Essa foi minha primeira percepção de que uma aplicação Flask é basicamente composta por **\*\*rotas que executam funções Python\*\***.



**---**



**# 7. 🧱 Começando a utilizar HTML**



Em vez de retornar apenas texto:



\`\`\`python

return "Pagina de Produtos"

\`\`\`



comecei a utilizar templates HTML.



Primeiro importei:



\`\`\`python

from flask import Flask, render_template

\`\`\`



\> Atenção: o nome correto é \`render_template\`, no singular.

\> \`render_templates\` não é a função utilizada pelo Flask.



Criei a pasta:



\`\`\`text

templates/

\`\`\`



E dentro dela:



\`\`\`text

templates/

└── produtos.html

\`\`\`



Meu HTML inicial:



\`\`\`html

\<!DOCTYPE html>

\<html lang="pt-br">



\<head>

&#x20;   \<meta charset="UTF-8">



&#x20;   \<meta

&#x20;       name="viewport"

&#x20;       content="width=device-width, initial-scale=1.0"

&#x20;   \>



&#x20;   \<title>Produtos\</title>

\</head>



\<body>



&#x20;   \<h1>Produtos\</h1>



&#x20;   \<p>Garrafão 20L\</p>

&#x20;   \<p>Água 500ml\</p>



\</body>



\</html>

\`\`\`



**---**



**# 8. 🔄 \`render_template()\`**



A rota passou a ser:



\`\`\`python

@app.route("/produtos")

def produtos():

&#x20;   return render_template("produtos.html")

\`\`\`



O fluxo agora é:



\`\`\`text

Navegador

&#x20;   ↓

GET /produtos

&#x20;   ↓

Flask

&#x20;   ↓

função produtos()

&#x20;   ↓

render_template()

&#x20;   ↓

templates/produtos.html

&#x20;   ↓

HTML

&#x20;   ↓

Navegador

\`\`\`



**---**



**# 9. 📦 Passando dados do Python para o HTML**



Depois fiz um teste colocando os produtos diretamente no Python:



\`\`\`python

@app.route("/produtos")

def produtos():



&#x20;   produtos = [

&#x20;       {

&#x20;           "nome": "Agua fulanoDeTow 20L",

&#x20;           "preco": 10

&#x20;       }

&#x20;   ]



&#x20;   return render_template(

&#x20;       "produtos.html",

&#x20;       produtos=produtos

&#x20;   )

\`\`\`



Aqui estou enviando uma variável chamada:



\`\`\`python

produtos

\`\`\`



para o template.



**---**



**# 10. 🧩 Jinja**



No HTML posso utilizar Jinja:



\`\`\`html

{% for produto in produtos %}



\<div>



&#x20;   \<h2>{{ produto.nome }}\</h2>



&#x20;   \<p>

&#x20;       {{ produto.preco }}

&#x20;   \</p>



\</div>



{% endfor %}

\`\`\`



Existem duas estruturas importantes:



**## \`{{ }}\`**



Usado para mostrar valores.



Exemplo:



\`\`\`html

{{ produto.nome }}

\`\`\`



Significa:



\> Mostre o valor de \`produto.nome\`.



**---**



**## \`{% %}\`**



Usado para estruturas de controle do Jinja.



Exemplo:



\`\`\`html

{% for produto in produtos %}

\`\`\`



e:



\`\`\`html

{% endfor %}

\`\`\`



Isso permite percorrer uma lista.



**---**



**# 11. 📝 Testando Jinja na página Sobre**



Também fiz um teste passando informações do Python para \`sobre.html\`:



\`\`\`python

@app.route("/sobre")

def sobre():



&#x20;   sobre = [

&#x20;       {

&#x20;           "informacao": "O miriti é o nome dado à fibra leve e flexível extraída do pecíolo (talo da folha) da palmeira buritizeiro (Mauritia flexuosa), nativa das áreas alagadiças da Amazônia e do Cerrado. Conhecido popularmente como o 'isopor natural da Amazônia', esse material é biodegradável e sustentável, pois sua obtenção não exige o derrubamento da árvore, apenas a poda criteriosa das folhas mais velhas."

&#x20;       }

&#x20;   ]



&#x20;   return render_template(

&#x20;       "sobre.html",

&#x20;       sobre=sobre

&#x20;   )

\`\`\`



Esse exercício me ajudou a entender que o Flask pode pegar dados do Python e entregá-los para o Jinja.



**---**



**# 12. 🗄️ SQLite**



Depois comecei a trabalhar com banco de dados.



O Python já possui uma biblioteca própria para SQLite:



\`\`\`python

import sqlite3

\`\`\`



Não preciso instalar SQLite com \`pip\` para utilizar a biblioteca básica do Python.



Meu objetivo passou a ser deixar de armazenar os produtos diretamente no Python:



\`\`\`python

produtos = [

&#x20;   ...

]

\`\`\`



e passar a armazená-los em um banco de dados.



**---**



**# 13. 📁 \`database.py\`**



Criei um arquivo separado para concentrar as operações do banco:



\`\`\`text

database.py

\`\`\`



A ideia é separar:



\`\`\`text

app.py

&#x20;   ↓

rotas da aplicação





database.py

&#x20;   ↓

operações com banco

\`\`\`



**---**



**# 14. 🔌 Conectando ao SQLite**



Meu código:



\`\`\`python

import sqlite3





bancoDeDados = "aguaFacil.sql"





def conectar():



&#x20;   conectando = sqlite3.connect(bancoDeDados)



&#x20;   conectando.row_factory = sqlite3.Row



&#x20;   return conectando

\`\`\`



\> Durante meus testes usei nomes diferentes para o arquivo (\`aguaFacil.db\` / \`aguaFacil.sql\`). O ideal é manter um único nome e extensão para evitar confusão.



**---**



**# 15. 🧠 \`sqlite3.Row\`**



Uma descoberta importante foi:



\`\`\`python

conectando.row_factory = sqlite3.Row

\`\`\`



Isso faz com que os resultados das consultas sejam mais fáceis de trabalhar.



Sem \`row_factory\`, um resultado poderia parecer:



\`\`\`python

(1, "Garrafão 20L", 10.0, 43)

\`\`\`



Com:



\`\`\`python

sqlite3.Row

\`\`\`



posso acessar os dados pelo nome da coluna:



\`\`\`python

produto["nome"]

\`\`\`



Isso combina muito bem com Jinja.



**---**



**# 16. 🏗️ Criando a tabela de produtos**



Criei:



\`\`\`python

def criar_tabela_produtos():



&#x20;   conexao = conectar()



&#x20;   conexao.execute("""

&#x20;       CREATE TABLE IF NOT EXISTS produtos (

&#x20;           id INTEGER PRIMARY KEY AUTOINCREMENT,

&#x20;           nome TEXT NOT NULL,

&#x20;           preco REAL NOT NULL,

&#x20;           estoque INTEGER NOT NULL,

&#x20;           estoque_minimo INTEGER NOT NULL,

&#x20;           ativo INTEGER NOT NULL DEFAULT 1

&#x20;       )

&#x20;   """)



&#x20;   conexao.commit()

&#x20;   conexao.close()

\`\`\`



A tabela possui:



\`\`\`text

id

nome

preco

estoque

estoque_minimo

ativo

\`\`\`



**---**



**# 17. 🔑 Chave primária**



Usei:



\`\`\`sql

id INTEGER PRIMARY KEY AUTOINCREMENT

\`\`\`



O \`id\` identifica cada produto.



Por exemplo:



\`\`\`text

1 → Garrafão 20L

2 → Água 500ml

3 → Água 1,5L

\`\`\`



O \`AUTOINCREMENT\` permite que o SQLite gere os IDs automaticamente.



**---**



**# 18. ⚠️ Correção importante no código original**



Minha primeira versão tinha:



\`\`\`sql

id nome TEXT PRIMARY KEY

\`\`\`



Isso estava incorreto.



O correto é separar as colunas:



\`\`\`sql

id INTEGER PRIMARY KEY AUTOINCREMENT,

nome TEXT NOT NULL,

\`\`\`



**---**



**# 19. 💾 \`commit()\` e \`close()\`**



Depois de executar uma alteração:



\`\`\`python

conexao.commit()

\`\`\`



confirma a alteração no banco.



Depois:



\`\`\`python

conexao.close()

\`\`\`



fecha a conexão.



Fluxo:



\`\`\`text

conectar()

&#x20;   ↓

executar SQL

&#x20;   ↓

commit()

&#x20;   ↓

close()

\`\`\`



**---**



**# 20. ➕ Adicionando produtos**



Criei uma função para inserir produtos:



\`\`\`python

def adicionar(nome, preco, estoque, estoque_minimo):



&#x20;   conexao = conectar()



&#x20;   conexao.execute("""

&#x20;       INSERT INTO produtos

&#x20;       (nome, preco, estoque, estoque_minimo)

&#x20;       VALUES (?, ?, ?, ?)

&#x20;   """, (

&#x20;       nome,

&#x20;       preco,

&#x20;       estoque,

&#x20;       estoque_minimo

&#x20;   ))



&#x20;   conexao.commit()

&#x20;   conexao.close()

\`\`\`



Essa função utiliza:



\`\`\`sql

INSERT INTO

\`\`\`



para inserir um novo registro.



**---**



**# 21. ❓ Por que utilizar \`?\`**



Um conceito que achei muito importante foi o uso de:



\`\`\`sql

VALUES (?, ?, ?, ?)

\`\`\`



em vez de montar SQL com strings, como:



\`\`\`python

f"INSERT INTO produtos VALUES ('{nome}', ...)"

\`\`\`



Os \`?\` são parâmetros da consulta.



Isso ajuda a evitar **\*\*SQL Injection\*\*** e é a forma correta de passar valores para esse tipo de consulta.



Portanto:



\`\`\`python

conexao.execute(

&#x20;   """

&#x20;   INSERT INTO produtos

&#x20;   (nome, preco, estoque, estoque_minimo)

&#x20;   VALUES (?, ?, ?, ?)

&#x20;   """,

&#x20;   (nome, preco, estoque, estoque_minimo)

)

\`\`\`



é preferível a concatenar valores diretamente no SQL.



**---**



**# 22. 🔎 Consultando produtos**



Criei uma segunda função:



\`\`\`python

def consultar():



&#x20;   conexao = conectar()



&#x20;   produtos = conexao.execute("""

&#x20;       SELECT \*

&#x20;       FROM produtos

&#x20;       WHERE ativo = 1

&#x20;       ORDER BY nome

&#x20;   """).fetchall()



&#x20;   conexao.close()



&#x20;   return produtos

\`\`\`



Essa função utiliza:



\`\`\`sql

SELECT

\`\`\`



para consultar os produtos.



**---**



**# 23. Entendendo o SELECT**



\`\`\`sql

SELECT \*

FROM produtos

WHERE ativo = 1

ORDER BY nome

\`\`\`



Significa:



\`\`\`text

SELECT \*

&#x20;   ↓

selecione os dados



FROM produtos

&#x20;   ↓

da tabela produtos



WHERE ativo = 1

&#x20;   ↓

somente produtos ativos



ORDER BY nome

&#x20;   ↓

ordene pelo nome

\`\`\`



O:



\`\`\`python

.fetchall()

\`\`\`



retorna todos os resultados encontrados.



**---**



**# 24. 🔗 Ligando Flask e banco**



No \`app.py\` passei a importar as funções do banco:



\`\`\`python

from flask import Flask, render_template



from database import (

&#x20;   criar_tabela_produtos,

&#x20;   consultar

)

\`\`\`



Depois:



\`\`\`python

app = Flask(\_\_name\_\_)



criar_tabela_produtos()

\`\`\`



Isso garante que a tabela seja criada quando a aplicação for iniciada.



**---**



**# 25. 📦 Produtos agora vêm do banco**



A rota:



\`\`\`python

@app.route("/produtos")

def produtos():

&#x20;   return render_template(

&#x20;       "produtos.html",

&#x20;       produtos=consultar()

&#x20;   )

\`\`\`



Agora funciona assim:



\`\`\`text

Navegador

&#x20;   ↓

/produtos

&#x20;   ↓

Flask

&#x20;   ↓

consultar()

&#x20;   ↓

SQLite

&#x20;   ↓

SELECT

&#x20;   ↓

produtos

&#x20;   ↓

Jinja

&#x20;   ↓

produtos.html

\`\`\`



Esse foi um dos primeiros momentos em que o projeto deixou de ser apenas uma página estática.



**---**



**# 26. 🧱 \`base.html\` e herança de templates**



Depois comecei a estudar uma funcionalidade muito interessante do Jinja:



\`\`\`text

{% extends %}

{% block %}

\`\`\`



Criei:



\`\`\`text

templates/

├── base.html

├── produtos.html

└── novo_produto.html

\`\`\`



O \`base.html\` funciona como um **\*\*molde\*\*** para as outras páginas.



**---**



**# 27. \`base.html\`**



Minha estrutura:



\`\`\`html

\<!DOCTYPE html>



\<html lang="pt-br">



\<head>



&#x20;   \<meta charset="UTF-8">



&#x20;   \<meta

&#x20;       name="viewport"

&#x20;       content="width=device-width, initial-scale=1.0"

&#x20;   \>



&#x20;   \<title>

&#x20;       {% block title %}

&#x20;           Água Fácil

&#x20;       {% endblock %}

&#x20;   \</title>



&#x20;   \<link

&#x20;       rel="stylesheet"

&#x20;       href="{{ url_for('static', filename='css/style.css') }}"

&#x20;   \>



\</head>



\<body>



&#x20;   \<header>

&#x20;       \<h1>Água Fácil\</h1>

&#x20;   \</header>



&#x20;   \<main>



&#x20;       {% block content %}

&#x20;       {% endblock %}



&#x20;   \</main>



\</body>



\</html>

\`\`\`



**---**



**# 28. 🧠 O que são os Blocks?**



Os:



\`\`\`jinja

{% block title %}

{% endblock %}

\`\`\`



e:



\`\`\`jinja

{% block content %}

{% endblock %}

\`\`\`



definem espaços que podem ser preenchidos pelas páginas que utilizarem esse template.



Por isso considero o \`base.html\` como um **\*\*molde\*\***.



A ideia é:



\`\`\`text

base.html

│

├── estrutura HTML

├── cabeçalho

├── CSS

├── \<main>

│

└── espaço para conteúdo

\`\`\`



E outras páginas aproveitam essa estrutura.



**---**



**# 29. ♻️ \`extends\`**



No \`produtos.html\`:



\`\`\`jinja

{% extends "base.html" %}

\`\`\`



significa:



\> Esta página utiliza \`base.html\` como modelo.



Depois posso preencher o bloco:



\`\`\`jinja

{% block title %}

Produtos

{% endblock %}

\`\`\`



e:



\`\`\`jinja

{% block content %}



\<h2>Produtos\</h2>



{% endblock %}

\`\`\`



**---**



**# 30. Produtos utilizando o \`base.html\`**



O template ficou:



\`\`\`html

{% extends "base.html" %}



{% block title %}

Produtos

{% endblock %}



{% block content %}



\<h2>Produtos\</h2>



\<a href="/produtos/novo">

&#x20;   Novo Produto

\</a>



{% for produto in produtos %}



\<article>



&#x20;   \<h3>

&#x20;       {{ produto["nome"] }}

&#x20;   \</h3>



&#x20;   \<p>

&#x20;       R$ {{ "%.2f"|format(produto["preco"]) }}

&#x20;   \</p>



&#x20;   \<p>

&#x20;       Estoque:

&#x20;       {{ produto["estoque"] }}

&#x20;   \</p>



\</article>



{% endfor %}



{% endblock %}

\`\`\`



**---**



**# 31. 🔗 Link para cadastro**



Usei:



\`\`\`html

\<a href="/produtos/novo">

&#x20;   Novo Produto

\</a>

\`\`\`



Esse link leva para:



\`\`\`text

/produtos/novo

\`\`\`



A intenção é que essa rota apresente o formulário de cadastro.



**---**



**# 32. 📋 Formulário de novo produto**



Criei:



\`\`\`text

templates/novo_produto.html

\`\`\`



O formulário contém:



\`\`\`html

\<form method="POST">



&#x20;   \<label for="nome">

&#x20;       Nome

&#x20;   \</label>



&#x20;   \<input

&#x20;       type="text"

&#x20;       id="nome"

&#x20;       name="nome"

&#x20;       required

&#x20;   \>



&#x20;   \<label for="preco">

&#x20;       Preço

&#x20;   \</label>



&#x20;   \<input

&#x20;       type="number"

&#x20;       id="preco"

&#x20;       name="preco"

&#x20;       min="0"

&#x20;       required

&#x20;   \>



&#x20;   \<label for="estoque">

&#x20;       Estoque

&#x20;   \</label>



&#x20;   \<input

&#x20;       type="number"

&#x20;       id="estoque"

&#x20;       name="estoque"

&#x20;       required

&#x20;   \>



&#x20;   \<label for="estoque_minimo">

&#x20;       Estoque mínimo

&#x20;   \</label>



&#x20;   \<input

&#x20;       type="number"

&#x20;       id="estoque_minimo"

&#x20;       name="estoque_minimo"

&#x20;       required

&#x20;   \>



&#x20;   \<button type="submit">

&#x20;       Cadastrar

&#x20;   \</button>



\</form>

\`\`\`



**---**



**# 33. ⚠️ Correção importante no \`novo_produto.html\`**



Durante meus estudos, escrevi algo semelhante a:



\`\`\`html

{% extends "base.html" %}



{% block content %}

novo produto

{% endblock %}



{% block content %}

...

{% endblock %}

\`\`\`



Isso possui dois \`blocks\` com o mesmo nome.



O correto é utilizar **\*\*um único \`block content\`\*\***:



\`\`\`html

{% extends "base.html" %}



{% block title %}

Cadastro de Novo Produto

{% endblock %}



{% block content %}



\<h2>Novo Produto\</h2>



\<form method="POST">



&#x20;   ...



\</form>



{% endblock %}

\`\`\`



Além disso, quando utilizamos \`extends\`, ele deve ficar no início do template, e não dentro de \`\<body>\`.



**---**



**# 34. 🧭 Rota do novo produto

No `app.py`, a rota do novo produto passou a aceitar **GET e POST**:

```python
@app.route('/produtos/novo', methods=['GET', 'POST'])
def novo_produto():
    if request.method == 'POST':
        nome = request.form['nome'].strip()

        if not nome:
            return "Nome é obrigatório", 400

        try:
            preco = float(request.form['preco'])
        except ValueError:
            return "Necessário valor válido", 400

        try:
            estoque = int(request.form['estoque'])
        except ValueError:
            return "Necessário valor válido", 400

        try:
            estoque_minimo = int(request.form['estoque_minimo'])
        except ValueError:
            return "Necessário valor válido", 400

        adicionar(nome, preco, estoque, estoque_minimo)

        return redirect(url_for('inicio'))

    return render_template('novo_produto.html')
```

Agora a rota possui dois comportamentos:

```text
GET
 ↓
mostrar formulário
```

e:

```text
POST
 ↓
receber dados
 ↓
validar
 ↓
adicionar()
 ↓
INSERT
 ↓
SQLite
 ↓
redirect()
```

---

# 35. 📩 Entendendo `request.form`

No formulário HTML existem campos como:

```html
<input type="text" name="nome">
<input type="number" name="preco">
<input type="number" name="estoque">
<input type="number" name="estoque_minimo">
```

O atributo `name` é importante porque é através dele que o Flask identifica cada valor recebido.

Por exemplo:

```python
nome = request.form['nome']
```

significa:

> Pegue do formulário o valor cujo nome é `nome`.

O fluxo é:

```text
HTML
 ↓
name="nome"
 ↓
POST
 ↓
request.form['nome']
 ↓
Python
```

---

# 36. 🔢 Conversão dos valores do formulário

Uma coisa importante aprendida foi que os valores recebidos pelo formulário precisam ser tratados antes de serem utilizados.

Por exemplo:

```python
preco = float(request.form['preco'])
```

transforma o valor recebido em `float`.

Para números inteiros:

```python
estoque = int(request.form['estoque'])
```

e:

```python
estoque_minimo = int(request.form['estoque_minimo'])
```

A ideia é:

```text
Formulário
 ↓
request.form
 ↓
string recebida
 ↓
float() ou int()
 ↓
valor utilizado pelo Python
```

Também comecei a utilizar `try` / `except` para evitar que valores inválidos provoquem um erro inesperado:

```python
try:
    preco = float(request.form['preco'])
except ValueError:
    return "Necessário valor válido", 400
```

---

# 37. 🔄 POST → banco → redirect

Depois da validação, o produto é enviado para:

```python
adicionar(nome, preco, estoque, estoque_minimo)
```

A função `adicionar()` executa:

```sql
INSERT INTO produtos
(nome, preco, estoque, estoque_minimo)
VALUES (?, ?, ?, ?)
```

Depois:

```python
conexao.commit()
```

confirma a alteração.

Por fim, o Flask utiliza:

```python
redirect(url_for('inicio'))
```

para redirecionar o usuário.

O fluxo aprendido ficou:

```text
FORMULÁRIO
    ↓
POST
    ↓
request.form
    ↓
validação
    ↓
adicionar()
    ↓
INSERT
    ↓
commit()
    ↓
redirect()
```

Esse padrão será utilizado novamente na edição de produtos.

---

# 38. ✏️ Editando produtos

Depois do cadastro, o próximo passo do CRUD foi começar a trabalhar com a **edição de produtos**.

A rota utilizada é:

```python
@app.route('/produtos/<int:id>/editar', methods=['GET', 'POST'])
def editar_produto(id):
    ...
```

O trecho:

```text
<int:id>
```

faz com que o ID recebido pela URL seja tratado como um inteiro.

Por exemplo:

```text
/produtos/7/editar
```

faz a função receber:

```python
id = 7
```

---

# 39. 🔎 Buscando um produto pelo ID

Para editar um produto, primeiro precisamos encontrá-lo no banco.

Foi criada a função:

```python
def buscar_produto(id):
    conexao = conectar()

    produto = conexao.execute(
        """SELECT * FROM produtos WHERE id = ?""",
        (id,)
    ).fetchone()

    conexao.close()

    return produto
```

O fluxo é:

```text
id recebido pela URL
        ↓
buscar_produto(id)
        ↓
SELECT
        ↓
WHERE id = ?
        ↓
fetchone()
        ↓
produto
```

O `fetchone()` retorna apenas um registro.

Como o projeto utiliza:

```python
conectando.row_factory = sqlite3.Row
```

podemos acessar os valores pelo nome da coluna:

```python
produto["nome"]
produto["preco"]
produto["estoque"]
produto["estoque_minimo"]
```

---

# 40. ⚠️ `SELECT` não precisa de `commit()`

Durante a implementação de `buscar_produto()`, foi identificado que não é necessário utilizar:

```python
conexao.commit()
```

depois de um `SELECT`.

A diferença é:

```text
SELECT
 ↓
consulta dados
 ↓
fetchone() / fetchall()
 ↓
close()
```

Enquanto operações que alteram o banco precisam confirmar a alteração:

```text
INSERT / UPDATE / DELETE
 ↓
commit()
 ↓
close()
```

Uma regra importante aprendida:

> **SELECT lê dados. INSERT, UPDATE e DELETE modificam dados.**

---

# 41. 📝 Atualizando um produto

A função `atualizar()` já está preparada para receber o ID do produto:

```python
def atualizar(id, nome, preco, estoque, estoque_minimo):
    conexao = conectar()

    conexao.execute(
        """
        UPDATE produtos
        SET nome = ?, preco = ?, estoque = ?, estoque_minimo = ?
        WHERE id = ?
        """,
        (nome, preco, estoque, estoque_minimo, id)
    )

    conexao.commit()
    conexao.close()
```

O ponto mais importante é:

```sql
WHERE id = ?
```

Isso faz com que apenas o produto escolhido seja alterado.

Sem o `WHERE`, um `UPDATE` poderia alterar todos os registros da tabela.

O fluxo é:

```text
editar_produto(id)
       ↓
atualizar(id, ...)
       ↓
UPDATE
       ↓
WHERE id = ?
       ↓
commit()
       ↓
SQLite
```

---

# 42. 🧭 Fluxo GET e POST na edição

A rota de edição utiliza novamente os dois métodos HTTP.

### GET

Quando o usuário acessa:

```text
/produtos/7/editar
```

o objetivo é buscar o produto e mostrar o formulário:

```text
GET
 ↓
editar_produto(7)
 ↓
buscar_produto(7)
 ↓
SELECT
 ↓
produto
 ↓
editar_produto.html
```

### POST

Depois que o usuário altera os dados e envia o formulário:

```text
POST
 ↓
request.form
 ↓
validação
 ↓
atualizar(7, ...)
 ↓
UPDATE
 ↓
commit()
 ↓
redirect()
 ↓
/produtos
```

Esse fluxo é uma aplicação prática do conceito de GET e POST estudado anteriormente.

---

# 43. 🔗 Link para edição

Na lista de produtos, podemos criar um link para a rota de edição:

```html
<a href="{{ url_for('editar_produto', id=produto['id']) }}">
    Editar
</a>
```

Se o produto possuir:

```text
id = 7
```

o Flask poderá gerar:

```text
/produtos/7/editar
```

Assim, o ID do produto é transportado pela URL até a função Python.

---

# 44. 🧩 `novo_produto.html` x `editar_produto.html`

Neste momento, a ideia é manter os templates separados para facilitar o aprendizado:

```text
novo_produto.html
    ↓
CREATE
    ↓
INSERT
```

e:

```text
editar_produto.html
    ↓
UPDATE
    ↓
produto existente
```

Apesar de futuramente ser possível reutilizar partes dos templates, mantê-los separados neste momento ajuda a visualizar a diferença entre **criar** e **editar**.

---

# 45. 📋 Formulário de edição

O formulário de edição pode receber os dados atuais do banco através do Jinja:

```html
<input
    type="text"
    name="nome"
    value="{{ produto['nome'] }}"
    required
>
```

Se o banco possuir:

```text
nome = Água 20L
```

o navegador poderá apresentar:

```text
Nome:
┌──────────────────────┐
│ Água 20L             │
└──────────────────────┘
```

O mesmo princípio pode ser utilizado para preço, estoque e estoque mínimo.

O fluxo fica:

```text
SQLite
 ↓
produto
 ↓
Flask
 ↓
render_template()
 ↓
Jinja
 ↓
HTML
 ↓
formulário preenchido
```

---

# 46. 🔄 Fluxo completo de edição

O fluxo estudado até aqui pode ser representado assim:

```text
                  PRODUTOS
                     │
                     │ clicar em "Editar"
                     ▼
            /produtos/7/editar
                     │
                     ▼
             editar_produto(7)
                     │
                     ▼
             buscar_produto(7)
                     │
                     ▼
                  SQLite
                     │
                   SELECT
                     │
                     ▼
                 produto
                     │
                     ▼
             editar_produto.html
                     │
                     │ usuário altera
                     ▼
                    POST
                     │
                     ▼
               request.form
                     │
                     ▼
              atualizar(7, ...)
                     │
                     ▼
                   UPDATE
                     │
                     ▼
                  commit()
                     │
                     ▼
                 redirect()
                     │
                     ▼
                  /produtos
```

Esse é um dos primeiros fluxos completos de CRUD estudados no projeto.

---

# 47. 🏗️ Estado atual da aplicação

A estrutura atual está evoluindo para:

```text
agua-facil/

├── .venv/
│
├── app.py
├── database.py
├── aguaFacil.sql
│
├── templates/
│   ├── base.html
│   ├── inicio.html
│   ├── sobre.html
│   ├── produtos.html
│   ├── novo_produto.html
│   └── editar_produto.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── app.js
```

> A existência de `editar_produto.html` representa a próxima etapa da implementação da edição caso o template ainda esteja sendo criado.

---

# 48. 🔗 Arquitetura atual

A separação entre os arquivos está ficando mais clara:

```text
                 NAVEGADOR
                     │
                     ▼
                  app.py
                     │
              rotas Flask
                     │
                     ▼
                database.py
                     │
                     ▼
                  SQLite
```

Enquanto os templates cuidam da apresentação:

```text
Flask
  ↓
render_template()
  ↓
Jinja
  ↓
HTML
  ↓
Navegador
```

Essa separação permite que:

- `app.py` cuide das rotas e do fluxo da aplicação;
- `database.py` cuide das operações com o banco;
- `templates/` cuide das páginas HTML;
- `static/` contenha CSS e JavaScript;
- SQLite armazene os dados.

---

# 49. 🔄 Fluxo atual dos produtos

Para listar produtos:

```text
Navegador
    ↓
/produtos
    ↓
Flask
    ↓
produtos()
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
    ↓
Navegador
```

Para cadastrar:

```text
Navegador
    ↓
/produtos/novo
    ↓
GET
    ↓
novo_produto.html
    ↓
usuário preenche
    ↓
POST
    ↓
request.form
    ↓
validação
    ↓
adicionar()
    ↓
INSERT
    ↓
commit()
    ↓
redirect()
```

Para editar:

```text
Navegador
    ↓
/produtos/<id>/editar
    ↓
GET
    ↓
buscar_produto(id)
    ↓
SELECT
    ↓
formulário preenchido
    ↓
POST
    ↓
request.form
    ↓
atualizar(id, ...)
    ↓
UPDATE
    ↓
commit()
    ↓
redirect()
```

---

# 50. 🧠 O que já aprendi

Até aqui consegui entender os seguintes conceitos:

### Python

```python
import
def
return
list
dict
try
except
float()
int()
```

### Flask

```python
Flask()
@app.route()
app.run()
render_template()
request
request.form
redirect()
url_for()
```

### HTTP

```text
GET
POST
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
sqlite3.Row
commit()
close()
```

### SQL

```sql
CREATE TABLE
INSERT
SELECT
UPDATE
DELETE
WHERE
ORDER BY
```

### CRUD

```text
CREATE → INSERT
READ   → SELECT
UPDATE → UPDATE
DELETE → DELETE
```

### Segurança

```text
?
```

como parâmetros SQL, evitando a montagem insegura de consultas através de strings.

---

# 51. 🧠 Conceitos que preciso consolidar

Os próximos pontos de estudo são:

```text
GET e POST
     ↓
request.form
     ↓
validação
     ↓
redirect()
     ↓
url_for()
     ↓
UPDATE
     ↓
CRUD completo
```

Também preciso aprofundar:

- tratamento de erros;
- validação de formulários;
- edição de registros;
- exclusão lógica;
- relacionamento entre tabelas;
- chaves estrangeiras;
- `JOIN`;
- transações;
- controle de estoque.

---

# 52. 🎯 Próximos passos

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
[✓] Trabalhar com GET e POST
[✓] Receber formulário com request.form
[✓] Validar dados básicos do formulário
[✓] Inserir produto pelo formulário
[✓] Utilizar commit() após INSERT
[✓] Utilizar redirect() / url_for()
[✓] Criar função buscar_produto()
[✓] Criar função atualizar()
[~] Criar e testar edição completa do produto
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
   CLIENTES       PRODUTOS        PEDIDOS
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
conexao = sqlite3.connect("aguaFacil.sql")
```

## Confirmar alterações

```python
conexao.commit()
```

## Fechar conexão

```python
conexao.close()
```

## Buscar um único registro

```python
produto = conexao.execute(
    "SELECT * FROM produtos WHERE id = ?",
    (id,)
).fetchone()
```

## Atualizar um registro

```sql
UPDATE produtos
SET nome = ?, preco = ?, estoque = ?, estoque_minimo = ?
WHERE id = ?
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
           ROTAS           TEMPLATES
             │                 │
           PYTHON             JINJA
             │                 │
             └────────┬────────┘
                      │
                   SQLITE
                      │
                     SQL
```

O aprendizado mais importante neste momento é perceber que cada camada possui uma responsabilidade.

Quando um usuário edita um produto, por exemplo:

```text
HTML
 ↓
POST
 ↓
Flask
 ↓
request.form
 ↓
Python
 ↓
database.py
 ↓
UPDATE
 ↓
SQLite
 ↓
commit()
 ↓
redirect()
 ↓
Flask
 ↓
Jinja
 ↓
HTML
```

Esse fluxo conecta praticamente tudo que foi estudado até agora.

## Próxima etapa

O próximo objetivo é concluir e testar o ciclo de edição:

```text
/produtos
    ↓
Editar
    ↓
buscar_produto(id)
    ↓
editar_produto.html
    ↓
POST
    ↓
request.form
    ↓
atualizar()
    ↓
UPDATE
    ↓
SQLite
    ↓
redirect()
    ↓
/produtos
```

Depois disso, o projeto poderá avançar para **exclusão/desativação de produtos** e, posteriormente, para **clientes e pedidos**.

---

# 📚 Documentação para consulta

- [Python Documentation](https://docs.python.org/3/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLite Documentation](https://sqlite.org/docs.html)
- [Jinja Documentation](https://jinja.palletsprojects.com/)
- [MDN Web Docs](https://developer.mozilla.org/)

---

> **Princípio do projeto:** entender primeiro, abstrair depois.  
> A aplicação deve crescer junto com meu conhecimento, sem esconder a lógica atrás de abstrações que ainda não compreendo.
