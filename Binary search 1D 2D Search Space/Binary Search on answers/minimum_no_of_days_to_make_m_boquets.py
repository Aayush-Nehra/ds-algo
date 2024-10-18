def numberOfBouquetPossible(bloomDay, daysPassed, reqBunchSize):
    boquetsPossible = 0
    currentBunch = 0
    for i in range(len(bloomDay)):
        if bloomDay[i] <= daysPassed:
            currentBunch += 1
        else:
            currentBunch = 0

        if currentBunch == reqBunchSize:
            boquetsPossible += 1
            currentBunch = 0
    
    # print(boquetsPossible)
    return boquetsPossible

def findMinMax(arr):
    minimum = 999999999
    maximum = -1
    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
        if arr[i] < minimum:
            minimum = arr[i]
    
    return [minimum, maximum]

bloomDay = [1,10,3,10,2]
m = 3 
k = 1

#numberOfBouquetPossible(bloomDay, 10, 1)

#Solution 1 with linear search

def minDaysLinear(bloomDay, m, k):
    """
    bloomDay: day on which flower bloomed
    m: Required Boquets
    k: Adjacent Flower required/ bunchSize
    """
    if m * k > len(bloomDay):
        return -1
    low, high = findMinMax(bloomDay)

    for day in range(low, high+1):
        totalBoquetsOnDay = numberOfBouquetPossible(bloomDay, day, k)
        if totalBoquetsOnDay >= m:
            print(day)
            return day

    return -1

def minDaysBinary(bloomDay, m, k):
    """
    bloomDay: day on which flower bloomed
    m: Required Boquets
    k: Adjacent Flower required/ bunchSize
    """
    if m * k > len(bloomDay):
        return -1
    low, high = findMinMax(bloomDay)
    ans = 0
    while low <= high:
        mid = (low + high)//2
        totalBoquetsOnDay = numberOfBouquetPossible(bloomDay, mid, k)
        if totalBoquetsOnDay >= m:
            ans = mid
            high = mid-1
        else:
            low = mid + 1

    print(ans)
    return ans


#bloomDay, m, k = [7,7,7,7,12,7,7], 2, 3

minDaysBinary(bloomDay, m, k)

    


#Solution 2 with binary search
