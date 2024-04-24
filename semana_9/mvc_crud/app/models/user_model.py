from database import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.string(50), nullable=False)

    def __init__(self, first_name, last_name, mail, password, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
        self.password = password
        self.birthday = birthday

    def save(self):
        db.session.add(self)
        db.session.commit()


    @staticmethod
    def get_all():
        return User.query.all()


    @staticmethod
    def get_by_id(id):
        return User.query.get(id)


    def update(self):
        db.session.commit()
