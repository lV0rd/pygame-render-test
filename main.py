import pygame
import sys
import math
from settings import *
from map import *
from player import *
from raycasting import *

class game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.dt = 1
        self.paused = False
        self.newGame()
    def newGame(self):
        self.map = map(self)
        self.plr = plr(self)
        self.rc = rayCasting(self)

    def update(self):
        self.plr.update()
        self.rc.update()
        pygame.display.flip()
        self.dt = self.clock.tick(FPS)
        pygame.display.set_caption(f'RAYCAST RENDERER {round(self.clock.get_fps())} :FPS')

    def draw(self):
        self.screen.fill('black')
        #self.map.draw()
        #self.plr.draw()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
        
    def run(self):
        while True:
            self.checkEvents()
            self.update()
            self.draw()


newGame = game()
newGame.run()