import numpy as np

def rle2(x, color):
    dots = np.where(x.T.flatten() == color)[0]
    run_lengths = []
    prev = -2
    for b in dots:
        if b>prev+1: run_lengths.append([color, 0])
        run_lengths[-1][1] += 1
        prev = b

    return run_lengths

class Phan:

    def __init__(self, gbsize, win_standard):
        self.gbsize = gbsize
        self.win_standard = win_standard
        self.board = np.zeros((self.gbsize, self.gbsize))

    def dun_soo(self):   # 아직 비어 있는 곳을 의미

        moves = set()
        for y in range(self.gbsize):
            for x in range(self.gbsize):
                if self.board[x, y] == 0:
                    newmove = (x, y)
                    moves.add(newmove)

        return list(moves)

    def ganeung_soo(self):

        for y in range(self.gbsize):
            for x in range(self.gbsize):
                if self.board[x, y] == 0:
                    return True

        return False

    def iswin(self, color):
        dif = int(self.gbsize - self.win_standard)

        for i in range(self.gbsize):
            temp = rle2(self.board[i, :], color)
            temp2 = rle2(self.board[:, i], color)
            if [color, self.win_standard] in temp:
                return True
            if [color, self.win_standard] in temp2:
                return True

        for i in range(-dif, dif):
            alp = np.diag(self.board, k=i)
            alp2 = np.diag(np.fliplr(self.board), k=i)
            temp = rle2(alp, color)
            temp2 = rle2(alp2, color)
            if [color, self.win_standard] in temp:
                return True
            if [color, self.win_standard] in temp2:
                return True

        return False

    def moving(self, move, color):
        (x, y) = move
        self.board[x, y] = color
