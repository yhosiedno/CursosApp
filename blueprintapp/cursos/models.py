from blueprintapp.app import db

class Curso(db.Model):

    __tablename__ = 'cursos'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    descripcion = db.Column(
        db.String(200),
        nullable=False
    )

    estudiante_id = db.Column(
        db.Integer,
        db.ForeignKey('estudiantes.id'),
        nullable=False
    )