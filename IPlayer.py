class IPlayer:
    def make_move(self, x, y):
        raise NotImplementedError('Interface, not implemented')

    def get_identifier(self):
        raise NotImplementedError('Interface, not implemented')
