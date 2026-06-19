"""
Armar un modelo para representar una direccion
"""

from pydantic import BaseModel
from typing import Optional


class Direccion(BaseModel):
    calle: str
    altura: int
    localidad: str
    provincia: str
    cp: str
    piso: str
    departamento: Optional[str] = None


d = Direccion(
    calle="xxx",
    altura=0,
    localidad="localidad_direccion",
    provincia="provincia_direccion",
    cp="AW123",
    piso="3"
)

print(d)

d.piso = "5"

print(d)
