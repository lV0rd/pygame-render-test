import pygame
import math
import random
from settings import *

class rayCasting:
    def __init__(self, game):
        self.game = game

    def raycast(self):
        ox, oy = self.game.plr.pos
        x_m, y_m = self.game.plr.mapPos
        rayAngle = self.game.plr.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS):
            sin_a = math.sin(rayAngle)
            cos_a = math.cos(rayAngle)

            y_hor, dy = (y_m + 1, 1) if sin_a > 0 else (y_m - 1e-6, -1)

            depth_h = (y_hor - oy) / sin_a
            x_hor = ox + depth_h * cos_a

            delta_depth = dy/sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_h += delta_depth

            x_vert, dx = (x_m + 1, 1) if cos_a > 0 else (x_m - 1e-6, -1)
            depth_v = (x_vert - ox) / cos_a
            y_vert = oy  + depth_v * sin_a

            delta_depth = dx/cos_a
            dy = delta_depth * sin_a


            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_v += delta_depth

            if depth_v < depth_h:
                depth = depth_v
            else:
                depth = depth_h

            # rid fishbowl eff
            depth *= math.cos(self.game.plr.angle - rayAngle)

            # proj
            proj_height = SCREEN_DIST / (depth + 0.0001)


            wallColor = [200 / (3 + depth ** 8 * 0.00002)] * 3

            pygame.draw.rect(self.game.screen,
                wallColor,
                (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

            rayAngle += DELTA_ANGLE

    def update(self):
        self.raycast()