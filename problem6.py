#Euler problem 6
#Difference between sum of squares and square of sum till 100

def sumSquares(n):
    ans = 0
    for x in range(1,n+1):
        ans += x*x
    return ans

def squareSum(n):
    ans = 0
    for x in range(1, n+1):
        ans += x
    return ans*ans

print(squareSum(100) - sumSquares(100))