#Euler problem 11
#First triangle number with over five hundred divisors

from functools import reduce

counter = 1

def factors(n): #Slightly modified one I found on stack overflow. My method was too slow
    return len(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0))))

def triangleNumber(n):
    return sum(range(1,n+1))

while(factors(triangleNumber(counter)) < 500):
    counter += 1   

print(triangleNumber(counter))
    
