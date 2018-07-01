
class ApiException(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)


class UserAlreadyExistsException(ApiException):
    def __init__(self, username):
        super().__init__(
            f"'{username}' already exists", 1)


class InvalidDateRangeException(ApiException):
    def __init__(self, from_inclusive, to_exclusive):
        super().__init__(
            f"provided date range is invalid: <{from_inclusive},{to_exclusive})", 2)

class PublisherNotFoundException(ApiException):
    def __init__(self, pub_id):
        super().__init__(
            f"There is no publisher with id: {pub_id}", 5)

class BodyValidationException(ApiException):
    def __init__(self, errors):
        super().__init__(
            f"{str(errors)}", 8)


class UserNotFoundException(ApiException):
    def __init__(self, username):
        super().__init__(
            f"'{username}' user does not exist", 11)


# class Error(Exception):
#     def __init__(self, message):
#         self.message = message


# class ValidationError(Error):
#     pass


# class BookNotFound(Error):
#     def __init__(self):
#         super(BookNotFound, self).__init__("Book Not Found")



