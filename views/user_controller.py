from flask import render_template, request
from config import app
from models.user import User


class UsersController(object):

    @staticmethod
    @app.route('/user/admin')
    def admin():
        return render_template('users/admin.html')

    @staticmethod
    @app.route('/users/login')
    def login():
        return render_template('users/login.html')

    @staticmethod
    @app.route('/user/logout')
    def logout():
        return render_template('user/logout.html')

    @staticmethod
    @app.route('/user/profile')
    def profile():
        return render_template('user/profile.html')

    @staticmethod
    @app.route('/users/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'GET':
            return render_template('users/register.html')
        elif request.method == 'POST':
            login = request.form.get('login')
            pass1 = request.form.get('pass1')
            pass2 = request.form.get('pass2')
            email = request.form.get('email')
            
            passwod = '?'
            regdate = '?'
            status = 'new_user'
            #User.register(login, password, email, regdate, status)

            return render_template('users/register_info.html', context={
                'login': login,
                'pass1': pass1,
                'pass2': pass2,
                'email': email
            })