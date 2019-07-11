from IPlayer import IPlayer
from logger.ILogger import ILogger
from typing import Iterable


class Board:
    def __init__(self, players: Iterable[IPlayer], logger: ILogger):
        self.players = players
        self.logger = logger

    def draw_board(self):
        self.logger.log('Drawing board')
        print('   |   |   ')
        print('---+---+---')
        print('   |   |   ')
        print('---+---+---')
        print('   |   |   ')

    def reset_board(self):
        self.logger.log('Reseting and Re-drawing board')
        self.draw_board()
