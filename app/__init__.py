from flask import Flask
import flask_login
from app.models.base import db

login_manager = flask_login.LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录和注册'

    with app.app_context():
        db.create_all()

    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
