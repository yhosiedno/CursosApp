from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from blueprintapp.app import db
from blueprintapp.estudiantes.models import Estudiante

bp_estudiante = Blueprint('bp_estudiante',__name__,template_folder='templates')

@bp_estudiante.route('/')
def index():

    estudiantes = Estudiante.query.all()

    return render_template('estudiante/index.html',estudiantes=estudiantes)

@bp_estudiante.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == 'GET':

        return render_template(
            'estudiante/create.html'
        )

    estudiante = Estudiante(
        nombre=request.form.get('nombre'),
        correo=request.form.get('correo'),
        carrera=request.form.get('carrera')
    )

    db.session.add(estudiante)

    db.session.commit()

    return redirect(
        url_for('bp_estudiante.index')
    )

@bp_estudiante.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    estudiante = Estudiante.query.get_or_404(id)

    if request.method == 'GET':

        return render_template(
            'estudiante/edit.html',
            estudiante=estudiante
        )

    estudiante.nombre = request.form.get('nombre')
    estudiante.correo = request.form.get('correo')
    estudiante.carrera = request.form.get('carrera')

    db.session.commit()

    return redirect(
        url_for('bp_estudiante.index')
    )

@bp_estudiante.route('/delete/<int:id>')
def delete(id):

    estudiante = Estudiante.query.get_or_404(id)

    db.session.delete(estudiante)

    db.session.commit()

    return redirect(
        url_for('bp_estudiante.index')
    )