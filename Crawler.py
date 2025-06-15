import pygame

WIDTH = 650
HEIGHT = 650
FPS = 30
x = 325
y = 610
speed = 2
ax = 10
ay = 10

# define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crawler')
clock = pygame.time.Clock()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT +20

        self.rect.x = x
        self.rect.y = y

    #def constraints(player):
        #if self.rect.x >

    def update(self):
        if keys[pygame.K_a]:
            self.rect.x -= (speed * ax)
        if keys[pygame.K_d]:
            self.rect.x += (speed * ax)
        if keys[pygame.K_s]:
            self.rect.y += ay
        if keys[pygame.K_w]:
            self.rect.y -= ay



all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
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
    all_sprites.update()
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # after drawing everything
    pygame.display.flip()

pygame.quit()


