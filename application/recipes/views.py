from application import app, db, login_required
from flask import render_template, request, url_for, redirect
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm
from flask_login import current_user


@app.route("/recipes/new/")
@login_required(role="ADMIN")
def recipes_form():
    return render_template("recipes/new.html", form=RecipeForm())


@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes=Recipe.query.all())


@app.route("/recipes/", methods=["POST"])
@login_required(role="ADMIN")
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form = form)
        
    t = Recipe(form.name.data)
    t.description = form.description.data
    t.content = form.content.data
    t.account_id = current_user.id
    
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("recipes_index"))


@app.route("/recipes/<recipe_id>/")
def recipes_view(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    return render_template('recipe.html', recipe=recipe)

