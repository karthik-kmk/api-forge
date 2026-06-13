class InvalidURLException(Exception):

    def __init__(self):

        self.message = "Invalid or blocked URL"

        super().__init__(self.message)