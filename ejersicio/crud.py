from models import Autor, Libro
from schemas import AutorSchema, LibroSchema


def crear_autor(datos: AutorSchema):

    autor = Autor.create(
        nombre=datos.nombre,
        apellido=datos.apellido,
        pais=datos.pais
    )

    return autor


def crear_libro(datos: LibroSchema):

    autor = Autor.get_by_id(datos.autor_id)

    libro = Libro.create(
        titulo=datos.titulo,
        autor=autor,
        genero=datos.genero,
        editorial=datos.editorial,
        fecha_publicacion=datos.fecha_publicacion
    )

    return libro


def listar_libros_por_autor(id_autor: int):

    autor = Autor.get_by_id(id_autor)

    print(f"\nLibros de {autor.nombre} {autor.apellido}")

    for libro in autor.libros:
        print(
            f"- {libro.titulo} "
            f"({libro.genero})"
        )