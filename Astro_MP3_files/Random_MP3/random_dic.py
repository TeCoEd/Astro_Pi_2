#####Made by TECOED####
import random
import time

#pos = "0,5"
pos = random.randrange(0, 31)

print pos

Lookup_Letter = {00: "A", 01: "B", 02: "C", 03: "D", 04: "E", 05: "F", 06 :"G", 07 :"H",
                 10: "I", 11: "J", 12: "K", 13: "L", 14: "M", 15: "N", 16: "O", 17: "P",
                 20: "Q", 21: "R", 22: "S", 23: "T", 24: "U", 25: "V", 26: "W", 27: "X",
                 30: "Y", 31:"Z"
                 }

while True:
    pos = random.randrange(0, 31)
    brackets = ("'")
    print (brackets)
    print  type(pos)

    #final = str(brackets + pos + brackets)
    #print final
    
    letter = Lookup_Letter.get(pos)
    print letter
    time.sleep(1)
