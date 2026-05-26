from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from blueprintapp.app import db

from blueprintapp.cursos.models import Curso
from blueprintapp.estudiantes.models import Estudiante

bp_curso = Blueprint('bp_curso',__name__,template_folder='templates')

@bp_curso.route('/')
def index():

    cursos = Curso.query.all()

    return render_template(
        'curso/index.html',
        cursos=cursos
    )

@bp_curso.route('/create', methods=['GET', 'POST'])
def create():

    estudiantes = Estudiante.query.all()

    if request.method == 'GET':

        return render_template(
            'curso/create.html',
            estudiantes=estudiantes
        )

    curso = Curso(
        nombre=request.form.get('nombre'),
        descripcion=request.form.get('descripcion'),
        estudiante_id=request.form.get('estudiante_id')
    )

    db.session.add(curso)

    db.session.commit()

    return redirect(
        url_for('bp_curso.index')
    )

@bp_curso.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    curso = Curso.query.get_or_404(id)

    estudiantes = Estudiante.query.all()

    if request.method == 'GET':

        return render_template(
            'curso/edit.html',
            curso=curso,
            estudiantes=estudiantes
        )

    curso.nombre = request.form.get('nombre')
    curso.descripcion = request.form.get('descripcion')
    curso.estudiante_id = request.form.get('estudiante_id')

    db.session.commit()

    return redirect(
        url_for('bp_curso.index')
    )

@bp_curso.route('/delete/<int:id>')
def delete(id):

    curso = Curso.query.get_or_404(id)

    db.session.delete(curso)

    db.session.commit()

    return redirect(
        url_for('bp_curso.index')
    )