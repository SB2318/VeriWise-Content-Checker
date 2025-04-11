# Initialize Flask
from flask import Flask

def create_app():
    app = Flask(__name__)
    # register grammer route
    from .routes.routes import grammar_routes
    app.register_blueprint(grammar_routes)
    return app