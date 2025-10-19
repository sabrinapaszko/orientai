from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(255), nullable=False)
    
