from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"
@auth.route('/artisphere')
def artisphere():
    return "<p>Upload File</p>"