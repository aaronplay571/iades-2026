from dataclasses import dataclass


@dataclass
class Producto:
    id: int
    nombre: str


# Generar una instancia de producto
p1 = Producto(id=8, nombre="cuaderno")
print(p1)

# Generar una instancia de producto
p2 = Producto(9, "cuaderno")
print(p2)

# Generar una instancia de producto
p3 = Producto("8", 9.0)
print(p3)
