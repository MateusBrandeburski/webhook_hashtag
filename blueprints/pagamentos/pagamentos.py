from flask import Blueprint, request
from classes.webhooks.pagamentos import Pagamento
from classes.database.database import db, Pagamentos, Acessos
from classes.envia_email.gmail import envia_email
from datetime import datetime, timedelta
import json

pagamentos = Blueprint('pagamentos', __name__, template_folder='templates')

# rota que recebe os webrooks dos pagamentos.
@pagamentos.route('/webhook-pagamentos', methods=['POST'])
def webhook():

    if request.method == 'POST':
        """ A classe 'Pagamento' é quem recebe o webhook, e as classes 'Pagamentos' e 'Acessos' são as tabelas no DB.
        Na primeira linha, ele recebe o webhook em bytes, converte em string, depois em json. A classe das tabelas, rebem a classe do 'Pagamento' que é a classe do webhook + a sua respectiva função que trás o dado tratado.
        """     
        webhook = json.loads(request.data.decode('utf-8'))
        pagamentos = Pagamentos(Pagamento(webhook).nome(), Pagamento(webhook).email(), Pagamento(webhook).status(), Pagamento(webhook).forma_de_pagamento(), Pagamento(webhook).parcelas())
        
        db.session.add(pagamentos)
        db.session.commit()        
            
        if Pagamento(webhook).status() == "aprovado":
            """_Eu fiquei na dúvida se fazia uma classe apenas para essa tratativa do sistema, mas necesse caso em específico, achei mais simples passar direto uma string no parametro da classe da tavela 'Acessos'.
            """
            data = (datetime.now() - timedelta(hours=3)).strftime('%d/%m/%Y %H:%M')
            
            acessos = Acessos("acesso_liberado", Pagamento(webhook).email(), data)
            
            db.session.add(acessos)
            db.session.commit()
            
            """ Aqui poderia ser passada uma função para enviar um email para a pessoa avisado, ou para o adm, caso não seja automatizado. Coloquei um 'Try' para não exibir o erro do email fake.
            """
            try:
                envia_email("Seu acessso foi aprovado", Pagamento(webhook).email())
            except:
                print('Enviar mensagem de boas vindas para o email: fulano@email.com')
                
        
        elif Pagamento(webhook).status() == "recusado":
            acessos = Acessos("acesso_recusado", Pagamento(webhook).email(), data)
            
            db.session.add(acessos)
            db.session.commit()
            
            print('Enviar mensagem avisando que foi recusado para o email: fulano@email.com')
            
        elif Pagamento(webhook).status() == "reembolsado":
            acessos = Acessos("acesso_bloqueado", Pagamento(webhook).email(), data)
            
            db.session.add(acessos)
            db.session.commit()

            print('Enviar mensagem avisando que foi reembolsado e o acesso foi retirado para o email: fulano@email.com')
    
        return "STATUS OK", 200
    
    return "Method Not Allowed", 405


