import math


def minEatingSpeedBruteForce(piles, h):
    ans = 0
    for k in range(1, 9999999999):
        freshPile = list(piles)
        i = 0
        for hour in range(h):
            if k >= freshPile[i]:
                freshPile[i] = 0
                i += 1
            elif k < freshPile[i]:
                freshPile[i] -= k
            if i == len(freshPile) and freshPile[i-1] == 0:
                ans = k
                break
        if ans != 0:
            break
    
    print(ans)

def minEatingSpeedBinarySearch(piles, h):
    low = 1
    high = max(piles)
    ans = 0

    while low <= high:
        mid = (low+high)//2
        i = 0
        freshPile = list(piles)
        for _ in range(h):
            if mid >= freshPile[i]:
                freshPile[i] = 0
                i += 1
            elif mid < freshPile[i]:
                freshPile[i] -= mid
            if i == len(freshPile) and freshPile[i-1] == 0:
                ans = mid
                break
        if ans == mid:
            high = mid - 1
        else:
            low = mid + 1

    return ans

def minEatingSpeedBinarySearchOptimal(piles, h):
    low = 1
    high = max(piles)
    ans = 0

    while low <= high:
        mid = (low+high)//2
        hoursReq = 0
        for i in range(len(piles)):
            curHours = math.ceil(piles[i]/mid)
            hoursReq += curHours
        if hoursReq <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

def minEatingSpeedBinarySearchOptimal2(piles, h):
    if h <= len(piles):
        return max(piles)

    minVal, maxVal, res = math.ceil(sum(piles)/h), max(piles), float('inf')

    print(minVal, maxVal)

    while minVal <= maxVal:
        midVal = (minVal + maxVal) // 2
        totalTime = sum([math.ceil(val / midVal) for val in piles])

        if totalTime > h:
            minVal = midVal + 1
        else:
            res = min(res, midVal)
            maxVal = midVal - 1

    return res


piles = [3,6,7,11]
h = 8

piles = [312884470]
h = 312884469

piles =[30,11,23,4,20]
h = 6

print(minEatingSpeedBinarySearchOptimal2(piles, h))

        
