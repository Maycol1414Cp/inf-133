from flask import Blueprint, request, jsonify
from app.models.book_model import book
from app.views.book_view import render_book_list, render_book_detail

# Crear un blueprint para el controlador de bookes
book_bp = Blueprint("Book", __name__)


# Ruta para obtener la lista de bookes
@book_bp.route("/books", methods=["GET"])
def get_books():
    books = book.get_all()
    return jsonify(render_book_list(books))


# Ruta para obtener un book específico por su ID
@book_bp.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = book.get_by_id(id)
    if book:
        return jsonify(render_book_detail(book))
    return jsonify({"error": "book no encontrado"}), 404


# Ruta para crear un nuevo book
@book_bp.route("/books", methods=["POST"])
def create_book():
    data = request.json
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad")

    # Validación simple de datos de entrada
    if not titulo or not autor or edicion is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo book y guardarlo en la base de datos
    book = book(titulo=titulo, autor=autor, edicion=edicion, disponibilidad=disponibilidad)
    book.save()

    return jsonify(render_book_detail(book)), 201


# Ruta para actualizar un book existente
@book_bp.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book = book.get_by_id(id)

    if not book:
        return jsonify({"error": "book no encontrado"}), 404

    data = request.json
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad")

    # Actualizar los datos del book
    book.update(titulo=titulo, autor=autor, edicion=edicion, disponibilidad=disponibilidad)

    return jsonify(render_book_detail(book))


# Ruta para eliminar un book existente
@book_bp.route("/books/<string:titulo>", methods=["DELETE"])
def delete_book(titulo):
    book = book.get_by_titulo(titulo)

    if not book:
        return jsonify({"error": "book no encontrado"}), 404

    # Eliminar el book de la base de datos
    book.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
