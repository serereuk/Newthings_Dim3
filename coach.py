import numpy as np
from mcts import mcts


class coaching():
    def __init__(self, game, nnet, mcts1):
        self.game = game
        self.nnet = nnet
        #self.pnet = self.nnet.__class__(self.game)
        self.mcts = mcts1
        #self.trainexamplehistory = []
        self.prints = False

    def executeepisode(self):
        trainexample = []
        board = self.game.startphan()
        new_board = self.game.dim_board()
        self.curplayer = -1
        episodestep = 0

        while True:
            episodestep += 1
            oneminusone = self.game.oneminusone(board, self.curplayer)
            temp = int(episodestep < 40)
            pi = self.mcts.getactionprob(oneminusone, new_board, temp)
            sym = self.game.symme(new_board, pi)
            for b, p in sym:
                trainexample.append([b, self.curplayer, p, None])
            action = np.random.choice(len(pi), p=pi)
            board, self.curplayer,  new_board = self.game.nextstate(board, new_board, self.curplayer, action)
            if self.prints:
                print("episode :", episodestep, "\n", board)
            r = self.game.ggeutnam(board, self.curplayer)

            if r != 0:
                return [(x[0], x[2], r * ((-1) ** (x[1] != self.curplayer))) for x in trainexample]

    def learn(self):

        self.nnet.loading("~/", "model1.ckpt")
        for iter in range(1000):
            print("iteration : ", iter+1)
            self.nnet.saving("~/", "model1.ckpt")
            self.prints = False
            iterationtrainexample = []
            finalexample = []
            try:
                for i in range(1):
                    print("game:", i+1)
                    if i == 0:
                        self.prints = True
                    iterationtrainexample += self.executeepisode()

                    for ssh in iterationtrainexample:
                        finalexample.append(ssh)

                self.nnet.train(finalexample)
                self.mcts = mcts(self.game, self.nnet)
            except:
                self.nnet.saving("~/", "model1.ckpt")

        self.nnet.saving("~/", "model1.ckpt")










