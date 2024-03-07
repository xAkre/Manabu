from os import path


class Config:
    BASE_DIR = path.abspath(path.dirname(__file__))
    TEMPLATES_FOLDER = path.abspath("src/templates")
    STATIC_FOLDER = path.abspath("src/static")
    DATABASE_URL = "sqlite:///" + path.abspath("manabu.sqlite")
