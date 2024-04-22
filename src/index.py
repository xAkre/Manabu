from secrets import token_urlsafe
from flask import Flask, session as f_session
from flask_session import Session as ServerSideSession
from database import session as d_session, set_database
from database.models import User
from routes import general_router, auth_router, categories_router, todos_router
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
app.register_blueprint(todos_router)

set_database(Config.DATABASE_URL)


@app.before_request
def set_user() -> None:
    """
    Add the current user to flask session on creating a request
    """
    if f_session.get("user"):
        f_session.pop("user")

    user_uuid = f_session.get("user_uuid")
    if user_uuid:
        user = d_session.get(User, user_uuid)
        f_session.update({"user": user})


@app.teardown_appcontext
def shutdown_session(
    _,
) -> None:
    """
    Rollback any uncommitted changes and remove the current session after every request
    """
    d_session.rollback()
    d_session.remove()
