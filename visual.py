import matplotlib
import matplotlib.pyplot as plt
import pickle

#Reference visual.py

class visual():

    def __init__(self, gbsize, win_standard):
        self.gbsize = gbsize
        self.win_standard = win_standard

    def prepare_display(self):
        plt.ion()
        fig, axis = plt.subplots(figsize=(self.gbsize, self.gbsize))
        fig.canvas.mpl_connect("close_event", exit)
        axis.set_facecolor("xkcd:puce")
        plt.axis((-1, self.gbsize, -1, self.gbsize))

        for y in range(0, self.gbsize):
            plt.axhline(y=y, color="k", linestyle="-")
            plt.axvline(x=y, color="k", linestyle="-")

        return fig, axis

    def draw_screen(self, player, act, gameover):
        plt.title("Tobigo : AI vs AI")
        if (gameover == False):
            if (player == 1):
                plt.plot(act[0], act[1], 'ko', markersize=30)
            else:
                plt.plot(act[0], act[1], 'wo', markersize=30)
        else:
            # 게임이 끝났다면 바툭판을 원상복귀
            plt.close("all")  # 초기화
            self.prepare_display()


