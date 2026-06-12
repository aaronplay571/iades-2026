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

# cantidad de usuarios
user_cantidad = User.select().count()
cant_pag = int(input("cuantos usuarios x pagina: "))

# aca algo hay que hacer
paginas = int(user_cantidad / cant_pag)

if user_cantidad % cant_pag:
    paginas +=1

print(f"Hay {paginas} paginas en total")

limite = cant_pag
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
