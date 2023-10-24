
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    vitamins = db.Column(db.String(255))
    minerals = db.Column(db.String(255))
    lipids = db.Column(db.Float)
    proteins = db.Column(db.Float)
    carbohydrates = db.Column(db.Float)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # For simplicity, no encryption
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)

class BMIRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bmi_value = db.Column(db.Float)
    date_recorded = db.Column(db.Date, default=db.func.current_date())
