from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=2)])
    description = TextAreaField("Description", [validators.Length(max=144)])
    content = TextAreaField("Content")
    class Meta:
        csrf = False

