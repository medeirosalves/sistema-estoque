from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Produto(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column()
    sku: Mapped[str] = mapped_column(unique=True)
    preco: Mapped[float] = mapped_column()
    quantidade: Mapped[int] = mapped_column()

    def __init__(self, nome, sku, preco, quantidade):
        self.nome = nome
        self.sku = sku
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return (
            f"Produto: {self.nome}, "
            f"SKU: {self.sku}, "
            f"Preço: {self.preco}, "
            f"Quantidade: {self.quantidade}"
        )