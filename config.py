import os

base_dir = os.path.dirname(os.path.abspath(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'bki_clients.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    PORT = 5000
