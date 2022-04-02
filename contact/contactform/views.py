from flask import Blueprint, render_template
from .forms import ContactForm


mod = Blueprint('index', __name__,
                template_folder='templates')


@mod.route('/')
def index():
    form = ContactForm()
    return render_template('contactform/index.html', form=form)
