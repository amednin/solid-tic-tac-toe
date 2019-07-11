from TicTacToe import TicTacToe
from logger.StdoutLogger import StdoutLogger
from game_constants import GameMode


stdoutLogger = StdoutLogger()
game = TicTacToe(GameMode.ONE_TO_ONE, stdoutLogger)
game.init()
