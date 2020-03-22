from flask import request, make_response, redirect, render_template, session, url_for, flash

import unittest

from app import create_app
from app.forms import LoginForm


app = create_app()

TODOS = ['Comprar cafe', 'Enviar solicitud de ', 'Aprender Flask']





@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


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

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Usuario registrado correctamente')

        return redirect(url_for('index'))

    return render_template('hello.html', **context)
