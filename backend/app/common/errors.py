'''
    Houses custom exceptions.
'''


class ServerException(Exception):
    '''
        Custom Server Exceptions
    '''
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        super().__init__(message)


class ServiceException(Exception):
    '''
        Custom Service Exception.
    '''


class SchemaException(Exception):
    '''
        Custom Schema Error
    '''