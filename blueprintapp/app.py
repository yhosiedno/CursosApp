from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///universidad.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from blueprintapp.core.routes import bp_core
    from blueprintapp.estudiantes.routes import bp_estudiante
    from blueprintapp.cursos.routes import bp_curso

    app.register_blueprint(bp_core)
    app.register_blueprint(bp_estudiante,url_prefix='/estudiantes')
    app.register_blueprint(bp_curso,url_prefix='/cursos')

    return app