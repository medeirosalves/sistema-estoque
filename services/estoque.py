class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, sku):
        self.produtos = [produto for produto in self.produtos if produto.sku != sku]

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, sku):
        for produto in self.produtos:
            if produto.sku == sku:
                return produto
        return None