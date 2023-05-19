from flask import Blueprint, render_template, session, redirect, url_for


home = Blueprint('home', __name__, template_folder='templates')


@home.route('/home')
def index():
    
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('cadastro.index'))
    else:
        return render_template('home/home.html')

