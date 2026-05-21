"""
Quiero dar de alta un alumno

Nombre 
edad

y fecha y hora de creacion

guardar un registro en un archivo json

"""

import json

from datetime import datetime


class Alumno:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.fecha = datetime.now()

    def to_json():
        pass

        return object_json

alumno = {
    "nombre": "Hernan",
    "edad": 26,
    "fecha": datetime.now().isoformat()
}


print(alumno)

alumno_json = json.dumps(alumno)

print(alumno_json)

alumno = json.loads(alumno_json)

print(alumno)

fecha = datetime.fromisoformat(alumno["fecha"])


alumno["fecha"] = fecha

print(alumno)


