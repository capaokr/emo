from flask import Flask
from itsdangerous import URLSafeSerializer
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('config.py')
serializer = URLSafeSerializer(app.config['SECRET_KEY'])
login_manager = LoginManager()
login_manager.init_app(app)

from home_routes import *
from post_routes import *
from protected_routes import *

# login_manager.login_view = 'login'
if __name__ == '__main__':
    app.run(debug=True)
