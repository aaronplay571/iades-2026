from datetime import date
from pydantic import BaseModel


class AutorSchema(BaseModel):
    nombre: str
    apellido: str
    pais: str


class LibroSchema(BaseModel):
    titulo: str
    autor_id: int
    genero: str
    editorial: str
    fecha_publicacion: date