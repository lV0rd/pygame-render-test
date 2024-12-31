import pygame

_ = False

map1 = [
    [1,1,1,1,1,1,1,1],
    [1,_,_,_,_,1,_,1],
    [1,1,_,1,_,_,_,1],
    [1,_,_,1,_,_,_,1],
    [1,_,_,1,_,_,_,1],
    [1,1,1,1,1,1,1,1],
]

map2 = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1],
]

class map:
    def __init__(self, game):
        self.game = game
        self.mini_map = map1
        self.world_map = {}
        self.getMap()
    
    def getMap(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
    
    def draw(self):
        for pos in self.world_map:
            pygame.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)        
