from app.database import db
class product(db.Model):
    # id, name, desdcription,price, stock
    __tablename__ = 'product'
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(255))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    def __init__(self, id, name, description, price, stock):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
    def save (self):
        db.session.add(self)
        db.session.commit()

    def get_all():
        return product.query.all()
    def get_by_id(id):
        return product.query.get(id)
    def update(self, name=None, description=None, price=None, stock=None, quantity=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if stock is not None:
            self.stock = stock
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()