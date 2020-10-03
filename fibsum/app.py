from flask import Flask
from fibsum import api


def create_app(testing=False):
    """Application factory, used to create application
    """
    app = Flask("fibsum")
    app.config.from_object("fibsum.config")

    if testing is True:
        app.config["TESTING"] = True

    register_blueprints(app)
    return app


def register_blueprints(app):
    """register all blueprints for application
    """
    app.register_blueprint(api.views.blueprint)
