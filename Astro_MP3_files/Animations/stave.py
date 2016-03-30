import time
import random 
from sense_hat import SenseHat
sense = SenseHat()
o = [255,255,255]
k = [0,0,255]
l = [254,254,254]
h = [100,30,110]

r1 = (0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)

r2 = (5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7)
r1 = 5
r2 = 6    
while True:
        hello=[
        k, k, k, k, k, k, k, k,
        l, l, l, l, l, l, l, l,
        l, l, l, l, l, l, l, l,
        k, k, k, k, k, k, k, k,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        k, k, k, k, k, k, k, k,
        o, o, o, o, o, o, o, o]
        sense.set_pixels(hello)
        time.sleep(0.5)
        x = random.randrange(5,7)
        print x
        
        if x == 5:
            hello=[
            k, k, k, k, k, k, k, k,
            l, l, l, h, h, l, l, l,
            l, l, l, h, h, l, l, l,
            k, k, k, k, h, k, k, k,
            o, o, o, o, h, o, o, o,
            o, o, o, o, h, o, o, o,
            k, k, k, k, k, k, k, k,
            o, o, o, o, o, o, o, o]
            sense.set_pixels(hello)

            time.sleep(0.5)

        if x == 6:
            hi=[
            k, k, k, k, k, k, k, k,
            l, l, l, l, h, l, l, l,
            l, l, l, l, h, l, l, l,
            k, k, k, k, h, k, k, k,
            o, o, o, h, h, o, o, o,
            o, o, o, h, h, o, o, o,
            k, k, k, k, k, k, k, k,
            o, o, o, o, o, o, o, o]
            sense.set_pixels(hi)
            time.sleep(0.5)
            
            

