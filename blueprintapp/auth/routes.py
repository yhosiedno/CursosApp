from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user

from blueprintapp.app import db
from blueprintapp.app import bcrypt

from blueprintapp.auth.models import Usuario

auth = Blueprint(
    'auth',
    __name__,
    template_folder='templates',
    url_prefix='/auth'
)


@auth.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        usuario_existente = Usuario.query.filter_by(
            username=username
        ).first()

        if usuario_existente:

            flash(
                'El usuario ya existe',
                'warning'
            )

            return render_template(
                'auth/register.html'
            )

        password_hash = bcrypt.generate_password_hash(
            password
        ).decode('utf-8')

        usuario = Usuario(
            username=username,
            password=password_hash
        )

        db.session.add(usuario)
        db.session.commit()

        flash(
            'Usuario registrado correctamente',
            'success'
        )

        return redirect(
            url_for('auth.login')
        )

    return render_template(
        'auth/register.html'
    )


@auth.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        usuario = Usuario.query.filter_by(
            username=username
        ).first()

        if usuario and bcrypt.check_password_hash(
            usuario.password,
            password
        ):

            login_user(usuario)

            return redirect('/')

        flash(
            'Usuario o contraseña incorrectos',
            'danger'
        )

    return render_template(
        'auth/login.html'
    )


@auth.route('/logout')
def logout():

    logout_user()

    flash(
        'Sesión cerrada correctamente',
        'info'
    )

    return redirect(
        url_for('auth.login')
    )