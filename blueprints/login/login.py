from flask import Blueprint, session, render_template, redirect, url_for, request, flash
from flask_bcrypt import Bcrypt
from classes.database.database import Usuarios


bcrypt = Bcrypt()
login = Blueprint('login', __name__, template_folder='templates')


# renderiza a página de login, verificando o session logado
@login.route('/')
def index():
        
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return render_template('login/login.html')
    
    else:
        return render_template('home/home.html')


# Processa o login
@login.route('/autenticar', methods=['POST'])
def autenticar():
    
    email = request.form['email']
    senha = request.form['senha']
    usuario = Usuarios.query.filter_by(email=email).first()

    if usuario is not None and bcrypt.check_password_hash(usuario.senha, senha):
        
        session['usuario_logado'] = usuario.email
        return redirect(url_for('home.index'))

    flash('Username ou password inválidos')
    return redirect(url_for('login.index'))
   
  
@login.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('login.index'))