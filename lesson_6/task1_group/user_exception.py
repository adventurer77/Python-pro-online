class UserException(Exception):

    def __init__(self, message,limit):

        super().__init__()
        self.message = message
        self.limit = limit


    def __str__(self) -> str:

        return f"{self.message}. Limit: {self.limit}"
