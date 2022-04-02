import os
import redis
from flask import Flask
from flask_mail import Mail
from rq import Queue
from dotenv import load_dotenv

load_dotenv()

cache = redis.Redis(host="redis", port=6379)
queue = Queue(connection=cache)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY'] 

app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = os.environ['MAIL_PORT']
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_SSL'] = True 
   
mail = Mail(app)

from .views import mod as index 
app.register_blueprint(index)
