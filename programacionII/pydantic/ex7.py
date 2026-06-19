"""
Tipos de datos soportados
"""


# Tipos prmitivos
from datetime import datetime, timedelta
from uuid import UUID
from pathlib import Path
from decimal import Decimal
from pydantic import BaseModel
from typing import Any, Optional


class Tipos(BaseModel):
    cadena: str
    entero: int
    flotante: float
    booleano: bool
    cualquiera: Any


class Mixto(BaseModel):
    lista: list[int]
    diccionario: dict[str, Any]
    tupla: tuple
    conjunto: set


t = Tipos(
    cadena="Hola",
    entero=56,
    flotante=78.9,
    booleano=True,
    cualquiera=45
)

m = Mixto(
    lista=[0, 4],
    diccionario={"A": 34},
    tupla=(8, 9),
    conjunto={8, 9, 0}

)

print(t)
print(m)


# Uniones

class Especial(BaseModel):
    campo_opcional: Optional[str] = None     # str | None = None
    campo_multivalor: int | str


e1 = Especial(campo_multivalor=56)
print(e1)

e2 = Especial(campo_multivalor="Hola mundo!!!")
print(e2)


e3 = Especial(campo_opcional="ppp", campo_multivalor=677)
print(e3)


# tipos de datos mas avanzados!
class TiposAvanzados(BaseModel):
    fecha_hora: datetime
    duracion: timedelta
    id: UUID
    path: Path
    precio: Decimal


fecha_hora = datetime.now()
duracion = timedelta(days=2)
id = UUID("12345678-1234-5678-1234-567812345678")
path = Path("/tmp")
precio = Decimal("23.67")

ta = TiposAvanzados(
    fecha_hora=fecha_hora,
    duracion=duracion,
    id=id,
    path=path,
    precio=precio

)

print(ta)
