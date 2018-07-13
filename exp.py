from omokgame import Omokgame as games
from nn import nn
from mcts import mcts
from visual2 import Result
import os
import pickle


os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
g = games(9, 5)
nnet = nn(g)
Mcts = mcts(g, nnet)
VV = Result(g, nnet, Mcts)
try:
    savings = VV.perform()
    with open("savings.txt", "wb") as f:
        pickle.dump(savings, f)
        print(savings)
except Exception as err:
    print(err)