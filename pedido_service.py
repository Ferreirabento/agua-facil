from database import (
    conectar,
    buscar_cliente_na_conexao,
    criar_pedido_na_conexao,
    buscar_produto_na_conexao,
    descontar_estoque_na_conexao,
    criar_item_pedido_na_conexao,
)


def registrar_pedido(cliente_id, itens):
    """Registra pedido, itens e baixa de estoque em uma única transação."""

    if not itens:
        raise ValueError("O pedido precisa ter pelo menos um produto.")

    conexao = conectar()

    try:
        conexao.execute("BEGIN")

        cliente = buscar_cliente_na_conexao(conexao, cliente_id)
        if cliente is None:
            raise ValueError("Cliente não encontrado ou indisponível.")

        pedido_id = criar_pedido_na_conexao(conexao, cliente_id)

        for item in itens:
            try:
                produto_id = int(item["produto_id"])
                quantidade = int(item["quantidade"])
            except (KeyError, TypeError, ValueError):
                raise ValueError("Informe um produto e uma quantidade válidos.")

            if quantidade <= 0:
                raise ValueError("A quantidade deve ser maior que zero.")

            produto = buscar_produto_na_conexao(conexao, produto_id)
            if produto is None:
                raise ValueError(
                    f"Produto {produto_id} não encontrado ou indisponível."
                )

            linhas_atualizadas = descontar_estoque_na_conexao(
                conexao, produto_id, quantidade
            )
            if linhas_atualizadas == 0:
                raise ValueError(
                    f"Estoque insuficiente para o produto {produto_id}."
                )

            criar_item_pedido_na_conexao(
                conexao,
                pedido_id,
                produto_id,
                quantidade,
                produto["preco"],
            )

        conexao.commit()
        return pedido_id

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()
