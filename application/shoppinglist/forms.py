from flask_wtf import FlaskForm
from wtforms import StringField, validators


class ListForm(FlaskForm):
    name = StringField("Product", [validators.Length(min=2)])
    quantity = StringField("Quantity")
    
    class Meta:
        csrf = False
