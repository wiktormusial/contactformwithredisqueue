from flask import Flask
from .contactform.views import mod as index 


def create_app():
    app = Flask(__name__)
    app.register_blueprint(index)

    return app
