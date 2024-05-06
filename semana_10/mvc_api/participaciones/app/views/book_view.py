def render_book_list(books):
    # Representa una lista de animales como una lista de diccionarios
    return [
        {
            "titulo": book.titulo,
            "autor": book.autor,
            "edicion": book.edicion,
            "disponibilidad": book.disponibilidad
        }
        for book in books
    ]


def render_book_detail(book):
    # Representa los detalles de un animal como un diccionario
    return {
        "titulo": book.titulo,
        "autor": book.autor,
        "edicion": book.edicion,
        "disponibilidad": book.disponibilidad,
    }
