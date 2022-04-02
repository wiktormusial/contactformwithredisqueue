import os
from flask import Flask
import redis
from dotenv import load_dotenv
from .contactform.views import mod as index 


load_dotenv()

def create_app():
    app = Flask(__name__)
    cache = redis.Redis(host="redis", port=6379)
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY'] 
    app.register_blueprint(index)

    return app
