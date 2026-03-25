class ApiException(Exception):
    def __init__(self, message):
        self.message = message

class ValidationException(ApiException):
    pass
