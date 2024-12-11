def myPow(x,n):
    ans = 1.00000
    if n>0:
        for _ in range(n):
            ans *= x
    else:
        for _ in range(-n):
            ans /= x

    return round(ans, 5)

# The interviewer is not happy and asked to reduce Time

def myPow2(x, n):
    ans = 1.0
    power = n
    if power < 0:
        power *= -1

    while power != 0:
        if power % 2 == 0:
            x = x*x
            #ans = ans * x
            power = power/2
        else:
            ans = ans * x
            power = power - 1

    if n<0:
        ans = 1/ans

    return round(ans, 5)


def findPositivePow(x,n):
    ans = 1
    if n == 0:
        return 1
    if n%2 == 0:
        ans = findPositivePow(x*x, n//2)
    else:
        ans = x * findPositivePow(x, n-1)
    return ans

def myPow3(x, n):
    # Recursive logn solution for finding power
    if n < 0:
        return round(1/findPositivePow(x, -1*n),5)
    else:
        return round(findPositivePow(x, n), 5)




print(myPow(2,10))
