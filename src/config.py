from os import path


class Config:
    BASE_DIR = path.abspath(path.dirname(__file__))
    TEMPLATES_FOLDER = path.join(path.dirname(__file__), "templates")
    STATIC_FOLDER = path.join(path.dirname(__file__), "static")
    DATABASE_URL = "sqlite:///" + path.join(path.dirname(__file__), "manabu.sqlite")
