from fastapi import FastAPI
from database import criar_banco
from routes.usuarios_routes import router as usuarios_router

app = FastAPI()

criar_banco()

app.include_router(usuarios_router, prefix="/usuarios", tags=["Usuários"])

@app.get("/")
def raiz():
    return {"message": "API funcionando!"}
