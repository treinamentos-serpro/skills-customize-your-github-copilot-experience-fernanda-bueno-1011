# Código Inicial para a Tarefa de APIs REST com FastAPI
# Execute com: uvicorn main:app --reload
# Renomeie este arquivo para main.py antes de executar.

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


# Tarefa 1: Criar o Primeiro Endpoint

@app.get("/")
def read_root():
    # Retornar um dicionário com a chave "message"
    pass


@app.get("/greet/{name}")
def greet(name: str):
    # Retornar um dicionário com a chave "greeting"
    pass


# Tarefa 2: Receber Dados com Modelos Pydantic

class Book(BaseModel):
    # Definir os campos: title, author, year e pages (opcional)
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    # Cadastrar o livro e retornar os dados
    pass


# Tarefa 3: Implementar um CRUD Completo

books_db: dict[int, Book] = {}
next_id = 1


@app.get("/books")
def list_books():
    # Retornar todos os livros
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # Retornar o livro ou lançar HTTPException 404
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    # Substituir os dados do livro ou lançar HTTPException 404
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # Remover o livro ou lançar HTTPException 404
    pass
