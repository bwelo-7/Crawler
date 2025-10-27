import pygame
from pygame.joystick import Joystick

from stuff import GREEN, WIDTH, HEIGHT, spr_width, spr_height, ax, ay, speed
from utils import bracket





class Thing(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((spr_width, spr_height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        # self.rect.centerx = WIDTH / 2
        # self.rect.bottom = HEIGHT + 20
        self.fx = 0.8
        self.fy = 0.8
        self.dx = 0
        self.dy = 0
        self.rect.x = x
        self.rect.y = y

class Bob(Thing):
    def __init__(self, x, y):
            Thing.__init__(self,x,y)

    def update(self, keys, joystick, walls):
        deadzone = 0.1
        left_x = joystick.get_axis(0)
        left_y = joystick.get_axis(1)
        # self.collide(walls)

        if abs(left_x) > deadzone or abs(left_y) > deadzone:
            self.con_movement(joystick)
        else:
            self.dynamic_movement(keys)

        self.dx = bracket(self.dx, -10, 10)
        self.dy = bracket(self.dy, -10, 10)

        self.rect.x += (self.dx)
        self.rect.y += (self.dy)

        self.rect.x = bracket(self.rect.x, 0, WIDTH - spr_width)
        self.rect.y = bracket(self.rect.y, 0, HEIGHT - spr_height)

        print("dx:", self.dx, "x: ", self.rect.x, "dy:", self.dy, "y: ", self.rect.y)

    def dynamic_movement(self, keys):
        if keys[pygame.K_a]:
            self.dx -= ax
        elif keys[pygame.K_d]:
            self.dx += ax
        else:
            self.dx *= self.fx

        if keys[pygame.K_w]:
            self.dy -= ay
        elif keys[pygame.K_s]:
            self.dy += ay
        else:
            self.dy *= self.fy

        if 0.1 > self.dx > -0.1:
            self.dx = 0
        if 0.1 > self.dy > -0.1:
            self.dy = 0

    def con_movement(self, joystick):
        left_x = joystick.get_axis(0)
        left_y = joystick.get_axis(1)

        deadzone = 0.4

        if abs(left_x) < deadzone:
            left_x = 0
        if abs(left_y) < deadzone:
            left_y = 0

        if left_x != 0:
            self.dx = left_x * ax
        else:
            self.dx *= self.fx

        if left_y != 0:
            self.dy = left_y * ay
        else:
            self.dy *= self.fy

