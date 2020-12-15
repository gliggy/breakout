import pygame as p

s=p.display.set_mode((720,360))
c=p.Color(0,0,0)
for i in range(360,0,-1):
    c.hsla=(i,100,50,100)
    p.draw.circle(s,c,(360,360),i)
    __import__('time').sleep(0.1)
    p.display.flip()