# Água Fácil — Documento de Requisitos do Sistema

**Versão:** 1.0  
**Data:** 23/11/2026  
**Tipo de documento:** Especificação de Requisitos de Software  
**Projeto:** Água Fácil

---

## 1. Apresentação do projeto

O Água Fácil é um sistema de gerenciamento de vendas desenvolvido para pequenos comerciantes que trabalham com a revenda de garrafões de água.

O sistema tem como finalidade facilitar o controle de produtos, clientes, estoque e pedidos, oferecendo uma ferramenta simples para organizar as atividades comerciais do negócio.

A aplicação será desenvolvida com foco em facilidade de utilização, baixo consumo de recursos e boa experiência em dispositivos móveis, considerando que seu público pode ter pouca familiaridade com sistemas informatizados.

### 1.1. Objetivo geral

Desenvolver um sistema que permita ao comerciante cadastrar e gerenciar produtos e clientes, registrar pedidos, acompanhar seus respectivos status e controlar a disponibilidade dos produtos em estoque.

### 1.2. Público-alvo

Pequenos comerciantes e revendedores de água que necessitam de uma ferramenta simples para organizar suas vendas e acompanhar seus pedidos.

### 1.3. Escopo inicial

A primeira versão do sistema deverá contemplar:

- Cadastro, consulta e edição de produtos.
- Cadastro, consulta e edição de clientes.
- Controle de estoque dos produtos.
- Cadastro de pedidos vinculados a clientes.
- Seleção de produtos e quantidades.
- Cálculo automático dos valores dos pedidos.
- Consulta dos pedidos cadastrados.
- Acompanhamento e atualização do status dos pedidos.

---

## 2. Requisitos funcionais (RF)

Os requisitos funcionais descrevem as operações e funcionalidades que o sistema deverá oferecer aos usuários.

### RF01 — Cadastro de produtos

O sistema deverá permitir que o usuário cadastre produtos, informando:

- Nome do produto.
- Preço de venda.
- Quantidade disponível em estoque.
- Quantidade mínima de estoque.

**Critério de aceitação:** o sistema deverá salvar o produto e disponibilizá-lo na listagem de produtos e na seleção de produtos durante o cadastro de pedidos.

### RF02 — Consulta de produtos

O sistema deverá apresentar uma listagem dos produtos cadastrados, contendo pelo menos:

- Nome.
- Preço.
- Quantidade em estoque.
- Estoque mínimo.

**Critério de aceitação:** o usuário deverá conseguir visualizar os produtos disponíveis e identificar aqueles que precisam de reposição.

### RF03 — Edição de produtos

O sistema deverá permitir que o usuário altere as informações de um produto previamente cadastrado.

**Critério de aceitação:** após salvar as alterações, os dados atualizados deverão aparecer na listagem de produtos.

### RF04 — Cadastro de clientes

O sistema deverá permitir o cadastro de clientes, contendo:

- Nome.
- Telefone.

**Critério de aceitação:** o cliente cadastrado deverá ficar disponível para seleção durante a criação de um pedido.

### RF05 — Consulta de clientes

O sistema deverá apresentar uma listagem dos clientes cadastrados, permitindo a identificação de cada cliente por seu nome e telefone.

### RF06 — Edição de clientes

O sistema deverá permitir que o usuário altere as informações de clientes previamente cadastrados.

**Critério de aceitação:** as alterações deverão ser salvas e exibidas na listagem de clientes.

### RF07 — Consulta de pedidos

O sistema deverá permitir que o usuário visualize os pedidos cadastrados.

A listagem deverá apresentar, no mínimo:

- Número ou identificador do pedido.
- Nome do cliente.
- Data do pedido.
- Valor total.
- Status atual.

**Critério de aceitação:** o usuário deverá conseguir identificar os pedidos e acompanhar sua situação sem precisar consultar diretamente o banco de dados.

### RF08 — Cadastro de pedidos

O sistema deverá permitir que o usuário registre um pedido para um cliente previamente cadastrado.

O processo deverá permitir:

1. Selecionar um cliente existente.
2. Selecionar um ou mais produtos cadastrados.
3. Informar a quantidade desejada de cada produto.
4. Visualizar o preço unitário.
5. Calcular automaticamente o subtotal de cada item.
6. Calcular automaticamente o valor total do pedido.
7. Confirmar e cadastrar o pedido.

**Critério de aceitação:** o pedido deverá ser registrado com os dados do cliente, data, status inicial, produtos, quantidades e preços praticados no momento da venda.

### RF09 — Validação do cliente no pedido

O sistema deverá verificar se o cliente selecionado existe e está disponível para utilização.

Caso o cliente não esteja cadastrado, o usuário deverá ser orientado a realizar seu cadastro na seção de clientes antes de continuar.

**Critério de aceitação:** não deverá ser possível registrar um pedido sem um cliente válido.

### RF10 — Validação dos produtos no pedido

O sistema deverá verificar se cada produto selecionado existe e está ativo.

**Critério de aceitação:** não deverá ser possível registrar um pedido utilizando produtos inexistentes ou indisponíveis.

### RF11 — Validação de quantidade e estoque

O sistema deverá verificar se a quantidade informada é válida e se existe estoque suficiente para atender ao pedido.

Regras:

- A quantidade deverá ser um número inteiro maior que zero.
- A quantidade solicitada não poderá ultrapassar o estoque disponível.
- O sistema deverá informar quando o estoque for insuficiente.
- O sistema deverá atualizar o estoque após o registro bem-sucedido do pedido.

**Critério de aceitação:** não deverá ser possível concluir um pedido com quantidade superior à disponibilidade do produto.

### RF12 — Cálculo automático dos valores

O sistema deverá calcular automaticamente os valores dos produtos selecionados.

**Fórmulas:**

Subtotal do item:

`Subtotal = Quantidade × Preço unitário`

Valor total do pedido:

`Total = Soma dos subtotais dos itens`

**Critério de aceitação:** os valores deverão ser apresentados ao usuário antes da confirmação do pedido e registrados corretamente no banco de dados.

### RF13 — Armazenamento do preço praticado

O sistema deverá armazenar o preço unitário de cada produto no momento da realização do pedido.

**Critério de aceitação:** alterações posteriores no preço de um produto não deverão modificar os valores dos pedidos anteriores.

### RF14 — Atualização do status do pedido

O sistema deverá permitir que o usuário visualize e atualize o status de cada pedido.

Sugestão inicial de estados:

- Pendente.
- Em preparação.
- Saiu para entrega.
- Entregue.
- Cancelado.

**Critério de aceitação:** o status atualizado deverá ser salvo e apresentado na listagem de pedidos.

### RF15 — Cancelamento e preservação do histórico

O sistema deverá permitir o cancelamento de pedidos sem apagar permanentemente seus registros.

Quando um pedido for cancelado, o estoque reservado ou descontado deverá ser devolvido à disponibilidade, conforme a regra de controle de estoque adotada.

**Critério de aceitação:** pedidos cancelados deverão continuar consultáveis, identificados com o status correspondente.

### RF16 — Preservação dos cadastros utilizados em pedidos

O sistema deverá evitar a exclusão definitiva de produtos e clientes que estejam vinculados a pedidos anteriores.

Quando necessário, deverá permitir a desativação desses cadastros, preservando o histórico comercial.

**Critério de aceitação:** a desativação de um produto ou cliente não deverá apagar informações de pedidos anteriores.

---

## 3. Requisitos não funcionais (RNF)

Os requisitos não funcionais descrevem características de qualidade, desempenho, segurança e usabilidade que o sistema deverá atender.

### RNF01 — Usabilidade

O sistema deverá possuir uma interface simples, intuitiva e de fácil compreensão, considerando usuários com pouca experiência em tecnologia.

### RNF02 — Responsividade

O sistema deverá adaptar sua interface a diferentes tamanhos de tela, priorizando o uso em smartphones.

### RNF03 — Desempenho

As operações de cadastro, consulta, edição e registro de pedidos deverão ocorrer sem atrasos perceptíveis durante o uso normal do sistema.

### RNF04 — Persistência de dados

As informações cadastradas deverão permanecer armazenadas após o encerramento da aplicação, utilizando banco de dados SQLite na versão inicial.

### RNF05 — Integridade dos dados

O sistema deverá utilizar mecanismos de integridade referencial para evitar registros inconsistentes entre produtos, clientes, pedidos e itens dos pedidos.

### RNF06 — Segurança

O sistema deverá utilizar consultas parametrizadas para evitar injeção de SQL e deverá validar os dados recebidos dos formulários antes de armazená-los.

### RNF07 — Confiabilidade das operações

O registro de um pedido e de seus respectivos itens deverá ocorrer de forma consistente. Caso alguma etapa falhe, a operação deverá ser revertida para evitar pedidos incompletos.

### RNF08 — Manutenibilidade

O código deverá ser organizado de forma modular, separando as responsabilidades de rotas, acesso ao banco de dados e apresentação das páginas.

### RNF09 — Compatibilidade

A aplicação deverá funcionar nos navegadores modernos utilizados em computadores e dispositivos móveis.

### RNF10 — Eficiência de recursos

O sistema deverá priorizar tecnologias leves e baixo consumo de memória e processamento, considerando dispositivos com recursos limitados.

---

## 4. Regras de negócio (RN)

As regras de negócio definem condições que devem ser respeitadas durante a utilização do sistema.

| Código | Regra |
|---|---|
| RN01 | Todo pedido deverá estar associado a um cliente cadastrado. |
| RN02 | Todo item de pedido deverá estar associado a um produto cadastrado. |
| RN03 | A quantidade solicitada deverá ser maior que zero. |
| RN04 | A quantidade solicitada não poderá ultrapassar o estoque disponível. |
| RN05 | O preço unitário deverá corresponder ao preço praticado no momento da venda. |
| RN06 | O subtotal deverá ser calculado pela multiplicação da quantidade pelo preço unitário. |
| RN07 | O total do pedido deverá corresponder à soma dos subtotais dos itens. |
| RN08 | O pedido deverá receber automaticamente uma data de cadastro. |
| RN09 | O pedido deverá possuir um status inicial definido pelo sistema. |
| RN10 | Pedidos cancelados deverão preservar seu histórico. |
| RN11 | Produtos e clientes vinculados a pedidos anteriores não deverão ser apagados definitivamente. |
| RN12 | O estoque deverá ser atualizado de maneira consistente após a confirmação ou o cancelamento de um pedido. |

---

## 5. Modelo de dados previsto

A estrutura inicial do banco de dados deverá contemplar quatro entidades principais.

### Produtos

Armazena as informações dos produtos comercializados.

Campos previstos:

- `id`
- `nome`
- `preco`
- `estoque`
- `estoque_minimo`
- `ativo`

### Clientes

Armazena as informações dos clientes.

Campos previstos:

- `id`
- `nome`
- `telefone`
- `ativo`

### Pedidos

Armazena as informações gerais de cada pedido.

Campos previstos:

- `id`
- `cliente_id`
- `data_pedido`
- `status`
- `ativo`

### Itens do pedido

Relaciona os produtos aos pedidos, permitindo que um pedido possua vários produtos.

Campos previstos:

- `id`
- `pedido_id`
- `produto_id`
- `quantidade`
- `preco_unitario`

**Relacionamentos:**

- Um cliente poderá possuir vários pedidos.
- Um pedido deverá pertencer a um único cliente.
- Um pedido poderá possuir vários itens.
- Um produto poderá aparecer em vários itens de pedidos.
- Cada item deverá pertencer a um pedido e referenciar um produto.

---

## 6. Fluxo principal de utilização

O fluxo esperado para a utilização do Água Fácil será:

1. O usuário acessa o sistema.
2. Cadastra os produtos comercializados.
3. Cadastra os clientes.
4. Consulta ou corrige informações de produtos e clientes quando necessário.
5. Acessa a seção de pedidos.
6. Consulta os pedidos existentes e seus respectivos status.
7. Caso precise registrar uma nova venda, inicia um novo pedido.
8. Seleciona um cliente já cadastrado.
9. Seleciona os produtos desejados.
10. Informa as quantidades.
11. O sistema verifica a disponibilidade do estoque.
12. O sistema calcula os subtotais e o valor total.
13. O usuário confere as informações.
14. Confirma o cadastro do pedido.
15. O sistema registra o pedido, seus itens e atualiza o estoque.
16. O usuário acompanha e atualiza o status do pedido até sua conclusão.

---

## 7. Critérios gerais de conclusão do projeto

A primeira versão do Água Fácil poderá ser considerada funcional quando:

- [ ] For possível cadastrar, consultar e editar produtos.
- [ ] For possível cadastrar, consultar e editar clientes.
- [ ] For possível visualizar os pedidos registrados.
- [ ] For possível identificar o cliente de cada pedido.
- [ ] For possível selecionar produtos cadastrados em um pedido.
- [ ] For possível inserir a quantidade desejada.
- [ ] O sistema impedir pedidos com estoque insuficiente.
- [ ] O sistema calcular os subtotais automaticamente.
- [ ] O sistema calcular o valor total do pedido.
- [ ] O sistema armazenar os preços praticados na venda.
- [ ] O sistema registrar pedidos e seus respectivos itens corretamente.
- [ ] O estoque ser atualizado após a confirmação do pedido.
- [ ] O usuário conseguir consultar e atualizar o status.
- [ ] O cancelamento preservar o histórico e tratar corretamente o estoque.
- [ ] A interface funcionar adequadamente em smartphones.
- [ ] Os dados permanecerem salvos após reiniciar a aplicação.
- [ ] As operações principais serem testadas com dados válidos e inválidos.

---

## 8. Fora do escopo da primeira versão

Para manter o desenvolvimento controlado, as seguintes funcionalidades não são obrigatórias para a primeira versão:

- Integração com WhatsApp.
- Emissão de notas fiscais.
- Integração com sistemas de pagamento.
- Gestão financeira completa.
- Relatórios avançados e dashboards.
- Controle de múltiplos estabelecimentos.
- Aplicativo nativo para Android ou iOS.

Essas funcionalidades poderão ser consideradas em versões futuras, conforme as necessidades do negócio.

---

## 9. Considerações finais

O Água Fácil deverá funcionar como uma ferramenta de apoio à operação diária de um pequeno comércio de revenda de água.

A prioridade do desenvolvimento será garantir que o fluxo de produtos, clientes, pedidos e estoque funcione corretamente antes da implementação de recursos adicionais.

Este documento servirá como referência para o desenvolvimento, os testes e a evolução do sistema, podendo ser atualizado conforme novas necessidades forem identificadas.