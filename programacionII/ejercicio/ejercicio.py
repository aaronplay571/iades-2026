"""

Modelos Peewee — Autor y Libro con relación ForeignKeyField y backref.
Hacer un CRUD con pydantic

Autor
- nombre
- apellido
- pais

Libro
- titulo
- autor ---> ForeignKey
- genero
- editorial
- fecha_publicacion


modelos.py   ---> DB
schemas.py  ----> validar datos de entrada
crud.py
main.py 

README.py

1. Creamos el entorno virtual
2. Activamos
3. instalamos peewee y pydantic
4. Cremos un models.py
    - peewee
    - modelo BaseModel
    - modelo Autor
    - modelo Libro
"""

