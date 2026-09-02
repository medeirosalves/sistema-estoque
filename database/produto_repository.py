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


def listar_produtos():
    session = SessionLocal()

    try:
        return session.query(Produto).all()
    finally:
        session.close()


def buscar_produto(sku):
    session = SessionLocal()

    try:
        return session.query(Produto).filter_by(sku=sku).first()
    finally:
        session.close()


def remover_produto(sku):
    session = SessionLocal()

    try:
        produto = session.query(Produto).filter_by(sku=sku).first()

        if produto:
            session.delete(produto)
            session.commit()
            return True

        return False

    finally:
        session.close()

def atualizar_produto(sku, nome, preco, quantidade):
    session = SessionLocal()

    try:
        produto = session.query(Produto).filter_by(sku=sku).first()

        if produto:
            produto.nome = nome
            produto.preco = preco
            produto.quantidade = quantidade

            session.commit()
            session.refresh(produto)

            return produto

        return None

    finally:
        session.close()