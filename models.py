from flask_login import UserMixin

from app import db

class Person(db.Model):
    __tablename__='people'
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)

    def __repr__(self):
        return f"Person named {self.name} is {self.age} years old and is working as {self.job}."
    

class User(db.Model, UserMixin):
    __tablename__='users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50))
    description = db.Column(db.String)

    def __repr__(self):
        return f"User: {self.username}, Role: {self.role}"
    
    def get_id(self):
        return self.uid