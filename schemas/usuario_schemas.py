from sqlmodel import SQLModel

class UsuarioUpdate(SQLModel):
    nome: str | None = None
    email: str | None = None