#Euler problem 7
#what is the 10001st prime?

def getPrime():
    primes = [2]
    n = 3
    while len(primes) <= 10000:
        if all(n % x != 0 for x in primes):
            primes.append(n)
        n += 2
    return primes[-1]

print(getPrime())
