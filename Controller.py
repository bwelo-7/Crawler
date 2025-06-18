import pygame

pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print('Mate plug the controller in')

joystick = pygame.joystick.Joystick()
joystick.init()

left_x = joystick.get_axis(0)
left_y = joystick.get_axis(1)

deadzone = 0.4

if abs(left_x) < deadzone: #abs means that if its like -7 then it becomes 7
    left_x = 0
if abs(left_y) < deadzone:
    left_y = 0

