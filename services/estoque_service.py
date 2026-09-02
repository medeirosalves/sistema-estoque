from database.produto_repository import (
    adicionar_produto,
    listar_produtos,
    buscar_produto,
    remover_produto,
    atualizar_produto
)


class Estoque:

    def adicionar_produto(self, produto):
        adicionar_produto(produto)

    def listar_produtos(self):
        return listar_produtos()

    def buscar_produto(self, sku):
        return buscar_produto(sku)

    def remover_produto(self, sku):
        return remover_produto(sku)

    def atualizar_produto(self, sku, nome, preco, quantidade):
        return atualizar_produto(sku, nome, preco, quantidade)