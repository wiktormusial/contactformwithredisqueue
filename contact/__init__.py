import os
from flask import Flask
from flask_mail import Mail, Message
import redis
from dotenv import load_dotenv
from .contactform.views import mod as index 

load_dotenv()

app = Flask(__name__)
cache = redis.Redis(host="redis", port=6379)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY'] 

app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = os.environ['MAIL_PORT']
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_SSL'] = True 

app.register_blueprint(index)
mail = Mail(app)
