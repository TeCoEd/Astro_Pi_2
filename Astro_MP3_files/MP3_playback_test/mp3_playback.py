import pygame
import time
import glob
from pygame.locals import *
from sense_hat import SenseHat

pygame.init()
pygame.display.set_mode((100, 100))
sense = SenseHat()
sense.clear()

volume = 0

pygame.mixer.music.load('/home/pi/Astro_MP3/MP3_files/Afr.mp3')
pygame.mixer.music.play()

while True:
    pygame.mixer.music.set_volume(volume)
    #sense.show_letter(str(volume))
    volume = volume + 1
    print volume
