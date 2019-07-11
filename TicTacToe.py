from Board import Board
from logger.ILogger import ILogger
from Evaluator import Evaluator
from game_constants import GameMode
from Human import Human
from Computer import Computer


class TicTacToe:
    def __init__(self, mode, logger: ILogger):
        self.logger = logger
        self.evaluator = Evaluator(logger)

        if mode == GameMode.ONE_TO_ONE:
            self.players = [Human('X', logger), Human('Y', logger)]
        else:
            self.players = [Human('X', logger), Computer('Y', logger)]

        self.board = Board(self.players, logger)

    def init(self):
        self.logger.log('Initializing Game')
        self.board.draw_board()

    def restart(self):
        self.board.reset_board()
        self.evaluator.reset_moves()
