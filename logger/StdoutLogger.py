from logger.ILogger import ILogger


class StdoutLogger(ILogger):
    def __init__(self):
        self.type = 'STDOUT'

    def log(self, message):
        print(message)

    def get_type(self):
        return self.type
