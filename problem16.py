#Euler problem 17
#sum of digits in 2^1000

a = 2**1000
b = str(a)
c = 0
for x in b:
    c += int(x)
print(c)