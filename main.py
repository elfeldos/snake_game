# import pygame 
import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            # create a rectangle
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # draw rectangle
            pygame.draw.rect(screen, pygame.Color('Magenta'), block_rect)

    def move_snake(self):
        # extend snake when fruit is hit - otherwise keep going
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True


class FRUIT:
    def __init__(self):
        self.randomize()
        
    
    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(int(self.x * cell_size), int(self.y * cell_size), cell_size, cell_size)
        # draw the rectangle
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
    
    def randomize(self):
        # crate an x and y position
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


# game logic
class MAIN:
    # when initiating main, creating snake and fruit
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_collison()
        self.check_fail()

    def draw_elements(self):
        # draw fruit
        self.fruit.draw_fruit()
        # draw snake
        self.snake.draw_snake()
    
    def check_collison(self):
        if self.fruit.pos == self.snake.body[0]:
            print("Snack")
            # reposition fruit
            self.fruit.randomize()
            # add another block to snake
            self.snake.add_block()

    def check_fail(self):
        # check if snake hits walls
        if not 0 <= self.snake.body[0].x < cell_number:
            self.game_over()
        elif not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        # checks if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                pygame.quit()
                sys.exit()
                
    
    def game_over(self):
        pygame.quit()
        sys.exit()



# initialize pygame
pygame.init()
cell_size = 40
cell_number = 20
# create a screen (width, height) - in a tuple
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # .quit is opposite of .init & sys.exit to make sure everything will be closed
            pygame.quit()
            sys.exit()
        # update every 150ms to move snake
        if event.type == SCREEN_UPDATE:
            main_game.update()
        # register keymovement of specific keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)


    screen.fill((175, 215, 70))
    # draw all our elements
    main_game.draw_elements()
    pygame.display.update()
    # limiting the while loop because of different speed of computers / 60 = framerate
    clock.tick(60)