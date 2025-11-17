📘 CRUD de Usuários com FastAPI + SQLModel

Este projeto é um CRUD completo de usuários desenvolvido com FastAPI, SQLModel e SQLite.
O objetivo é praticar organização de projeto, divisão em módulos e a construção de uma API profissional.

🚀 Tecnologias utilizadas

Python 3.11+

FastAPI

Uvicorn

SQLModel

SQLite

Pydantic

📁 Estrutura do projeto
📦 projeto-fastapi-crud

├── models/usuario_models.py

├── schemas/usuario_schemas.py

├── routes/usuarios_routes.py

├── database.py

├── database.db

├── main.py

└── README.md


models/ → classes que representam as tabelas no banco

schemas/ → modelos usados para entrada/saída de dados (DTOs)

routes/ → arquivos com todos os endpoints organizados

database.py → engine e criação do banco

main.py → ponto de entrada da aplicação

📌 Funcionalidades da API

✔ Listar usuários

GET /usuarios/usuarios

Com filtros opcionais:

id

nome

email


✔ Criar usuário

POST /usuarios/usuarios/criar


✔ Atualizar usuário

PATCH /usuarios/usuarios/atualizar/{id}


✔ Deletar usuário

DELETE /usuarios/usuarios/deletar/{id}


▶ Como rodar o projeto

Instale as dependências:

pip install fastapi uvicorn sqlmodel


Rode a API:

uvicorn main:app --reload


Acesse a documentação automática:

http://127.0.0.1:8000/docs
