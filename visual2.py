
import numpy as np

class Result():
    def __init__(self, game, nnet_1, mcts_1):
        self.game = game
        self.nnet = nnet_1
        self.mcts = mcts_1
        self.over = False

    def perform(self):
        board = self.game.startphan()
        new_board = self.game.dim_board()
        self.curplayer = -1
        action_1 = []
        self.nnet.loading("a", "model1.ckpt")

        while True:
            oneminusone = self.game.oneminusone(board, self.curplayer)
            pi = self.mcts.getactionprob(oneminusone, new_board, 0)
            action = np.random.choice(len(pi), p=pi)
            board, self.curplayer, new_board = self.game.nextstate(board, new_board, self.curplayer, action)
            r = self.game.ggeutnam(board, self.curplayer)
            action_1.append([action // 9, action % 9])
            if r != 0:
                self.over = True
                action_1.append(self.over)
                return action_1

