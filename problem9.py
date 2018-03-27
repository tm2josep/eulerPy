#Euler problem 9
#pythagorean triplet where a + b + c = 1000, find abc

import math


def getC(a,b):
    return math.sqrt(a*a + b*b)

for a in range(1, 1000):
    for b in range(1, 1000):
        if(a + b + getC(a,b) == 1000):
            print(a*b*getC(a,b))
