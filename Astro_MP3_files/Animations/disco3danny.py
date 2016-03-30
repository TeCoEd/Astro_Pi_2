import time
from sense_hat import SenseHat
sense = SenseHat()
import random
while True:
    o =[255,0,0]
    b =[0,255,255]
    s1=[
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, b, b, o, o, o,
    o, o, o, b, b, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    sense.set_pixels(s1)
    time.sleep(0.1)

    o =[255,0,0]
    b =[0,255,255]
    s1=[
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, b, o, o, b, o, o,
    o, o, o, b, b, o, o, o,
    o, o, o, b, b, o, o, o,
    o, o, b, o, o, b, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    sense.set_pixels(s1)
    time.sleep(0.1)
    o =[255,0,0]
    b =[0,255,255]
    s1=[
    o, o, o, o, o, o, o, o,
    o, b, o, o, o, o, b, o,
    o, o, b, o, o, b, o, o,
    o, o, o, b, b, o, o, o,
    o, o, o, b, b, o, o, o,
    o, o, b, o, o, b, o, o,
    o, b, o, o, o, o, b, o,
    o, o, o, o, o, o, o, o]
    sense.set_pixels(s1)
    time.sleep(0.1)


    
    s1=[
    b, o, o, o, o, o, o, b,
    o, b, o, o, o, o, b, o,
    o, o, b, o, o, b, o, o,
    o, o, o, b, b, o, o, o,
    o, o, o, b, b, o, o, o,
    o, o, b, o, o, b, o, o,
    o, b, o, o, o, o, b, o,
    b, o, o, o, o, o, o, b]
    sense.set_pixels(s1)
    time.sleep(0.1)
    
    x = random.randrange(50,255)
    timer = 5
    while timer>0:
       
        
        b = [x, x, x]
        s1=[
        b, b, b, b, b, b, b, b,
        o, b, o, o, o, o, b, o,
        o, o, b, o, o, b, o, o,
        o, o, o, b, b, o, o, o,
        o, o, o, b, b, o, o, o,
        o, o, b, o, o, b, o, o,
        o, b, o, o, o, o, b, o,
        b, o, o, o, o, o, o, b]
        sense.set_pixels(s1)
        time.sleep(0.1)
        timer = timer-1
        print timer
        if timer == 0:
            timer = 5

