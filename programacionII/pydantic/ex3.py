"""
Un modelo Usuario que tenga los siguientes campos
nombre edad mail
"""

from pydantic import BaseModel


class Usuario(BaseModel):
    nombre: str
    edad: int = 0
    email: str


# Generar una instancia
u = Usuario(nombre="pepe", edad=45, email="pepe@mail.com")
print(u)

print("nombre:", u.nombre)
print("edad: ", u.edad)

print(u.model_dump())

print(u.model_dump_json())


print(u.model_json_schema())