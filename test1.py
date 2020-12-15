import pygame



def Create():
    pygame.init()
    done = False
    pygame.display.set_caption('Breakout')
    surface = pygame.display.set_mode((255,255)) 
    color = (255,0,0)
    orange = (255,128,0)
    yellow = (255,255,0)
    green = (0,255,0)
    blue = (0,0,255)
    violet = (191,0,255)
    while not done: 
        pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

Create()



