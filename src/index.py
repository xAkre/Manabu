from secrets import token_urlsafe
from flask import Flask
from flask_session import Session as ServerSideSession
from database import session, set_database
from routes import general_router, auth_router, categories_router
from config import Config

app = Flask(
    __name__,
    static_folder=Config.STATIC_FOLDER,
    template_folder=Config.TEMPLATES_FOLDER,
)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = token_urlsafe(16)

ServerSideSession(app)

app.register_blueprint(general_router)
app.register_blueprint(auth_router)
app.register_blueprint(categories_router)

set_database(Config.DATABASE_URL)


@app.teardown_appcontext
def shutdown_session(
    _,
) -> None:
    """
    Rollback any uncommitted changes and remove the current session after every request
    """
    session.rollback()
    session.remove()
