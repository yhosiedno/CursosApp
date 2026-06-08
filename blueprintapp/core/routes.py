from flask import Blueprint
from flask import render_template

from flask_login import login_required

bp_core = Blueprint(
    'bp_core',
    __name__,
    template_folder='templates'
)

@bp_core.route('/')
@login_required
def index():

    return render_template(
        'core/index.html'
    )