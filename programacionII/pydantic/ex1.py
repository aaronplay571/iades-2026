"""
pydantic: Instalación

pip install pydantic   (v2 --- RUST)    (v1)

"""
from pydantic import BaseModel


class Producto(BaseModel):
    id: int
    nombre: str


p = Producto(id=5, nombre="cuaderno")
print("producto: ", p)

# asi no
# p1 = Producto(6, "cuaderno")
# print("producto: ", p1)

p2_dict = {
    "id": 10,
    "nombre": "marcador"
}
p2 = Producto(**p2_dict)
print("producto: ", p2)


p3 = Producto(id="15", nombre="cuaderno")
print("producto: ", p3)


print("p3 id", p3.id)
print(type(p3.id))

p3 = Producto(id="15", nombre=67)