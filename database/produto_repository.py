from database.connection import SessionLocal
from models.produto import Produto


def adicionar_produto(produto):
    session = SessionLocal()

    try:
        session.add(produto)
        session.commit()
        session.refresh(produto)
        return produto
    finally:
        session.close()