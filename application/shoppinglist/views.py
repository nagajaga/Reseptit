from application import app, db
from flask import render_template, request, url_for, redirect
from application.shoppinglist.models import ShoppingList
from application.shoppinglist.forms import ListForm
from flask_login import login_required, current_user


@app.route("/shopping/add")
@login_required
def shopping_form():
    return render_template("shopping/add.html", form=ListForm())


@app.route("/shopping", methods=["POST"])
@login_required
def shopping_add():
    form = ListForm(request.form)

    if not form.validate():
        return render_template("shopping/add.html", form = form)

    t = ShoppingList(form.name.data)
    t.quantity = form.quantity.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return render_template("shopping/add.html", form = form)

@app.route("/shopping/", methods=["GET"])
@login_required
def shopping_index():
    return render_template("shopping/list.html", shoppinglist=ShoppingList.query.all())