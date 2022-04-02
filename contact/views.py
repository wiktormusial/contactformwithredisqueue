from flask import Blueprint, render_template, request
from flask_mail import Message
from contact import queue
from .forms import ContactForm
from .tasks import send_mail

mod = Blueprint('index', __name__,
                template_folder='templates')

@mod.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'POST' and form.validate():
        queue.enqueue(send_mail, "test@o2.pl", "asd", "onet")
        print('success')
    return render_template('contactform/index.html', form=form)
