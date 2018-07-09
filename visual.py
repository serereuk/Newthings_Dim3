import matplotlib.pyplot as plt

#Reference visual.py

class visual():

    def __init__(self, gbsize, win_standard):
        self.gbsize = gbsize
        self.win_standard = win_standard
        self.player1 = 1
        self.player2 = -1

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
        plt.title("Tobigo : Human vs AI")
        if (gameover == False):
            if (player == self.player1):
                plt.plot(act[0], act[1], 'ko', markersize=30)
            else:
                plt.plot(act[0], act[1], 'wo', markersize=30)
        else:
            # 게임이 끝났다면 바툭판을 원상복귀
            plt.close("all")  # 초기화
            self.prepare_display()





#gridSize =10
#STONE_PLAYER1 = 1
#STONE_PLAYER2 = -1

#def _prepare_display():
#    plt.ion() # interactive 모드
#    """게임을 화면에 보여주기 위해 matplotlib 으로 출력할 화면을 설정합니다. 화면은 grid 사이즈 만큼."""
#    fig, axis = plt.subplots(figsize=(gridSize, gridSize))

    # 화면을 닫으면 프로그램을 종료합니다.
#    fig.canvas.mpl_connect('close_event', exit)

    #바둑판 색에 맞추어 색 변경
#    axis.set_facecolor('xkcd:puce')#참고 색상표 : https://xkcd.com/color/rgb/

    #화면에 출력할 축의 길이를 설정 [X축: -1 ~ 10],[Y축: -1 ~ 10]
#    plt.axis((-1, gridSize, -1, gridSize))

    #바둑판의 선을 그려주는 내용
#    for y in range(0,gridSize):
#        plt.axhline(y=y, color='k', linestyle='-')
#        plt.axvline(x=y, color='k', linestyle='-')

#    return fig, axis

#def _draw_screen(player,act,gameOver):
#    title = " Avg. Reward: %d Reward: %d Total Game: %d"

    #제목, 들어갈 내용: 에피소드, 리워드, 등등
#    plt.title(title + "Tobig's 5 go")
#    if(gameOver == False):
#        if(player == STONE_PLAYER1):
#            plt.plot([act // gridSize], [act % gridSize], 'ko', markersize=30)
#        else:
#            plt.plot([act // gridSize], [act % gridSize], 'wo', markersize=30)
#    else:
        #게임이 끝났다면 바툭판을 원상복귀
#        plt.cla() #초기화
#        axis.set_facecolor('xkcd:puce')  # 참고 색상표 : https://xkcd.com/color/rgb/
#        plt.title("Game Over")
#        for y in range(0, gridSize):
#            plt.axhline(y=y, color='k', linestyle='-')
#            plt.axvline(x=y, color='k', linestyle='-')
#    plt.pause(1)

#fig, axis = _prepare_display()

#예시코드
#_draw_screen(player= STONE_PLAYER1,act = 55, gameOver= False)
#_draw_screen(player= STONE_PLAYER2,act = 66, gameOver= False)
#_draw_screen(player= STONE_PLAYER1,act = 44, gameOver= False)
#_draw_screen(player= STONE_PLAYER2,act = 45, gameOver= False)
#_draw_screen(player= STONE_PLAYER1,act = 54, gameOver= False)
#_draw_screen(player= STONE_PLAYER2,act = 56, gameOver= False)
#_draw_screen(player= STONE_PLAYER1,act = 34, gameOver= True)
