"""
Hacer un modelo que permita relacionar un id (entero) correspondiente a un pedido con su estado (pendiente, enviado, entregado, cancelado)
"""
from enum import Enum

from pydantic import BaseModel


class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"


class Pedido(BaseModel):
    id: int
    estado: EstadoPedido = EstadoPedido.PENDIENTE


p = Pedido(id=23)
print(p)

p.estado = EstadoPedido.ENVIADO

print(p)

print(p.model_dump_json())

data = {
    "id": 67,
    "estado": "pendiente"
}

p1 = Pedido(**data)
print(p1)
