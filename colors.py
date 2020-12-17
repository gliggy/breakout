# Importing the library 
import pygame 
import sys
import random
import math
  
# Initializing Pygame 
pygame.init() 
fps=30
fpsclock=pygame.time.Clock()
done = False
pygame.display.set_caption('Colors')

# Initializing surface 
surface = pygame.display.set_mode((710,250)) 

# Initialing Color 
red    = [255,0,0,255]
orange = [255,128,0,255]
yellow = [255,255,0,255]
green  = [0,255,0,255]
blue   = [0,0,255,255]
violet = [191,0,255,255] 

def make_bricks(height, color, number):
    left = 10
    for x in number:
        if x == 1:
            pygame.draw.rect(surface, color, pygame.Rect(left, height, 60, 30))
            color[2] = (color[2] + 50) % 256
        else:
            pygame.draw.rect(surface, (0,0,0), pygame.Rect(left, height, 60, 30))
        left += 70

while not done:  
    # Drawing Bricks 
    brick_pos_y = [10,50,90,130,170,210]
    
    colorArrays = [[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]
    red_array    = colorArrays[0]
    orange_array = colorArrays[1]
    yellow_array = colorArrays[2]
    green_array  = colorArrays[3]
    blue_array   = colorArrays[4]
    violet_array = colorArrays[5]

    make_bricks(brick_pos_y[0], red, red_array)
    make_bricks(brick_pos_y[1], orange, orange_array)
    make_bricks(brick_pos_y[2], yellow, yellow_array)
    make_bricks(brick_pos_y[3], green, green_array)
    make_bricks(brick_pos_y[4], blue, blue_array)
    make_bricks(brick_pos_y[5], violet, violet_array)
    
    # draw and quit
    key_input = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip() 
    fpsclock.tick(fps)