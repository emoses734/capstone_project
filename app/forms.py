from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired



# class SearchForm(Form):
#     choices = [('Restaurant','Restaurant'), ('Rating','Rating')]
#     select = SelectField('Search by Restaurant or Rating:', choices=choices)
#     search = StringField('')


class SearchDFForm(FlaskForm):

    input = StringField("search")
    submit= SubmitField("submit")
    
