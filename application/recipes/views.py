from flask_login import current_user
from application import app, db, login_required, login_manager
from flask import render_template, request, url_for, redirect
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm



@app.route("/recipes/new/")
@login_required(role="ADMIN")
def recipes_form():
    return render_template("recipes/new.html", form=RecipeForm())


@app.route("/recipes", methods=["GET"])
@login_required(role="ADMIN")
def recipes_index():
    return render_template("recipes/list.html", recipes=Recipe.query.all())


@app.route("/recipes/", methods=["POST"])
@login_required(role="ADMIN")
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form = form)
        
    recipe = Recipe(form.name.data)
    recipe.description = form.description.data
    recipe.content = form.content.data
    recipe.account_id = current_user.id
    
    db.session().add(recipe)
    db.session().commit()

    return redirect(url_for("recipes_index"))


@app.route("/recipes/<recipe_id>/")
@login_required(role="ADMIN")
def recipes_view(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    return render_template('recipe.html', recipe=recipe)


@app.route("/recipes/<recipe_id>/update/", methods=['POST', 'GET'])
@login_required(role="ADMIN")
def recipes_update(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    
    if recipe.account_id != current_user.id:
        return login_manager.unauthorized()
    
    form = RecipeForm()
    if not form.validate():
        return render_template("recipes/modify.html", form = form, recipe=recipe)

    recipe.name = form.name.data
    recipe.description = form.description.data
    recipe.content = form.content.data
    db.session.commit()
    
    return redirect(url_for("recipes_index"))
    
@app.route("/recipes/<recipe_id>/delete/", methods=["POST", "GET"])
@login_required(role="ADMIN")
def recipes_delete(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe.account_id != current_user.id:
        return login_manager.unauthorized()
    
    db.session().delete(recipe)
    db.session().commit()

    return redirect(url_for("recipes_index"))

