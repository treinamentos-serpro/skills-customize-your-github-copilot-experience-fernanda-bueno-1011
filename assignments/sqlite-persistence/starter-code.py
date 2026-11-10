from contextlib import closing
import sqlite3

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

DATABASE_NAME = "books.db"
app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    year: int


def connect_database() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    with closing(connect_database()) as connection:
        with connection:
            # Crie a tabela books com um ID autoincrementado.
            pass


def list_books() -> list[dict]:
    with closing(connect_database()) as connection:
        # Retorne todas as linhas como dicionários.
        pass


def find_book(book_id: int) -> dict | None:
    with closing(connect_database()) as connection:
        # Retorne um livro como dicionário ou None se ele não existir.
        pass


def create_book(book: Book) -> int:
    with closing(connect_database()) as connection:
        with connection:
            # Insira o livro com parâmetros SQL e retorne o novo ID.
            pass


def update_book(book_id: int, book: Book) -> bool:
    with closing(connect_database()) as connection:
        with connection:
            # Atualize o livro e indique se alguma linha foi alterada.
            pass


def delete_book(book_id: int) -> bool:
    with closing(connect_database()) as connection:
        with connection:
            # Exclua o livro e indique se alguma linha foi alterada.
            pass


@app.on_event("startup")
def startup() -> None:
    initialize_database()


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book_endpoint(book: Book):
    # Salve o livro e retorne o ID junto com os dados enviados.
    pass


@app.get("/books")
def list_books_endpoint():
    return list_books()


@app.get("/books/{book_id}")
def get_book_endpoint(book_id: int):
    book = find_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.put("/books/{book_id}")
def update_book_endpoint(book_id: int, book: Book):
    # Atualize o livro ou gere HTTPException se ele não existir.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_endpoint(book_id: int):
    # Exclua o livro ou gere HTTPException se ele não existir.
    pass