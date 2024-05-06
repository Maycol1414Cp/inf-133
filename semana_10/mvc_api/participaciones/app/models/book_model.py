from database import db
class Book(db.Model):
    __tablename__ = "books"

    # Define las columnas de la tabla `animals`
    titulo = db.Column(db.String(100), primary_key=True)
    autor = db.Column(db.String(100), nullable=False)
    edicion = db.Column(db.Integer, nullable=False)
    disponibilidad = db.Column(db.Integer, nullable=False)

    # Inicializa la clase `Animal`
    def __init__(self, titulo, autor, edicion, disponibilidad):
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion
        self.disponibilidad = disponibilidad

    # Guarda un animal en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los animales de la base de datos
    @staticmethod
    def get_all():
        return Book.query.all()

    # Obtiene un animal por su ID
    @staticmethod
    def get_by_id(id):
        return Book.query.get(id)

    # Actualiza un animal en la base de datos
    def update(self, titulo=None, autor=None, edicion=None, disponibilidad=None):
        if titulo:
            self.titulo = titulo
        if autor:
            self.autor = autor
        if edicion:
            self.edicion = edicion
        if disponibilidad:
            self.disponibilidad = disponibilidad
        db.session.commit()
    # Elimina un animal de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
