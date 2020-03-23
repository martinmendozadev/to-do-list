from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username =  StringField('User name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TodoForm(FlaskForm):
    descripcion = StringField('Activity', validators=[DataRequired()])
    submit = SubmitField('Save')

class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Delete')


class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Update')
