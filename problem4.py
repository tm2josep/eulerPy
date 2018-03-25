#Euler problem 4
#Find the largest palindrome from the product of two 3 digit numbers
largestPalim = 0


for i in range(0, 999):
    for j in range(0, 999):
        n = i*j
        if(str(n) == str(n)[::-1] and n > largestPalim):
            largestPalim = n

print(largestPalim)