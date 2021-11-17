from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = 'GOLDSHIRE'

    from .routes import db_edit

    app.register_blueprint(db_edit, url_prefix='/db')
    return app
