from flask import Blueprint, request, redirect, url_for

from views import user_view

from models.user_model import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def usuarios():
    
    users = User.get_all()
    
    return user_view.usuarios(users)


@user_bp.route('/users', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        
        user = User(first_name, last_name, request.form['email'], request.form['password'], request.form['birthday'])
        
        user.save()
        
        return redirect(url_for('user.usuarios'))
    
    return user_view.registro()

