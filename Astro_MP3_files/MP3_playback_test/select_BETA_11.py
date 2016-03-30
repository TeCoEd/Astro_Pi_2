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

###change interface###
music_interface = [
A, A, A, A, A, A, A, A, #ALPHA
A, A, A, A, A, A, A, A,
A, A, A, A, A, A, A, A,
A, A, X, X, X, X, X, X,
X, X, X, X, X, X, X, Reset,
M, M, M, M, X, X, X, Volume, #MOOD AND VOLUME
X, X, X, X, X, X, X, M, #Random song
P, P, P, P, X, X, X, End] #PLAYLISTS

sense.set_pixels(music_interface)

x = 0
y = 0
volume = 0.5
volume_change = 0.10
pygame.mixer.music.set_volume(volume)
v_on = [0,255,0] 
v_off =[30,30,30]

#sense.set_pixels(x, y, 255, 255, 255)

'''dictonary of letters'''

Lookup_Letter = {00: "A", 01: "B", 02: "C", 03: "D", 04: "E", 05: "F", 06 :"G", 07 :"H",
                 10: "I", 11: "J", 12: "K", 13: "L", 14: "M", 15: "N", 16: "O", 17: "P",
                 20: "Q", 21: "R", 22: "S", 23: "T", 24: "U", 25: "V", 26: "W", 27: "X",
                 30: "Y", 31:"Z", 32: "*", 33: "*", 34: "*", 35: "*", 36: "*", 37: "*",
                 40: "*", 41:"*", 42: "*", 43: "*", 44: "*", 45: "*", 46: "*", 47: "@",       
                 50: "*", 51:"*", 52: "*", 53: "*", 54: "*", 55: "*", 56: "*", 57: "#",
                 60: "*", 61:"*", 62: "*", 63: "*", 64: "*", 65: "*", 66: "*", 67: "!", 
                 70: "1", 71:"2", 72: "3", 73: "4", 74: "*", 75: "*", 76: "*", 77: "%"}

    
                

##############################################
     ###   play all songs in the play list
############################################

'''Controls the PLaylist Music'''
def MP3_Playlist():
        #play_list = True
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
                        #
                        pygame.mixer.music.play()
                        print("Playing Song")
                        the_song = the_song + 1
                        print ("the song number is", str(the_song))

                        ##add an animation  / picture ############################
                        
                        while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)  ###waits for song
                                
                                
                        
                                
        else:
                print ("end of playlist")
                
             
        
###################################
### PLay song by Title Letter
####################################
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



sense.load_image("Rasp.png")
time.sleep(2)

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

                #################
                #####Play Lists##
                #################    
                    
                if letter == "1":   ###'''add 3,4,5,6,7,8,9'''
                        print ("PLAYLIST 1")
                        sense.show_message("PlayList 1: Space", text_colour = [255, 255, 255])
                        MP3_Playlist()
                elif letter == "2":   ###'''add 3,4,5,6,7,8,9'''
                        print ("PLAYLIST 2")
                        MP3_Playlist()
                elif letter == "3":   ###'''add 3,4,5,6,7,8,9'''
                        print ("PLAYLIST 3")
                        MP3_Playlist()
                elif letter == "4":   ###'''add 3,4,5,6,7,8,9'''
                        print ("PLAYLIST 4")
                        MP3_Playlist()

                ###############################
                ##### RANDOM PLAY LIST ########
                ###############################
                        
                elif letter == "!":
                        random_play = True
                        print ("Random")
                        sense.show_message("RANDOM SONG", text_colour = [155, 100, 155])
                        while random_play == True:
                                if pygame.mixer.music.get_busy() == False:
                                        pos = random.randrange(0, 3) ###change to 31
                                        if pos == 'None':
                                            pass
                                            print ("playing")    
                                        else:
                                            brackets = ("'")
                                            print (brackets)
                                            print  type(pos)

                                            #final = str(brackets + pos + brackets)
                                            #print final
                                            
                                            letter = Lookup_Letter.get(pos)
                                            print letter
                                            time.sleep(1)

                                            
                                            MP3_Player() ###import the code

                                            
                                #elif pygame.mixer.music.get_busy() == True:
                                      #  for event in pygame.event.get():
                                         #   if event.type == KEYDOWN:
                                               #     if event.key == K_RETURN:
                                                       #     pygame.mixer.music.stop()
                                                         #   random_play == False
                                               # else:
                                                    #    pass

                        ##################################
                        #####WHAT HAPPENS WHEN NONE
                            

                        #####ADD THE FOR MOOD LISTS#########

                ###################
                ##### reset #######
                ###################
                            
                elif letter == "@":   ###'''add 3,4,5,6,7,8,9'''
                        print ("RESET")
                        sense.show_message("RESET", text_colour = [255, 0, 0])
                        pygame.mixer.music.stop()
                        y = 0
                        x = 0
                        #sense.set_pixel(0, 0, 255, 255, 0)
                        sense.set_pixels(music_interface)
                                

                 ######add instructions#####               

                
                        
                #elif letter == "5":   ###'''add 3,4,5,6,7,8,9'''
                     #   print ("PLAYLIST 5")
                      #  MP3_Playlist()
                #elif letter == "6":   ###'''add 3,4,5,6,7,8,9'''
                       # print ("PLAYLIST 6")
                       # MP3_Playlist()

                #####################
                ###Close Player######
                #####################        
                        
                elif letter == "%":   ###'''add 3,4,5,6,7,8,9'''
                        pygame.mixer.music.stop()
                        sense.show_message("BYE BYE", text_colour = [255, 0, 0])
                        running = False

                        ###add a picture#####
                        
                                
                        
               #####################                
               ###Volume Control ###
               #####################
                        
                elif letter == "#":   ###'''add 3,4,5,6,7,8,9'''
                        print ("VOLUME CONTROL")
                        volume_running = True
                        while volume_running == True:
            
                            #print volume_change
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_b:
                                         #print volume
                                         volume = volume + volume_change
                                        
                                         print volume
                                         pygame.mixer.music.set_volume(volume)
                                         
                                         sense.show_letter(str("+"))
                                         time.sleep(0.2)

                                if event.type == KEYDOWN:
                                    if event.key == K_a:
                                         #print volume
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

                            conversion = 64/1
                            pixels_on = int(volume * conversion)
                            pixels_off = int(64 - pixels_on)

                            volume_display = []             
                            
                            volume_display.extend([v_off] * pixels_off)
                            volume_display.extend([v_on] * pixels_on)
                            sense.set_pixels(volume_display)
                            print ("TEST")
                        #buffer
                        
                        
                        ###run the playlist
                        ###add picture
                else:
                        MP3_Player()
                #song = 0  
                
                
            
                
        time.sleep(0.11)
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

                  
        if event.type == QUIT:
            running = False
            print("BYE")
