'''
    Reads environment variables and creates a configuration
    object to be consumed by the flask application.
'''
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)


class Config():
    ''' Shared config across all environments. '''
    # pylint: disable-next=C0301
    ENV_TYPE = os.getenv('ENV')
    SECRET_KEY = os.getenv('SECRET_KEY')
    REDIS_PORT = os.getenv('REDIS_PORT', 6380)


class ProdConfig(Config):
    PROD = True


class DevConfig(Config):
    ''' Config for Dev Environment. '''
    DEV = True
    DEBUG = True


def get_environment():
    ''' Returns the appropriate environment configuration. '''
    env = os.getenv('ENV')

    if env == 'prod':
        return ProdConfig()
    elif env == 'dev':
        return DevConfig()

    raise Exception('Invalid environment...')