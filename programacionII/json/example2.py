"""
json con archivos
"""


import json


"""
python ----> json
"""

datos = {
    "nombre": "Juan",
    "apellido": "Gramardi",
    "edad": 26,
    "altura": 76.8,
    "estado": True,
    "activo": False,
    "notas": None,
    "cursos": [ "0", "1" ],
    "atributos": {
        "A": 0,
        "B": 1,
    },
    "colores": ("rojo", "azul")
}

print("datos python")
print(datos)
print("type", type(datos))

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)


"""
json ----> python
"""


with open("datos.json", "r") as archivo:
    datos = json.load(archivo)

print("datos python")
print(datos)
