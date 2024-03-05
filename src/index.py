from secrets import token_urlsafe
from flask import Flask
from flask_session import Session as ServerSideSession
from database import session, set_database
from routes import general_router, auth_router
from config import Config


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = token_urlsafe(16)

ServerSideSession(app)

app.register_blueprint(general_router)
app.register_blueprint(auth_router)

set_database(Config.DATABASE_URL)


@app.teardown_appcontext
def shutdown_session(exc=None) -> None: # noqa: Suppress "Parameter 'exc' value is not used". Flask requires the parameter to be there
    """
    Rollback any uncommitted changes and remove the current session after every request
    """
    session.rollback()
    session.remove()
