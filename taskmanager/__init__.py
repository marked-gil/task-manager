import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Since env.py is not pushed to GitHub, this file will not be visible once deployed to Heroku, & will throw an error
# So, we only need to import env if the OS can find an existing file path for the env.py file itself
if os.path.exists("env.py"):
    import env   # noqa

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")     

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  #heroku

db = SQLAlchemy(app)

from taskmanager import routes  # noqa

