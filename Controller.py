import pygame

pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print('Mate plug the controller in')

joystick = pygame.joystick.Joystick()
joystick.init()

left_x = joystick.get_axis(0)
left_y = joystick.get_axis(1)