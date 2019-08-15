from flask import render_template
from application import app
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html", has_recipe=User.users_with_recipes())
