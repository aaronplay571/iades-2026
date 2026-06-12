from models import Message, User


usuario = {
    "username": "prueba5",
    "email": "prueba5@mail.com",
    "password": "mipassword",
}


# opcion 1
# foo = User(**usuario)
# foo.save()

# opcion 2
foo = User.create(**usuario)

print("id: ", foo.id)


"""
class Message(BaseModel):
    user = ForeignKeyField(User, backref="mens")
    message = TextField()
    created_at = DateTimeField(default=datetime.now)
"""

# opcion 1
mensaje = Message(user=foo, message="Hola mundo!!!")
mensaje.save()

# opcion 2
mensaje = Message.create(user=foo, message="Chau mundo!!!")