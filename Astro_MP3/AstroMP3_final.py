###Created by Ben, Danny, Cal, and Mr Aldred###
###written for Python 2 ###
###print statements left in for understanding code ###
##Error on Random play list - loops with not break out! ### working on it

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
P = (255, 255, 0) #YellowGreen      
M = (60, 200, 130)
Reset = (255,165,0)
End = (255, 0, 0) 
Volume = (0, 255, 0) #Green
instruc = (255, 255, 255)

###interface###
music_interface = [
A, A, A, A, A, A, A, A, #ALPHA
A, A, A, A, A, A, A, A,
A, A, A, A, A, A, A, A,
A, A, X, X, X, X, X, X,
X, X, X, X, X, X, X, instruc,
M, M, M, M, X, X, X, Volume, #MOOD AND VOLUME
X, X, X, X, X, X, X, M, #Random song
P, P, P, P, X, X, Reset, End] #PLAYLISTS

sense.set_pixels(music_interface)

x = 0
y = 0
volume = 0.5
volume_change = 0.10
pygame.mixer.music.set_volume(volume)
v_on = [0,255,0] 
v_off =[30,30,30]

'''dictionary of letters'''

Lookup_Letter = {00: "A", 01: "B", 02: "C", 03: "D", 04: "E", 05: "F", 06 :"G", 07 :"H",
                 10: "I", 11: "J", 12: "K", 13: "L", 14: "M", 15: "N", 16: "O", 17: "P",
                 20: "Q", 21: "R", 22: "S", 23: "T", 24: "U", 25: "V", 26: "W", 27: "X",
                 30: "Y", 31:"Z", 32: " ", 33: " ", 34: " ", 35: " ", 36: " ", 37: " ",
                 40: " ", 41:" ", 42: " ", 43: " ", 44: " ", 45: " ", 46: " ", 47: "i",       
                 50: "1", 51:"2", 52: "3", 53: "4", 54: " ", 55: " ", 56: " ", 57: "#",
                 60: " ", 61:" ", 62: " ", 63: " ", 64: " ", 65: " ", 66: " ", 67: "!", 
                 70: "5", 71:"6", 72: "7", 73: "8", 74: " ", 75: " ", 76: "@", 77: "%"}

###############################################
###################Animation###################
###############################################

def animation():
    repeat = 3
    p = [0, 255, 0]
    q = [0, 0, 255]
    r = [255, 255,0]
    s = [0, 255, 255]
    t = [255, 0, 255]
    v = [255, 128, 0]
    u = [128, 255, 0]
    while repeat > 0:
        o = [255, 0, 0]

        bob= [
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, q, u, u, q, o, o,
        o, o, u, s, r, u, o, o,
        o, o, u, r, s, u, o, o,
        o, o, q, u, u, q, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o]
        sense.set_pixels(bob)
        time.sleep(0.1)

        bod= [
        o, o, o, o, o, o, o, o,
        o, q, u, u, u, u, q, o,
        o, u, o, o, o, o, u, o,
        o, u, o, r, s, o, u, o,
        o, u, o, s, r, o, u, o,
        o, u, o, o, o, o, u, o,
        o, q, u, u, u, u, q, o,
        o, o, o, o, o, o, o, o]
        sense.set_pixels(bod)
        time.sleep(0.1)

        bod= [
        o, o, o, o, o, o, o, o,
        o, q, u, u, u, u, q, o,
        o, u, o, o, o, o, u, o,
        o, u, o, s, r, o, u, o,
        o, u, o, r, s, o, u, o,
        o, u, o, o, o, o, u, o,
        o, q, u, u, u, u, q, o,
        o, o, o, o, o, o, o, o]
        sense.set_pixels(bod)
        time.sleep(0.1)

        o = [0,0,255]
        
        bod= [
        q, u, u, u, u, u, u, q,
        u, o, o, o, o, o, o, u,
        u, o, o, o, o, o, o, u,
        u, o, o, r, s, o, o, u,
        u, o, o, s, r, o, o, u,
        u, o, o, o, o, o, o, u,
        u, o, o, o, o, o, o, u,
        q, u, u, u, u, u, u, q]
        sense.set_pixels(bod)
        time.sleep(0.1)

        bod= [
        o, o, o, o, o, o, o, o,
        o, q, u, u, u, u, q, o,
        o, u, o, o, o, o, u, o,
        o, u, o, s, r, o, u, o,
        o, u, o, r, s, o, u, o,
        o, u, o, o, o, o, u, o,
        o, q, u, u, u, u, q, o,
        o, o, o, o, o, o, o, o]
        sense.set_pixels(bod)
        time.sleep(0.1)

        bod= [
        o, o, o, o, o, o, o, o,
        o, q, u, u, u, u, q, o,
        o, u, o, o, o, o, u, o,
        o, u, o, r, s, o, u, o,
        o, u, o, s, r, o, u, o,
        o, u, o, o, o, o, u, o,
        o, q, u, u, u, u, q, o,
        o, o, o, o, o, o, o, o]
        sense.set_pixels(bod)
        time.sleep(0.1)
        bob= [
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, q, u, u, q, o, o,
        o, o, u, s, r, u, o, o,
        o, o, u, r, s, u, o, o,
        o, o, q, u, u, q, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o]
        sense.set_pixels(bob)
        time.sleep(0.1)

        repeat = repeat - 1

        

############################################
###   play all songs in the play list ######
############################################

'''Controls the PLaylist Music'''
def MP3_Playlist():
        
        pygame.mixer.music.stop()
        the_song = 0
        
        print ("THIS IS THE PLAYLIST FUNCTION RUNNING")
        print ("YOU SELECTED", letter)
        print letter
        print type(letter)
        '''checks for mp3s in playlist 1 - 8'''    
        mp3_files_playlist = glob.glob('/home/pi/Astro_MP3/MP3_files/Playlist/' + letter + '*.mp3')
        
            
        songs_found  = mp3_files_playlist
        print ("I have found the following song", songs_found)
        number_of_songs = len(songs_found)
        print ("there are", number_of_songs)

        print type(number_of_songs)
               
        if pygame.mixer.music.get_busy()==False:
                while the_song < number_of_songs:
                        
                        pygame.mixer.music.load(songs_found[the_song])
                        
                        pygame.mixer.music.play()
                        print("Playing Song")
                        the_song = the_song + 1
                        print ("the song number is", str(the_song))
                              
                        while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)  ###waits for song
                                

                                #############################################################
                                ####press enter to skip through the songs in the playlist####
                                #############################################################

                                for event in pygame.event.get():
                                        if event.type == KEYDOWN:
                                                if event.key == K_RETURN:
                                                       print ("FFGDFGSFJGS")
                                                       pygame.mixer.music.stop()
                                                       
                                                       break
                           
                        
                                
        else:
                print ("end of playlist")
                sense.show_message("End of Playlist", text_colour = [255, 255, 255])
                
             
        
###################################
### PLay song by Title Letter #####
###################################
'''Controls the select song by letter'''
def MP3_Player():

        ###run length error### needs to be less than the song length 'songs found' length ?? may be solved
        
        global song
        print ("YOU SELECTED", letter)
        print type(letter)
            
        mp3_files = glob.glob('/home/pi/Astro_MP3/MP3_files/' + letter + '*.mp3')
            
        songs_found  = mp3_files
        print ("I have found the following song", songs_found)
           
        print ("songs found", len(songs_found))
                    
        number_of_songs = len(songs_found)

        print type(number_of_songs)

        print (song)

        
       
        try:
                if pygame.mixer.music.get_busy() == False:
                                
                                print ("I played ")
                                print (song)
                                pygame.mixer.music.load(songs_found[song])
                                pygame.mixer.music.play()
                                animation()
                                animation()
                                

                                
                elif pygame.mixer.music.get_busy() == True:
                                pygame.mixer.music.stop()
                                if song == number_of_songs - 1:
                                        print("END OF SONGS")
                                        
                                        song = 0
                                        return song
                                else:
                                        song = song + 1
                                        print ("I played a new song")
                                        print (song)
                                        pygame.mixer.music.load(songs_found[song])
                                        pygame.mixer.music.play()
                                        animation()
                                        

        except:
                print ("No MP3s")
                songs = 1
                print (songs)
                sense.show_message("NO MP3s", text_colour = [255, 0, 0])
                ####scroll NO MP3S

sense.load_image("/home/pi/Astro_MP3/Images8x8/hi.png")
time.sleep(2)
pygame.mixer.music.load("/home/pi/Astro_MP3/MP3_files/Intro.mp3")
sense.load_image("/home/pi/Astro_MP3/Images8x8/Rasp.png")
pygame.mixer.music.play()
time.sleep(3.8)

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
                

                #################
                #####Mood #######
                #################    
                    
                if letter == "1":  
                        print ("Mood 1")
                        sense.show_message("Thinking", text_colour = [186, 145, 34])
                        sense.load_image("/home/pi/Astro_MP3/Images8x8/Yellowstar.png")
                        MP3_Playlist()

                elif letter == "2":   
                        print ("Mood 2")
                        sense.show_message("Relaxing", text_colour = [34, 173, 186])
                        sense.load_image("/home/pi/Astro_MP3/Images8x8/smile.png")
                        MP3_Playlist() 


                elif letter == "3":   
                        print ("Mood 3")
                        sense.show_message("ISS Party!", text_colour = [255, 255, 0])
                        sense.load_image("/home/pi/Astro_MP3/Images8x8/ISS.png")
                        MP3_Playlist()
                        
                elif letter == "4":   
                        print ("Mood 4")
                        sense.show_message("Bowie", text_colour = [255, 30, 55], back_colour = [43, 132, 255])
                        sense.load_image("/home/pi/Astro_MP3/Images8x8/Bowie.png")
                        MP3_Playlist()
                        
                #################
                #####Play Lists##
                #################       


                elif letter == "5":   
                        print ("PLAYLIST 1")
                        sense.show_message("Playlist: Rock", text_colour = [255, 128, 0], back_colour = [0, 153, 0])
                        sense.load_image("/home/pi/Astro_MP3/Images8x8/Rock.png")
                        MP3_Playlist()        
                
                elif letter == "6":   
                        print ("PLAYLIST 2")
                        sense.show_message("Playlist: Rap", text_colour = [196, 174, 77])
                        sense.load_image("/home/pi/Astro_MP3/Images8x8/Rap.png")
                        MP3_Playlist()
                elif letter == "7":   
                        sense.show_message("Playlist: Space", text_colour = [0, 0, 0], back_colour = [181, 179, 176])
                        sense.load_image("/home/pi/Astro_MP3/Images8x8/star2.png")
                        print ("PLAYLIST 3")
                        MP3_Playlist()
                elif letter == "8":   
                        print ("PLAYLIST 4")
                        sense.show_message("PlayList: Sonic Pi", text_colour = [255, 89, 230])
                        sense.load_image("/home/pi/Astro_MP3/Images8x8/Sonic.png")
                        MP3_Playlist()
                        time.sleep(3)

                ###############################
                ##### INSTRUCTIONS  ###########
                ###############################
                        
                elif letter == "i":
                        print ("INSTRUCTIONS")
                        import intro
                        song = 0
                       
                        
                ###############################
                ##### RANDOM PLAY LIST ########
                ###############################
                        
                elif letter == "!":
                        pygame.mixer.music.stop()
                        random_play = True
                        print ("Random")
                        sense.show_message("RANDOM SONG", text_colour = [153, 255, 204])
                        while random_play == True:
                                if pygame.mixer.music.get_busy() == False:
                                        pos = random.randrange(0, 31) ###31 is the top letter pos x, y ###
                                        if pos == 'None':
                                            pass
                                            print ("playing")    
                                        else:
                                            brackets = ("'")
                                            print (brackets)
                                            print  type(pos)
                                            
                                            letter = Lookup_Letter.get(pos)
                                            print letter
                                            time.sleep(1)

                                            
                                            MP3_Player() ###import the code

                                            

                ####Needs a break to exit the random play ERROR DOES NOT BREAK ######
                   
                ###################
                ##### reset #######
                ###################
                            
                elif letter == "@":   
                        print ("RESET")
                        sense.show_message("RESET", text_colour = [102, 0, 204])
                        pygame.mixer.music.stop()
                        y = 0
                        x = 0
                        song = 0
                        
                        sense.set_pixels(music_interface)
                                

                 
                #####################
                ###Close Player######
                #####################        
                        
                elif letter == "%":   
                        pygame.mixer.music.stop()
                        sense.show_message("BYE BYE", text_colour = [0, 0, 255], back_colour = [255, 255, 0])
                        sense.clear()
                        sense.load_image("/home/pi/Astro_MP3/Images8x8/comp.png")
                        time.sleep(2)
                        running = False
                        

                        
               #####################                
               ###Volume Control ###
               #####################
                        
                elif letter == "#":   
                        print ("VOLUME CONTROL")
                        sense.show_message("Volume", text_colour = [0, 255, 0])
                        volume_running = True
                        while volume_running == True:
            
                            
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_b:
                                         
                                         volume = volume + volume_change
                                        
                                         print volume
                                         pygame.mixer.music.set_volume(volume)
                                         
                                         sense.show_letter(str("+"))
                                         time.sleep(0.2)

                                if event.type == KEYDOWN:
                                    if event.key == K_a:
                                         
                                         volume = volume - volume_change
                                        
                                         print volume
                                         pygame.mixer.music.set_volume(volume)
                                         
                                         sense.show_letter(str("-"))
                                         time.sleep(0.2)
                                         
                                if event.type == KEYDOWN:
                                    if event.key == K_RETURN:
                                            volume_running = False
                                            

                            if volume > 1:
                                volume = 1
                            elif volume <= 0:
                                volume = 0
                                print "mute"
                                                                
                                sense.load_image("/home/pi/Astro_MP3/Images8x8/mute.png")
                                time.sleep(1.5)

                            conversion = 64/1
                            pixels_on = int(volume * conversion)
                            pixels_off = int(64 - pixels_on)

                            volume_display = []             
                            
                            volume_display.extend([v_off] * pixels_off)
                            volume_display.extend([v_on] * pixels_on)
                            sense.set_pixels(volume_display)
                            print ("TEST")
                        
                    
                else:
                        MP3_Player()
                 
                
                
            
                
        time.sleep(0.11)
        sense.set_pixel(x, y, 255, 255, 0)
        print (x, y)
        
        x_pos_number = str(x)
        y_pos_number = str(y)
        pos = (y_pos_number+x_pos_number)
        print pos         
        pos = int(pos)     

        ###SHOW LETTER###
        letter = Lookup_Letter.get(pos)
        print letter
        sense.show_letter(str(letter))

                  
        if event.type == QUIT:
            running = False
            print("BYE")
