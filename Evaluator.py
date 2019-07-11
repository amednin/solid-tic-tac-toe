from logger.ILogger import ILogger


class Evaluator:
    def __init__(self, logger: ILogger):
        self.logger = logger
        self.moves = []

    def calculate_winner(self, move, mark):
        self.logger.log(mark + ' ON (' + move.x + ', ' + move.y + ')')
        return ''

    def reset_moves(self):
        self.moves = []
