from models import db_init
from datetime import date
from schemas import AutorSchema, LibroSchema
from crud import (
    crear_autor,
    crear_libro,
    listar_libros_por_autor
)


def main():

    db_init()

    autor = AutorSchema(
        nombre="Gabriel",
        apellido="Garcia Marquez",
        pais="Colombia"
    )

    nuevo_autor = crear_autor(autor)

    libro = LibroSchema(
        titulo="Cien años de soledad",
        autor_id=nuevo_autor.id,
        genero="Realismo Magico",
        editorial="Sudamericana",
        fecha_publicacion=date(1967, 5, 30)  # 👈 FIX
    )

    crear_libro(libro)

    listar_libros_por_autor(nuevo_autor.id)


if __name__ == "__main__":
    main()