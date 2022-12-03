#!/usr/bin/env python3

# Importing the libraries 
import pygame 
import sys
import random
import math
import json 
  
# Initializing Pygame 
pygame.init() 
fps=30
fpsclock=pygame.time.Clock()
done = False
pygame.display.set_caption('Breakout')

# Initializing surface 
surface = pygame.display.set_mode((710,540)) 

# set icon
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)

font = pygame.font.SysFont('Nimbus Sans Bold', 48, True, False)
  
# Initialing Color 
red    = [255,0,0,255]
orange = [255,128,0,255]
yellow = [255,255,0,255]
green  = [0,255,0,255]
blue   = [0,0,255,255]
violet = [191,0,255,255] 

def make_bricks(height, color, number):
    left = 10
    color_original = color[2]
    direction = 1 if color_original == 0 else -1
    for x in number:
        if x == 1:
            pygame.draw.rect(surface, color, pygame.Rect(left, height, 60, 30))
            color[2] = (color[2] + direction * 2) % 256
            # print(color[color_changer])
        else:
            pygame.draw.rect(surface, (0,0,0), pygame.Rect(left, height, 60, 30))
        left += 70
    color[2] = color_original

def remove_brick(ball_x):
    remove = math.floor(ball_x/71)
    return remove
    #remove = []
    #left = 5
    #number = [0,1,2,3,4,5,6,7,8,9]
    #array_pos = 0
    #for x in number:
    #    if ball_x in range(left, left + 65):
    #        remove.append(array_pos)
    #    else:
    #        remove.append(1)
    #    left += 65
    #    array_pos += 1
    #return remove
    

def make_paddle(x_pos_new, x_pos_old):
    pygame.draw.rect(surface, (0,0,0), pygame.Rect(x_pos_old - 55, 480, 110, 10))
    pygame.draw.rect(surface, (255,255,0), pygame.Rect(x_pos_new - 55, 480, 110, 10))

#b = 0

def make_ball(x_pos_new, x_pos_old, y_pos_new, y_pos_old):
    #pixel = surface.get_at((int(x_pos_new), int(y_pos_new)))
    #if pixel != (255,255,0,255):
        #b = pixel[2]
        #print(b)
    pygame.draw.circle(surface, (0,0,0), (x_pos_old, y_pos_old), 20)
    pygame.draw.circle(surface, (255,255,0), (x_pos_new, y_pos_new), 20)
    return [x_pos_new,y_pos_new]

def make_score(lives, score):
    pygame.draw.rect(surface, (0,0,0), pygame.Rect(0, 0, 710, 40))
    lives_write = font.render('Lives: {0}'.format(lives), 1, yellow)
    score_write = font.render('Score: {0}'.format(score), 1, yellow)
    # score_write.fill(yellow)
    surface.blit(lives_write, (10, 10))
    surface.blit(score_write, (480, 10))

# set pos vars
paddle_pos = 355
ball_pos_x = 355
ball_pos_y = 250

# x and y are the incremental steps
x = 0
y = 0
speed = 5

def pick_direction():
    angle = (random.random()*0.6 + 0.2)*math.pi
    x = math.cos(angle)*speed
    y = math.sin(angle)*speed
    return [x,y]
[x,y] = pick_direction()

# set lives and score
lives = 5
score = 0

# clear screen
pygame.draw.rect(surface, (0,0,0), pygame.Rect(0, 0, 710, 540))

# color arrays
colorArrays = [[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]

while not done:
    red_array    = colorArrays[0]
    orange_array = colorArrays[1]
    yellow_array = colorArrays[2]
    green_array  = colorArrays[3]
    blue_array   = colorArrays[4]
    violet_array = colorArrays[5]
  
    # Drawing Bricks 
    brick_pos_y = [50,90,130,170,210,250]    

    make_bricks(brick_pos_y[0], red, red_array)
    make_bricks(brick_pos_y[1], orange, orange_array)
    make_bricks(brick_pos_y[2], yellow, yellow_array)
    make_bricks(brick_pos_y[3], green, green_array)
    make_bricks(brick_pos_y[4], blue, blue_array)
    make_bricks(brick_pos_y[5], violet, violet_array)

    if ball_pos_x + 20 > 710 or ball_pos_x - 20 < 0:
        x = -x

    # make the ball bounce on the paddle
    if ball_pos_y + 20 > 480:
        if ball_pos_y + 20 < 490:
            if paddle_pos - 60 < ball_pos_x < paddle_pos + 60:
                y = -y
                if not(paddle_pos - 25 < ball_pos_x < paddle_pos + 25):
                    hit_right = ball_pos_x - paddle_pos > 0
                    moving_right = x > 0
                    if hit_right != moving_right:
                        x = -x
        if ball_pos_y + 20 > 500:
            lives -= 1
            pygame.draw.circle(surface, (0,0,0), (ball_pos_x, ball_pos_y), 20)
            ball_pos_x = 355
            ball_pos_y = 250
            [x,y] = pick_direction()
    
    make_score(str(lives), str(0))
    
    #if ball_pos_y - 20 < 40 and red_array != [0,0,0,0,0,0,0,0,0,0]:
    #    y = -y
    if ball_pos_y < 0:
        y = -y

    # erase bricks
    i = 0
    while (i < 6):
        #if i == 0 and ball_pos_y < 70:
        #    colorArrays[0][remove_brick(ball_pos_x)] = 0
        if (brick_pos_y[i-1] if i else 0) < ball_pos_y < brick_pos_y[i]:
            v = colorArrays[i][remove_brick(ball_pos_x)]
            colorArrays[i][remove_brick(ball_pos_x)] = 0
            if v != 0:
                y = -y
        i += 1

    previous_ball_pos_x = ball_pos_x
    previous_ball_pos_y = ball_pos_y
    ball_pos_x += x
    ball_pos_y += y
    make_ball(ball_pos_x, previous_ball_pos_x, ball_pos_y, previous_ball_pos_y)

    #print(lives)    
    #display_lives = font.render(lives, True, (255,255,255))


    # draw and quit
    previous_paddle_pos = paddle_pos
    paddle_speed = 40
    key_input = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_pos -= paddle_speed
            if event.key == pygame.K_RIGHT:
                paddle_pos += paddle_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_pos = paddle_pos
    if lives < 0:
        done = True

    make_paddle(paddle_pos, previous_paddle_pos)
    pygame.display.flip() 
    fpsclock.tick(fps)
