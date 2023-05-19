from flask import Blueprint, redirect, jsonify, url_for, request, render_template
from classes.webhooks.pagamentos import Pagamento
from classes.database.database import db, Pagamentos, Acessos
import json

pagamentos = Blueprint('pagamentos', __name__, template_folder='templates')

# rota que recebe os webrooks dos pagamentos.
@pagamentos.route('/webhook-pagamentos', methods=['POST'])
def webhook():

    if request.method == 'POST':
        webhook = json.loads(request.data.decode('utf-8'))
        pagamentos = Pagamentos(Pagamento(webhook).nome(), Pagamento(webhook).email(), Pagamento(webhook).status(), Pagamento(webhook).forma_de_pagamento(), Pagamento(webhook).parcelas())
        
        db.session.add(pagamentos)
        db.session.commit()
        
        return "ok"

    return "Metódo não Permitido"


