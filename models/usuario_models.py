from sqlmodel import SQLModel, Field

class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    email: str
