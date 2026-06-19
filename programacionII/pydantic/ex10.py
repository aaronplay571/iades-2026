"""
Crear un modelo para un ticket
id: int
estado: str
fecha_creacion: 
"""

from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, ConfigDict

# Representa la estructura en la DB
class Pedido(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        strict=False,
        frozen=False,
        populate_by_name=True
    )

    id: UUID = Field(default_factory=uuid4)
    nombre: str = Field(alias="name")
    codigo: int = Field(gt=0)
    estado: str = "pendiente"
    descripcion: str = Field(min_length=2, max_length=50, description="Descripcion del producto")
    fecha_creacion: datetime = Field(default_factory=datetime.now)
    fecha_modificacion: datetime = Field(default_factory=datetime.now)


class PedidoUpdate(BaseModel):
    codigo: str
    estado: str
    fecha_modificacion: datetime = Field(default_factory=datetime.now)



p = Pedido(name="NombreProducto", codigo="67", descripcion="Producto nuevo")
print(p)

print(Pedido.model_config)

print("dict python: ",p.model_dump())
print("json: ", p.model_dump_json())

print(p.model_json_schema())
