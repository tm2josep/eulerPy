#Euler problem 1
#Find the sum of all multiples of 3 or 5 below 1000.
multiples = []
sum = 0

def getMultiples(n):
    for x in range(3, n+1):
        if x % 3 == 0 or x % 5 == 0:
            multiples.append(x)

getMultiples(1000)

for x in multiples:
    sum += x

print(multiples)
print(sum)
