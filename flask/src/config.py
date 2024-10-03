import os
class Config:
    SECRET_KEY = os.urandom(24)
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:toor@localhost:5432/prueba'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
