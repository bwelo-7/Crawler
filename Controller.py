import pygame
from Bob import Bob
pygame.joystick.init()



# left_x = joystick.get_axis(0)
# left_y = joystick.get_axis(1)



# def controller(left_x, left_y):
#     if abs(left_x) < deadzone: #abs means that if its like -7 then it becomes 7
#         return 0
#     else:
#         return left_x

def con_movement(self, joystick):
    left_x = joystick.get_axis(0)
    left_y = joystick.get_axis(1)

    deadzone = 0.4


    if abs(left_x) < deadzone:
        left_x = 0
    if abs(left_y) < deadzone:
        left_y = 0


    if left_x != 0:
        self.dx = left_x * self.ax
    else:
        self.dx *= self.fx

    if left_y != 0:
        self.dy = left_y * self.ay
    else:
        self.dy *= self.fy


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
