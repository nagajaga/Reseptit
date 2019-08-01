from application import app, db
from flask import render_template, request, url_for, redirect
from application.recipes.models import Recipe


@app.route("/recipes/<recipe_id>/", methods=["POST"])
def recipe_set_type(recipe_id):
    b = Recipe.query.get(recipe_id)
    b.type = "Vegetarian"
    db.session().commit()

    return redirect(url_for("recipes_index"))


@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes=Recipe.query.all())


@app.route("/recipes/new/")
def recipes_form():
    return render_template("recipes/new.html")


@app.route("/recipes/", methods=["POST"])
def recipes_create():
    t = Recipe(request.form.get("name"))
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("recipes_index"))
