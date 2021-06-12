from api import db


class ClientModel(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=False)
    surname = db.Column(db.String(32), unique=False)
    email = db.Column(db.String(120), unique=True)
    loans = db.relationship('LoanModel', backref='client', lazy='joined', cascade="all, delete-orphan")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
