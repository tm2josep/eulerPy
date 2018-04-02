# Euler problem 10
#sum of primes below 2 million
#Rather long run time, I'll figure out how to make it faster

def isPrime(n, arr):
    for x in arr:
        if(n%x == 0):
            return False
    print(n)
    return True

def getPrimes():
    primes = [2]
    n = 3
    while n <= 2000000:
        if(isPrime(n, primes)):
            primes.append(n)
        n += 2
    return primes

print(sum(getPrimes()))

