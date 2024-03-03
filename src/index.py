from typing import Any
from flask import Flask


app = Flask(__name__)


@app.route("/")
def landing_page() -> Any:
    """
    The application's landing page
    """
    return "Hello, world!"
