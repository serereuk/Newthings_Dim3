from coach import coaching
from omokgame import Omokgame as game
from nn import nn
from mcts import mcts
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


g = game(13, 5)
nnet = nn(g)
Mcts = mcts(g, nnet)

c = coaching(g, nnet, Mcts)
c.learn()

