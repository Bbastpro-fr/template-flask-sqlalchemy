from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)