def findSquareRoot(num):
    low = 1
    high = num

    while low <= high:
        mid = (low + high)//2
        sqMid = mid ** 2
        if sqMid == num:
            return mid
        elif sqMid > num:
            high = mid - 1
        else:
            low = mid + 1

    return min(low, high)

print(findSquareRoot(28))