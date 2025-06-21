import pygame

pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print('Mate plug the controller in')

joystick = pygame.joystick.Joystick(0)
joystick.init()

left_x = joystick.get_axis(0)
left_y = joystick.get_axis(1)

deadzone = 0.4

def controller(left_x, left_y):
    if abs(left_x) < deadzone: #abs means that if its like -7 then it becomes 7
        return 0
    else:
        return left_x

def con_movement(self, keys):
    if abs(left_y) < deadzone:
        return 0
    else:
        return left_y

    if abs(left_x) => deadzone:
        self.dx -= ax
    elif abs(left_x) > 0.8:
        self.dx -= t_ax

    if abs(left_x) = > deadzone:
        self.dx -= ax
    elif abs(left_x) > 0.8:
        self.dx -= t_ax

    if abs(left_x) = > deadzone:
        self.dx -= ax
    elif abs(left_x) > 0.8:
        self.dx -= t_ax


