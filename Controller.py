import pygame
from Bob import Bob
pygame.joystick.init()

class KeyboardController:
    def get_axis(self, axis):
        keys = pygame.key.get_pressed()

        if axis == 0:
            if keys[pygame.K_j]:
                return -1
            elif keys[pygame.K_l]:
                return 1
            else:
                return 0
        if axis == 1:
            if keys[pygame.K_i]:
                return -1
            elif keys[pygame.K_k]:
                return 1
            else:
                return 0
        if axis == 2:
            if keys[pygame.K_a]:
                return -1
            elif keys[pygame.K_d]:
                return 1
            else:
                return 0

        if axis == 5:
            if keys[pygame.K_a]:
                return -1
            elif keys[pygame.K_d]:
                return 1
            else:
                return 0


        if axis == 3:
            if keys[pygame.K_s]:
                return -1
            elif keys[pygame.K_w]:
                return 1
            else:
                return 0
