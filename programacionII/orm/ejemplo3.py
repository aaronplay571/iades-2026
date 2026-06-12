"""
leer un usuario por un atributo  
"""


from peewee import CharField, Model, SqliteDatabase, DoesNotExist

DB_NAME = "iades_2026"


plsql = SqliteDatabase(DB_NAME)


class BaseModel(Model):

    class Meta:
        database = plsql


class User(BaseModel):
    username = CharField(max_length=20, unique=True)


# busca el usuario carlos14 en la tabla User
user = User.get(username="carlos14")

print("username: ", user.username)


# Usuario ingrese un username y lo busque

# Usuario a buscar
user = input("Ingrese el nombre de usuario a buscar: ")

try:
    user_obj = User.get(username=user)
    print(f"id: {user_obj.id}   -- username: {user_obj.username}")
except DoesNotExist:
    print(f"El usuario {user} no existe!!!")

