from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def config_extensions(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

