# Importing the library 
import pygame 
import sys
  
# Initializing Pygame 
pygame.init() 
fps=30
fpsclock=pygame.time.Clock()
done = False
pygame.display.set_caption('Breakout')

# Initializing surface 
surface = pygame.display.set_mode((710,500)) 
  
# Initialing Color 

red = (255,0,0)
orange = (255,128,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
violet = (191,0,255) 

def make_bricks(height, color):
    count = 0
    left = 10
    while count < 10:
        pygame.draw.rect(surface, color, pygame.Rect(left, height, 60, 30))
        left += 70
        count += 1

def make_paddle(x_pos_new, x_pos_old):
    pygame.draw.rect(surface, (0,0,0), pygame.Rect(x_pos_old - 55, 480, 110, 10))
    pygame.draw.rect(surface, (255,255,0), pygame.Rect(x_pos_new - 55, 480, 110, 10))

paddle_pos = 355

while not done:  
    # Drawing Rectangle 
    make_bricks(10, red)
    make_bricks(50, orange)
    make_bricks(90, yellow)
    make_bricks(130, green)
    make_bricks(170, blue)
    make_bricks(210, violet)


    

    # draw and quit
    previous_paddle_pos = paddle_pos
    paddle_speed = 40
    key_input = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if key_input[pygame.K_LEFT]:
            paddle_pos -= paddle_speed
        if key_input[pygame.K_RIGHT]:
            paddle_pos += paddle_speed

    make_paddle(paddle_pos, previous_paddle_pos)
    pygame.display.flip() 
    fpsclock.tick(fps)
