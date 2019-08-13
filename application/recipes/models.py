from application import db

from application.models import Base


class Recipe(Base):

    name = db.Column(db.String(144), nullable=False)
    type = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(4000), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.type = "Regular"
        self.description = "none"
        self.content = "none"