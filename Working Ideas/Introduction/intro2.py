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
Green = (0, 255, 0)
Orange = (255, 189, 51)
###change interface###
music_interface = [
A, A, A, A, A, A, A, A, #ALPHA
A, A, A, A, A, A, A, A,
A, A, A, A, A, A, A, A,
A, A, X, X, X, X, X, X,
X, X, X, X, X, X, X, Orange,

M, M, M, M, X, X, X, Green, #MOOD AND VOLUME
X, X, X, X, X, X, X, M,

P, P, P, P, X, X, X, End] #PLAYLISTS

sense.set_pixels(music_interface)

time.sleep(3)


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
time.sleep(3)

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

###yellow play lists
time.sleep(3)

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

###reset
time.sleep(3)

music_interface = [
X, X, X, X, X, X, X, X, #ALPHA
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, Orange,

X, X, X, X, X, X, X, X, #MOOD AND VOLUME
X, X, X, X, X, X, X, X,

X, X, X, X, X, X, X,X] #PLAYLISTS

sense.set_pixels(music_interface)

###volume
time.sleep(3)

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

###Random
time.sleep(3)

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


###Exit
time.sleep(3)

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
