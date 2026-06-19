"""
Direccion
- calle
- ciudad
- codigo_postal
- pais


Contacto
- tipo:   # email telefono
- valor: 

Cliente:
- id entero
- nombre
- direccion
- contactos : Aca se guardan los contactos lista con los diferentes tipos de contactos
"""

from pydantic import BaseModel


class Direccion(BaseModel):
    calle: str
    ciudad: str
    codigo_postal: str 
    pais: str     


class Contacto(BaseModel):
    tipo: str
    valor: str


class Cliente(BaseModel):
    id: int
    nombre: str
    direccion: Direccion
    contactos: list[Contacto]


d = Direccion(calle="Sin nombre", ciudad="ciudad", codigo_postal="4546", pais="ARG")
c1 = Contacto(tipo="emai", valor="un@mail.com")
c2 = Contacto(tipo="telefono", valor="3243534534")
contactos = [c1, c2]

cl = Cliente(id=6, nombre="fulano", direccion=d, contactos=contactos)

print(cl.model_dump())
