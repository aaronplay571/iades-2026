"""
Los modelos por default son mutables
"""
import os

from dotenv import load_dotenv
from pydantic import BaseModel


class ConfigServer(BaseModel):
    model_config = {
        "frozen": True
    }
    host: str
    puerto: int


load_dotenv()

mail_server = ConfigServer(
    host=os.getenv("MAIL_DIRECCION"),
    puerto=os.getenv("MAIL_PUERTO")
)

print(mail_server)

# da error
# mail_server.puerto = 9000
