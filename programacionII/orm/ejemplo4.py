"""
Ingresar un id y lo vamos a borrar

"""


from peewee import CharField, Model, SqliteDatabase, DoesNotExist

DB_NAME = "iades_2026"


plsql = SqliteDatabase(DB_NAME)


class BaseModel(Model):

    class Meta:
        database = plsql


class User(BaseModel):
    username = CharField(max_length=20, unique=True)


id_user = int(input("ingrese el id del usuario a eliminar: "))

try:
    user_obj = User.get_by_id(id_user)
except DoesNotExist:
    print(f"El usuario con el id {id_user} no existe")
    exit(1)


status = user_obj.delete_instance()

print("DEBUG-- status: ", status)

if status:
    print("Se elimino el usuario exitosamente")