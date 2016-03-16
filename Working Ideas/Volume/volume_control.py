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


volume = 0.5
volume_change = 0.10


pygame.mixer.music.load('/home/pi/Astro_MP3/MP3_files/Atest1.mp3')

#pygame.mixer.music.play()
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play()  


#print volume
print ("test")


while running:

    if volume > 1:
        volume = 1
    elif volume <= 0:
        volume = 0
        print "mute"
    #global volume
    
    #print volume_change
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a:
                 #print volume
                 volume = volume + volume_change
                
                 print volume
                 pygame.mixer.music.set_volume(volume)
                 print ("voulme up")

        if event.type == KEYDOWN:
            if event.key == K_b:
                 #print volume
                 volume = volume - volume_change
                
                 print volume
                 pygame.mixer.music.set_volume(volume)
                 print ("voulme down")

 
        
        #time.sleep(1)
        #print roll
#
     #   if roll > 0 and roll < 100:
      #      print (roll)
      #      pygame.mixer.music.set_volume(roll)
            
    
'''volume = 0

pygame.mixer.music.load('/home/pi/Astro_MP3/MP3_files/Afr.mp3')
pygame.mixer.music.play()

while True:
    pygame.mixer.music.set_volume(volume)
    #sense.show_letter(str(volume))
    volume = volume + 1
    print volume'''
