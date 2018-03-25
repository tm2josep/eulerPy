#Euler problem 5
#smallest positive number divisible by 1 through 20
answer = 2520

def isDivis(n, checks):
    for x in checks:
        if(n % x != 0):
            print(x, end=" ")
            return False
    return True

while isDivis(answer, range(2,21)) != True:
    print(answer)
    answer += 2520


print(answer)