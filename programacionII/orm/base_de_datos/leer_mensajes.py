"""
Listar los usuarios por id
Seleccionar un id y mostrar los mensajes de ese usuario
"""

from models import User, Message

# Listar los usuarios

users = User.select()  # tengo la consulta a todos los usuarios

for user in users:
    print(f"id: {user.id} ---- username: {user.username}")

id = int(input("Seleccione el usuario: "))


user = User.get_by_id(id)


print(f"mensajes de : {user.username}")

mensajes = Message.select().where(Message.user == user)

for mensaje in mensajes:
    print(mensaje.message)


# usar la referencia
print("Mensajes por la referencia")

for mensaje in user.mens:
    print(f"mensaje: {mensaje.message} -- creado: {mensaje.created_at}")