# import pygame 
import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            # create a rectangle
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # draw rectangle
            pygame.draw.rect(screen, pygame.Color('Magenta'), block_rect)

class FRUIT:
    def __init__(self):
        # crate an x and y position
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(int(self.x * cell_size), int(self.y * cell_size), cell_size, cell_size)
        # draw the rectangle
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

# initialize pygame
pygame.init()
cell_size = 40
cell_number = 20
# create a screen (width, height) - in a tuple
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

fruit = FRUIT()
snake = SNAKE()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # .quit is opposite of .init & sys.exit to make sure everything will be closed
            pygame.quit()
            sys.exit()
    screen.fill((175, 215, 70))
    # draw fruit
    fruit.draw_fruit()
    # draw snake
    snake.draw_snake()
    # draw all our elements
    pygame.display.update()
    # limiting the while loop because of different speed of computers / 60 = framerate
    clock.tick(60)