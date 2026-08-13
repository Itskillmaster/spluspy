class SplusPyError(Exception):
    pass

class FloodWait(SplusPyError):
    def __init__(self, seconds: int):
        self.seconds = seconds
        super().__init__(f"Flood wait of {seconds} seconds")

class Unauthorized(SplusPyError):
    def __init__(self, message="Unauthorized"):
        super().__init__(message)

class BadRequest(SplusPyError):
    def __init__(self, message="Bad Request"):
        super().__init__(message)
