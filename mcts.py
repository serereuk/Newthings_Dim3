import math
import numpy as np

class mcts():
    def __init__(self, game, nnet):
        self.game = game
        self.nnet = nnet
        self.Qsa = {}
        self.Nsa = {}
        self.Ns = {}
        self.Ps = {}
        self.Es = {}
        self.Vs = {}

    def getactionprob(self, oneminusone, temp=1):
        for i in range(100):
            self.search(oneminusone)

        s = self.game.stringstring(oneminusone)
        counts = [self.Nsa[(s, a)] if (s, a) in self.Nsa else 0 for a in range(self.game.actionsize())]

        if temp == 0:
            bestA = int(np.argmax(counts))
            probs = [0] * len(counts)
            probs[bestA] = 1
            return probs

        counts = [x**(1. / temp) for x in counts]
        probs = [x / float(sum(counts)) for x in counts]
        return probs

    def search(self, oneminusone):
        s = self.game.stringstring(oneminusone)

        if s not in self.Es:
            self.Es[s] = self.game.ggeutnam(oneminusone, 1)
        if self.Es[s] != 0:
            return -self.Es[s]

        if s not in self.Ps:
            # leaf node
            self.Ps[s], v = self.nnet.predict(oneminusone)
            valids = self.game.validmove(oneminusone, 1)
            self.Ps[s] = self.Ps[s] * valids  # masking invalid moves
            sum_Ps_s = np.sum(self.Ps[s])
            if sum_Ps_s > 0:
                self.Ps[s] /= sum_Ps_s  # renormalize
            else:
                print("All valid moves were masked, do workaround.")
                self.Ps[s] = self.Ps[s] + valids
                self.Ps[s] /= np.sum(self.Ps[s])

            self.Vs[s] = valids
            self.Ns[s] = 0
            return -v

        valids = self.Vs[s]
        cur_best = -float('inf')
        best_act = -1

        for a in range(self.game.actionsize()):
            if valids[a]:
                if (s, a) in self.Qsa:
                    u = self.Qsa[(s, a)] + 5 * self.Ps[s][a] * math.sqrt(self.Ns[s]) / (1 + self.Nsa[(s, a)])
                else:
                    u = 5 * self.Ps[s][a] * math.sqrt(self.Ns[s] + 1e-8)  # Q = 0 ?

                if u > cur_best:
                    cur_best = u
                    best_act = a

        a = best_act
        next_s, next_player = self.game.nextstate(oneminusone, 1, a)
        next_s = self.game.oneminusone(next_s, next_player)

        v = self.search(next_s)

        if (s, a) in self.Qsa:
            self.Qsa[(s, a)] = (self.Nsa[(s, a)] * self.Qsa[(s, a)] + v) / (self.Nsa[(s, a)] + 1)
            self.Nsa[(s, a)] += 1

        else:
            self.Qsa[(s, a)] = v
            self.Nsa[(s, a)] = 1

        self.Ns[s] += 1
        return -v

