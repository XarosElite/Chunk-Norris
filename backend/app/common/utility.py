'''
    Common utility functions for the server.
'''
from flask import jsonify, abort


# This probably doesnt belong here but IDK where it would go.
VALID_GAME_IMAGES = [
    "itzg/minecraft-server",
    "ForrestPlaceholder",
    "thijsvanloef/palworld-server-docker:latest"]


def create_server_res(message, code: int) -> dict:
    '''
        Creates a generic message for the API response.

        ARGS:
            message (str): message to encapsulate.
            code (int): HTTP Status code.

        RETURNS:
            Dict { msg: <message> }, <code> - The JSONified message.
    '''
    return jsonify({
        'msg': message
    }), code


def validate_parameter(schema):
    """
        A decorator to validate a single parameter with a marshmallow schema.


    Args:
        schema (schema): The Schema to load the parameter into.
    """
    def wrapper(func):
        def val(*args, **kwargs):
            try:
                kwargs = schema.load(kwargs)
            except Exception as err:
                abort(422, err.messages_dict)
            return func(*args, **kwargs)
        return val
    return wrapper
