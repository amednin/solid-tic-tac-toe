from IPlayer import IPlayer
from logger.ILogger import ILogger


class Computer(IPlayer):
    def __init__(self, mark, logger: ILogger):
        self.identifier = mark
        self.logger = logger

    def get_identifier(self):
        return self.identifier

    def make_move(self, x, y):
        self.logger.log('Player ' + self.identifier + ' moves to (' + x + ', ' + y + ')')

    def find_optimal_move(self):
        pass

    def predict_move(self):
        pass
