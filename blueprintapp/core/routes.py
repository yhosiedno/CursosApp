from flask import Blueprint
from flask import render_template

bp_core = Blueprint('bp_core',__name__,template_folder='templates')

@bp_core.route('/')
def index():

    return render_template(
        'core/index.html'
    )