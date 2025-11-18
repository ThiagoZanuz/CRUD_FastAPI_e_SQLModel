from sqlmodel import SQLModel, create_engine

DATABASE_URL = 'sqlite:///database.db'
engine = create_engine(DATABASE_URL)

def criar_banco():
    SQLModel.metadata.create_all(engine)
