from sense_hat import SenseHat
sense = SenseHat()
import time
sense.clear()

def animation():
    p = [0, 255, 0]
    q = [0, 0, 255]
    r = [255, 255,0]
    s = [0, 255, 255]
    t = [255, 0, 255]
    v = [255, 128, 0]
    u = [128, 255, 0]
    while True:
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


         
