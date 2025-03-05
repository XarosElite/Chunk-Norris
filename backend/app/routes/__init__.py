'''
    All routes are assigned to the base API blueprint in
    this file.
'''
from flask import Blueprint
from app.routes.examples import example_routes

api_routes = Blueprint("ChunkNorris", __name__, url_prefix="/ChunkNorris")
api_routes.register_blueprint(example_routes)
