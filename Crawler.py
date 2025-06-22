import pygame
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

all_sprites = pygame.sprite.Group()
all_sprites.add(Bob(200, 200))
all_sprites.add(Bill(300, 300))
all_sprites.add(Fireball(200 ,300))
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

    #pygame.draw.
    # Update
    all_sprites.update(keys)
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # after drawing everything
    pygame.display.flip()

pygame.quit()


