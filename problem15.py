#Euler problem 15
#How many ways can you get to the bottom of a 20x20 grid.
#If you can only move down and right?

'''
did some analysis, for the last point on any lattice, it takes 
n choose n/2 ways to get from one end to the other.
So i just pulled up the choose formula and wrote it here, hopefully it works

'''
import math

def getPathLength(gridSize):
    ans = math.factorial(gridSize*2)/(math.factorial(gridSize)*math.factorial((gridSize*2)-gridSize))
    return ans

print(getPathLength(20))


