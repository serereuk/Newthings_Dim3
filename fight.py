import numpy as np
from phan import Phan
from omokgame import Omokgame
from visual import visual
from nn import nn
from mcts import mcts

class fight():

    def __init__(self, gbsize, win_standard):
        self.human = None
        self.gbsize = gbsize
        self.win_standard = win_standard

    def set_player(self, p):
        self.human = p

    def Act(self, board):
        try:
            where = input("move, ex(3,7)")
            b = Phan(self.gbsize, self.win_standard)
            b.board = np.copy(board)
            b.moving(where, self.human)
            board = np.copy(b.board)

        except Exception as e:
            move = -1

        if move == -1 or move not in Omokgame(self.gbsize, self.win_standard).validmove(board, self.human):
            print("Impossible move, retry")
            move = self.Act(board)

        return move

def Run():
    try:
        b = Phan(13, 5)
        board = Omokgame.startphan()
        b.board = np.copy(board)
        display = visual(13, 5)
        display.prepare_display()
        f = fight(13, 5)
        human_move = f.Act(b.board)



        best_model = nn.loading("folder", "model1")
        best_mcts = mcts(Omokgame(13, 5), best_model)

    except KeyboardInterrupt:
        print("error")








