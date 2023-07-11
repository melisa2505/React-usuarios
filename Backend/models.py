from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/reactp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'mysecretkey'

db = SQLAlchemy(app)

class usuarios(db.Model):
    name = db.Column(db.String(45), primary_key=True)
    email = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<usuarios {self.name}>'
    
    def serialize(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

with app.app_context():
    db.create_all()


