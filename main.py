# import pygame 
import pygame, sys

# initialize pygame
pygame.init()
# create a screen (width, height) - in a tuple
screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # .quit is opposite of .init & sys.exit to make sure everything will be closed
            pygame.quit()
            sys.exit()
    screen.fill((175, 215, 70))
    # draw all our elements
    pygame.display.update()
    # limiting the while loop because of different speed of computers / 60 = framerate
    clock.tick(60)