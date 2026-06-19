"""
Un modelo producto

que tenga un id, nombre, precio, tags(lista de str), descriprion (Opcional)
"""

from pydantic import BaseModel
from typing import Optional


class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    tags: list[str] = []
    descripcion: Optional[str] = None


# creación directa
p = Producto(id=34, nombre="batidora", precio=5000.0)
print(p)


# desde un diccionario
p_dict = {
    "id": 78,
    "nombre": "Televisor",
    "precio": 60000.0,
    "tags": ["9", "9"],
    "descripcion": "Televisor de 40 pulgadas" 
}

p1 = Producto(**p_dict)
print(p1)

# model_validate
p2 = Producto.model_validate(p_dict)
print(p2)

# Acceso a los atributos

print("nombre", p2.nombre)

# como un dict

p2_dict = p2.model_dump()
print("p2: ", p2_dict)

# como json
print(p2.model_dump_json())

# json schema

print(p2.model_json_schema())