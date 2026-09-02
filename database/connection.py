from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database/produtos.db")

SessionLocal = sessionmaker(bind=engine)