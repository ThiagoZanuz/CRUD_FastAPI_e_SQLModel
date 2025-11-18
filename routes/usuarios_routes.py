from database import engine
from models.usuario_models import Usuario
from schemas.usuario_schemas import UsuarioUpdate

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import Session, select

router = APIRouter(prefix='/usuarios', tags=['Usuários'])

@router.get('/')
def listar_usuario(
    id: int | None = Query(None),
    nome: str | None = Query(None),
    email: str | None = Query(None)
):
    with Session(engine) as session:
        statement = select(Usuario)

        if id is not None:
            statement = statement.where(Usuario.id == id)
        if nome is not None:
            statement = statement.where(Usuario.nome == nome)
        if email is not None:
            statement = statement.where(Usuario.email == email)
        
        resultado = session.exec(statement).all()
        return resultado
    

@router.post('/criar')
def criar_usuario(usuario: Usuario):
    with Session(engine) as session:
        session.add(usuario)
        session.commit()
        session.refresh(usuario)
        return usuario
    
@router.patch('/atualizar/{usuario_id}')
def atualizar_usuario(usuario_id: int, dados: UsuarioUpdate):
    with Session(engine) as session:
        usuario_consultado = session.get(Usuario, usuario_id)

        if not usuario_consultado:
            raise HTTPException(status_code = 404, detail = 'Usuário não encontrado')
        
        if dados.nome is not None:
            usuario_consultado.nome = dados.nome

        if dados.email is not None:
            usuario_consultado.email = dados.email
        
        session.add(usuario_consultado)
        session.commit()
        session.refresh(usuario_consultado)

        return usuario_consultado

@router.delete('/deletar/{usuario_id}')
def deletar_usuario(usuario_id: int):
    with Session(engine) as session:
        usuario_consultado = session.get(Usuario, usuario_id)

        if not usuario_consultado:
            raise HTTPException(status_code=404, detail='Usuário não encontrado')
        
        session.delete(usuario_consultado)
        session.commit()
        return {'message': 'Usuário deletado com sucesso!'}