import pygame
import time
import glob
import random
from pygame.locals import *
from sense_hat import SenseHat

pygame.init()
pygame.display.set_mode((100, 100))
sense = SenseHat()
sense.clear()

A = (0, 0, 255) #Blue
X = (0, 0, 0) #Black
P = (255, 255, 0) #YellowGreen      
M = (60, 200, 130)
Reset = (255,165,0)
End = (255, 0, 0) 
Volume = (0, 255, 0) #Green

###change interface###
music_interface = [
A, A, A, A, A, A, A, A, #ALPHA
A, A, A, A, A, A, A, A,
A, A, A, A, A, A, A, A,
A, A, X, X, X, X, X, X,
X, X, X, X, X, X, X, Reset,
M, M, M, M, X, X, X, Volume, #MOOD AND VOLUME
X, X, X, X, X, X, X, M,
P, P, P, P, X, X, X, End] #PLAYLISTS

sense.set_pixels(music_interface)


