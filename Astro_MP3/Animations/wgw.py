
import time
from sense_hat import SenseHat
sense = SenseHat()

while True:
    o = [255,0,0]
    h = [0,255,0]


    chase = [
    h, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [ 
    h, h, h, h, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [ 
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, h, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, h, h, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, h, h, h, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, h, h, h, h, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    
    chase = [
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, h, o, o, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, o, o, h, h, h,
    h, h, h, o, o, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, o, h, h, h,
    h, h, h, o, o, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, o, o, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, o, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    h = [255,0,0]
    o = [0,255,0]

    chase = [
    h, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [ 
    h, h, h, h, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [ 
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, o]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, h, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, h, h, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, h, h, h, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, h, h, h, h, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    o, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    
    chase = [
    h, h, h, h, h, h, h, h,
    o, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    
    chase = [
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, o, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, o, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, o, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, o, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, o, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, o, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, o, o, o, h, h, h,
    h, h, h, o, o, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, o, o, h, h, h,
    h, h, h, o, o, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, o, h, h, h,
    h, h, h, o, o, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, o, o, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, o, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)
    chase = [
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h]
    sense.set_pixels(chase)
    time.sleep(0.05)

