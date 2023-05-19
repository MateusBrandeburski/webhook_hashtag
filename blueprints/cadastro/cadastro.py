from flask import Blueprint, render_template, request, flash, url_for, redirect
from validate_email import validate_email
from flask_bcrypt import Bcrypt
from classes.database.database import db, Usuarios
from sqlalchemy.exc import IntegrityError
import os

cadastro = Blueprint('cadastro', __name__, template_folder='templates')

# rota que renderiza a página de cadastro
@cadastro.route('/')
def index():
    return render_template('cadastro/cadastro.html')

# rota que processa o cadastro.
@cadastro.route('/processa-cadastro', methods=['POST'])
def processa_cadastro():
      
    if request.method == 'POST':    
                                
        try:
            # captura os dados do input
            email = request.form['email']
            senha = request.form['senha']
            confirma_senha = request.form['confirma_senha']
            token = request.form['token']
                   
            # verifica a confirmção de senha
            if confirma_senha == senha:
                # transforma a senha em hash
                bcrypt = Bcrypt()
                hashed_password = bcrypt.generate_password_hash(senha).decode('utf-8')
            
 
                # verifica se o email é valido. É uma verificação superficial (verifica se tem @ no email) 
                is_valid = validate_email(email)
                if is_valid:             
                    pass
            
                    # verifica o token de adm para criação da conta
                    if token == os.environ['TOKEN_ADM']:
                                    
                        novo_usuario = Usuarios(email, hashed_password, token)  
                        db.session.add(novo_usuario)
                        db.session.commit()
                        
                                               
                    else:
                        flash('Token inválido')
                        return redirect(url_for('cadastro.register'))
                    
                else:
                    flash('Email inválido.')
                    return redirect(url_for('cadastro.register'))

            else:
                flash('As senhas precisam ser idênticas.')
                return redirect(url_for('cadastro.register'))

        # esse erro acontece quando já existem um usuário o email cadastrado no DB
        except IntegrityError:
            flash('Usuário ou Email já cadastrados.')
            return redirect(url_for('cadastro.register'))
        
        # essa erro acontece quando nenhum campo é preenchido
        except ValueError:
            flash('Todos os campos precissam ser preenchidos.')
            return redirect(url_for('cadastro.register'))
    
    return "deu pau"