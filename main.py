from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    author: str
    paginas: int
    editorial: str

# Ruta de mi API: http://127.0.0.1:8000

@app.get("/") # cuando se llame a la ruta raiz quiero ejecutar esta funcion...
def index():
    return {'mensaje':'hola bro'}

@app.get('/libros/{id}')
def mostrar_libro(id:int):
    'docstring de la funcion mostrar_libro'
    return {'data': id}

@app.post("/libros")
def insertar_libro(libro: Libro):
    return {'mensaje': f'libro {libro.titulo} insertado'}



