import numpy as np
from mcts import mcts


class coaching():
    def __init__(self, game, nnet, mcts1):
        self.game = game
        self.nnet = nnet
        #self.pnet = self.nnet.__class__(self.game)
        self.mcts = mcts1
        self.trainexamplehistory = []

    def executeepisode(self):
        trainexample = []
        board = self.game.startphan()
        self.curplayer = 1
        episodestep = 0

        while True:
            episodestep += 1
            oneminusone = self.game.oneminusone(board, self.curplayer)
            temp = int(episodestep < 20)
            pi = self.mcts.getactionprob(oneminusone)
            sym = self.game.symme(oneminusone, pi)
            for b, p in sym:
                trainexample.append([b, self.curplayer, p, None])

            action = np.random.choice(len(pi), p=pi)
            board, self.curplayer = self.game.nextstate(board, self.curplayer, action)
            print("episode :", episodestep, "\n", board)
            r = self.game.ggeutnam(board, self.curplayer)

            if r != 0:
                return [(x[0], x[2], r * ((-1) ** (x[1] != self.curplayer))) for x in trainexample]

    def learn(self):

        for iter in range(5):
            iterationtrainexample = []
            finalexample = []

            for i in range(10):
                print("game:", i)
                iterationtrainexample += self.executeepisode()

            self.trainexamplehistory.append(iterationtrainexample)

            for e in self.trainexamplehistory:
                finalexample.append(e)

            self.nnet.train(finalexample)
            self.mcts = mcts(self.game, self.nnet)



        #self.executeepisode()
        #self.nnet.saving("~/", "model1.ckpt")
        #self.pnet.loading("~/", "model1.ckpt")









