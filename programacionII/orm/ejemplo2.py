"""
Vamos a dar de alta un usuario

"""

from peewee import CharField, Model, SqliteDatabase

DB_NAME = "iades_2026"


plsql = SqliteDatabase(DB_NAME)


class BaseModel(Model):

    class Meta:
        database = plsql


class User(BaseModel):
    username = CharField(max_length=20, unique=True)


user = User(username="carlos17")
user.save()
