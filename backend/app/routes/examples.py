from flask import current_app
from flask_smorest import Blueprint

from app.common.utility import (
    create_server_res, validate_parameter
)


example_routes = Blueprint("examples", __name__, url_prefix="/examples")


@example_routes.get('/')
def get_hello():
    """
        Gets a list of all running servers.

        Returns 200, result
    """

    return create_server_res("Hello world from Chunky Norris", 200)
