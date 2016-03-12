import pygame
import time
from pygame.locals import *
from sense_hat import SenseHat

pygame.init()
pygame.display.set_mode((100, 100))
sense = SenseHat()
sense.clear()

running = True

A = (0, 255, 0)
X = (0, 0, 0)
P = (125, 80, 200)
M = (60, 200, 130)

music_interface = [
A, X, A, X, A, X, A, X,
A, X, A, X, A, X, A, X,
A, X, A, X, A, X, A, X,
A, X, A, X, A, X, A, X,
X, X, X, X, X, X, X, X,
M, M, M, M, M, M, M, M,
X, X, X, X, X, X, X, X,
P, P, P, P, P, P, P, P]

sense.set_pixels(music_interface)

x = 0
y = 0

#sense.set_pixels(x, y, 255, 255, 255)

while running:
    Co_Ord = {"0, 0": "A" }
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            '''Turns Pixel Off'''
            sense.set_pixel(x, y, 0, 0, 0)  # Black 0,0,0 means OFF

            sense.set_pixels(music_interface)

            if event.key == K_DOWN and y < 7:
                y = y + 1
            elif event.key == K_UP and y > 0:
                y = y - 1
            elif event.key == K_RIGHT and x < 7:
                x = x + 1
            elif event.key == K_LEFT and x > 0:
                x = x - 1

        sense.set_pixel(x, y, 255, 255, 255)
        print (x, y)
        print (type(x))
        print (type(y))
        #position = str("x" + "," +" y")
        #print (position)
        #print type(position)

        
        #for position, v in Co_Ord:
            #print (v)


      

        ###SHOW LETTER###
        
            
        if event.type == QUIT:
            running = False
            print("BYE")
