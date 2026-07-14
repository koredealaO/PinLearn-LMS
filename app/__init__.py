"""
PinLearn LMS

Application Factory
"""

from flask import Flask

from config import DevelopmentConfig

from .extensions import (
    db,
    migrate,
    login_manager,
    mail,
    csrf,
    cache,
    limiter
)


def create_app(config_class=DevelopmentConfig):

    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)

    mail.init_app(app)

    csrf.init_app(app)

    cache.init_app(app)

    limiter.init_app(app)

    from .core import core_bp

    app.register_blueprint(core_bp)

    return app