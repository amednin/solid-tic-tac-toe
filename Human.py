from IPlayer import IPlayer
from logger.ILogger import ILogger


class Human(IPlayer):
    def __init__(self, mark, logger: ILogger):
        self.identifier = mark
        self.logger = logger

    def get_identifier(self):
        return self.identifier

    def make_move(self, x, y):
        self.logger.log('Player ' + self.identifier + ' moves to (' + x + ', ' + y + ')')
