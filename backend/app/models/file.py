'''  Defines the User model class. '''
from sqlalchemy.orm import  mapped_column

from app.extensions import db
from .base import BaseModel


class File(db.Model, BaseModel):
    '''
        User model class definition. Inherits BaseModel class.
        
        attributes:
            ID: Number
            username: String
            email: String
            password_hash: String
            created_at: DateTime
            verified: Boolean
        methods:
            create
            set_password
            validate_password
    '''
    __tablename__ = 'file'

    # pylint: disable-next=E1136
    name = mapped_column(db.String(256), unique=True, nullable=False)

    @staticmethod
    def create(name):
        '''
            Creates an instance of the User model.
            
            ARGS:
                username (str): The user's username
                email (str): The user's email.
            returns:
                User - the created user.
        '''
        file = File()
        file.name = name

        return file

