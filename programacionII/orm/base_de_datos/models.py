from datetime import datetime

from peewee import BooleanField, CharField, DecimalField, ForeignKeyField, DateTimeField, Model, TextField

from db import plsql


class BaseModel(Model):

    class Meta:
        database = plsql


class User(BaseModel):
    username = CharField(max_length=20)
    email = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    active = BooleanField(default=True)
    updated_at = DateTimeField(default=datetime.now)
    created_at = DateTimeField(default=datetime.now)


class Message(BaseModel):
    user = ForeignKeyField(User, backref="mens")
    message = TextField()
    created_at = DateTimeField(default=datetime.now)


class Producto(BaseModel):
    nombre = CharField(max_length=100)
    precio_neto = DecimalField(decimal_places=2, auto_round=True)
    alicuota_iva = DecimalField(decimal_places=2, default=0.21)
    
    @property
    def precio_bruto(self):
        return self.precio_neto + self.alicuota_iva * self.precio_neto