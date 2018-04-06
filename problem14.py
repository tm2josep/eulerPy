#Euler problem 14
#Longest Collatz sequence from a number under 1000000
currNum = 0
currLen = 0

def getCollatzlength(n):
    count = 1
    while(n!=1):
        count += 1
        n = n/2 if(n%2==0) else 3*n + 1
    return count

for x in range(1,1000001):
    print(x)
    newLen = getCollatzlength(x)
    if(newLen > currLen):
        currNum = x
        currLen = newLen

print(currNum)