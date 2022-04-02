from flask import Flask
import redis
from .contactform.views import mod as index 


def create_app():
    app = Flask(__name__)
    cache = redis.Redis(host="redis", port=6379)

    app.register_blueprint(index)

    return app
