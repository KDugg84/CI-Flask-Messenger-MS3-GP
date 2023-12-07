import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

# variable creates an instance of the Bcrypt class
# with the app variable passed as an argument
bcrypt = Bcrypt(app)

# variable creates an instance of the LoginManager class
# with the app variable passed as an argument
login_manager = LoginManager(app)
login_manager.login_view = 'login'
# adds styles to the login prompt message
login_manager.login_message_category = 'info'

from flaskmessenger import routes  # noqa