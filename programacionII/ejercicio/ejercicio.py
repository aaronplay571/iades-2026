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

README.md

1. Creamos el entorno virtual
2. Activamos el entorno 
3. Instalamos peewee y pydantic
4. Creamos los modelos [models.py]
    - peewee
    - modelo BaseModel
    - modelo Autor
    - modelo Libro
5.Crear schemas de pydantic para los modelos [schemas.py]
6. Crear las siguientes funciones
    - crear_autor
    - crear_libro
    -listar_libros_por_autor
"""

