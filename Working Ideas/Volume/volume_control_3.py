import pygame
import time
import glob
from pygame.locals import *
from sense_hat import SenseHat
global volume

running = True
pygame.init()
pygame.display.set_mode((100, 100))
sense = SenseHat()
sense.clear()

v_on = [0,255,0] ###CHANGE TO ORANGE
v_off =[30,30,30]


volume = 0.5
volume_change = 0.10
#pixels_on = 1/64
#pixels_off = 64 - pixels_on

pygame.mixer.music.load('/home/pi/Astro_MP3/MP3_files/Atest1.mp3')

pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play()  


while running:
            
    #print volume_change
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a:
                 #print volume
                 volume = volume + volume_change
                
                 print volume
                 pygame.mixer.music.set_volume(volume)
                 
                 sense.show_letter(str("+"))
                 time.sleep(0.5)

        if event.type == KEYDOWN:
            if event.key == K_b:
                 #print volume
                 volume = volume - volume_change
                
                 print volume
                 pygame.mixer.music.set_volume(volume)
                 
                 sense.show_letter(str("-"))
                 time.sleep(0.5)

    if volume > 1:
        volume = 1
    elif volume <= 0:
        volume = 0
        print "mute"             

    conversion = 64/1
    pixels_on = int(volume * conversion)
    pixels_off = int(64 - pixels_on)

    volume_display = []             
    
    volume_display.extend([v_off] * pixels_off)
    volume_display.extend([v_on] * pixels_on)
    sense.set_pixels(volume_display)
 
    
