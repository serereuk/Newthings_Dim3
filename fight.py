import numpy as np
from phan import Phan
from omokgame import Omokgame
from visual import visual
from nn import nn
from mcts import mcts

class fight():

    def __init__(self, gbsize, win_standard, order):
        self.human = None
        if order == "black":
            self.human = 1
        else:
            self.human = -1
        self.gbsize = gbsize
        self.win_standard = win_standard

    def set_player(self, p):
        self.human = p

    def Act(self, board):
        try:
            where = int(input("move, ex) 37 = (3,7)"))
            moves = [int(where / 10), int(where % 10)]
            b = Phan(self.gbsize, self.win_standard)
            b.board = np.copy(board)
            b.moving(moves, self.human)
            board = np.copy(b.board)

        except Exception as e:
            moves = -1

        if moves == -1 or moves not in Omokgame(self.gbsize, self.win_standard).validmove(board, self.human):
            print("Impossible move, retry")
            self.Act(board)

        return board

def Run():
    try:
        b = Phan(13, 5)
        game = Omokgame(13,5)
        board = game.startphan()
        new_board = game.dim_board()
        b.board = np.copy(board)
        player = -1
        display = visual(13, 5)
        display.prepare_display()
        f = fight(13, 5)
        while True:
            human_move = f.Act(b.board)
            oneminusone = game.oneminusone(board, player)




        best_model = nn.loading("folder", "model1")
        best_mcts = mcts(Omokgame(13, 5), best_model)

    except KeyboardInterrupt:
        print("error")








