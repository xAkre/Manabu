from secrets import token_urlsafe
from flask import Flask
from flask_session import Session as ServerSideSession
from routes import general_router, auth_router


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = token_urlsafe(16)

ServerSideSession(app)

app.register_blueprint(general_router)
app.register_blueprint(auth_router)
