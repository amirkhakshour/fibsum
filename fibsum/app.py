from flask import Flask


def create_app(testing=False):
    """Application factory, used to create application
    """
    app = Flask("fibsum")
    app.config.from_object("fibsum.config")

    if testing is True:
        app.config["TESTING"] = True

    return app
