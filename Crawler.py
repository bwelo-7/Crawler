import pygame
from pygame.joystick import Joystick

from Bill import Bill
from Bob import Bob
from Fireball import Fireball
#from Controller import con_movement
from stuff import BLACK, WIDTH, HEIGHT







FPS = 30
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crawler')
clock = pygame.time.Clock()


if pygame.joystick.get_count() == 0:
    print('Mate plug the controller in')


joystick = pygame.joystick.Joystick(0)
joystick.init()


fireballs = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

all_sprites.add(Bob(200, 200))

all_sprites.add(Bill(300, 300))

Fireball_cooldown = 500
last_fireball_time = 0



#game loop
running = True
while running:
    #keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
            #check for closing the window
            if event.type == pygame.QUIT:
                running = False


    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()
    R2_axis = joystick.get_axis(5)

    # Update
    if R2_axis > 0.5:
        for sprite in all_sprites:
            if isinstance(sprite, Bob):
                if current_time - last_fireball_time > Fireball_cooldown:
                    fireball = Fireball(sprite.rect.centerx, sprite.rect.centery, dx = 0, dy= 10 )
                    all_sprites.add(fireball)
                    last_fireball_time = current_time


    for sprite in all_sprites:
        sprite.update(keys, joystick)

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # after drawing everything
    pygame.display.flip()

pygame.quit()


