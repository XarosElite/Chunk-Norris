'''
    Holds instantations of certain flask services
    so that they can be accessed across the application.
'''
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
from flask_migrate import Migrate



# Database
class BaseDeclarativeModel(DeclarativeBase):
    '''
        Defines metadata for our postgres database creation.
    '''
    metadata = MetaData(naming_convention={
        "ix": 'ix_%(column_0_label)s',
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
    })


db = SQLAlchemy(model_class=BaseDeclarativeModel)

migrate = Migrate()