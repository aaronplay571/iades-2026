"""
Vamos a crear la Base y la tabla User

"""

from peewee import CharField, Model, SqliteDatabase

DB_NAME = "iades_2026"


plsql = SqliteDatabase(DB_NAME)


class BaseModel(Model):

    class Meta:
        database = plsql


class User(BaseModel):
    username = CharField(max_length=20, unique=True)


plsql.connect()
# plsql.create_tables([User])


tables = plsql.get_tables()

for table in tables:
    print("tabla: ", table)

