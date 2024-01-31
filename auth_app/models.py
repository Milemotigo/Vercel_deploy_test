from datetime import datetime
from ..api.app import db

from flask_login import UserMixin

class User(UserMixin, db.Model):
    '''User table'''
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(100))
    profile_photo = db.Column(db.String(255), nullable=True)  # Allow nullable
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

