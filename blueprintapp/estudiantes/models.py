from blueprintapp.app import db

class Estudiante(db.Model):

    __tablename__ = 'estudiantes'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    correo = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    carrera = db.Column(
        db.String(100),
        nullable=False
    )

    cursos = db.relationship(
        'Curso',
        backref='estudiante',
        cascade='all, delete',
        lazy=True
    )