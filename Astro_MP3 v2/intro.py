import pygame

import time

from sense_hat import SenseHat

#pygame.init()
#pygame.display.set_mode((100, 100))

sense = SenseHat()
sense.clear

pygame.mixer.music.stop()


A = (0, 0, 255) #Blue
X = (0, 0, 0) #Black
P = (255, 255, 0) #Yellow      
M = (60, 200, 130)
End = (255, 0, 0)
Green = (0, 255, 0)
Orange = (255, 189, 51)
W = (255, 255, 255)

sense.show_message("Instructions", text_colour = [255, 255, 255])

###change interface###
pygame.mixer.music.load("/home/pi/Astro_MP3/MP3_files/Instructions/Voice001.mp3")                
pygame.mixer.music.play()


music_interface = [
A, A, A, A, A, A, A, A, #ALPHA
A, A, A, A, A, A, A, A,
A, A, A, A, A, A, A, A,
A, A, X, X, X, X, X, X,
X, X, X, X, X, X, X, W,

M, M, M, M, X, X, X, Green, #MOOD AND VOLUME
X, X, X, X, X, X, X, M,

P, P, P, P, X, X, Orange, End] #PLAYLISTS

sense.set_pixels(music_interface)

time.sleep(6)
pygame.mixer.music.stop()

###blue letters

pygame.mixer.music.load("/home/pi/Astro_MP3/MP3_files/Instructions/Voice002.mp3")                
pygame.mixer.music.play()


music_interface = [
A, A, A, A, A, A, A, A, #ALPHA
A, A, A, A, A, A, A, A,
A, A, A, A, A, A, A, A,
A, A, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, X, X, #MOOD AND VOLUME
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, X,X] #PLAYLISTS

sense.set_pixels(music_interface)

time.sleep(11)
pygame.mixer.music.stop()


###volume
pygame.mixer.music.load("/home/pi/Astro_MP3/MP3_files/Instructions/Voice004.mp3")                
pygame.mixer.music.play()

music_interface = [
X, X, X, X, X, X, X, X, #ALPHA
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, X, Green, #MOOD AND VOLUME
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, X,X] #PLAYLISTS

sense.set_pixels(music_interface)
time.sleep(9)
pygame.mixer.music.stop()

###Reset

pygame.mixer.music.load("/home/pi/Astro_MP3/MP3_files/Instructions/Voice005.mp3")                
pygame.mixer.music.play()

music_interface = [
X, X, X, X, X, X, X, X, #ALPHA
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, X, X, #MOOD AND VOLUME
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, Orange,X] #PLAYLISTS

sense.set_pixels(music_interface)

time.sleep(6)
pygame.mixer.music.stop()

###Exit

pygame.mixer.music.load("/home/pi/Astro_MP3/MP3_files/Instructions/Voice006.mp3")                
pygame.mixer.music.play()

music_interface = [
X, X, X, X, X, X, X, X, #ALPHA
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, X, X, #MOOD AND VOLUME
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, X,End] #PLAYLISTS

sense.set_pixels(music_interface)

time.sleep(5)

##moods

pygame.mixer.music.load("/home/pi/Astro_MP3/MP3_files/Instructions/Voice007.mp3")                
pygame.mixer.music.play()

music_interface = [
X, X, X, X, X, X, X, X, #ALPHA
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,

M, M, M, M, X, X, X, X, #MOOD AND VOLUME
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, X,X] #PLAYLISTS

sense.set_pixels(music_interface)

time.sleep(10)
pygame.mixer.music.stop()

###yellow play lists

pygame.mixer.music.load("/home/pi/Astro_MP3/MP3_files/Instructions/Voice008.mp3")                
pygame.mixer.music.play()

music_interface = [
X, X, X, X, X, X, X, X, #ALPHA
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, X, X, #MOOD AND VOLUME
X, X, X, X, X, X, X, X,

P, P, P, P, X, X, X,X] #PLAYLISTS

sense.set_pixels(music_interface)

time.sleep(12)
pygame.mixer.music.stop()

###Random

pygame.mixer.music.load("/home/pi/Astro_MP3/MP3_files/Instructions/Voice009.mp3")                
pygame.mixer.music.play()


music_interface = [
X, X, X, X, X, X, X, X, #ALPHA
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, X, X, #MOOD AND VOLUME
X, X, X, X, X, X, X, M,

X, X, X, X, X, X, X,X] #PLAYLISTS

sense.set_pixels(music_interface)
time.sleep(10)
pygame.mixer.music.stop()

sense.load_image("/home/pi/Astro_MP3/Images8x8/relax.png")

pygame.mixer.music.load("/home/pi/Astro_MP3/MP3_files/Instructions/Voice010.mp3")                
pygame.mixer.music.play()
time.sleep(6)
pygame.mixer.music.load("/home/pi/Astro_MP3/MP3_files/Instructions/Voice011.mp3")                
pygame.mixer.music.play()
time.sleep(3)





