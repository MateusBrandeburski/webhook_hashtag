from flask import Flask
from blueprints.pagamentos.pagamentos import pagamentos
from blueprints.cadastro.cadastro import cadastro
from blueprints.home.home import home
from blueprints.login.login import login
from classes.database.database import db
import os

app = Flask(__name__)

# secret_key é para o cookie do navegador
app.secret_key = ['M4T3usBrand']

# conexão com DB por meio do SQLALchemy, coloquei aqui porque eu preciso passar o 'app' como parâmetro e não posso gerar 'cirule_import'.
def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_WEBHOOK']
    db.init_app(app)
    return app

app.register_blueprint(pagamentos)
app.register_blueprint(cadastro)
app.register_blueprint(home)
app.register_blueprint(login)

app = create_app()
if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8000, debug=True)
