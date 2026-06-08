from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'clave'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///universidad.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message = ""

    from blueprintapp.auth.models import Usuario

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    from blueprintapp.core.routes import bp_core
    from blueprintapp.estudiantes.routes import bp_estudiante
    from blueprintapp.cursos.routes import bp_curso
    from blueprintapp.auth.routes import auth

    app.register_blueprint(bp_core)
    app.register_blueprint(bp_estudiante, url_prefix='/estudiantes')
    app.register_blueprint(bp_curso, url_prefix='/cursos')
    app.register_blueprint(auth)

    return app