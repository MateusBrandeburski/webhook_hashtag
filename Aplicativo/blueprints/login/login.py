from flask import Blueprint, render_template


login = Blueprint('login', __name__, template_folder='templates')

@login.route('/')
def index():
    return render_template('login/login.html')