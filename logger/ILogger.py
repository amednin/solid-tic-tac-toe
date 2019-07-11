class ILogger:
    def log(self, message):
        raise NotImplementedError('Interface, not implemented!')

    def get_type(self):
        raise NotImplementedError('Interface, not implemented!')
