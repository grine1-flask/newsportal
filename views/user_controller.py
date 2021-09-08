from flask import render_template
from config import app


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
    @app.route('/users/register')
    def register():
        return render_template('users/register.html')