from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

TODOS = ['Comprar cafe', 'Enviar solicitud de ', 'Aprender Flask']

app.config['SECRET_KEY'] = 'SUPER SEGURO'


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


@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    context = {
         'user_ip' : user_ip, 
         'TODOS' : TODOS,
    }

    return render_template('hello.html', **context)
