"""

validar varias veces mayor de 18


"""
from typing import Annotated
from pydantic import BaseModel, Field


Mayor18 = Annotated[int, Field(gt=18) ]


class A(BaseModel):
    edad: Mayor18


class B(BaseModel):
    edad_participante: Mayor18


class C(BaseModel):
    edad_empleado: Mayor18

print(A(edad=78))

