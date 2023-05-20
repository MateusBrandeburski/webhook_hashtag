from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pagamentos(db.Model):
    
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(150))
    status = db.Column(db.String(50))
    forma_pagamento = db.Column(db.String(50))
    parcelas = db.Column(db.String(50))
    

    def __init__(self, nome, email, status, forma_pagamento, parcelas):
        self.nome = nome
        self.email = email
        self.status = status
        self.forma_pagamento = forma_pagamento
        self.parcelas = parcelas


class Acessos(db.Model):
    
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), nullable=False)
    status_no_sistema = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(20), nullable=False)


    def __init__(self, status_no_sistema, email):
        self.email = email
        self.status_no_sistema = status_no_sistema
        
class Usuarios(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), unique=True)
    senha = db.Column(db.String(256), nullable=False)
    token = db.Column(db.String(20), nullable=False)
    data = db.Column(db.String(20), nullable=False)

    def __init__(self, email, senha, token):
        self.email = email
        self.senha = senha
        self.token = token

