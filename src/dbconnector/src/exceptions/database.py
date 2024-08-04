class DBConnectionError(Exception):
    def __init__(self, message, reason):
        self.message = message
        self.reason = reason
        