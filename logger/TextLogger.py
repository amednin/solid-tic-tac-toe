from logger.ILogger import ILogger

PATH = '/logs/'


class TextLogger(ILogger):
    def __init__(self, filename):
        self.type = 'Text File Writer'
        self.filename = PATH + filename

    def log(self, message):
        log_text_file = open(self.filename, 'w')
        log_text_file.write(message + '\n')
        log_text_file.close()

    def get_type(self):
        return self.type
