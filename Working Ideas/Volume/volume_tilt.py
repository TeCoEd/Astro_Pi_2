import pygame
import time
import glob
from pygame.locals import *
from sense_hat import SenseHat

pygame.init()
pygame.display.set_mode((100, 100))
sense = SenseHat()
sense.clear()


pygame.mixer.music.load('/home/pi/Astro_MP3/MP3_files/Atest1.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0)


while True:
    roll = sense.get_orientation()['roll']
    if roll < 80:
        
        #time.sleep(1)
        #print roll

        if roll > 0 and roll < 100:
            print (roll)
            pygame.mixer.music.set_volume(roll)
            
    
'''volume = 0

pygame.mixer.music.load('/home/pi/Astro_MP3/MP3_files/Afr.mp3')
pygame.mixer.music.play()

while True:
    pygame.mixer.music.set_volume(volume)
    #sense.show_letter(str(volume))
    volume = volume + 1
    print volume'''
