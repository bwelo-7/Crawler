import pygame

pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print('Mate plug the controller in')

