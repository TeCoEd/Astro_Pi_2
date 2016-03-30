import pygame
import time

import random

from sense_hat import SenseHat


sense = SenseHat()
sense.clear

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

time.sleep(5)


###blue letters
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


##moods
time.sleep(5)

music_interface = [
X, X, X, X, X, X, X, X, #ALPHA
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,

M, M, M, M, X, X, X, End, #MOOD AND VOLUME
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, X,X] #PLAYLISTS

sense.set_pixels(music_interface)

###yellow play lists
time.sleep(5)

music_interface = [
X, X, X, X, X, X, X, X, #ALPHA
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, X, X, #MOOD AND VOLUME
X, X, X, X, X, X, X, X,

P, P, P, P, P, P, X,X] #PLAYLISTS

sense.set_pixels(music_interface)
