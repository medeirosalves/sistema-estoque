class Produto:
    def __init__(self, nome, sku, preco, quantidade):
        self.nome = nome
        self.sku = sku
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"Produto: {self.nome}, SKU: {self.sku}, Preço: {self.preco}, Quantidade: {self.quantidade}"