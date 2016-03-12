import pygame
import time
import glob
from pygame.locals import *
from sense_hat import SenseHat

pygame.init()
pygame.display.set_mode((100, 100))
sense = SenseHat()
sense.clear()

running = True

A = (0, 255, 0)
X = (0, 0, 0)
P = (0, 0, 255)
M = (60, 200, 130)

###change interface###
music_interface = [
A, P, A, P, A, P, A, P,
A, P, A, P, A, P, A, P,
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

'''dictonary of letters'''

Lookup_Letter = {00: "A", 01: "B", 02: "C", 03: "D", 04: "E", 05: "F", 06 :"G", 07 :"H",
                 10: "I", 11: "J", 12: "K", 13: "L", 14: "M", 15: "N", 16: "O", 17: "P",
                 20: "Q", 21: "R", 22: "S", 23: "T", 24: "U", 25: "V", 26: "W", 27: "X",
                 30: "Y", 31:"Z", 77: "PL8"}

def MP3_Player():
    try:
        song = 0
        
        print ("YOU SELECTED", letter)
        print type(letter)
        #file_test = ('/home/pi/Astro_MP3/MP3_files/' + letter + '*.mp3')
        #print (file_test)
        mp3_files = glob.glob('/home/pi/Astro_MP3/MP3_files/' + letter + '*.mp3')
        #print (mp3_files)
        songs_found  = mp3_files
        print ("I have found the following song", songs_found)

        song_number_total = len(songs_found)
        print ("songs found", song_number_total)
        print songs_found
          
        pygame.mixer.music.load(songs_found[song])
        print("Playing Song")
        pygame.mixer.music.play()

       
   
        #for song in mp3_files:
          #  print song
          #  pygame.mixer.music.load(song)
          #  print("Playing Song")
          #  pygame.mixer.music.play()
            
            

        ###load mp3 play move forward
    except:
        print ("No MP3s")
        '''scroll NO MP3S'''





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
            elif event.key == K_RETURN:
                #break
                #print ("YOU SELECTED", letter)
                MP3_Player()
            
                
        time.sleep(0.3)
        sense.set_pixel(x, y, 255, 255, 255)
        print (x, y)
        #print (type(x))
        #print (type(y))
        x_pos_number = str(x)
        y_pos_number = str(y)
        pos = (y_pos_number+x_pos_number)
        print pos         
        pos = int(pos)     

        ###SHOW LETTER###
        letter = Lookup_Letter.get(pos)
        print letter
        sense.show_letter(str(letter))

        #if
            
        
        
            
        if event.type == QUIT:
            running = False
            print("BYE")
