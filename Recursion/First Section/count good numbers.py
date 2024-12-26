def countGoodNumbers(n):
    ans = 1
    if n%2 == 0:
        ans = pow(5,n//2) * pow(4,n//2)
    else:
        ans = pow(5,n-n//2) * pow(4, n//2)

    return ans