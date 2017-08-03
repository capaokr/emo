from flask_app import app, serializer, login_manager
from flask_login import UserMixin

class Users(UserMixin):
    def __init__(self, username, password):
        id = 1
        self.username = username
        self.password = password
        self.session_token = serializer.dumps([self.username, self.password])

    def get_id(self):
        return unicode(self.session_token)

@login_manager.user_loader
def load_user(session_token):
    noted_token = serializer.dumps([app.config['ADMIN_ACCOUNT'], app.config['ADMIN_KEY']])
    if(session_token == noted_token):
        return Users(app.config['ADMIN_ACCOUNT'], app.config['ADMIN_KEY'])
    else:
        return None
