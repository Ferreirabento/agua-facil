# 💧 Água Fácil

**Sistema de gerenciamento de vendas para pequenos comerciantes de água.**

O Água Fácil é um projeto de desenvolvimento de software que tem como objetivo auxiliar pequenos comerciantes e revendedores de garrafões de água no gerenciamento de produtos, clientes, estoque e pedidos.

A proposta é oferecer uma ferramenta simples, leve e intuitiva, que ajude a organizar as atividades comerciais do dia a dia, especialmente em negócios que ainda realizam seus controles manualmente.

O projeto está sendo desenvolvido com Python, Flask e SQLite, priorizando uma arquitetura simples, baixo consumo de recursos e uma interface adaptável a dispositivos móveis.

> **Status do projeto:** Em desenvolvimento — primeira versão (MVP).

---

## 📌 1. O problema que o projeto busca resolver

Pequenos comerciantes frequentemente precisam controlar diversas informações ao mesmo tempo:

- Quais produtos estão disponíveis para venda?
- Quanto custa cada produto?
- Quantas unidades ainda existem no estoque?
- Quem são os clientes?
- Quais pedidos foram realizados?
- Quais pedidos ainda estão pendentes?
- Quanto cada pedido representa em vendas?

Quando essas informações são controladas manualmente, podem surgir dificuldades como perda de registros, erros de cálculo, falta de controle do estoque e dificuldade para acompanhar os pedidos.

O Água Fácil busca centralizar essas informações em um único sistema, tornando o gerenciamento mais organizado e acessível.

## 🎯 2. Objetivos do projeto

### Objetivo geral

Desenvolver um sistema que permita ao comerciante cadastrar e gerenciar produtos e clientes, registrar pedidos, acompanhar seus respectivos status e controlar a disponibilidade dos produtos em estoque.

### Objetivos específicos

- Organizar o cadastro e a consulta de produtos.
- Manter os dados dos clientes registrados.
- Facilitar a criação e consulta de pedidos.
- Automatizar o cálculo dos valores das vendas.
- Evitar pedidos com quantidade superior ao estoque disponível.
- Permitir o acompanhamento do andamento dos pedidos.
- Preservar o histórico comercial do estabelecimento.

## 👥 3. Público-alvo

O sistema é direcionado a pequenos comerciantes e revendedores de água que precisam de uma ferramenta para organizar suas vendas, mas que podem não possuir familiaridade com sistemas informatizados.

Por esse motivo, a simplicidade de utilização é uma decisão importante do projeto.

A interface deverá priorizar:
- Navegação intuitiva.
- Formulários objetivos.
- Informações organizadas.
- Boa visualização em smartphones.
- Poucas etapas para realizar operações comuns.

---

## ⚙️ 4. Tecnologias utilizadas

| Tecnologia | Responsabilidade |
|---|---|
| Python | Linguagem principal da aplicação. |
| Flask | Framework responsável pelas rotas e pela comunicação entre as partes do sistema. |
| SQLite | Banco de dados utilizado para armazenar as informações. |
| HTML | Estrutura das páginas. |
| CSS | Estilização e adaptação da interface. |
| Jinja2 | Integração entre os dados enviados pelo Flask e as páginas HTML. |

### Por que essas tecnologias foram escolhidas?

**Python**

Foi escolhido por ser uma linguagem versátil, com sintaxe relativamente simples e ampla utilização no desenvolvimento de aplicações e na área de tecnologia.

Além disso, permite que o projeto seja desenvolvido sem exigir uma infraestrutura complexa.

**Flask**

O Flask foi escolhido por ser um framework leve para desenvolvimento web.

Diferentemente de frameworks mais completos, ele permite selecionar e organizar os componentes necessários conforme o crescimento do projeto.

Essa escolha ajuda a manter a aplicação simples e facilita o aprendizado dos conceitos de desenvolvimento web.

**SQLite**

O SQLite foi escolhido por armazenar os dados em um arquivo, sem exigir a instalação e administração de um servidor de banco de dados separado.

Isso reduz a complexidade da configuração e atende às necessidades de armazenamento da primeira versão.

**HTML, CSS e Jinja2**

O HTML estrutura as páginas, o CSS controla a apresentação visual e o Jinja2 permite apresentar informações dinâmicas, como produtos, clientes e pedidos consultados no banco de dados.

A separação dessas responsabilidades facilita a manutenção da interface.

---

## 🧩 5. Organização e funcionamento do sistema

O Água Fácil está organizado em módulos que representam as principais atividades do comércio.

### 5.1. Módulo de produtos

Responsável pelo gerenciamento dos produtos comercializados.

Cada produto deverá possuir:

- Identificador único (`id`).
- Nome.
- Preço de venda.
- Quantidade disponível em estoque.
- Quantidade mínima de estoque.
- Indicador de atividade (`ativo`).

**Operações previstas:**
- Cadastrar produtos.
- Consultar produtos.
- Editar informações.
- Identificar produtos que precisam de reposição.

**Por que existe o campo `estoque_minimo`?**

A quantidade mínima funciona como uma referência para identificar quando o estoque de determinado produto está baixo.

Por exemplo: se o estoque mínimo de um produto for 5 unidades e a quantidade disponível chegar a 4, o comerciante poderá identificar que precisa providenciar uma reposição.

**Por que existe o campo `ativo`?**

O campo permite desativar um produto sem apagar definitivamente seu registro.

Essa decisão é importante porque um produto pode ter participado de pedidos anteriores. Mesmo que deixe de ser comercializado, suas informações precisam continuar disponíveis para preservar o histórico.

### 5.2. Módulo de clientes

Responsável pelo cadastro e gerenciamento dos clientes.

Cada cliente deverá possuir:

- Identificador único (`id`).
- Nome.
- Telefone.
- Indicador de atividade (`ativo`).

**Operações previstas:**
- Cadastrar clientes.
- Consultar clientes.
- Editar informações.

**Por que os pedidos utilizam clientes previamente cadastrados?**

Essa decisão evita que o mesmo cliente seja registrado de diferentes maneiras em cada venda.

Ao selecionar um cliente existente, o pedido fica vinculado ao cadastro correto, facilitando a consulta e a organização do histórico comercial.

Caso o cliente ainda não esteja cadastrado, o usuário deverá acessar a seção de clientes e realizar o cadastro antes de criar o pedido.

O campo `ativo` também permite preservar os dados de clientes antigos sem disponibilizá-los para novas operações.

### 5.3. Módulo de pedidos

O módulo de pedidos é responsável por registrar as vendas realizadas pelo comerciante.

Cada pedido deverá estar associado a um cliente previamente cadastrado.

O processo de criação deverá permitir:

1. Selecionar um cliente.
2. Selecionar um ou mais produtos.
3. Informar a quantidade desejada de cada produto.
4. Visualizar o preço unitário.
5. Consultar o subtotal de cada item.
6. Visualizar o valor total do pedido.
7. Confirmar o cadastro.

**Por que os pedidos são separados dos produtos?**

Um pedido representa uma venda realizada para determinado cliente. Ele possui informações próprias, como data de cadastro e status.

Os produtos, por outro lado, representam os itens comercializados.

Separar essas informações permite que um mesmo cliente realize vários pedidos e que um pedido contenha diferentes produtos.

### 5.4. Módulo de itens do pedido

O módulo de itens conecta os pedidos aos produtos.

Essa separação é necessária porque um pedido poderá possuir vários produtos e um mesmo produto poderá aparecer em diversos pedidos.

Cada item deverá armazenar:

- Identificador único (`id`).
- Identificador do pedido (`pedido_id`).
- Identificador do produto (`produto_id`).
- Quantidade.
- Preço unitário praticado na venda.

**Por que existe uma tabela separada para os itens?**

Imagine uma venda contendo:

- 2 garrafões de água de 20 litros.
- 1 garrafão de água de 10 litros.
- 3 unidades de outro produto.

Se os produtos fossem armazenados diretamente na tabela de pedidos, seria necessário criar campos adicionais para cada produto, tornando a estrutura limitada e difícil de manter.

A tabela `itens_pedido` resolve esse problema permitindo que cada produto seja registrado como uma linha vinculada ao pedido.

### 5.5. Consulta e acompanhamento dos pedidos

O sistema deverá disponibilizar uma listagem com as principais informações de cada pedido:

- Identificador do pedido.
- Nome do cliente.
- Data do pedido.
- Valor total.
- Status atual.

O objetivo é permitir que o comerciante acompanhe as vendas sem precisar consultar diretamente o banco de dados.

Os status inicialmente previstos são:

| Status | Significado |
|---|---|
| Pendente | Pedido registrado, aguardando andamento. |
| Em preparação | Pedido em organização. |
| Saiu para entrega | Pedido encaminhado para entrega. |
| Entregue | Pedido concluído. |
| Cancelado | Pedido cancelado. |

A atualização do status permitirá acompanhar o andamento de cada venda.

---

## 🗄️ 6. Modelagem do banco de dados

A primeira versão utiliza quatro entidades principais: `produtos`, `clientes`, `pedidos` e `itens_pedido`.

### 6.1. Tabela `produtos`

Armazena os produtos comercializados.

| Campo | Finalidade |
|---|---|
| `id` | Identificador do produto. |
| `nome` | Nome do produto. |
| `preco` | Preço de venda. |
| `estoque` | Quantidade disponível. |
| `estoque_minimo` | Quantidade mínima de referência. |
| `ativo` | Indica se o produto está disponível para utilização. |

### 6.2. Tabela `clientes`

Armazena os clientes cadastrados.

| Campo | Finalidade |
|---|---|
| `id` | Identificador do cliente. |
| `nome` | Nome do cliente. |
| `telefone` | Telefone para contato. |
| `ativo` | Indica se o cadastro está disponível para utilização. |

### 6.3. Tabela `pedidos`

Armazena as informações gerais das vendas.

| Campo | Finalidade |
|---|---|
| `id` | Identificador do pedido. |
| `cliente_id` | Referência ao cliente responsável pelo pedido. |
| `data_pedido` | Data e horário do cadastro. |
| `status` | Situação atual do pedido. |
| `ativo` | Indicador de atividade do registro. |

### 6.4. Tabela `itens_pedido`

Armazena os produtos que compõem cada pedido.

| Campo | Finalidade |
|---|---|
| `id` | Identificador do item. |
| `pedido_id` | Referência ao pedido. |
| `produto_id` | Referência ao produto. |
| `quantidade` | Quantidade comercializada. |
| `preco_unitario` | Preço praticado no momento da venda. |

### 6.5. Relacionamentos

A modelagem utiliza relacionamentos entre as quatro tabelas:

- Um cliente poderá possuir vários pedidos.
- Um pedido deverá pertencer a um único cliente.
- Um pedido poderá possuir vários itens.
- Um produto poderá aparecer em vários itens de pedidos.
- Cada item deverá pertencer a um pedido e referenciar um produto.

**Representação simplificada:**

```text
CLIENTES
   |
   | 1:N
   |
PEDIDOS
   |
   | 1:N
   |
ITENS_PEDIDO
   |
   | N:1
   |
PRODUTOS
```

Essa estrutura permite organizar os dados sem duplicar informações desnecessariamente.

---

## 💰 7. Regras de cálculo das vendas

O sistema deverá calcular automaticamente os valores dos pedidos.

### Subtotal de cada item

```text
Subtotal = Quantidade × Preço unitário
```

Exemplo:

```text
Produto: Garrafão de 20 litros
Quantidade: 3
Preço unitário: R$ 12,00

Subtotal: R$ 36,00
```

### Total do pedido

```text
Total = Soma dos subtotais dos itens
```

Exemplo:

```text
Produto A: R$ 36,00
Produto B: R$ 15,00
Produto C: R$ 20,00

Total do pedido: R$ 71,00
```

### Por que armazenar o preço praticado no momento da venda?

O preço de um produto pode mudar com o passar do tempo.

Se o sistema consultasse sempre o preço atual do cadastro para calcular pedidos antigos, uma alteração no preço poderia modificar indevidamente o valor de vendas anteriores.

Por isso, a tabela `itens_pedido` possui o campo `preco_unitario`.

Ele registra o valor praticado no momento da venda, preservando a informação histórica.

---

## 📦 8. Controle de estoque

O estoque deverá ser considerado durante a criação dos pedidos.

Antes de confirmar uma venda, o sistema deverá verificar:

1. Se o produto existe e está ativo.
2. Se a quantidade informada é um número inteiro.
3. Se a quantidade é maior que zero.
4. Se existe estoque suficiente para atender ao pedido.

Não deverá ser permitido registrar uma quantidade superior à disponibilidade.

Após a confirmação bem-sucedida do pedido, o sistema deverá atualizar o estoque.

Quando um pedido for cancelado, o estoque deverá ser tratado de maneira consistente, devolvendo à disponibilidade a quantidade anteriormente descontada.

**Por que o controle de estoque precisa ser integrado aos pedidos?**

O estoque não pode ser tratado como uma informação independente das vendas.

Quando um pedido é registrado, a quantidade disponível muda. Caso essa atualização não aconteça, o sistema poderá apresentar uma quantidade incorreta e permitir vendas de produtos indisponíveis.

Por isso, o registro do pedido e a atualização do estoque precisam funcionar de maneira consistente.

---

## 🔒 9. Preservação do histórico e integridade dos dados

O projeto prevê mecanismos para evitar a perda de informações importantes.

### Desativação em vez de exclusão definitiva

Produtos e clientes poderão ser desativados quando não forem mais utilizados.

Essa decisão evita que registros antigos percam suas referências.

Por exemplo: um cliente pode deixar de comprar no estabelecimento, mas seus pedidos anteriores ainda precisam continuar associados ao seu cadastro.

### Integridade referencial

As tabelas utilizam chaves estrangeiras para garantir que os relacionamentos entre clientes, pedidos, produtos e itens sejam válidos.

Isso evita que um pedido faça referência a um cliente inexistente ou que um item seja associado a um produto que não existe.

### Operações consistentes

O registro de um pedido e de seus itens deverá ocorrer de maneira consistente.

Caso uma etapa do processo falhe, a operação deverá ser revertida para evitar que o banco de dados fique com um pedido incompleto.

Para isso, o projeto prevê o uso de transações no banco de dados.

---

## 🔄 10. Fluxo principal de utilização

O funcionamento esperado da primeira versão segue esta sequência:

```text
        ACESSO AO SISTEMA
                |
                v
        CADASTRAR PRODUTOS
                |
                v
         CADASTRAR CLIENTES
                |
                v
         ACESSAR PEDIDOS
                |
                v
       CONSULTAR PEDIDOS EXISTENTES
                |
                v
          NOVO PEDIDO
                |
                v
        SELECIONAR CLIENTE
                |
                v
       SELECIONAR PRODUTOS
                |
                v
        INFORMAR QUANTIDADES
                |
                v
        VALIDAR O ESTOQUE
                |
                v
       CALCULAR OS SUBTOTAIS
                |
                v
       CALCULAR O VALOR TOTAL
                |
                v
         CONFIRMAR PEDIDO
                |
                v
       REGISTRAR PEDIDO E ITENS
                |
                v
        ATUALIZAR O ESTOQUE
                |
                v
       ACOMPANHAR O STATUS
```

Caso o cliente não esteja cadastrado, o usuário deverá realizar seu cadastro na seção de clientes antes de continuar.

---

## 🏗️ 11. Organização do código

O projeto busca separar as responsabilidades da aplicação para facilitar a manutenção e a evolução do sistema.

A organização conceitual é:

| Componente | Responsabilidade |
|---|---|
| `app.py` | Gerenciar as rotas, receber dados dos formulários e controlar o fluxo da aplicação. |
| `database.py` | Concentrar as operações de criação, consulta, atualização e acesso ao banco de dados. |
| `templates/` | Armazenar os arquivos HTML utilizados na apresentação das páginas. |
| `static/` | Armazenar recursos estáticos, como folhas de estilo CSS. |
| `aguaFacil.sql` | Arquivo utilizado como banco de dados SQLite. |

**Por que separar `app.py` e `database.py`?**

O arquivo `app.py` deve cuidar da comunicação entre o usuário e a aplicação, enquanto `database.py` deve concentrar as operações relacionadas ao armazenamento dos dados.

Essa separação evita que as consultas SQL fiquem espalhadas pelas rotas e torna o código mais organizado.

Também facilita futuras alterações: por exemplo, uma mudança na forma de consultar produtos pode ser concentrada nas funções de acesso ao banco de dados.

---

## 📋 12. Requisitos não funcionais

Além das funcionalidades, o Água Fácil possui requisitos relacionados à qualidade do sistema.

| Requisito | Aplicação no projeto |
|---|---|
| Usabilidade | Interface simples e intuitiva. |
| Responsividade | Adaptação a diferentes tamanhos de tela, priorizando smartphones. |
| Desempenho | Operações sem atrasos perceptíveis no uso normal. |
| Persistência | Dados armazenados em SQLite. |
| Integridade | Uso de chaves estrangeiras e validações. |
| Segurança | Consultas parametrizadas e validação dos formulários. |
| Confiabilidade | Operações consistentes, com uso de transações. |
| Manutenibilidade | Separação das responsabilidades do código. |
| Compatibilidade | Funcionamento em navegadores modernos. |
| Eficiência | Uso de tecnologias leves e baixo consumo de recursos. |

---

## 🚧 13. Estado atual do desenvolvimento

O projeto está sendo desenvolvido de forma incremental. As funcionalidades são implementadas e testadas por etapas.

| Área | Situação |
|---|---|
| Estrutura inicial com Flask | Em desenvolvimento |
| Cadastro e consulta de produtos | Implementação inicial |
| Edição de produtos | Implementação inicial |
| Cadastro e consulta de clientes | Implementação inicial |
| Edição de clientes | Implementação inicial |
| Estrutura das tabelas de pedidos | Implementação inicial |
| Cadastro de pedidos e itens | Implementação inicial |
| Consulta completa dos pedidos | Pendente de ajustes |
| Validação de estoque | Pendente |
| Cálculo automático dos valores na interface | Pendente |
| Atualização automática do estoque | Pendente |
| Atualização de status | Pendente |
| Cancelamento e restauração do estoque | Pendente |
| Testes das operações principais | Pendente |
| Revisão da interface para smartphones | Em desenvolvimento |

A tabela representa o andamento conhecido durante a elaboração desta documentação. Ela deverá ser atualizada conforme as funcionalidades forem implementadas e testadas.

---

## 🗺️ 14. Próximas etapas

O desenvolvimento da primeira versão seguirá uma ordem de prioridades:

**Etapa 1 — Cadastros**
- Finalizar o cadastro de produtos.
- Finalizar o cadastro de clientes.
- Revisar as operações de edição e desativação.

**Etapa 2 — Pedidos**
- Finalizar a seleção de clientes.
- Permitir a seleção de um ou mais produtos.
- Implementar a validação de quantidade.
- Implementar a validação de estoque.
- Calcular subtotais e total.
- Registrar pedidos e itens de maneira consistente.

**Etapa 3 — Consulta e acompanhamento**
- Exibir os dados completos dos pedidos.
- Apresentar o valor total.
- Permitir a atualização do status.

**Etapa 4 — Estoque e preservação do histórico**
- Atualizar o estoque após a confirmação.
- Tratar o estoque em pedidos cancelados.
- Preservar os registros históricos.

**Etapa 5 — Testes e ajustes**
- Testar formulários com dados válidos e inválidos.
- Verificar a integridade dos relacionamentos.
- Testar a aplicação em smartphones.
- Revisar a experiência de utilização.

---

## 🚫 15. Fora do escopo da primeira versão

Para manter o desenvolvimento controlado e priorizar as funcionalidades essenciais, alguns recursos não fazem parte dos objetivos obrigatórios do primeiro lançamento:

- Integração com WhatsApp.
- Emissão de notas fiscais.
- Integração com sistemas de pagamento.
- Gestão financeira completa.
- Relatórios avançados e dashboards.
- Controle de múltiplos estabelecimentos.
- Aplicativo nativo para Android ou iOS.

Essas funcionalidades poderão ser consideradas em versões futuras, conforme as necessidades do negócio.

---

## ▶️ 16. Como executar o projeto

### Pré-requisitos

- Python instalado.
- Git instalado.
- Ambiente virtual Python.
- Navegador moderno.

### 1. Clonar o repositório

```bash
git clone https://github.com/Ferreirabento/agua-facil.git
```

### 2. Entrar na pasta do projeto

```bash
cd agua-facil
```

### 3. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

### 5. Instalar o Flask

```bash
pip install Flask
```

### 6. Executar a aplicação

```bash
python app.py
```

Após iniciar a aplicação, acesse no navegador:

```text
http://127.0.0.1:5000
```

> Observação: as instruções de execução poderão ser atualizadas caso novas dependências sejam adicionadas ao projeto.

---

## 📚 17. Aprendizados e propósito acadêmico

O Água Fácil também representa uma oportunidade de aplicar, na prática, conhecimentos relacionados ao curso de Análise e Desenvolvimento de Sistemas.

Durante o desenvolvimento, são trabalhados conceitos como:

- Lógica de programação.
- Desenvolvimento web com Python e Flask.
- Operações CRUD.
- Modelagem de banco de dados relacional.
- SQL e SQLite.
- Chaves primárias e estrangeiras.
- Relacionamentos entre entidades.
- Validação de dados.
- Separação de responsabilidades.
- Organização de projetos.
- Experiência do usuário e responsividade.
- Testes e manutenção de software.

O objetivo não é apenas construir uma aplicação funcional, mas compreender as decisões tomadas durante o desenvolvimento e os motivos pelos quais cada parte do sistema existe.

---

## 📄 18. Documentação de requisitos

O desenvolvimento do Água Fácil é orientado pelo documento **Água Fácil — Documento de Requisitos do Sistema**, versão 1.0, de 23/11/2026.

Esse documento define:

- Requisitos funcionais.
- Requisitos não funcionais.
- Regras de negócio.
- Modelo de dados previsto.
- Fluxo principal de utilização.
- Critérios de conclusão da primeira versão.
- Funcionalidades fora do escopo inicial.

Ele serve como referência para implementar, testar e evoluir o sistema, evitando que novas funcionalidades sejam adicionadas sem considerar os objetivos originais do projeto.

---

## 👨‍💻 19. Autor

**João Bento**

Estudante de Análise e Desenvolvimento de Sistemas.

Projeto desenvolvido com finalidade acadêmica e prática, buscando aplicar conhecimentos de programação, banco de dados e desenvolvimento de software em um problema real de pequenos comerciantes.

- GitHub: [Ferreirabento](https://github.com/Ferreirabento)

---

**Água Fácil — Organização simples para o dia a dia de quem vende água.**