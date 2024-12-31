from settings import *
import pygame
import math

class plr:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.dt
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin

        if keys[pygame.K_q]:
            dx += speed_sin
            dy += -speed_cos

        if keys[pygame.K_d]:
            dx += -speed_sin
            dy += speed_cos


        self.checkWallColl(dx, dy)

        if keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROTATION_SPEED * self.game.dt
        if keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROTATION_SPEED * self.game.dt
        
        self.angle %= math.tau

    def draw(self):
        pygame.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def checkWall(self, x, y):
        return (x, y) not in self.game.map.world_map
    
    def checkWallColl(self, dx, dy):
        if self.checkWall(int(self.x + dx), int(self.y)):
            self.x += dx
        
        if self.checkWall(int(self.x), int(self.y + dy)):
            self.y += dy
        
    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def mapPos(self):
        return int(self.x), int(self.y)

    
    