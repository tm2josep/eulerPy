#Euler problem 2
#Find sum of even fibonacci numbers under 4 million
n1 = 1
n2 = 2
nextNum = 0
fibSum = 2 #2 is already an even number

while nextNum <= 4000000:
    nextNum = n1 + n2
    if nextNum % 2 == 0:
        fibSum += nextNum
    n1 = n2
    n2 = nextNum

print(fibSum)