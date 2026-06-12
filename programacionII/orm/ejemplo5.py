"""
Seleccionar todo!!!

"""

from peewee import CharField, Model, SqliteDatabase

DB_NAME = "iades_2026"


plsql = SqliteDatabase(DB_NAME)


class BaseModel(Model):

    class Meta:
        database = plsql


class User(BaseModel):
    username = CharField(max_length=20, unique=True)


# leemos todos los registros
limite = 2
offset = 0
usuarios = User.select().limit(limite).offset(offset)     # lazy 

# cantidad de usuarios
user_cantidad = User.select().count()


for usuario in usuarios:
    print(f"id: {usuario.id}  username: {usuario.username}")

offset = offset + limite

usuarios = User.select().limit(limite).offset(offset)
for usuario in usuarios:
    print(f"id: {usuario.id}  username: {usuario.username}")


print("la cantidad de usuarios es: ", user_cantidad)

limite = 2
offset = 0
pagina = 1

while True:

    usuarios = User.select().limit(limite).offset(offset)     # lazy 
    
    if not usuarios:
        break

    print("pagina:", pagina)
    for usuario in usuarios:
        print(f"id: {usuario.id}  username: {usuario.username}")

    input()
    offset = offset + limite
    pagina += 1
