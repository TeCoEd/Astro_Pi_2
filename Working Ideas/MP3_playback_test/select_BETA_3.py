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

running = True
global song
song = 0

A = (0, 0, 255) #Blue
X = (0, 0, 0) #Black
P = (255, 255, 0) #Yellow      
M = (60, 200, 130)
End = (255, 0, 0)

###change interface###
music_interface = [
M, A, A, A, A, A, A, A, #ALPHA
A, A, A, A, A, A, A, A,
A, A, A, A, A, A, A, A,
A, M, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,

M, M, M, M, X, X, X, End, #MOOD AND VOLUME
X, X, X, X, X, X, X, X,

P, P, P, P, P, P, P, P] #PLAYLISTS

sense.set_pixels(music_interface)

x = 0
y = 0

#sense.set_pixels(x, y, 255, 255, 255)

'''dictonary of letters'''

Lookup_Letter = {00: "A", 01: "B", 02: "C", 03: "D", 04: "E", 05: "F", 06 :"G", 07 :"H",
                 10: "I", 11: "J", 12: "K", 13: "L", 14: "M", 15: "N", 16: "O", 17: "P",
                 20: "Q", 21: "R", 22: "S", 23: "T", 24: "U", 25: "V", 26: "W", 27: "X",
                 30: "Y", 31:"Z", 32: "*", 33: "*", 34: "*", 35: "*", 36: "*", 37: "*",
                 40: "*", 41:"*", 42: "*", 43: "*", 44: "*", 45: "*", 46: "*", 47: "*",       
                 50: "*", 51:"*", 52: "*", 53: "*", 54: "*", 55: "*", 56: "*", 57: "*",
                 60: "*", 61:"*", 62: "*", 63: "*", 64: "*", 65: "*", 66: "*", 67: "*", 
                 70: "1", 71:"2", 72: "*", 73: "*", 74: "*", 75: "*", 76: "*", 77: "PL8"}

'''Controls the PLaylist Music'''
def MP3_Playlist():
        ###add the play list
        print ("THIS IS THE PLAYLIST FUNCTION RUNNING")
        print ("YOU SELECTED", letter)
        print type(letter)
        '''checks for mp3s in playlist 1 - 8'''    
        mp3_files = glob.glob('/home/pi/Astro_MP3/MP3_files/Playlist' + letter + '*.mp3')
            
        songs_found  = mp3_files
        print ("I have found the following song", songs_found)
        
'''Controls the select song by letter'''
def MP3_Player():

        ###run length error### needs to be less than the song length 'songs found' length
        
        global song
        print ("YOU SELECTED", letter)
        print type(letter)
            
        mp3_files = glob.glob('/home/pi/Astro_MP3/MP3_files/' + letter + '*.mp3')
            
        songs_found  = mp3_files
        print ("I have found the following song", songs_found)

            #random_song = random.randrange(0, len(songs_found))
            #print random_song
        print ("songs found", len(songs_found))
                    
        number_of_songs = len(songs_found)

        print type(number_of_songs)

        print (song)

       
        try:
                if pygame.mixer.music.get_busy() == False:
                                #pygame.mixer.music.stop()
                        #if event.key == K_RIGHT:
                                #song = song + 1
                                print ("I played ")
                                print (song)
                                pygame.mixer.music.load(songs_found[song])
                                pygame.mixer.music.play()

                elif pygame.mixer.music.get_busy() == True:
                                pygame.mixer.music.stop()
                                if song == number_of_songs - 1:
                                        print("HAKT")
                                        
                                        song = 0
                        #if event.key == K_RIGHT:
                                else:
                                        song = song + 1
                                        print ("I played a new song")
                                        print (song)
                                        pygame.mixer.music.load(songs_found[song])
                                        pygame.mixer.music.play()                

        except:
                print ("No MP3s")
                songs = 1
                print (songs)
                sense.show_message("NO MP3s", text_colour = [255, 0, 0])
                ####scroll NO MP3S





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
                if letter == "1" or "2":
                        print ("PLAYLIST 1")
                        MP3_Playlist()
                        
                        ###run the playlist
                        ###add picture
                else:
                        MP3_Player()
                #song = 0  
                
                
            
                
        time.sleep(0.3)
        sense.set_pixel(x, y, 255, 255, 0)
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
