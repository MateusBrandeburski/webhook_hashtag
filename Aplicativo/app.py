from flask import Flask
from blueprints.login.login import login


app = Flask(__name__)

# secret_key é para o cookie do navegador
app.secret_key = ['M4T3usBrnd3']

app.register_blueprint(login)

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8000, debug=True)