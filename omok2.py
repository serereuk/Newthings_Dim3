
import pygame, sys, numpy, time
from pygame.locals import *
from omokgame import Omokgame

class Ogame():

    def __init__(self, game, gbsize):
        self.white = [255, 255, 255]
        self.black = [0, 0, 0]
        self.base = [234, 132, 42]
        self.game = game
        self.state = game.startphan()
        self.turn = 0
        self.cellsize = gbsize

    def stone(self, x, y):
        a = int(round(x/self.cellsize)) * self.cellsize
        b = int(round(y/self.cellsize)) * self.cellsize
        return a, b

    def matr(self, phan, move):
        phan[move[1], move[0]] = move[2]
        self.state = phan
        return self.state


    def main(self):
        pygame.init()
        pygame.display.set_caption("OMOK")
        self.displaysurf = pygame.display.set_mode((self.cellsize * 40, self.cellsize * 40))
        self.displaysurf.fill(self.base)
        for i in range(self.cellsize):
            for j in range(self.cellsize):
                pygame.draw.rect(self.displaysurf, self.black,
                                 [2*self.cellsize + 4 * i * self.cellsize, 2*self.cellsize + 4 * j * self.cellsize,
                                  self.cellsize * 4, self.cellsize * 4], 2)
                pygame.display.update()
                pygame.draw.circle(self.displaysurf, self.black, (144, 144), 13)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and self.turn == 1:
                    mousex, mousey = pygame.mouse.get_pos()
                    a, b = self.stone(mousex, mousey)
                    print(a, b)
                    if a % 32 == 0 or b % 32 == 0:
                        print("retry")
                        continue
                    if a % 2 == 1 or b % 2 == 1:
                        print("retry")
                        continue
                    self.state = self.matr(self.state,
                                           [int((a/(2*self.cellsize)-1)/2), int((b/(2*self.cellsize)-1)/2), self.turn * 2 - 1])
                    pygame.draw.circle(self.displaysurf, self.black, self.stone(mousex, mousey), 13)
                    pygame.display.update()
                    self.turn = 0

                elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and self.turn == 0:
                    mousex, mousey = pygame.mouse.get_pos()
                    a, b = self.stone(mousex, mousey)
                    print(a, b)
                    if a % 32 == 0 or b % 32 == 0:
                        print("retry")
                        continue
                    if a % 2 == 1 or b % 2 == 1:
                        print("retry")
                        continue
                    self.state = self.matr(self.state,
                                           [int((a/(2*self.cellsize) - 1)/2), int((b/(2*self.cellsize)-1)/2),
                                            self.turn * 2 - 1])
                    pygame.draw.circle(self.displaysurf, self.white, self.stone(mousex, mousey), 13)
                    pygame.display.update()
                    self.turn = 1

                if event.type == pygame.KEYDOWN:
                    print(self.state)



Ogame(Omokgame(9,5), 8).main()