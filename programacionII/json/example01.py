"""
json: Java Script Object Notation
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
    "cursos": [ "0", "1"],
    "atributos": {
        "A": 0,
        "B": 1,
    },
    "colores": ("rojo", "azul")
}

print("datos python")
print(datos)
print("type", type(datos))

datos_json = json.dumps(datos, indent=4)


print("datos_json")
print(datos_json)
print("type: ", type(datos_json))

"""
json ----> python
"""

datos_python = json.loads(datos_json)

print("datos python")
print(datos_python)
