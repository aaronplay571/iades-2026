"""
Generar un modelo para guardar usuario y contraseña
"""
import os

from dotenv import load_dotenv
from pydantic import BaseModel, SecretStr


class UserConnect(BaseModel):
    username : str
    password: SecretStr


load_dotenv()

user = os.getenv("USER_APP")
password = os.getenv("USER_PASSWORD")

c = UserConnect(username=user, password=password)

print(c)
print(c.password.get_secret_value())