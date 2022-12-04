#!/usr/bin/env python3

# Importing the libraries 
import pygame 
from pygame.locals import *
import sys
import random
import math
import json 
import time
  
# Initializing Pygame 
pygame.init() 
fps=30
fpsclock=pygame.time.Clock()
done = False
pygame.display.set_caption('Breakout')

# Initialing Color 
red    = [255,0,0,255]
orange = [255,128,0,255]
yellow = [255,255,0,255]
green  = [0,255,0,255]
blue   = [0,0,255,255]
violet = [191,0,255,255] 
gray   = [200, 200, 200]

surface = pygame.display.set_mode((700, 300))

def get_input(prompt, color):
    input = ""
    font = pygame.font.SysFont(None, 48)
    img = font.render(prompt, True, color)
    rect = img.get_rect()
    rect.topleft = (20, 20)
    cursor = Rect(rect.topright, (3, rect.height))
    inputting = True
    background = gray
    while inputting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(input)>0:
                        input = input[:-1]
                elif event.key == K_RETURN:
                    inputting = False
                elif event.unicode.isdigit():
                    input += event.unicode
                img = font.render(prompt + input, True, color)
                rect.size=img.get_size()
                cursor.topleft = rect.topright
    
        surface.fill(background)
        surface.blit(img, rect)
        if time.time() % 1 > 0.5:
            pygame.draw.rect(surface, color, cursor)
        pygame.display.update()
    return int(input)

# units
ball_size = get_input("Ball size: ", violet)
paddle_width = 120
brick_width = 60
brick_height = 30
gap = 10
brick_amount = get_input("Number of columns: ", red)
rows = 7
screen_width = (brick_amount*brick_width + (brick_amount+1)*gap)
screen_height = 2*(rows*brick_height + (rows+1)*gap) # 580
score_width = 200
score_height = 40
paddle_hover = 50

# Initializing surface 
surface = pygame.display.set_mode((screen_width,screen_height)) 

# set icon
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)

font = pygame.font.SysFont('Nimbus Sans Bold', 48, True, False)

def make_bricks(height, color, number):
    left = gap
    for x in number:
        if x == 1:
            pygame.draw.rect(surface, color, pygame.Rect(left, height, brick_width, brick_height))
        else:
            pygame.draw.rect(surface, (0,0,0), pygame.Rect(left, height, brick_width, brick_height))
        left += 70 # brick_width + gap

def remove_brick(ball_x,ball_y):
    divide_x = screen_width/brick_amount
    divide_y = (screen_height/2)/rows
    remove_x = math.floor(ball_x/divide_x)
    remove_y = math.floor(ball_y/divide_y)
    return (remove_x,remove_y)

def make_paddle(x_pos_new, x_pos_old):
    pygame.draw.rect(surface, (0,0,0), pygame.Rect(x_pos_old - paddle_width/2, screen_height - paddle_hover, paddle_width, 10))
    pygame.draw.rect(surface, (255,255,0), pygame.Rect(x_pos_new - paddle_width/2, screen_height - 50, paddle_width, 10))

def make_ball(x_pos_new, x_pos_old, y_pos_new, y_pos_old):
    pygame.draw.circle(surface, (0,0,0), (x_pos_old, y_pos_old), ball_size)
    pygame.draw.circle(surface, (255,255,0), (x_pos_new, y_pos_new), ball_size)
    return [x_pos_new,y_pos_new]

def make_score(lives, score):
    pygame.draw.rect(surface, (0,0,0), pygame.Rect(0, 0, screen_width, score_height))
    lives_write = font.render('Lives: {0}'.format(lives), 1, yellow)
    score_write = font.render('Score: {0}'.format(score), 1, yellow)
    surface.blit(lives_write, (gap, gap))
    surface.blit(score_write, (screen_width - (score_width + gap), gap))

# set pos vars
paddle_pos = screen_width/2 - paddle_width/2
ball_pos_x = screen_width/2 - ball_size/2
ball_pos_y = screen_height/2 - ball_size/2

# x and y are the incremental steps
x = 0
y = 0
speed = 10

def pick_direction():
    random_angle = random.random()*0.6 + 0.2
    while (0.4 < random_angle < 0.6):
        random_angle = random.random()*0.6 + 0.2
    angle = random_angle*math.pi
    x = math.cos(angle)*speed
    y = math.sin(angle)*speed
    return [x,y]
[x,y] = pick_direction()

# set lives and score
lives = 5
score = 0

# clear screen
pygame.draw.rect(surface, (0,0,0), pygame.Rect(0, 0, screen_width, screen_height))

# color arrays
#colorArrays = [[1] * brick_amount] * 6
#rows, cols = (5, 5)
colorArrays = [[1 for i in range(brick_amount + 1)] for j in range(6)]
#colorArrays = [[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]

while not done:
    red_array    = colorArrays[0]
    orange_array = colorArrays[1]
    yellow_array = colorArrays[2]
    green_array  = colorArrays[3]
    blue_array   = colorArrays[4]
    violet_array = colorArrays[5]
  
    # Drawing Bricks 
    colors = [red,orange,yellow,green,blue,violet]
    brick_pos_y = [50,90,130,170,210,250]    

    for i in range(len(colorArrays)):
        make_bricks(((score_height + gap) + (brick_height + gap)*i), colors[i], colorArrays[i])

    if ball_pos_x + ball_size > screen_width or ball_pos_x - ball_size < 0:
        x = -x
    if ball_pos_y - ball_size < 0:
        y = -y

    # make the ball bounce on the paddle
    if ball_pos_y + ball_size > screen_height - paddle_hover:
        if ball_pos_y + ball_size < screen_height - paddle_hover + 10:
            if paddle_pos - 70 < ball_pos_x < paddle_pos + 70:
                y = -y
                if not(paddle_pos - 25 < ball_pos_x < paddle_pos + 25):
                    hit_right = ball_pos_x - paddle_pos > 0
                    moving_right = x > 0
                    if hit_right != moving_right:
                        x = -x
        if ball_pos_y + ball_size > screen_height - paddle_hover + 20:
            lives -= 1
            pygame.draw.circle(surface, (0,0,0), (ball_pos_x, ball_pos_y), ball_size)
            pygame.draw.rect(surface, (0,0,0), pygame.Rect(paddle_pos - paddle_width/2, screen_height - paddle_hover, paddle_width, 10))
            ball_pos_x = screen_width/2 - ball_size/2
            ball_pos_y = screen_height/2 - ball_size/2
            paddle_pos = screen_width/2 - paddle_width/2
            [x,y] = pick_direction()

    make_score(str(lives), str(score))

    # erase bricks
    rem_brick = remove_brick(ball_pos_x,ball_pos_y)
    rem_brick_shift = rem_brick[1] - 1
    v = 0
    if 0 < rem_brick[1] < 7:
        v = colorArrays[rem_brick_shift][rem_brick[0]]
        colorArrays[rem_brick_shift][rem_brick[0]] = 0
    if v != 0:
            score += 7 - rem_brick[1]
            y = -y

    previous_ball_pos_x = ball_pos_x
    previous_ball_pos_y = ball_pos_y
    ball_pos_x += x
    ball_pos_y += y
    make_ball(ball_pos_x, previous_ball_pos_x, ball_pos_y, previous_ball_pos_y)

    # draw and quit
    previous_paddle_pos = paddle_pos
    paddle_speed = 10

    #key_input = pygame.key.get_pressed()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_pos -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_pos += paddle_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if lives < 0:
        done = True

    make_paddle(paddle_pos, previous_paddle_pos)
    pygame.display.flip() 
    fpsclock.tick(fps)
