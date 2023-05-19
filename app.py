from flask import Flask
from blueprints.pagamentos.pagamentos import pagamentos

from classes.database.database import db
import os

app = Flask(__name__)


# conexão com DB por meio do SQLALchemy, coloquei aqui porque eu preciso passar o 'app' como parâmetro e não posso gerar 'cirule_import'.
def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DB_WEBHOOK_HASHTAG"]
    db.init_app(app)
    return app

app.register_blueprint(pagamentos)



app = create_app()
if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8000, debug=True)
