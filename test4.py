import pygame
import sys
from pygame.locals import *
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((640, 400))
cursor = pygame.mouse.set_cursor(*pygame.cursors.diamond)


class Player(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(x=x, y=y)

player1, player2 = Player('square.png', 100, 100), Player('square1.png', 200, 200)
players = pygame.sprite.Group(player1, player2)

while True:
    screen.fill(black)

    if player1.rect.colliderect(player2.rect):
        print ('collision!')

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_w:
                player1.rect.move_ip(0, -10) 
            elif event.key == K_s:
                player1.rect.move_ip(0, 10)
            elif event.key == K_a:
                player1.rect.move_ip(-10, 0)
            elif event.key == K_d:
                player1.rect.move_ip(10, 0)
            if event.key == K_UP:
                player2.rect.move_ip(0, -10)
            elif event.key == K_DOWN:
                player2.rect.move_ip(0, 10)
            elif event.key == K_LEFT:
                player2.rect.move_ip(-10, 0)
            elif event.key == K_RIGHT:
                player2.rect.move_ip(10, 0)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    players.draw(screen)
    pygame.display.update()
