from application import app, db
from flask import render_template, request, url_for, redirect
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm
from flask_login import login_required, current_user


@app.route("/recipes/new/")
@login_required
def recipes_form():
    return render_template("recipes/new.html", form=RecipeForm())


@app.route("/recipes", methods=["GET"])
@login_required
def recipes_index():
    return render_template("recipes/list.html", recipes=Recipe.query.all())


@app.route("/recipes/", methods=["POST"])
@login_required
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form = form)
        
    t = Recipe(form.name.data)
    t.description = form.description.data
    t.account_id = current_user.id
    
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("recipes_index"))
