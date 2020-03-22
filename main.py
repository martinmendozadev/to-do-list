from flask import Flask, request, make_response, redirect, render_template, session, url_for
from flask_bootstrap import Bootstrap
from wtforms import Form, StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)

TODOS = ['Comprar cafe', 'Enviar solicitud de ', 'Aprender Flask']

app.config['SECRET_KEY'] = 'SUPER SEGURO'

class LoginForm(Form):
    username =  StringField('User name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def not_found(error):

    return render_template('404.html', error = error)


@app.errorhandler(500)
def not_found(error):
    
    return render_template('500.html', error = error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    user_ip = session.get('user_ip')
    username = session.get('username')
    login_form = LoginForm()

    context = {
         'user_ip' : user_ip, 
         'TODOS' : TODOS,
         'login_form' : login_form,
         'username' : username
    }

    if login_form.validate():
        username = login_form.username.data
        session['username'] = username

        return redirect(url_for('indexs'))

    return render_template('hello.html', **context)


##if __name__ == "__main__":
##    app.run(debug=True)
