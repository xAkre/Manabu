from typing import Any
from secrets import token_urlsafe
from flask import Flask
from flask_session import Session as ServerSideSession


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = token_urlsafe(16)

ServerSideSession(app)


@app.route("/")
def landing_page() -> Any:
    """
    The application's landing page
    """
    return "Hello, world!"
