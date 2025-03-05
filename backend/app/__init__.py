'''
    Creates an instance of the flask application.
'''
import traceback

from flask import Flask, send_from_directory
from werkzeug.exceptions import default_exceptions

from app.routes import api_routes
from app.common.errors import ServerException
# from app.common.logger import configure_logger, log_details
from app.common.utility import create_server_res
from config import get_environment


def create_app(config=get_environment()):
    '''
        Creates an instance of the Flask App
    '''
    app = Flask(__name__, static_folder='../dist', static_url_path='/')
    app.register_blueprint(api_routes)

    app.config.from_object(config)
    register_error_routes(app)
    register_frontend(app)

    # Configure logger
    # configure_logger(app)

    return app


def register_error_routes(app: Flask):
    '''
        Assigns handlers for common API error codes.
    '''
    def handle_http_error(err):
        # app.logger.error(log_details(f'{err.description}'))
        return create_server_res(err.description, err.code)

    for code in default_exceptions:
        app.errorhandler(code)(handle_http_error)

    @app.errorhandler(Exception)
    def server_error(error):
        '''
            Catch-all error handler. Catches any error that is not handled above.
        '''
        app.logger.error(type(error))
        app.logger.error(''.join(traceback.format_exception(None, error, error.__traceback__)))

        if isinstance(error, ServerException):
            if error.code:
                return create_server_res(error.message, error.code)

        return create_server_res('Internal server error.', 500)


def register_frontend(app: Flask):
    '''
        Serve frontend in production.
    '''
    if app.config.get('PROD'):
        @app.route('/')
        def index():
            return send_from_directory(app.static_folder, 'index.html')