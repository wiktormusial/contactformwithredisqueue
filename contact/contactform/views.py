import contact
from flask import Blueprint, render_template, request
from flask_mail import Message
from .forms import ContactForm

mod = Blueprint('index', __name__,
                template_folder='templates')

@mod.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'POST' and form.validate():
        msg = Message("test",
                      sender="test@gmail.com",
                      recipients=["wiktormusial@icloud.com"])
        contact.mail.send(msg)
        print('success')
    return render_template('contactform/index.html', form=form)
