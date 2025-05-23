# Initialize Flask
# from flask import Flask

# def create_app():
#   app = Flask(__name__)
    # register grammer route
#    from .routes.routes import grammar_routes
#    app.register_blueprint(grammar_routes)
#   return app

from fastapi import FastAPI
from app.routes.routes import register_routes

def create_app():
    app = FastAPI()
    register_routes(app)
    return app