from visual import visual
import numpy as np
from omokgame import Omokgame as games
from nn import nn
from mcts import mcts
from visual2 import Result
import os


os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
g = games(9, 5)
nnet = nn(g)
Mcts = mcts(g, nnet)
c = visual(9,5)
c.prepare_display()
#c.prepare_display()
#visual(9, 5).prepare_display()
#visual(9, 5).draw_screen(1, [4, 4], False)
#VV = Result(g, nnet, Mcts)
#VV.perform()
